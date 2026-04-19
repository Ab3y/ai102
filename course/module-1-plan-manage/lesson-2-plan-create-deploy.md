# Lesson 2: Plan, Create, and Deploy AI Resources

## Learning Objectives

- Create Azure AI service resources using Azure Portal, CLI, and Bicep
- Choose appropriate AI models for specific scenarios
- Configure SDK and REST API access to AI services
- Deploy AI services in containers for edge and isolated environments
- Integrate AI service provisioning into CI/CD pipelines

---

## Creating Azure AI Resources

### Method 1: Azure Portal

1. Navigate to **Create a resource** → search for **Azure AI services**
2. Select resource type:
   - **Azure AI services** (multi-service) — for bundled access
   - Specific service (e.g., **Computer Vision**, **Language**) — for isolated access
3. Configure:
   - **Subscription** and **Resource group**
   - **Region** — affects available features, latency, and compliance
   - **Pricing tier** — Free (F0) for testing, Standard (S0) for production
   - **Networking** — public access vs. private endpoint

> ### 📝 Exam Tip
> Not all services are available in all regions. **Azure OpenAI** has limited regional availability. The exam may test whether you know to check region availability before provisioning.

### Method 2: Azure CLI

```bash
# Create a resource group
az group create --name rg-ai-services --location eastus

# Create a multi-service resource
az cognitiveservices account create \
    --name my-ai-services \
    --resource-group rg-ai-services \
    --kind CognitiveServices \
    --sku S0 \
    --location eastus \
    --yes

# Create a single-service resource (e.g., Computer Vision)
az cognitiveservices account create \
    --name my-computer-vision \
    --resource-group rg-ai-services \
    --kind ComputerVision \
    --sku S1 \
    --location eastus \
    --yes

# Create an Azure OpenAI resource
az cognitiveservices account create \
    --name my-openai \
    --resource-group rg-ai-services \
    --kind OpenAI \
    --sku S0 \
    --location eastus2 \
    --yes
```

### Retrieve keys and endpoint

```bash
# Get endpoint
az cognitiveservices account show \
    --name my-ai-services \
    --resource-group rg-ai-services \
    --query properties.endpoint

# Get keys
az cognitiveservices account keys list \
    --name my-ai-services \
    --resource-group rg-ai-services
```

### Method 3: Bicep / ARM Template

```bicep
@description('Name of the AI Services resource')
param aiServicesName string = 'my-ai-services'

@description('Location for the resource')
param location string = resourceGroup().location

@allowed(['S0', 'F0'])
param sku string = 'S0'

resource aiServices 'Microsoft.CognitiveServices/accounts@2023-10-01-preview' = {
  name: aiServicesName
  location: location
  kind: 'CognitiveServices'
  sku: {
    name: sku
  }
  properties: {
    publicNetworkAccess: 'Enabled'
    customSubDomainName: aiServicesName
  }
  identity: {
    type: 'SystemAssigned'
  }
}

output endpoint string = aiServices.properties.endpoint
output principalId string = aiServices.identity.principalId
```

Deploy with:
```bash
az deployment group create \
    --resource-group rg-ai-services \
    --template-file ai-services.bicep \
    --parameters aiServicesName=my-ai-services
```

> ### 📝 Exam Tip
> The exam tests Bicep/ARM template properties. Know that `kind` determines the service type (`CognitiveServices`, `OpenAI`, `ComputerVision`, `TextAnalytics`, etc.) and `customSubDomainName` is required for certain authentication scenarios (AAD/managed identity).

---

## Choosing AI Models

### Azure OpenAI Model Selection

| Model | Best For | Context Window | Notes |
|-------|----------|---------------|-------|
| **GPT-4o** | General-purpose chat, reasoning, multimodal | 128K tokens | Recommended default |
| **GPT-4o-mini** | Cost-effective tasks, high throughput | 128K tokens | Lower cost, good quality |
| **GPT-4** | Complex reasoning | 8K–128K tokens | Previous generation |
| **text-embedding-ada-002** | Embeddings for search/RAG | 8K tokens | 1536 dimensions |
| **text-embedding-3-small/large** | Newer embeddings | 8K tokens | Configurable dimensions |
| **DALL-E 3** | Image generation | N/A | From text prompts |
| **Whisper** | Speech-to-text | N/A | Audio transcription |

### Deploying a Model in Azure OpenAI

```bash
# Deploy a GPT-4o model
az cognitiveservices account deployment create \
    --name my-openai \
    --resource-group rg-ai-services \
    --deployment-name gpt-4o-deploy \
    --model-name gpt-4o \
    --model-version "2024-05-13" \
    --model-format OpenAI \
    --sku-capacity 10 \
    --sku-name Standard
```

---

## SDK Installation and Setup

### Python SDK Installation

```bash
# Core Azure AI services
pip install azure-ai-textanalytics
pip install azure-ai-vision-imageanalysis
pip install azure-cognitiveservices-speech
pip install azure-ai-formrecognizer       # Document Intelligence
pip install azure-search-documents         # Azure AI Search

# Azure OpenAI
pip install openai

# Authentication
pip install azure-identity
```

### Python SDK — Basic Pattern

```python
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# Option 1: Key-based authentication
endpoint = "https://my-ai-services.cognitiveservices.azure.com/"
credential = AzureKeyCredential("<your-key>")
client = TextAnalyticsClient(endpoint, credential)

# Option 2: Azure AD / Managed Identity (recommended for production)
from azure.identity import DefaultAzureCredential

credential = DefaultAzureCredential()
client = TextAnalyticsClient(endpoint, credential)
```

### REST API — Endpoint Structure

All Azure AI services follow a consistent REST pattern:

```
https://<resource-name>.cognitiveservices.azure.com/<service>/<version>/<operation>
```

**Examples:**
```
# Text Analytics - Sentiment
POST https://my-ai.cognitiveservices.azure.com/text/analytics/v3.1/sentiment

# Computer Vision - Analyze
POST https://my-ai.cognitiveservices.azure.com/vision/v3.2/analyze

# Azure OpenAI - Chat Completions
POST https://my-openai.openai.azure.com/openai/deployments/{deployment}/chat/completions?api-version=2024-02-01
```

### REST API — Authentication Headers

```http
# Key-based authentication
Ocp-Apim-Subscription-Key: <your-key>

# OR Bearer token (Azure AD)
Authorization: Bearer <access-token>
```

> ### 📝 Exam Tip
> Azure OpenAI uses a **different endpoint domain** (`openai.azure.com`) compared to other AI services (`cognitiveservices.azure.com`). The API key header is also different: `api-key` instead of `Ocp-Apim-Subscription-Key`.

---

## Container Deployment

Azure AI services can be deployed as Docker containers for **edge**, **air-gapped**, or **data-sovereignty** scenarios.

### Available Container Services

Not all services support containers. Key ones that do:

| Service | Container Available |
|---------|-------------------|
| Language (sentiment, NER, key phrases) | ✅ |
| Translator | ✅ (connected) |
| Speech (STT, TTS) | ✅ |
| Computer Vision (OCR/Read) | ✅ |
| Document Intelligence | ✅ |
| Face | ✅ |
| LUIS (legacy) | ✅ |

### Required Environment Variables

Every AI services container requires **three** environment variables:

| Variable | Required | Description |
|----------|----------|-------------|
| `ApiKey` | ✅ | Subscription key for billing authentication |
| `Billing` | ✅ | Endpoint URI of the Azure resource (for billing) |
| `Eula` | ✅ | Must be set to `accept` |

### Docker Run Example

```bash
docker run --rm -it \
    -p 5000:5000 \
    --memory 4g \
    --cpus 2 \
    -e ApiKey=<your-key> \
    -e Billing=https://my-ai.cognitiveservices.azure.com/ \
    -e Eula=accept \
    mcr.microsoft.com/azure-cognitive-services/textanalytics/sentiment:latest
```

### Key Container Concepts

- **Billing endpoint required**: Containers phone home to Azure for billing even when running locally. No internet = no processing after billing grace period.
- **Data stays local**: Input data is processed locally in the container; only billing/metering data is sent to Azure.
- **Same API surface**: The container exposes the same REST API as the cloud service on `http://localhost:5000`.

```python
# Calling a containerized service — same SDK, different endpoint
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Point to local container instead of cloud
client = TextAnalyticsClient(
    endpoint="http://localhost:5000",
    credential=AzureKeyCredential("<your-key>")
)

result = client.analyze_sentiment(["The service is running locally!"])
```

> ### 📝 Exam Tip
> The three required container environment variables (`ApiKey`, `Billing`, `Eula=accept`) are **heavily tested**. Know that containers still require an internet connection for billing — they are NOT fully offline.

---

## CI/CD Integration

### Azure DevOps Pipeline Example

```yaml
# azure-pipelines.yml
trigger:
  branches:
    include:
      - main

stages:
  - stage: DeployAI
    jobs:
      - job: ProvisionResources
        steps:
          - task: AzureCLI@2
            inputs:
              azureSubscription: 'my-service-connection'
              scriptType: bash
              scriptLocation: inlineScript
              inlineScript: |
                az deployment group create \
                  --resource-group rg-ai-prod \
                  --template-file infra/ai-services.bicep \
                  --parameters @infra/params.prod.json

      - job: DeployModel
        dependsOn: ProvisionResources
        steps:
          - task: AzureCLI@2
            inputs:
              azureSubscription: 'my-service-connection'
              scriptType: bash
              scriptLocation: inlineScript
              inlineScript: |
                az cognitiveservices account deployment create \
                  --name my-openai-prod \
                  --resource-group rg-ai-prod \
                  --deployment-name gpt-4o \
                  --model-name gpt-4o \
                  --model-version "2024-05-13" \
                  --model-format OpenAI \
                  --sku-capacity 20 \
                  --sku-name Standard
```

---

## Key Takeaways

1. **Three ways to create resources**: Portal (interactive), CLI (scriptable), Bicep/ARM (declarative, repeatable).
2. **`kind` property** determines which service(s) the resource provides — `CognitiveServices` for multi-service, specific values for single-service.
3. **Model deployment** in Azure OpenAI is a separate step from resource creation — you create the resource, then deploy models to it.
4. **SDK pattern**: Install service-specific package → create credential → create client → call operations.
5. **Container deployment** requires `ApiKey`, `Billing`, and `Eula=accept` environment variables and still needs internet for billing.
6. **REST endpoints** differ between standard AI services (`cognitiveservices.azure.com`) and OpenAI (`openai.azure.com`).

---

## Further Reading

- [Create Azure AI services resource](https://learn.microsoft.com/en-us/azure/ai-services/multi-service-resource)
- [Azure OpenAI deployment guide](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/create-resource)
- [Deploy AI services in containers](https://learn.microsoft.com/en-us/azure/ai-services/cognitive-services-container-support)
- [Azure AI services SDKs](https://learn.microsoft.com/en-us/azure/ai-services/reference/sdk-package-resources)
