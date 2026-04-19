# AI-102 Hands-On Lab Index & Walkthrough Guide

> **Master reference** for all AI-102 certification labs.
> Links every Bicep template, Python script, REST API sample, and PowerShell script in this repo.

| Module | Domain | Exam Weight | Labs |
|--------|--------|-------------|------|
| 1 | Plan & Manage Azure AI Solutions | 15–20% | 5 |
| 2 | Implement Generative AI Solutions | 15–20% | 5 |
| 3 | Implement Agentic AI Solutions | 5–10% | 2 |
| 4 | Implement Computer Vision Solutions | 15–20% | 4 |
| 5 | Implement NLP Solutions | 25–30% | 4 |
| 6 | Knowledge Mining & Document Intelligence | 10–15% | 3 |
| E2E | End-to-End Integration | — | 1 |
| **Total** | | **100%** | **24** |

---

## Lab Environment Setup

### Prerequisites

| Tool | Minimum Version | Install |
|------|----------------|---------|
| Azure Subscription | Pay-As-You-Go or MSDN | [azure.microsoft.com/free](https://azure.microsoft.com/free) |
| Python | 3.10+ | [python.org/downloads](https://www.python.org/downloads/) |
| Azure CLI | 2.60+ | `winget install Microsoft.AzureCLI` |
| VS Code | Latest | `winget install Microsoft.VisualStudioCode` |
| Docker Desktop | 4.x | `winget install Docker.DockerDesktop` |
| Git | 2.40+ | `winget install Git.Git` |
| REST Client (VS Code) | Latest | Extension: `humao.rest-client` |
| Bicep CLI | 0.25+ | Ships with Azure CLI |

### Clone This Repo and MS Learn Lab Repos

```bash
# This repo (primary)
git clone https://github.com/YOUR-ORG/AI102.git
cd AI102

# MS Learn companion repos
git clone https://github.com/MicrosoftLearning/mslearn-ai-studio.git        ../mslearn-ai-studio
git clone https://github.com/MicrosoftLearning/mslearn-ai-vision.git         ../mslearn-ai-vision
git clone https://github.com/MicrosoftLearning/mslearn-ai-language.git        ../mslearn-ai-language
git clone https://github.com/MicrosoftLearning/mslearn-ai-document-intelligence.git ../mslearn-ai-document-intelligence
git clone https://github.com/MicrosoftLearning/mslearn-knowledge-mining.git   ../mslearn-knowledge-mining
```

### Create Resource Group and Deploy Base AI Services

```bash
# Login and set subscription
az login
az account set -s "<subscription-id>"

# Create resource group
az group create -n ai102-labs-rg -l eastus

# Deploy multi-service AI resource (Bicep)
az deployment group create \
  -g ai102-labs-rg \
  -f infra/ai-services.bicep \
  --parameters name=ai102-services location=eastus sku=S0

# Automated lab provisioning (all-in-one)
pwsh scripts/powershell/provision-lab-environment.ps1
```

### Python Virtual Environment Setup

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### Environment Variables

```bash
cp .env.template .env
# Edit .env with your resource keys and endpoints
```

The `.env.template` includes:

| Variable | Service |
|----------|---------|
| `AI_SERVICES_ENDPOINT` / `AI_SERVICES_KEY` | Azure AI Services (multi-service) |
| `AZURE_OPENAI_ENDPOINT` / `AZURE_OPENAI_KEY` | Azure OpenAI |
| `SEARCH_ENDPOINT` / `SEARCH_ADMIN_KEY` | Azure AI Search |
| `SPEECH_KEY` / `SPEECH_REGION` | Speech Services |
| `DOC_INTELLIGENCE_ENDPOINT` / `DOC_INTELLIGENCE_KEY` | Document Intelligence |

### Estimated Cost

| Duration | Estimated Cost | Notes |
|----------|---------------|-------|
| 2–3 weeks | **$30–60** | Tear down resources after each session |
| Full 12-week course | $80–150 | Use free-tier where possible |

> **Cost tip:** Always run cleanup commands after lab sessions. OpenAI model deployments and AI Search indexes are the biggest cost drivers.

### Cleanup Commands

```bash
# Delete everything in one shot
az group delete -n ai102-labs-rg --yes --no-wait

# Automated cleanup script
pwsh scripts/powershell/cleanup-lab-environment.ps1
```

---

# Module 1 — Plan and Manage an Azure AI Solution

> **Exam Weight: 15–20%** | 5 Labs

---

## Lab 1.1: Provision and Explore Azure AI Services

**Module:** 1 | **Exam Weight:** 15–20% | **Estimated Time:** 45 min | **Cost:** ~$0.50

### Objective

Create a multi-service Azure AI resource three ways (Portal, CLI, Bicep), then test it with both the REST API and the Python SDK.

### Azure Resources Needed

- Resource Group: `ai102-labs-rg`
- Azure AI Services (multi-service, S0 tier)

### Step-by-Step Walkthrough

1. **Portal method** — Navigate to Azure Portal → Create a resource → Search "Azure AI services" → Create with S0 tier in `ai102-labs-rg`.
2. **CLI method:**
   ```bash
   az cognitiveservices account create \
     -n ai102-services-cli -g ai102-labs-rg \
     -l eastus --kind CognitiveServices --sku S0 \
     --yes
   ```
3. **Bicep method:**
   ```bash
   az deployment group create \
     -g ai102-labs-rg -f infra/ai-services.bicep \
     --parameters name=ai102-services location=eastus sku=S0
   ```
4. **Retrieve keys and endpoint:**
   ```bash
   az cognitiveservices account keys list -n ai102-services-cli -g ai102-labs-rg
   az cognitiveservices account show -n ai102-services-cli -g ai102-labs-rg --query properties.endpoint
   ```
5. **Update `.env`** with the endpoint and key values.
6. **Test with REST API** — Open `scripts/rest-api/detect-language.http` in VS Code with the REST Client extension. Send the request and inspect the response for detected language and confidence score.
7. **Test with Python SDK:**
   ```bash
   python scripts/python/services/provision-and-test.py
   ```
8. Verify both methods return a detected language with confidence > 0.9.

### Repo Files

| File | Purpose |
|------|---------|
| `infra/ai-services.bicep` | Bicep template — deploys multi-service AI resource |
| `scripts/python/services/provision-and-test.py` | Python SDK — tests language detection |
| `scripts/rest-api/detect-language.http` | REST API — language detection request |
| `scripts/powershell/provision-lab-environment.ps1` | Automated provisioning script |

### Exam-Relevant Takeaways

> **EXAM TIP:** The multi-service resource (`kind: CognitiveServices`) provides a single key for Language, Vision, Speech, and more. Use it unless you need service-specific networking or pricing.

> **EXAM TIP:** Know the three provisioning methods and when to use each. Bicep/ARM is required for repeatable IaC deployments.

> **EXAM TIP:** The REST API endpoint pattern is: `https://<name>.cognitiveservices.azure.com/<service>/<version>/<operation>`

### Cleanup

```bash
az cognitiveservices account delete -n ai102-services-cli -g ai102-labs-rg
```

---

## Lab 1.2: Secure Azure AI Services

**Module:** 1 | **Exam Weight:** 15–20% | **Estimated Time:** 60 min | **Cost:** ~$1

### Objective

Secure an Azure AI Services resource using Key Vault for secret management, managed identity for keyless authentication, RBAC roles, and Private Link for network isolation.

### Azure Resources Needed

- Azure AI Services (from Lab 1.1)
- Azure Key Vault
- Virtual Network (for Private Link)
- Managed Identity

### Step-by-Step Walkthrough

1. **Create a Key Vault:**
   ```bash
   az keyvault create -n ai102-kv-$RANDOM -g ai102-labs-rg -l eastus
   ```
2. **Store the AI Services key in Key Vault:**
   ```bash
   KEY=$(az cognitiveservices account keys list -n ai102-services -g ai102-labs-rg --query key1 -o tsv)
   az keyvault secret set --vault-name ai102-kv --name ai-services-key --value $KEY
   ```
3. **Enable system-assigned managed identity** on your compute resource (VM, App Service, or local dev with `az login`).
4. **Assign RBAC — Cognitive Services User** role:
   ```bash
   az role assignment create \
     --assignee <principal-id> \
     --role "Cognitive Services User" \
     --scope /subscriptions/<sub-id>/resourceGroups/ai102-labs-rg
   ```
5. **Configure Private Link** (optional — exam-relevant but costly):
   ```bash
   az network private-endpoint create \
     -n ai102-pe -g ai102-labs-rg --vnet-name ai102-vnet \
     --subnet default --private-connection-resource-id <resource-id> \
     --group-id account --connection-name ai102-pe-conn
   ```
6. **Run the secure access script:**
   ```bash
   python scripts/python/services/secure-access.py
   ```
7. Verify the script authenticates using `DefaultAzureCredential` (managed identity → CLI → environment variables fallback chain).

### Repo Files

| File | Purpose |
|------|---------|
| `scripts/python/services/secure-access.py` | Python — demonstrates Key Vault + managed identity auth |

### Exam-Relevant Takeaways

> **EXAM TIP:** `DefaultAzureCredential` tries these in order: Environment → Managed Identity → Azure CLI → Interactive Browser. Managed identity is the production-recommended approach.

> **EXAM TIP:** The `Cognitive Services User` role allows calling APIs. `Cognitive Services Contributor` allows managing resources but NOT calling APIs.

> **EXAM TIP:** Private Link creates a private IP in your VNet. Set `publicNetworkAccess: Disabled` to force all traffic through the private endpoint.

### Cleanup

```bash
az keyvault delete -n ai102-kv -g ai102-labs-rg
az keyvault purge -n ai102-kv
```

---

## Lab 1.3: Monitor Azure AI Services

**Module:** 1 | **Exam Weight:** 15–20% | **Estimated Time:** 30 min | **Cost:** ~$0.50

### Objective

Configure diagnostic settings, send logs to Log Analytics, create alert rules, and explore built-in metrics for Azure AI Services.

### Azure Resources Needed

- Azure AI Services (from Lab 1.1)
- Log Analytics Workspace

### Step-by-Step Walkthrough

1. **Run the monitoring configuration script:**
   ```bash
   pwsh scripts/powershell/configure-monitoring.ps1
   ```
2. **Verify diagnostic settings** in the Portal: AI Services resource → Diagnostic settings → Confirm Log Analytics destination.
3. **Generate traffic** — Run Lab 1.1 tests to create API calls.
4. **Query logs** in Log Analytics (allow 5–10 min for ingestion):
   ```kusto
   AzureDiagnostics
   | where ResourceType == "COGNITIVESERVICES"
   | summarize count() by OperationName, bin(TimeGenerated, 1h)
   | order by TimeGenerated desc
   ```
5. **Explore built-in metrics:** AI Services → Metrics → Select "Total Calls", "Total Errors", "Latency".
6. **Create an alert rule:** Metrics → New alert rule → Total Errors > 10 in 5 min → Action group (email).

### Repo Files

| File | Purpose |
|------|---------|
| `scripts/powershell/configure-monitoring.ps1` | PowerShell — configures diagnostic settings + Log Analytics |

### Exam-Relevant Takeaways

> **EXAM TIP:** Diagnostic settings categories for AI Services: `Audit`, `RequestResponse`, `Trace`. Request/Response logs are the most useful for debugging.

> **EXAM TIP:** Metrics are available immediately; logs take 5–15 minutes to appear in Log Analytics.

> **EXAM TIP:** Use `AzureMetrics` table for numeric data and `AzureDiagnostics` for detailed request/response logs.

### Cleanup

```bash
az monitor diagnostic-settings delete -n ai102-diag --resource <resource-id>
```

---

## Lab 1.4: Deploy AI Services in Containers

**Module:** 1 | **Exam Weight:** 15–20% | **Estimated Time:** 45 min | **Cost:** ~$2

### Objective

Pull an AI Services container image, configure required environment variables (`ApiKey`, `Billing`, `Eula`), run it locally with Docker, and deploy to Azure Container Instances (ACI).

### Azure Resources Needed

- Azure AI Services (for billing endpoint)
- Docker Desktop (local)
- Azure Container Instances

### Step-by-Step Walkthrough

1. **Pull the Language container image:**
   ```bash
   docker pull mcr.microsoft.com/azure-cognitive-services/textanalytics/language:latest
   ```
2. **Run locally with required environment variables:**
   ```bash
   docker run --rm -p 5000:5000 \
     -e ApiKey=<your-key> \
     -e Billing=https://<your-resource>.cognitiveservices.azure.com/ \
     -e Eula=accept \
     mcr.microsoft.com/azure-cognitive-services/textanalytics/language:latest
   ```
3. **Test the local container:**
   ```bash
   curl -X POST "http://localhost:5000/text/analytics/v3.1/languages" \
     -H "Content-Type: application/json" \
     -d '{"documents":[{"id":"1","text":"Hello world"}]}'
   ```
4. **Deploy to ACI using the PowerShell script:**
   ```bash
   pwsh scripts/powershell/deploy-container.ps1
   ```
5. **Verify ACI deployment:**
   ```bash
   az container show -n ai102-container -g ai102-labs-rg --query instanceView.state
   ```
6. Test the ACI endpoint the same way as step 3, replacing `localhost:5000` with the ACI FQDN.

### Repo Files

| File | Purpose |
|------|---------|
| `scripts/powershell/deploy-container.ps1` | PowerShell — deploys AI Services container to ACI |

### Exam-Relevant Takeaways

> **EXAM TIP:** Three **required** environment variables for all AI Services containers: `ApiKey`, `Billing` (endpoint URL), and `Eula=accept`. The container still calls Azure for billing — it does NOT run fully offline.

> **EXAM TIP:** Containers enable data sovereignty (data stays on-premises) and reduce latency, but they still require network connectivity to the billing endpoint.

> **EXAM TIP:** The container exposes the same REST API as the cloud service. No code changes needed to switch between cloud and container.

### Cleanup

```bash
az container delete -n ai102-container -g ai102-labs-rg --yes
docker rmi mcr.microsoft.com/azure-cognitive-services/textanalytics/language:latest
```

---

## Lab 1.5: Content Safety & Responsible AI

**Module:** 1 | **Exam Weight:** 15–20% | **Estimated Time:** 40 min | **Cost:** ~$0.50

### Objective

Use the Azure AI Content Safety SDK to analyze text and images for harmful content, configure severity thresholds, manage custom blocklists, and understand prompt shields.

### Azure Resources Needed

- Azure AI Content Safety resource (or multi-service AI resource)

### Step-by-Step Walkthrough

1. **Ensure Content Safety is available** in your region (East US, West Europe, etc.).
2. **Update `.env`** with Content Safety endpoint and key (uses the same AI Services key if multi-service).
3. **Run the Content Safety script:**
   ```bash
   python scripts/python/services/content-safety.py
   ```
4. **Examine the output** — severity levels (0=safe, 2=low, 4=medium, 6=high) across four categories:
   - Hate
   - Self-Harm
   - Sexual
   - Violence
5. **Experiment with thresholds** — Modify the script to reject content at severity ≥ 2 vs ≥ 4 and observe differences.
6. **Create a custom blocklist:**
   ```python
   # In the script: add terms to a blocklist, then analyze text that includes them
   ```
7. **Understand Prompt Shields** — Review how jailbreak detection works for LLM inputs (covered deeper in Module 2).

### Repo Files

| File | Purpose |
|------|---------|
| `scripts/python/services/content-safety.py` | Python — Content Safety SDK text/image analysis |

### Exam-Relevant Takeaways

> **EXAM TIP:** Content Safety returns severity levels 0/2/4/6 (not 1–10). Categories: Hate, Self-Harm, Sexual, Violence.

> **EXAM TIP:** Blocklists are exact-match or regex patterns applied BEFORE the AI model analyzes content. They're additive to the built-in classifiers.

> **EXAM TIP:** Responsible AI: Know the six Microsoft principles — Fairness, Reliability & Safety, Privacy & Security, Inclusiveness, Transparency, Accountability. The exam tests scenario-based application of these.

### Cleanup

```bash
# No additional resources to clean up (uses existing AI Services resource)
```

---

# Module 2 — Implement Generative AI Solutions

> **Exam Weight: 15–20%** | 5 Labs

---

## Lab 2.1: Deploy and Use Azure OpenAI

**Module:** 2 | **Exam Weight:** 15–20% | **Estimated Time:** 60 min | **Cost:** ~$2

### Objective

Provision an Azure OpenAI resource, deploy GPT-4o and text-embedding-ada-002 models, and use chat completions with system messages, temperature, max_tokens, and other parameters.

### Azure Resources Needed

- Azure OpenAI resource (S0)
- Model deployments: `gpt-4o`, `text-embedding-ada-002`

### Step-by-Step Walkthrough

1. **Deploy Azure OpenAI with Bicep:**
   ```bash
   az deployment group create \
     -g ai102-labs-rg -f infra/openai.bicep \
     --parameters name=ai102-openai location=eastus
   ```
2. **Deploy models via CLI:**
   ```bash
   az cognitiveservices account deployment create \
     -n ai102-openai -g ai102-labs-rg \
     --deployment-name gpt-4o --model-name gpt-4o \
     --model-version "2024-05-13" --model-format OpenAI \
     --sku-capacity 10 --sku-name Standard

   az cognitiveservices account deployment create \
     -n ai102-openai -g ai102-labs-rg \
     --deployment-name text-embedding-ada-002 --model-name text-embedding-ada-002 \
     --model-version "2" --model-format OpenAI \
     --sku-capacity 10 --sku-name Standard
   ```
3. **Update `.env`** with the OpenAI endpoint and key.
4. **Test with REST API** — Open `scripts/rest-api/openai-chat.http` and send a chat completion request.
5. **Run the Python SDK script:**
   ```bash
   python scripts/python/openai/chat-completions.py
   ```
6. **Experiment with parameters:**
   - `temperature`: 0 (deterministic) → 1.0 (creative)
   - `max_tokens`: Limit response length
   - `top_p`: Nucleus sampling
   - `frequency_penalty` / `presence_penalty`: Control repetition
   - `stop`: Define stop sequences
7. **Test the system message** — Modify the system prompt to constrain the model's behavior (e.g., "You are a helpful travel agent. Only answer travel-related questions.").

### Repo Files

| File | Purpose |
|------|---------|
| `infra/openai.bicep` | Bicep — provisions Azure OpenAI resource |
| `scripts/python/openai/chat-completions.py` | Python — chat completions with parameter tuning |
| `scripts/rest-api/openai-chat.http` | REST — chat completion request |

### Exam-Relevant Takeaways

> **EXAM TIP:** The system message sets the model's persona and guardrails. It's processed first and cannot be overridden by user messages (but can be jailbroken without Content Safety).

> **EXAM TIP:** `temperature=0` gives deterministic output. `temperature` and `top_p` should NOT be modified simultaneously — pick one.

> **EXAM TIP:** Azure OpenAI uses deployment names, not model names, in API calls. The API version is required in the URL: `?api-version=2024-02-01`.

> **EXAM TIP:** Token limits are per-request. `max_tokens` controls completion length only; the prompt tokens count against the model's context window separately.

### Cleanup

```bash
az cognitiveservices account deployment delete -n ai102-openai -g ai102-labs-rg --deployment-name gpt-4o
az cognitiveservices account deployment delete -n ai102-openai -g ai102-labs-rg --deployment-name text-embedding-ada-002
```

---

## Lab 2.2: Implement RAG (Retrieval-Augmented Generation)

**Module:** 2 | **Exam Weight:** 15–20% | **Estimated Time:** 75 min | **Cost:** ~$3

### Objective

Build a RAG pipeline that uses Azure AI Search as a retrieval source to ground Azure OpenAI responses in your own data, reducing hallucinations.

### Azure Resources Needed

- Azure OpenAI (from Lab 2.1)
- Azure AI Search (Basic tier or higher for semantic ranking)
- Azure Storage Account (for source documents)

### Step-by-Step Walkthrough

1. **Deploy AI Search:**
   ```bash
   az deployment group create \
     -g ai102-labs-rg -f infra/ai-search.bicep \
     --parameters name=ai102-search location=eastus sku=basic
   ```
2. **Upload sample documents** to a blob container (PDFs, Word docs, or plain text).
3. **Create a search index with vector fields** using `scripts/python/search/create-index.py`.
4. **Generate embeddings** for your documents using the `text-embedding-ada-002` deployment.
5. **Run the RAG pattern script:**
   ```bash
   python scripts/python/openai/rag-pattern.py
   ```
6. **Examine the RAG flow:**
   - User query → Generate embedding → Vector search in AI Search → Retrieve top-k documents → Inject into system message as context → Send to GPT-4o → Grounded response
7. **Compare responses** with and without grounding data to see hallucination reduction.
8. **Test with the Azure OpenAI "On Your Data" feature** in Azure AI Studio as an alternative.

### Repo Files

| File | Purpose |
|------|---------|
| `scripts/python/openai/rag-pattern.py` | Python — end-to-end RAG pipeline |
| `scripts/python/search/create-index.py` | Python — creates AI Search index with vector fields |
| `scripts/python/search/query-index.py` | Python — queries the search index |
| `infra/ai-search.bicep` | Bicep — provisions AI Search resource |

### Exam-Relevant Takeaways

> **EXAM TIP:** RAG = Retrieve relevant docs → Augment the prompt with them → Generate a response. It's the primary pattern for grounding LLMs in enterprise data.

> **EXAM TIP:** "On Your Data" in Azure OpenAI automatically handles the RAG pipeline. For custom RAG, you control chunking, embedding, retrieval, and prompt construction.

> **EXAM TIP:** Vector search requires an embedding model (e.g., `text-embedding-ada-002`) and vector fields in the search index. Hybrid search combines keyword + vector for best results.

### Cleanup

```bash
az search service delete -n ai102-search -g ai102-labs-rg --yes
```

---

## Lab 2.3: Build with Microsoft AI Foundry

**Module:** 2 | **Exam Weight:** 15–20% | **Estimated Time:** 60 min | **Cost:** ~$2

### Objective

Create an AI Foundry hub and project, build a prompt flow, evaluate model outputs, and deploy a flow as a managed endpoint.

### Azure Resources Needed

- AI Foundry Hub + Project
- Azure OpenAI (from Lab 2.1)
- Azure AI Search (optional, for grounding)

### Step-by-Step Walkthrough

1. **Deploy AI Foundry with Bicep:**
   ```bash
   az deployment group create \
     -g ai102-labs-rg -f infra/ai-foundry.bicep \
     --parameters name=ai102-foundry location=eastus
   ```
2. **Open AI Foundry portal** at [ai.azure.com](https://ai.azure.com).
3. **Create a project** within the hub.
4. **Connect your Azure OpenAI resource** as a model endpoint.
5. **Build a prompt flow:**
   - Add an LLM node with a system prompt
   - Add an input node for user questions
   - Add a Python node for post-processing
   - Connect the nodes and test
6. **Run an evaluation:**
   - Upload a test dataset (question + expected answer pairs)
   - Select metrics: Groundedness, Relevance, Coherence, Fluency
   - Compare runs
7. **Deploy the flow** as a managed online endpoint.
8. **Test the deployed endpoint** with a REST call.

### Repo Files

| File | Purpose |
|------|---------|
| `infra/ai-foundry.bicep` | Bicep — provisions AI Foundry hub + dependencies |

### Exam-Relevant Takeaways

> **EXAM TIP:** AI Foundry hub = shared resources (compute, connections, storage). Project = isolated workspace within a hub for a specific use case.

> **EXAM TIP:** Prompt flow supports LLM, Python, and tool nodes. Evaluation metrics (Groundedness, Relevance, Coherence) help compare prompt engineering iterations.

> **EXAM TIP:** Know the relationship: Hub → Project → Flow → Deployment. Connections (to OpenAI, Search, etc.) are defined at the hub level and shared across projects.

### Cleanup

```bash
# Delete the entire hub and all projects
az ml workspace delete -n ai102-foundry -g ai102-labs-rg --all-resources --yes
```

---

## Lab 2.4: Generate Images with DALL-E

**Module:** 2 | **Exam Weight:** 15–20% | **Estimated Time:** 30 min | **Cost:** ~$1

### Objective

Use the Azure OpenAI DALL-E model to generate images from text prompts, control image size and quality, and handle content filtering.

### Azure Resources Needed

- Azure OpenAI resource with DALL-E 3 deployment

### Step-by-Step Walkthrough

1. **Deploy DALL-E 3:**
   ```bash
   az cognitiveservices account deployment create \
     -n ai102-openai -g ai102-labs-rg \
     --deployment-name dall-e-3 --model-name dall-e-3 \
     --model-version "3.0" --model-format OpenAI \
     --sku-capacity 1 --sku-name Standard
   ```
2. **Run the image generation script:**
   ```bash
   python scripts/python/openai/generate-images.py
   ```
3. **Experiment with parameters:**
   - `size`: `1024x1024`, `1024x1792`, `1792x1024`
   - `quality`: `standard` or `hd`
   - `style`: `vivid` or `natural`
   - `n`: Number of images (DALL-E 3 only supports `n=1`)
4. **Test content filtering** — Try a prompt that triggers the content filter and handle the error gracefully.
5. **Save and display** the generated image using the returned URL.

### Repo Files

| File | Purpose |
|------|---------|
| `scripts/python/openai/generate-images.py` | Python — DALL-E 3 image generation |

### Exam-Relevant Takeaways

> **EXAM TIP:** DALL-E 3 only supports `n=1` per request (unlike DALL-E 2). Generate multiple images with multiple requests.

> **EXAM TIP:** Image URLs returned by the API are temporary (expire within hours). Download and store them if persistence is needed.

> **EXAM TIP:** Content filtering applies to both prompts and generated images. The `revised_prompt` field shows how DALL-E modified your prompt for safety.

### Cleanup

```bash
az cognitiveservices account deployment delete -n ai102-openai -g ai102-labs-rg --deployment-name dall-e-3
```

---

## Lab 2.5: Fine-Tune a Model

**Module:** 2 | **Exam Weight:** 15–20% | **Estimated Time:** 90 min | **Cost:** ~$5–15

### Objective

Prepare JSONL training data, upload it to Azure OpenAI, create a fine-tuning job, and deploy the fine-tuned model.

### Azure Resources Needed

- Azure OpenAI resource (fine-tuning-supported region)

### Step-by-Step Walkthrough

1. **Prepare training data** in JSONL format (minimum 10 examples, recommended 50–100):
   ```json
   {"messages": [{"role": "system", "content": "You are a support agent."}, {"role": "user", "content": "How do I reset my password?"}, {"role": "assistant", "content": "Navigate to Settings > Security > Reset Password."}]}
   ```
2. **Validate the JSONL format:**
   ```python
   import json
   with open("training_data.jsonl") as f:
       for i, line in enumerate(f):
           json.loads(line)  # Validates each line
   print(f"Validated {i+1} training examples")
   ```
3. **Upload the training file:**
   ```bash
   az cognitiveservices account file upload \
     -n ai102-openai -g ai102-labs-rg \
     --file-path training_data.jsonl --purpose fine-tune
   ```
4. **Create a fine-tuning job** via the Azure AI Foundry portal or REST API.
5. **Monitor the job** — Training typically takes 30–60 minutes for small datasets.
6. **Deploy the fine-tuned model** as a new deployment.
7. **Test the fine-tuned model** and compare responses with the base model.

### Repo Files

| File | Purpose |
|------|---------|
| *No specific script — uses Azure portal and CLI* | |

### Exam-Relevant Takeaways

> **EXAM TIP:** Fine-tuning training data must be in JSONL (Chat format for GPT models). Each line is a complete conversation with system, user, and assistant messages.

> **EXAM TIP:** Fine-tuning is for adapting model behavior/style, NOT for adding knowledge (use RAG for that). Fine-tuning + RAG can be combined.

> **EXAM TIP:** Fine-tuned models incur higher per-token costs than base models and require their own deployment. They don't share capacity with base model deployments.

### Cleanup

```bash
# Delete the fine-tuned model deployment
az cognitiveservices account deployment delete -n ai102-openai -g ai102-labs-rg --deployment-name <fine-tuned-deployment>
```

---

# Module 3 — Implement Agentic AI Solutions

> **Exam Weight: 5–10%** | 2 Labs

---

## Lab 3.1: Build Custom Agents

**Module:** 3 | **Exam Weight:** 5–10% | **Estimated Time:** 60 min | **Cost:** ~$2

### Objective

Build a custom AI agent using Azure AI Foundry Agent Service with function calling, code interpreter, and file search tools.

### Azure Resources Needed

- Azure AI Foundry project (from Lab 2.3)
- Azure OpenAI with GPT-4o deployment

### Step-by-Step Walkthrough

1. **Open AI Foundry portal** → Navigate to your project.
2. **Create an Agent** with:
   - Model: GPT-4o
   - System instructions: Define the agent's role and boundaries
   - Tools: Enable `code_interpreter` and/or `file_search`
3. **Add function definitions** (tool calling):
   ```json
   {
     "type": "function",
     "function": {
       "name": "get_weather",
       "description": "Get current weather for a location",
       "parameters": {
         "type": "object",
         "properties": {
           "location": {"type": "string", "description": "City name"}
         },
         "required": ["location"]
       }
     }
   }
   ```
4. **Create a thread** and send messages.
5. **Handle tool calls** — When the model returns a `tool_calls` response, execute the function and return results.
6. **Test code interpreter** — Ask the agent to generate a chart from data. The agent writes and executes Python code in a sandbox.
7. **Test file search** — Upload documents and ask questions. The agent performs RAG automatically.
8. **Review conversation history** and token usage.

### Repo Files

| File | Purpose |
|------|---------|
| `scripts/python/agents/` | Directory for agent scripts (extend with your implementations) |

### Exam-Relevant Takeaways

> **EXAM TIP:** Agents manage state via threads (conversation history). The API handles message ordering, context window management, and tool execution orchestration.

> **EXAM TIP:** Function calling: the model decides WHEN to call a function based on the user's request. You implement the function execution and return results.

> **EXAM TIP:** Code interpreter runs Python in a sandboxed environment. It can process uploaded files (CSV, Excel) and generate visualizations.

### Cleanup

```bash
# Delete agents and threads via the API or portal
```

---

## Lab 3.2: Multi-Agent Orchestration

**Module:** 3 | **Exam Weight:** 5–10% | **Estimated Time:** 75 min | **Cost:** ~$3

### Objective

Implement a multi-agent pattern using a planner agent that delegates tasks to specialized executor agents, demonstrating orchestration and inter-agent communication.

### Azure Resources Needed

- Azure AI Foundry project
- Azure OpenAI with GPT-4o deployment
- Multiple agent definitions

### Step-by-Step Walkthrough

1. **Design the agent topology:**
   - **Planner Agent**: Receives user request, breaks it into sub-tasks, delegates to specialists
   - **Research Agent**: Searches documents and knowledge bases
   - **Writer Agent**: Generates formatted content based on research
2. **Create each agent** in AI Foundry with specialized system prompts and tool configurations.
3. **Implement the orchestration loop:**
   ```
   User Request → Planner → [Research Agent, Writer Agent] → Planner → Final Response
   ```
4. **Handle agent handoffs** — The planner sends structured instructions to each executor and aggregates results.
5. **Add guardrails:**
   - Maximum iteration count (prevent infinite loops)
   - Token budget per agent
   - Content safety checks between agents
6. **Test with a complex query** that requires multiple agents to collaborate.
7. **Review the full execution trace** — Inspect which agents were called, in what order, and their token usage.

### Repo Files

| File | Purpose |
|------|---------|
| `scripts/python/agents/` | Directory for multi-agent implementations |

### Exam-Relevant Takeaways

> **EXAM TIP:** Multi-agent patterns: Sequential (pipeline), Parallel (fan-out/fan-in), and Hierarchical (planner/executor). The exam tests when to use each.

> **EXAM TIP:** Each agent has its own system prompt and tools. The planner agent doesn't need all tools — it delegates to specialists.

> **EXAM TIP:** Guardrails are critical: max iterations, token budgets, and human-in-the-loop checkpoints for high-stakes decisions.

### Cleanup

```bash
# Delete all agents and threads via the API or portal
```

---

# Module 4 — Implement Computer Vision Solutions

> **Exam Weight: 15–20%** | 4 Labs

---

## Lab 4.1: Analyze Images with Azure AI Vision

**Module:** 4 | **Exam Weight:** 15–20% | **Estimated Time:** 45 min | **Cost:** ~$0.50

### Objective

Use the Azure AI Vision 4.0 API to analyze images — extracting captions, tags, objects, people, text (OCR), and smart-cropped thumbnails.

### Azure Resources Needed

- Azure AI Vision resource (or multi-service AI resource)

### Step-by-Step Walkthrough

1. **Deploy Vision resource with Bicep:**
   ```bash
   az deployment group create \
     -g ai102-labs-rg -f infra/vision.bicep \
     --parameters name=ai102-vision location=eastus
   ```
2. **Update `.env`** with the Vision endpoint and key.
3. **Test with REST API** — Open `scripts/rest-api/vision-analyze.http`:
   ```
   POST {{endpoint}}/computervision/imageanalysis:analyze?api-version=2024-02-01
   &features=caption,tags,objects,people,read,smartCrops
   ```
4. **Run the Python analysis script:**
   ```bash
   python scripts/python/vision/analyze-image.py
   ```
5. **Examine each feature:**
   - **Caption**: Natural language description with confidence score
   - **Tags**: Flat list of content tags
   - **Objects**: Bounding boxes with labels
   - **People**: Detected people with bounding boxes (no identification)
   - **Read (OCR)**: Extracted text with line/word positions
   - **Smart Crops**: Aspect-ratio-aware thumbnail regions
6. **Test with various image types** — Photos, documents, screenshots, scanned forms.
7. **Use a custom image URL vs. binary upload** — Note the difference in request body format.

### Repo Files

| File | Purpose |
|------|---------|
| `infra/vision.bicep` | Bicep — provisions Computer Vision resource |
| `scripts/python/vision/analyze-image.py` | Python — Vision 4.0 image analysis |
| `scripts/rest-api/vision-analyze.http` | REST — image analysis request |

### Exam-Relevant Takeaways

> **EXAM TIP:** Vision 4.0 uses a single `imageanalysis:analyze` endpoint with a `features` query parameter. Older versions used separate endpoints per feature.

> **EXAM TIP:** OCR ("Read") in Vision 4.0 replaces the old Computer Vision Read API. It handles printed and handwritten text, multi-language, and mixed content.

> **EXAM TIP:** Images can be sent as a URL (`{"url": "..."}`) or binary data (`application/octet-stream`). Max image size: 20 MB. Min dimensions: 50×50 pixels.

### Cleanup

```bash
az cognitiveservices account delete -n ai102-vision -g ai102-labs-rg
```

---

## Lab 4.2: Custom Vision Models

**Module:** 4 | **Exam Weight:** 15–20% | **Estimated Time:** 60 min | **Cost:** ~$1

### Objective

Train custom image classification and object detection models using the Custom Vision service, both via the portal and code-first with the Python SDK.

### Azure Resources Needed

- Custom Vision resource (Training + Prediction)
- Training images (minimum 5 per class, recommended 50+)

### Step-by-Step Walkthrough

1. **Create Custom Vision resources:**
   ```bash
   az cognitiveservices account create \
     -n ai102-cv-training -g ai102-labs-rg -l eastus \
     --kind CustomVision.Training --sku S0
   az cognitiveservices account create \
     -n ai102-cv-prediction -g ai102-labs-rg -l eastus \
     --kind CustomVision.Prediction --sku S0
   ```
2. **Prepare training images** — Organize into folders by class (e.g., `cats/`, `dogs/`).
3. **Run the code-first training script:**
   ```bash
   python scripts/python/vision/custom-vision-train.py
   ```
4. **The script performs:**
   - Create a project (classification or object detection)
   - Upload and tag images
   - Train an iteration
   - Publish the trained iteration
   - Test with a new image
5. **Also try the portal workflow** at [customvision.ai](https://www.customvision.ai).
6. **Export the model** (optional) — Compact domains allow export to ONNX, TensorFlow, CoreML, or Docker.
7. **Compare classification types:**
   - Multiclass: One label per image
   - Multilabel: Multiple labels per image

### Repo Files

| File | Purpose |
|------|---------|
| `scripts/python/vision/custom-vision-train.py` | Python — Custom Vision SDK training + prediction |

### Exam-Relevant Takeaways

> **EXAM TIP:** Custom Vision requires TWO resources: Training and Prediction. They have different endpoints and keys.

> **EXAM TIP:** Minimum images per tag: 5 (classification) or 15 (object detection). Recommended: 50+ per tag for good accuracy.

> **EXAM TIP:** Use "Compact" domains to export models for edge deployment (ONNX, TensorFlow). "General" domains are cloud-only but more accurate.

> **EXAM TIP:** Object detection requires bounding box annotations (normalized 0–1 coordinates: left, top, width, height).

### Cleanup

```bash
az cognitiveservices account delete -n ai102-cv-training -g ai102-labs-rg
az cognitiveservices account delete -n ai102-cv-prediction -g ai102-labs-rg
```

---

## Lab 4.3: Analyze Videos with Video Indexer

**Module:** 4 | **Exam Weight:** 15–20% | **Estimated Time:** 45 min | **Cost:** ~$2

### Objective

Use Azure Video Indexer to extract insights from video content — transcripts, faces, topics, sentiments, OCR, labels, and spatial analysis.

### Azure Resources Needed

- Azure Video Indexer account
- Sample video file(s)

### Step-by-Step Walkthrough

1. **Create a Video Indexer account** at [videoindexer.ai](https://www.videoindexer.ai) (trial or paid).
2. **Upload a sample video** via the portal or API.
3. **Wait for indexing** to complete (time depends on video length).
4. **Explore extracted insights:**
   - **Transcript**: Full speech-to-text with timestamps and speaker identification
   - **Topics**: Key topics and named entities
   - **Sentiment**: Per-sentence sentiment analysis
   - **OCR**: Text detected in video frames
   - **Labels**: Scene and object labels per frame
   - **Faces**: Detected faces (identification requires approval)
   - **Scenes & Keyframes**: Automatic scene boundary detection
5. **Use the API** to retrieve insights programmatically:
   ```
   GET https://api.videoindexer.ai/{location}/Accounts/{accountId}/Videos/{videoId}/Index
   ```
6. **Embed the Video Indexer widget** in a web page using the provided iframe URL.
7. **Review spatial analysis** concepts — People counting, zone monitoring, social distancing (requires IoT Edge).

### Repo Files

| File | Purpose |
|------|---------|
| *Portal-based lab — no script files* | |

### Exam-Relevant Takeaways

> **EXAM TIP:** Video Indexer provides a unified JSON output with all insights. No need to call individual services (Speech, Vision, Language) separately.

> **EXAM TIP:** Face identification in videos requires Limited Access approval from Microsoft (Responsible AI policy).

> **EXAM TIP:** Spatial analysis (people counting, movement tracking) uses a separate Vision container deployed to IoT Edge — it's NOT part of Video Indexer.

### Cleanup

```bash
# Delete videos from the Video Indexer portal
```

---

## Lab 4.4: Face Detection and Analysis

**Module:** 4 | **Exam Weight:** 15–20% | **Estimated Time:** 30 min | **Cost:** ~$0.50

### Objective

Use the Azure AI Face API to detect faces, extract attributes (head pose, blur, occlusion, accessories), and understand responsible AI restrictions on identification and verification.

### Azure Resources Needed

- Azure AI Face resource (or multi-service)

### Step-by-Step Walkthrough

1. **Create a Face API resource** (or use multi-service AI resource).
2. **Detect faces in an image:**
   ```
   POST https://<endpoint>/face/v1.0/detect?returnFaceAttributes=headPose,blur,exposure,noise,occlusion,accessories
   ```
3. **Examine returned attributes:**
   - Face rectangle (bounding box)
   - Head pose (pitch, roll, yaw)
   - Blur, exposure, noise levels
   - Occlusion (forehead, eyes, mouth)
   - Accessories (glasses, headwear, mask)
4. **Understand the Limited Access gate:**
   - Face **detection** = freely available
   - Face **identification** and **verification** = requires approval form
   - Face **recognition** (Celebrity, emotion) = retired
5. **Test face comparison** (if approved):
   - Create a PersonGroup
   - Add persons with multiple face images
   - Train the PersonGroup
   - Identify unknown faces against the group
6. **Review the responsible AI principles** specific to facial recognition.

### Repo Files

| File | Purpose |
|------|---------|
| *Uses REST API calls — extend with custom scripts* | |

### Exam-Relevant Takeaways

> **EXAM TIP:** Face detection (bounding box + attributes) is freely available. Face identification/verification requires Limited Access approval.

> **EXAM TIP:** The emotion recognition and celebrity recognition features have been **retired** as of June 2023.

> **EXAM TIP:** Face identification workflow: Create PersonGroup → Add Persons → Add Faces → Train → Identify. Each PersonGroup supports up to 10,000 persons (or 1M with LargePersonGroup).

### Cleanup

```bash
# Delete PersonGroups via API
# DELETE https://<endpoint>/face/v1.0/persongroups/{personGroupId}
```

---

# Module 5 — Implement Natural Language Processing Solutions

> **Exam Weight: 25–30%** | 4 Labs

---

## Lab 5.1: Text Analytics

**Module:** 5 | **Exam Weight:** 25–30% | **Estimated Time:** 45 min | **Cost:** ~$0.50

### Objective

Use the Azure AI Language service to perform sentiment analysis, key phrase extraction, named entity recognition (NER), PII detection, and entity linking.

### Azure Resources Needed

- Azure AI Language resource (or multi-service)

### Step-by-Step Walkthrough

1. **Update `.env`** with the Language endpoint and key.
2. **Test with REST API** — Open `scripts/rest-api/text-analytics.http` and send requests for each operation.
3. **Run the Python SDK script:**
   ```bash
   python scripts/python/language/text-analytics.py
   ```
4. **Sentiment Analysis:**
   - Returns document-level and sentence-level sentiment (Positive, Negative, Neutral, Mixed)
   - Confidence scores for each sentiment
   - Opinion mining returns aspect-based sentiment (e.g., "The food was great" → food: positive)
5. **Key Phrase Extraction:** Returns important phrases without duplicates.
6. **Named Entity Recognition (NER):** Detects and categorizes entities (Person, Location, Organization, DateTime, Quantity, etc.).
7. **PII Detection:** Identifies and redacts personal data (SSN, email, phone, address). Returns redacted text and entity details.
8. **Entity Linking:** Disambiguates entities to Wikipedia entries (e.g., "Mars" → planet vs. company).
9. **Test with multi-language content** — The service auto-detects language.

### Repo Files

| File | Purpose |
|------|---------|
| `scripts/python/language/text-analytics.py` | Python — all text analytics operations |
| `scripts/rest-api/text-analytics.http` | REST — text analytics requests |

### Exam-Relevant Takeaways

> **EXAM TIP:** PII detection returns `redactedText` with entities replaced by `*****`. Entity types include SSN, email, phone, credit card, etc.

> **EXAM TIP:** Sentiment analysis with opinion mining uses `show_opinion_mining=True`. It returns aspect-based sentiment (target + assessment pairs).

> **EXAM TIP:** All text analytics operations accept up to 5,120 characters per document and 25 documents per request (synchronous). Async supports larger batches.

> **EXAM TIP:** Entity linking uses Wikipedia as the knowledge base. NER categorizes but doesn't disambiguate. Use entity linking when you need to distinguish between entities with the same name.

### Cleanup

```bash
# No additional resources to clean up (uses existing AI Services resource)
```

---

## Lab 5.2: Translate Text and Speech

**Module:** 5 | **Exam Weight:** 25–30% | **Estimated Time:** 40 min | **Cost:** ~$0.50

### Objective

Use Azure Translator for real-time text translation, language detection, transliteration, and custom translator with glossaries.

### Azure Resources Needed

- Azure Translator resource (or multi-service)

### Step-by-Step Walkthrough

1. **Create a Translator resource** (if not using multi-service):
   ```bash
   az cognitiveservices account create \
     -n ai102-translator -g ai102-labs-rg -l global \
     --kind TextTranslation --sku S1
   ```
2. **Translate text** via REST API:
   ```
   POST https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=fr&to=es
   Ocp-Apim-Subscription-Key: <key>
   Ocp-Apim-Subscription-Region: <region>
   ```
3. **Detect language:**
   ```
   POST https://api.cognitive.microsofttranslator.com/detect?api-version=3.0
   ```
4. **Transliterate** (convert script, e.g., Japanese Kanji → Romaji):
   ```
   POST https://api.cognitive.microsofttranslator.com/transliterate?api-version=3.0&language=ja&fromScript=Jpan&toScript=Latn
   ```
5. **Dictionary lookup** — Find alternative translations for specific words.
6. **Custom Translator** (portal-based):
   - Upload parallel sentence pairs (source + target language)
   - Train a custom model
   - Use `category` parameter in translate requests to use your custom model
7. **Test translation of technical/domain-specific content** to see where custom models improve quality.

### Repo Files

| File | Purpose |
|------|---------|
| *Extend with custom scripts as needed* | |

### Exam-Relevant Takeaways

> **EXAM TIP:** Translator uses a **global** endpoint (`api.cognitive.microsofttranslator.com`) with the subscription region in a header (`Ocp-Apim-Subscription-Region`).

> **EXAM TIP:** You can translate to multiple languages in one request by adding multiple `&to=` parameters.

> **EXAM TIP:** Custom Translator requires parallel corpora (aligned sentence pairs). Use the `category` query parameter to route requests to your custom model.

> **EXAM TIP:** Document Translation API translates entire documents (Word, PDF, HTML) while preserving formatting. It uses a different endpoint and requires blob storage.

### Cleanup

```bash
az cognitiveservices account delete -n ai102-translator -g ai102-labs-rg
```

---

## Lab 5.3: Speech Services

**Module:** 5 | **Exam Weight:** 25–30% | **Estimated Time:** 50 min | **Cost:** ~$1

### Objective

Implement speech-to-text (STT), text-to-speech (TTS), and deep dive into SSML (Speech Synthesis Markup Language) for fine-grained voice control.

### Azure Resources Needed

- Azure Speech resource (or multi-service)
- Microphone/speakers (for real-time STT/TTS testing)

### Step-by-Step Walkthrough

1. **Deploy Speech resource with Bicep:**
   ```bash
   az deployment group create \
     -g ai102-labs-rg -f infra/speech.bicep \
     --parameters name=ai102-speech location=eastus
   ```
2. **Update `.env`** with `SPEECH_KEY` and `SPEECH_REGION`.
3. **Run speech-to-text:**
   ```bash
   python scripts/python/speech/speech-to-text.py
   ```
4. **STT features to explore:**
   - Continuous recognition (for long audio)
   - Language detection (auto-detect source language)
   - Pronunciation assessment
   - Keyword spotting (wake word detection)
5. **Run text-to-speech:**
   ```bash
   python scripts/python/speech/text-to-speech.py
   ```
6. **TTS features and SSML:**
   ```xml
   <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
          xmlns:mstts="http://www.w3.org/2001/mstts" xml:lang="en-US">
     <voice name="en-US-JennyNeural">
       <mstts:express-as style="cheerful" styledegree="2">
         Welcome to the lab!
       </mstts:express-as>
       <prosody rate="-10%" pitch="+5%">
         Let me explain <break time="500ms"/> the key concepts.
       </prosody>
       <phoneme alphabet="ipa" ph="ˈkɒɡnɪtɪv">cognitive</phoneme>
     </voice>
   </speak>
   ```
7. **Test SSML elements:**
   - `<voice>`: Select neural voice
   - `<prosody>`: Rate, pitch, volume
   - `<break>`: Pauses
   - `<mstts:express-as>`: Emotion styles (cheerful, sad, angry, etc.)
   - `<phoneme>`: Custom pronunciation
   - `<say-as>`: Interpret content (date, time, telephone, cardinal, ordinal)
8. **Test audio file input/output** vs. microphone/speaker.

### Repo Files

| File | Purpose |
|------|---------|
| `infra/speech.bicep` | Bicep — provisions Speech resource |
| `scripts/python/speech/speech-to-text.py` | Python — speech-to-text recognition |
| `scripts/python/speech/text-to-speech.py` | Python — text-to-speech synthesis with SSML |

### Exam-Relevant Takeaways

> **EXAM TIP:** SSML is heavily tested. Know these elements: `<voice>`, `<prosody>` (rate/pitch/volume), `<break>`, `<mstts:express-as>` (styles), `<phoneme>`, `<say-as>`.

> **EXAM TIP:** Speech-to-text supports `RecognizeOnceAsync()` (single utterance) and `StartContinuousRecognitionAsync()` (ongoing). Use continuous for conversations.

> **EXAM TIP:** Speech SDK uses `SpeechConfig` (key + region) and `AudioConfig` (input/output). Default audio is microphone/speaker; use `AudioConfig.from_wav_file()` for files.

> **EXAM TIP:** Custom Neural Voice requires application and consent from the voice talent. Custom Speech (STT) uses training data to improve accuracy for domain-specific vocabulary.

### Cleanup

```bash
az cognitiveservices account delete -n ai102-speech -g ai102-labs-rg
```

---

## Lab 5.4: Custom Language Models (CLU & Question Answering)

**Module:** 5 | **Exam Weight:** 25–30% | **Estimated Time:** 60 min | **Cost:** ~$1

### Objective

Build a Conversational Language Understanding (CLU) model with intents and entities, and create a Question Answering knowledge base from documents and FAQ pages.

### Azure Resources Needed

- Azure AI Language resource (S tier for custom models)

### Step-by-Step Walkthrough

**Part A — Conversational Language Understanding (CLU):**

1. **Open Language Studio** at [language.cognitive.azure.com](https://language.cognitive.azure.com).
2. **Create a CLU project:**
   - Project type: Conversation
   - Add intents: `OrderPizza`, `CheckStatus`, `CancelOrder`
   - Add entities: `PizzaSize`, `PizzaTopping`, `OrderId`
3. **Add utterances** (10–15 per intent):
   - "I want to order a large pepperoni pizza" → Intent: `OrderPizza`, Entities: Size=large, Topping=pepperoni
   - "Where is my order #12345?" → Intent: `CheckStatus`, Entity: OrderId=12345
4. **Train the model** → Select standard training.
5. **Evaluate** — Review precision, recall, and F1 per intent/entity.
6. **Deploy** the model to a deployment slot.
7. **Query the deployed model** via REST:
   ```
   POST https://<endpoint>/language/:analyze-conversations?api-version=2023-04-01
   ```

**Part B — Question Answering:**

1. **Create a Question Answering project** in Language Studio.
2. **Add knowledge sources:**
   - URL (FAQ page): Add a public FAQ URL to auto-extract Q&A pairs
   - Manual: Add custom question-answer pairs
   - File: Upload a document (Word, PDF, TSV)
3. **Add follow-up prompts** for multi-turn conversations.
4. **Add chit-chat** personality (Professional, Friendly, Witty, etc.).
5. **Test in Language Studio** — Ask questions and review confidence scores.
6. **Deploy** the knowledge base.
7. **Query via REST:**
   ```
   POST https://<endpoint>/language/:query-knowledgebases?api-version=2021-10-01
   ```

### Repo Files

| File | Purpose |
|------|---------|
| *Portal-based lab — use Language Studio* | |

### Exam-Relevant Takeaways

> **EXAM TIP:** CLU replaces LUIS (Language Understanding). LUIS is deprecated — all exam content now references CLU.

> **EXAM TIP:** CLU entities: Learned (ML-based, needs labeled examples), List (exact match dictionary), Prebuilt (datetime, number, email, etc.), Regex (pattern-based).

> **EXAM TIP:** Question Answering: The `strictFilters` parameter applies metadata filters. `confidenceScoreThreshold` controls minimum confidence (0.0–1.0). Default threshold is 0.

> **EXAM TIP:** Multi-turn conversations in QA use "follow-up prompts" linked to specific answers. They guide users through complex Q&A flows.

### Cleanup

```bash
# Delete projects in Language Studio
# Or delete the Language resource:
az cognitiveservices account delete -n ai102-language -g ai102-labs-rg
```

---

# Module 6 — Knowledge Mining and Document Intelligence

> **Exam Weight: 10–15%** | 3 Labs

---

## Lab 6.1: Azure AI Search

**Module:** 6 | **Exam Weight:** 10–15% | **Estimated Time:** 75 min | **Cost:** ~$3

### Objective

Create a search index with an indexer and skillset (AI enrichment pipeline), then query using full-text, filter, facet, and vector search.

### Azure Resources Needed

- Azure AI Search (Basic or Standard)
- Azure Storage Account (blob container with documents)
- Azure AI Services (for built-in skills)

### Step-by-Step Walkthrough

1. **Deploy AI Search with Bicep:**
   ```bash
   az deployment group create \
     -g ai102-labs-rg -f infra/ai-search.bicep \
     --parameters name=ai102-search location=eastus sku=basic
   ```
2. **Upload sample documents** to a blob container.
3. **Create a data source** pointing to the blob container.
4. **Create a skillset** with built-in cognitive skills:
   - `#Microsoft.Skills.Text.EntityRecognitionSkill` — NER
   - `#Microsoft.Skills.Text.KeyPhraseExtractionSkill` — key phrases
   - `#Microsoft.Skills.Text.SentimentSkill` — sentiment
   - `#Microsoft.Skills.Vision.OcrSkill` — OCR for images
   - `#Microsoft.Skills.Text.SplitSkill` — text chunking
   - `#Microsoft.Skills.Text.AzureOpenAIEmbeddingSkill` — vector embeddings
5. **Define a knowledge store** (optional) — Project enriched data to tables or blob storage.
6. **Create an index** with fields, analyzers, and vector configurations:
   ```bash
   python scripts/python/search/create-index.py
   ```
7. **Create an indexer** to run the pipeline.
8. **Query the index:**
   ```bash
   python scripts/python/search/query-index.py
   ```
9. **Test query types:**
   - Full-text: `search=azure cognitive services`
   - Filter: `$filter=sentiment eq 'positive'`
   - Facets: `facet=category`
   - Vector: hybrid search with embeddings
   - Semantic ranking: `queryType=semantic&semanticConfiguration=my-config`

### Repo Files

| File | Purpose |
|------|---------|
| `infra/ai-search.bicep` | Bicep — provisions AI Search resource |
| `scripts/python/search/create-index.py` | Python — creates index with fields and vector config |
| `scripts/python/search/query-index.py` | Python — executes various query types |

### Exam-Relevant Takeaways

> **EXAM TIP:** The indexer pipeline: Data Source → Skillset (enrichment) → Index. The skillset defines AI transformations applied during indexing.

> **EXAM TIP:** Custom skills use a Web API skill (`#Microsoft.Skills.Custom.WebApiSkill`) — they call your own Azure Function or REST endpoint.

> **EXAM TIP:** Knowledge store projects enriched data to Azure Storage (tables/blobs/files) for downstream analytics. It's separate from the search index.

> **EXAM TIP:** Vector search requires: (1) vector field in the index, (2) embedding model to vectorize queries, (3) `vectorQueries` in the search request. Hybrid = text + vector.

### Cleanup

```bash
az search service delete -n ai102-search -g ai102-labs-rg --yes
```

---

## Lab 6.2: Document Intelligence

**Module:** 6 | **Exam Weight:** 10–15% | **Estimated Time:** 60 min | **Cost:** ~$1

### Objective

Use Azure AI Document Intelligence prebuilt models (invoices, receipts, IDs) and train a custom model for domain-specific documents, then compose models.

### Azure Resources Needed

- Azure AI Document Intelligence resource
- Sample documents (invoices, receipts, or custom forms)

### Step-by-Step Walkthrough

1. **Deploy Document Intelligence with Bicep:**
   ```bash
   az deployment group create \
     -g ai102-labs-rg -f infra/document-intelligence.bicep \
     --parameters name=ai102-docintell location=eastus
   ```
2. **Update `.env`** with Document Intelligence endpoint and key.
3. **Run the prebuilt invoice model:**
   ```bash
   python scripts/python/document-intelligence/prebuilt-invoice.py
   ```
4. **Examine prebuilt model output:**
   - Vendor name, address, invoice number, date, total
   - Line items with descriptions, quantities, amounts
   - Confidence scores per field
5. **Try other prebuilt models:**
   - `prebuilt-receipt` — retail receipts
   - `prebuilt-idDocument` — driver's licenses, passports
   - `prebuilt-businessCard` — business cards
   - `prebuilt-layout` — tables, structure, selection marks
   - `prebuilt-read` — OCR text extraction
6. **Train a custom model** using Document Intelligence Studio:
   - Upload 5+ labeled training documents
   - Label fields in the Studio UI
   - Train the model (template vs. neural)
   - Test with new documents
7. **Compose models** — Combine multiple custom models into a composed model that auto-routes to the correct sub-model.
8. **Compare model types:**
   - **Template (fixed)**: For structured forms with fixed layouts
   - **Neural**: For semi-structured and variable layouts (more flexible, slower)

### Repo Files

| File | Purpose |
|------|---------|
| `infra/document-intelligence.bicep` | Bicep — provisions Document Intelligence resource |
| `scripts/python/document-intelligence/prebuilt-invoice.py` | Python — prebuilt invoice extraction |

### Exam-Relevant Takeaways

> **EXAM TIP:** Prebuilt models require NO training. Use them first — only train custom models when prebuilt models don't cover your document type.

> **EXAM TIP:** Custom model types: Template (fast, structured, fixed layout) vs. Neural (flexible, variable layout, slower). Composed models combine up to 200 custom models.

> **EXAM TIP:** The `prebuilt-layout` model extracts tables, selection marks (checkboxes), and document structure — it's the foundation for custom models.

> **EXAM TIP:** Minimum training documents: 5 for template, 5 for neural. Training data must be in an Azure Blob Storage container with an OCR JSON file per document.

### Cleanup

```bash
az cognitiveservices account delete -n ai102-docintell -g ai102-labs-rg
```

---

## Lab 6.3: Content Understanding & OCR Pipelines

**Module:** 6 | **Exam Weight:** 10–15% | **Estimated Time:** 45 min | **Cost:** ~$1

### Objective

Build OCR pipelines combining Document Intelligence (for structured extraction) and AI Vision (for general OCR), then implement document classification workflows.

### Azure Resources Needed

- Azure AI Document Intelligence (from Lab 6.2)
- Azure AI Vision (from Lab 4.1)
- Azure AI Search (optional, for indexing extracted content)

### Step-by-Step Walkthrough

1. **Compare OCR approaches:**
   - **Document Intelligence Read**: Optimized for documents — preserves paragraphs, tables, reading order
   - **Vision 4.0 Read**: General-purpose OCR — good for photos, screenshots, signage
2. **Build a classification pipeline:**
   - Step 1: Use `prebuilt-layout` to extract document structure
   - Step 2: Use custom classification model to categorize document type
   - Step 3: Route to the appropriate custom extraction model
3. **Implement a document processing workflow:**
   ```python
   # Pseudocode
   document = read_document(file_path)
   doc_type = classify_document(document)  # invoice, receipt, contract
   extracted_data = extract_fields(document, model=doc_type)
   search_index.upload(extracted_data)  # Index for search
   ```
4. **Handle multi-page documents:**
   - Document Intelligence processes all pages automatically
   - Access individual page results via `result.pages[n]`
5. **Process tables:**
   - Tables have cells with `row_index`, `column_index`, and `content`
   - Header rows are identified with `kind="columnHeader"`
6. **Test with different document formats** — PDF, TIFF, JPEG, PNG, BMP, DOCX, XLSX, PPTX, HTML.

### Repo Files

| File | Purpose |
|------|---------|
| `scripts/python/document-intelligence/prebuilt-invoice.py` | Python — starting point for pipeline extension |

### Exam-Relevant Takeaways

> **EXAM TIP:** Document Intelligence supports: PDF, JPEG, PNG, BMP, TIFF, HEIF, DOCX, XLSX, PPTX, HTML. Max file size: 500 MB (Standard), 4 MB (Free).

> **EXAM TIP:** The `prebuilt-read` model is the simplest — text-only OCR. `prebuilt-layout` adds tables and structure. Prebuilt domain models (invoice, receipt) add field extraction.

> **EXAM TIP:** Composed models support automatic document type detection. The system analyzes the document and routes to the best sub-model. Max 200 sub-models per composed model.

### Cleanup

```bash
# Uses existing resources from Lab 6.2 — no additional cleanup needed
```

---

# End-to-End Lab

---

## Lab E2E: Document Search Application

**Module:** All | **Exam Weight:** Full exam | **Estimated Time:** 120 min | **Cost:** ~$5

### Objective

Build an end-to-end document search application that integrates all six modules: AI Services provisioning, OpenAI for generation, Vision for image analysis, Language for text enrichment, Document Intelligence for extraction, and AI Search for indexing and querying.

### Azure Resources Needed

- Azure AI Services (multi-service)
- Azure OpenAI (GPT-4o + embeddings)
- Azure AI Search (Basic)
- Azure AI Document Intelligence
- Azure Storage Account
- Resource Group: `ai102-labs-rg`

### Step-by-Step Walkthrough

1. **Provision all resources** using the lab provisioning script:
   ```bash
   pwsh scripts/powershell/provision-lab-environment.ps1
   ```
2. **Upload documents** to blob storage (mix of PDFs with text, images, and tables).
3. **Build the AI Search pipeline:**
   - Data source: Blob container
   - Skillset: OCR → Entity Recognition → Key Phrases → Embeddings
   - Index: Full-text + vector fields + enriched metadata
4. **Document Intelligence extraction** — Process invoices/receipts separately with prebuilt models.
5. **RAG implementation** — Query the search index, inject results into GPT-4o prompt, generate answers.
6. **Content Safety** — Add Content Safety checks on user queries and generated responses.
7. **Monitoring** — Configure diagnostic settings for all services.
8. **Secure the solution:**
   - Managed identity for inter-service authentication
   - Key Vault for secrets
   - Private networking (optional)
9. **Test the full pipeline:**
   ```bash
   # Navigate to the e2e solution directory
   cd scripts/python/e2e-solution
   # Run the application (implement your solution here)
   ```
10. **Verify** each module's contribution to the final solution.

### Repo Files

| File | Purpose |
|------|---------|
| `scripts/python/e2e-solution/` | Directory for end-to-end solution code |
| `scripts/powershell/provision-lab-environment.ps1` | PowerShell — provisions all lab resources |
| `scripts/powershell/cleanup-lab-environment.ps1` | PowerShell — tears down all resources |
| All Bicep templates in `infra/` | Infrastructure for each service |

### Exam-Relevant Takeaways

> **EXAM TIP:** The exam tests your ability to integrate multiple services. Know which service to use for which task — don't use Vision OCR when Document Intelligence is more appropriate for structured documents.

> **EXAM TIP:** Inter-service authentication: Use managed identity + RBAC in production. Keys are acceptable for development but NOT recommended for production.

> **EXAM TIP:** Cost optimization: Use multi-service resources where possible. Delete model deployments when not in use. Use free tiers for development.

### Cleanup

```bash
# Full cleanup — deletes everything
az group delete -n ai102-labs-rg --yes --no-wait
pwsh scripts/powershell/cleanup-lab-environment.ps1
```

---

# Quick Reference Tables

## File Size Limits by Service

| Service | Max File Size | Min Dimensions | Supported Formats |
|---------|--------------|----------------|-------------------|
| Document Intelligence (Standard) | 500 MB | — | PDF, JPEG, PNG, BMP, TIFF, HEIF, DOCX, XLSX, PPTX, HTML |
| Document Intelligence (Free) | 4 MB | — | Same as above |
| Custom Vision (training images) | 6 MB | 256×256 px | JPEG, PNG, BMP, GIF |
| Vision 4.0 (image analysis) | 20 MB | 50×50 px | JPEG, PNG, GIF, BMP, WEBP, ICO, TIFF |
| Speech (audio file) | 200 MB (batch) | — | WAV, MP3, OGG, FLAC, WMA, AAC |
| AI Search (document) | 16 MB (API push), 256 MB (blob indexer) | — | PDF, DOCX, PPTX, XLSX, HTML, JSON, CSV, TXT, EML, MSG |
| Video Indexer | 2 GB (upload) | — | MP4, MOV, WMV, AVI, FLV, MKV |

## REST Endpoint Patterns

```
# Azure AI Services (multi-service)
https://<name>.cognitiveservices.azure.com/

# Language / Text Analytics
https://<name>.cognitiveservices.azure.com/language/:analyze-text?api-version=2023-04-01
https://<name>.cognitiveservices.azure.com/language/:analyze-conversations?api-version=2023-04-01
https://<name>.cognitiveservices.azure.com/language/:query-knowledgebases?api-version=2021-10-01

# Vision 4.0
https://<name>.cognitiveservices.azure.com/computervision/imageanalysis:analyze?api-version=2024-02-01

# Face API
https://<name>.cognitiveservices.azure.com/face/v1.0/detect

# Azure OpenAI
https://<name>.openai.azure.com/openai/deployments/<deployment>/chat/completions?api-version=2024-02-01
https://<name>.openai.azure.com/openai/deployments/<deployment>/embeddings?api-version=2024-02-01
https://<name>.openai.azure.com/openai/deployments/<deployment>/images/generations?api-version=2024-02-01

# Translator (global endpoint)
https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=<lang>

# Speech
wss://<region>.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1
https://<region>.tts.speech.microsoft.com/cognitiveservices/v1

# Document Intelligence
https://<name>.cognitiveservices.azure.com/documentintelligence/documentModels/<model>:analyze?api-version=2024-02-29-preview

# AI Search
https://<name>.search.windows.net/indexes/<index>/docs/search?api-version=2024-07-01

# Content Safety
https://<name>.cognitiveservices.azure.com/contentsafety/text:analyze?api-version=2024-02-15-preview
```

## MS Learn Lab Repo Index

| Repo | Status | Topics | Link |
|------|--------|--------|------|
| mslearn-ai-studio | ✅ Active | AI Foundry, prompt flow, evaluation | [GitHub](https://github.com/MicrosoftLearning/mslearn-ai-studio) |
| mslearn-ai-vision | ✅ Active | Image analysis, Custom Vision, Face | [GitHub](https://github.com/MicrosoftLearning/mslearn-ai-vision) |
| mslearn-ai-language | ✅ Active | Text analytics, CLU, QA, translation | [GitHub](https://github.com/MicrosoftLearning/mslearn-ai-language) |
| mslearn-ai-document-intelligence | ✅ Active | Prebuilt & custom models, composed models | [GitHub](https://github.com/MicrosoftLearning/mslearn-ai-document-intelligence) |
| mslearn-knowledge-mining | ✅ Active | AI Search, skillsets, indexers, vector search | [GitHub](https://github.com/MicrosoftLearning/mslearn-knowledge-mining) |
| mslearn-openai | ✅ Active | Azure OpenAI, chat, DALL-E, RAG | [GitHub](https://github.com/MicrosoftLearning/mslearn-openai) |
| mslearn-ai-services | ✅ Active | Provisioning, security, monitoring, containers | [GitHub](https://github.com/MicrosoftLearning/mslearn-ai-services) |
| AI-102-AIEngineer | ⚠️ Archived | Legacy labs (replaced by above repos) | [GitHub](https://github.com/MicrosoftLearning/AI-102-AIEngineer) |

---

## Repo File Map

All files in this repository referenced by the labs above:

### Infrastructure (Bicep)

| File | Service | Labs |
|------|---------|------|
| `infra/ai-services.bicep` | Azure AI Services (multi-service) | 1.1 |
| `infra/openai.bicep` | Azure OpenAI | 2.1, 2.2 |
| `infra/ai-foundry.bicep` | AI Foundry Hub | 2.3 |
| `infra/vision.bicep` | Computer Vision | 4.1 |
| `infra/speech.bicep` | Speech Services | 5.3 |
| `infra/ai-search.bicep` | Azure AI Search | 2.2, 6.1 |
| `infra/document-intelligence.bicep` | Document Intelligence | 6.2 |

### Python Scripts

| File | Domain | Labs |
|------|--------|------|
| `scripts/python/services/provision-and-test.py` | AI Services SDK test | 1.1 |
| `scripts/python/services/secure-access.py` | Key Vault + managed identity | 1.2 |
| `scripts/python/services/content-safety.py` | Content Safety SDK | 1.5 |
| `scripts/python/openai/chat-completions.py` | Chat completions | 2.1 |
| `scripts/python/openai/rag-pattern.py` | RAG pipeline | 2.2 |
| `scripts/python/openai/generate-images.py` | DALL-E 3 | 2.4 |
| `scripts/python/vision/analyze-image.py` | Vision 4.0 analysis | 4.1 |
| `scripts/python/vision/custom-vision-train.py` | Custom Vision training | 4.2 |
| `scripts/python/language/text-analytics.py` | Text analytics operations | 5.1 |
| `scripts/python/speech/speech-to-text.py` | Speech recognition | 5.3 |
| `scripts/python/speech/text-to-speech.py` | Speech synthesis + SSML | 5.3 |
| `scripts/python/search/create-index.py` | AI Search index creation | 2.2, 6.1 |
| `scripts/python/search/query-index.py` | AI Search queries | 2.2, 6.1 |
| `scripts/python/document-intelligence/prebuilt-invoice.py` | Invoice extraction | 6.2, 6.3 |

### REST API Samples

| File | Service | Labs |
|------|---------|------|
| `scripts/rest-api/detect-language.http` | Language detection | 1.1 |
| `scripts/rest-api/openai-chat.http` | Chat completions | 2.1 |
| `scripts/rest-api/vision-analyze.http` | Image analysis | 4.1 |
| `scripts/rest-api/text-analytics.http` | Text analytics | 5.1 |

### PowerShell Scripts

| File | Purpose | Labs |
|------|---------|------|
| `scripts/powershell/provision-lab-environment.ps1` | Provision all lab resources | Setup, E2E |
| `scripts/powershell/cleanup-lab-environment.ps1` | Tear down all resources | Setup, E2E |
| `scripts/powershell/configure-monitoring.ps1` | Diagnostic settings + Log Analytics | 1.3 |
| `scripts/powershell/deploy-container.ps1` | Deploy AI container to ACI | 1.4 |

---

> **Last updated:** 2025 | **Exam version:** AI-102 (current)
>
> For the full course syllabus, see [`course/syllabus.md`](syllabus.md).
> For infrastructure details, see [`infra/README.md`](../infra/README.md).
> For script documentation, see [`scripts/README.md`](../scripts/README.md).
