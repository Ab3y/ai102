# Scripts Directory — AI-102 Lab Code Samples

This directory contains all runnable code samples organized by language and AI service area.

## Python SDK Samples (`python/`)

| Directory | Scripts | Maps to Module |
|-----------|---------|----------------|
| `services/` | provision-and-test, secure-access, content-safety | Module 1 |
| `openai/` | chat-completions, rag-pattern, generate-images, fine-tune, foundry-sdk-app | Module 2 |
| `agents/` | foundry-agent, multi-agent-orchestration | Module 3 |
| `vision/` | analyze-image, custom-vision-train, custom-vision-predict, video-indexer, face-detection | Module 4 |
| `language/` | text-analytics, translate-text, custom-translator, clu-client, qna-client | Module 5 |
| `speech/` | speech-to-text, text-to-speech, ssml-examples | Module 5 |
| `search/` | create-index, query-index, custom-skill-function | Module 6 |
| `document-intelligence/` | prebuilt-invoice, custom-model, content-understanding | Module 6 |
| `e2e-solution/` | Complete end-to-end AI document search application | All |

### Running Python Samples

```bash
# From repo root
python -m venv .venv
.venv\Scripts\Activate.ps1   # Windows
source .venv/bin/activate     # macOS/Linux
pip install -r requirements.txt

# Create .env file with your credentials
cp .env.template .env
# Edit .env with your Azure resource endpoints and keys

# Run a sample
python scripts/python/vision/analyze-image.py
```

## REST API Examples (`rest-api/`)

Use with [VS Code REST Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).

| File | Service | Module |
|------|---------|--------|
| `detect-language.http` | AI Language — detect language | Module 1 |
| `text-analytics.http` | AI Language — sentiment, entities, key phrases, PII | Module 5 |
| `vision-analyze.http` | AI Vision — image analysis, OCR | Module 4 |
| `openai-chat.http` | Azure OpenAI — chat completions, embeddings | Module 2 |

### Setup

Create a `.env` file in the `rest-api/` directory:

```
AI_SERVICES_ENDPOINT=https://your-resource.cognitiveservices.azure.com
AI_SERVICES_KEY=your-key-here
AZURE_OPENAI_ENDPOINT=https://your-openai.openai.azure.com
AZURE_OPENAI_KEY=your-key-here
```

## PowerShell Scripts (`powershell/`)

| Script | Purpose | Module |
|--------|---------|--------|
| `provision-lab-environment.ps1` | Deploy all AI resources for labs | Setup |
| `cleanup-lab-environment.ps1` | Delete all lab resources | Cleanup |
| `configure-monitoring.ps1` | Set up diagnostic logging & alerts | Module 1 |
| `deploy-container.ps1` | Deploy AI Services container to ACI | Module 1 |

### Running PowerShell Scripts

```powershell
# Ensure Az module is installed
Install-Module -Name Az -Scope CurrentUser -Force

# Log in
Connect-AzAccount

# Provision all lab resources
.\scripts\powershell\provision-lab-environment.ps1

# Clean up when done
.\scripts\powershell\cleanup-lab-environment.ps1
```

## Environment Variables

All scripts expect credentials via `.env` file or environment variables:

| Variable | Description |
|----------|-------------|
| `AI_SERVICES_ENDPOINT` | Azure AI Services multi-service endpoint |
| `AI_SERVICES_KEY` | Azure AI Services API key |
| `AZURE_OPENAI_ENDPOINT` | Azure OpenAI endpoint |
| `AZURE_OPENAI_KEY` | Azure OpenAI API key |
| `SEARCH_ENDPOINT` | Azure AI Search endpoint |
| `SEARCH_ADMIN_KEY` | Azure AI Search admin key |
| `SPEECH_KEY` | Azure Speech Services key |
| `SPEECH_REGION` | Azure Speech region (e.g., eastus) |
| `DOC_INTELLIGENCE_ENDPOINT` | Document Intelligence endpoint |
| `DOC_INTELLIGENCE_KEY` | Document Intelligence key |
