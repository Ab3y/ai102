# AI-102 Lab Infrastructure Templates

Bicep templates for provisioning Azure AI services used in the AI-102 certification labs.

> **⚠️ Cost Warning:** These resources incur Azure charges. Delete them immediately after completing your lab exercises.

## Prerequisites

- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) installed
- An active Azure subscription
- Logged in via `az login`

## Template Catalog

| Template | Service | Key Parameters | Outputs |
|---|---|---|---|
| `ai-services.bicep` | AI Services (multi-service) | `resourceName`, `sku` (F0/S0) | `endpoint`, `resourceId` |
| `openai.bicep` | Azure OpenAI + model deployments | `resourceName`, `chatModelName`, `embeddingModelName` | `endpoint`, `resourceId` |
| `ai-search.bicep` | Azure AI Search | `searchServiceName`, `sku` (free/basic/standard) | `endpoint`, `adminKeyResourceId` |
| `document-intelligence.bicep` | Document Intelligence | `resourceName`, `sku` (F0/S0) | `endpoint`, `resourceId` |
| `speech.bicep` | Speech Services | `resourceName`, `sku` (F0/S0) | `endpoint`, `region`, `resourceId` |
| `vision.bicep` | Computer Vision | `resourceName`, `sku` (F0/S0/S1) | `endpoint`, `resourceId` |
| `ai-foundry.bicep` | AI Foundry hub + project | `hubName`, `projectName` | `hubResourceId`, `projectResourceId`, `storageAccountName`, `keyVaultName` |

## Estimated Monthly Cost (S0 SKU / basic tier)

| Template | Approx. Cost | Notes |
|---|---|---|
| `ai-services.bicep` | ~$1–5 | Pay-per-use; minimal if idle |
| `openai.bicep` | ~$1–10 | Pay-per-token; depends on usage |
| `ai-search.bicep` | ~$75 | Basic tier has a fixed monthly cost |
| `document-intelligence.bicep` | ~$1–5 | Pay-per-page processed |
| `speech.bicep` | ~$1–5 | Pay-per-audio-hour |
| `vision.bicep` | ~$1–5 | Pay-per-transaction |
| `ai-foundry.bicep` | ~$3–10 | Storage + Log Analytics costs |

> Use `F0` (free) SKUs where available to minimize cost during study.

## Deployment Commands

### Setup — create a resource group

```bash
az group create --name rg-ai102-labs --location eastus
```

### AI Services (multi-service)

```bash
az deployment group create \
  --resource-group rg-ai102-labs \
  --template-file infra/ai-services.bicep \
  --parameters resourceName=ai102-cognitive
```

### Azure OpenAI

```bash
az deployment group create \
  --resource-group rg-ai102-labs \
  --template-file infra/openai.bicep \
  --parameters resourceName=ai102-openai
```

### AI Search

```bash
az deployment group create \
  --resource-group rg-ai102-labs \
  --template-file infra/ai-search.bicep \
  --parameters searchServiceName=ai102-search
```

### Document Intelligence

```bash
az deployment group create \
  --resource-group rg-ai102-labs \
  --template-file infra/document-intelligence.bicep \
  --parameters resourceName=ai102-docintell
```

### Speech Services

```bash
az deployment group create \
  --resource-group rg-ai102-labs \
  --template-file infra/speech.bicep \
  --parameters resourceName=ai102-speech
```

### Computer Vision

```bash
az deployment group create \
  --resource-group rg-ai102-labs \
  --template-file infra/vision.bicep \
  --parameters resourceName=ai102-vision
```

### AI Foundry Hub + Project

```bash
az deployment group create \
  --resource-group rg-ai102-labs \
  --template-file infra/ai-foundry.bicep \
  --parameters hubName=ai102-hub projectName=ai102-project
```

## Retrieving Keys and Endpoints

```bash
# AI Services / OpenAI / Speech / Vision / Document Intelligence
az cognitiveservices account keys list \
  --resource-group rg-ai102-labs \
  --name <resourceName>

# AI Search admin key
az search admin-key show \
  --resource-group rg-ai102-labs \
  --service-name <searchServiceName>
```

## Cleanup

Delete **all** lab resources in one command:

```bash
az group delete --name rg-ai102-labs --yes --no-wait
```

Or delete individual resources:

```bash
az resource delete --ids <resourceId>
```
