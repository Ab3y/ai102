# Abe's AI-102 Azure AI Engineer Certification Study Resources

![AI-102 Badge](https://learn.microsoft.com/en-us/media/learn/certification/badges/microsoft-certified-associate-badge.svg)

> **Exam AI-102** — Designing and Implementing a Microsoft Azure AI Solution
> **Passing Score:** 700 / 1000 · **Questions:** ~58 · **Duration:** 120 min
> **Prerequisite:** Azure fundamentals + Python or C# experience
> **Skills Measured Version:** December 23, 2025 · **Retires:** June 30, 2026

---

## 📬 Contact Information

- **[LinkedIn](https://www.linkedin.com/in/abeabraham/)**
- **[GitHub](https://github.com/Ab3y)**

---

## 🚀 Must-Have AI-102 Resources

- [AI-102 Exam Page](https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-102/)
- [AI-102 Study Guide](https://aka.ms/ai102-StudyGuide)
- [Exam Registration (Pearson VUE)](https://learn.microsoft.com/en-us/credentials/certifications/schedule-through-pearson-vue?examUid=exam.AI-102)
- [MeasureUp AI-102 Practice Exams](https://www.measureup.com/microsoft-practice-test-ai-102-designing-and-implementing-a-microsoft-azure-ai-solution.html)
- [MS Learn AI-102 Course](https://learn.microsoft.com/en-us/training/courses/ai-102t00)
- [MS Learn AI-102 Learning Path](https://learn.microsoft.com/en-us/training/browse/?terms=ai-102&resource_type=learning%20path)
- [Azure Free Account Signup](https://azure.microsoft.com/en-us/free/)
- [Free Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-102/practice/assessment?assessment-type=practice&assessmentId=61)

---

## 🎯 Exam Domain Weights

| # | Domain | Weight | Module |
|---|--------|--------|--------|
| 1 | Plan and manage an Azure AI solution | 20–25 % | [Module 1](course/module-1-plan-manage/) |
| 2 | Implement generative AI solutions | 15–20 % | [Module 2](course/module-2-generative-ai/) |
| 3 | Implement an agentic solution | 5–10 % | [Module 3](course/module-3-agentic-solutions/) |
| 4 | Implement computer vision solutions | 10–15 % | [Module 4](course/module-4-computer-vision/) |
| 5 | Implement NLP solutions | 15–20 % | [Module 5](course/module-5-nlp/) |
| 6 | Implement knowledge mining & info extraction | 15–20 % | [Module 6](course/module-6-knowledge-mining/) |

> Full objective-to-module mapping → [docs/ai102-objective-domain.md](docs/ai102-objective-domain.md)

---

## 🗺️ Repo Map at a Glance

```text
AI102/
├── course/                          # Self-paced training modules
│   ├── module-1-plan-manage/        # Plan & Manage (20-25%)
│   ├── module-2-generative-ai/      # Generative AI (15-20%)
│   ├── module-3-agentic-solutions/  # Agentic Solutions (5-10%)
│   ├── module-4-computer-vision/    # Computer Vision (10-15%)
│   ├── module-5-nlp/                # NLP (15-20%)
│   └── module-6-knowledge-mining/   # Knowledge Mining (15-20%)
├── docs/                            # Reference materials & exam mapping
│   └── ai102-objective-domain.md
├── images/                          # Architecture diagrams
├── infra/                           # Bicep IaC templates
│   ├── ai-services.bicep
│   ├── openai.bicep
│   ├── ai-search.bicep
│   ├── document-intelligence.bicep
│   ├── speech.bicep
│   ├── vision.bicep
│   ├── ai-foundry.bicep
│   └── README.md
├── scripts/
│   ├── python/                      # Python SDK samples
│   │   ├── services/                # Module 1 — AI Services mgmt
│   │   ├── openai/                  # Module 2 — Azure OpenAI
│   │   ├── agents/                  # Module 3 — Agentic AI
│   │   ├── vision/                  # Module 4 — Computer Vision
│   │   ├── language/                # Module 5 — Language
│   │   ├── speech/                  # Module 5 — Speech
│   │   ├── search/                  # Module 6 — AI Search
│   │   ├── document-intelligence/   # Module 6 — Doc Intelligence
│   │   └── e2e-solution/            # End-to-end capstone
│   ├── rest-api/                    # .http files for REST Client
│   └── powershell/                  # Provisioning & cleanup scripts
├── .env.template                    # Environment variable template
├── CLAUDE.md                        # Claude Code project instructions
├── CITATION.cff                     # Citation metadata
├── CODE_OF_CONDUCT.md               # Contributor Code of Conduct
├── CONTRIBUTING.md                   # Contribution guidelines
├── LICENSE                          # License
├── SECURITY.md                      # Security policy
├── SUPPORT.md                       # Support info
├── requirements.txt                 # Python dependencies
└── README.md                        # ← You are here
```

---

## 🚀 Quick Start

```text
1. Clone      → git clone https://github.com/Ab3y/ai102.git && cd ai102
2. Virtualenv → python -m venv .venv && .venv\Scripts\Activate.ps1
3. Install    → pip install -r requirements.txt
4. Azure      → az login && az group create -n rg-ai102-labs -l eastus
5. Deploy     → az deployment group create -g rg-ai102-labs -f infra/ai-services.bicep
```

> Copy `.env.template` → `.env` and fill in your Azure endpoints + keys before running scripts.

---

## 📚 Course Modules Navigation

### Module 1 — Plan & Manage an Azure AI Solution (20–25 %)

| Resource | Link |
|----------|------|
| 📂 Module Folder | [course/module-1-plan-manage/](course/module-1-plan-manage/) |
| 📖 Exam Objectives | [Domain 1 Mapping](docs/ai102-objective-domain.md) |

**Bicep Templates:**

| Template | Description |
|----------|-------------|
| [ai-services.bicep](infra/ai-services.bicep) | AI Services multi-service resource |
| [ai-foundry.bicep](infra/ai-foundry.bicep) | AI Foundry hub + project |

**Python Scripts:**

| Script | Description |
|--------|-------------|
| [provision-and-test.py](scripts/python/services/provision-and-test.py) | Provision & test AI Services |
| [secure-access.py](scripts/python/services/secure-access.py) | Managed identity & Key Vault |
| [content-safety.py](scripts/python/services/content-safety.py) | Content Safety API |

**REST API:**

| File | Description |
|------|-------------|
| [detect-language.http](scripts/rest-api/detect-language.http) | Language detection |

**PowerShell:**

| Script | Description |
|--------|-------------|
| [provision-lab-environment.ps1](scripts/powershell/provision-lab-environment.ps1) | Deploy all lab resources |
| [cleanup-lab-environment.ps1](scripts/powershell/cleanup-lab-environment.ps1) | Delete all lab resources |
| [configure-monitoring.ps1](scripts/powershell/configure-monitoring.ps1) | Diagnostic logging & alerts |
| [deploy-container.ps1](scripts/powershell/deploy-container.ps1) | Deploy AI container to ACI |

---

### Module 2 — Implement Generative AI Solutions (15–20 %)

| Resource | Link |
|----------|------|
| 📂 Module Folder | [course/module-2-generative-ai/](course/module-2-generative-ai/) |
| 📖 Exam Objectives | [Domain 2 Mapping](docs/ai102-objective-domain.md) |

**Bicep Templates:**

| Template | Description |
|----------|-------------|
| [openai.bicep](infra/openai.bicep) | Azure OpenAI + model deployments |

**Python Scripts:**

| Script | Description |
|--------|-------------|
| [chat-completions.py](scripts/python/openai/chat-completions.py) | Chat completions with GPT |
| [rag-pattern.py](scripts/python/openai/rag-pattern.py) | RAG pattern implementation |
| [generate-images.py](scripts/python/openai/generate-images.py) | DALL-E image generation |

**REST API:**

| File | Description |
|------|-------------|
| [openai-chat.http](scripts/rest-api/openai-chat.http) | Chat completions & embeddings |

---

### Module 3 — Implement an Agentic Solution (5–10 %)

| Resource | Link |
|----------|------|
| 📂 Module Folder | [course/module-3-agentic-solutions/](course/module-3-agentic-solutions/) |
| 📖 Exam Objectives | [Domain 3 Mapping](docs/ai102-objective-domain.md) |

**Bicep Templates:**

| Template | Description |
|----------|-------------|
| [ai-foundry.bicep](infra/ai-foundry.bicep) | AI Foundry hub + project |

**Python Scripts:**

| Script | Description |
|--------|-------------|
| 📂 [agents/](scripts/python/agents/) | Foundry Agent & multi-agent orchestration |

---

### Module 4 — Implement Computer Vision Solutions (10–15 %)

| Resource | Link |
|----------|------|
| 📂 Module Folder | [course/module-4-computer-vision/](course/module-4-computer-vision/) |
| 📖 Exam Objectives | [Domain 4 Mapping](docs/ai102-objective-domain.md) |

**Bicep Templates:**

| Template | Description |
|----------|-------------|
| [vision.bicep](infra/vision.bicep) | Computer Vision resource |

**Python Scripts:**

| Script | Description |
|--------|-------------|
| 📂 [vision/](scripts/python/vision/) | Image analysis, Custom Vision, Video Indexer, Face |

**REST API:**

| File | Description |
|------|-------------|
| [vision-analyze.http](scripts/rest-api/vision-analyze.http) | Image analysis & OCR |

---

### Module 5 — Implement NLP Solutions (15–20 %)

| Resource | Link |
|----------|------|
| 📂 Module Folder | [course/module-5-nlp/](course/module-5-nlp/) |
| 📖 Exam Objectives | [Domain 5 Mapping](docs/ai102-objective-domain.md) |

**Bicep Templates:**

| Template | Description |
|----------|-------------|
| [speech.bicep](infra/speech.bicep) | Speech Services resource |
| [ai-services.bicep](infra/ai-services.bicep) | AI Services (Language) |

**Python Scripts:**

| Script | Description |
|--------|-------------|
| 📂 [language/](scripts/python/language/) | Text analytics, translation, CLU, QnA |
| 📂 [speech/](scripts/python/speech/) | Speech-to-text, text-to-speech, SSML |

**REST API:**

| File | Description |
|------|-------------|
| [text-analytics.http](scripts/rest-api/text-analytics.http) | Sentiment, entities, key phrases, PII |

---

### Module 6 — Implement Knowledge Mining & Info Extraction (15–20 %)

| Resource | Link |
|----------|------|
| 📂 Module Folder | [course/module-6-knowledge-mining/](course/module-6-knowledge-mining/) |
| 📖 Exam Objectives | [Domain 6 Mapping](docs/ai102-objective-domain.md) |

**Bicep Templates:**

| Template | Description |
|----------|-------------|
| [ai-search.bicep](infra/ai-search.bicep) | Azure AI Search |
| [document-intelligence.bicep](infra/document-intelligence.bicep) | Document Intelligence |

**Python Scripts:**

| Script | Description |
|--------|-------------|
| 📂 [search/](scripts/python/search/) | Create/query indexes, custom skills |
| 📂 [document-intelligence/](scripts/python/document-intelligence/) | Prebuilt models, custom models |

---

## 🧪 End-to-End Lab

| Resource | Link |
|----------|------|
| 📂 Capstone Project | [scripts/python/e2e-solution/](scripts/python/e2e-solution/) |

A complete end-to-end AI document search application tying together Document Intelligence, AI Search, Azure OpenAI, and more — covering all 6 exam domains.

---

## 🛠 Lab Environment Setup

### Option A — Bash / macOS / Linux

```bash
# 1. Clone the repo
git clone https://github.com/Ab3y/ai102.git && cd ai102

# 2. Create virtual environment & install deps
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 3. Configure credentials
cp .env.template .env        # edit .env with your keys

# 4. Log in to Azure & deploy
az login
az group create --name rg-ai102-labs --location eastus
az deployment group create \
  --resource-group rg-ai102-labs \
  --template-file infra/ai-services.bicep \
  --parameters resourceName=ai102-cognitive

# 5. Cleanup when done
az group delete --name rg-ai102-labs --yes --no-wait
```

### Option B — PowerShell / Windows

```powershell
# 1. Clone the repo
git clone https://github.com/Ab3y/ai102.git; Set-Location ai102

# 2. Create virtual environment & install deps
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# 3. Configure credentials
Copy-Item .env.template .env   # edit .env with your keys

# 4. Log in to Azure & deploy
az login
az group create --name rg-ai102-labs --location eastus
az deployment group create `
  --resource-group rg-ai102-labs `
  --template-file infra/ai-services.bicep `
  --parameters resourceName=ai102-cognitive

# 5. Cleanup when done
az group delete --name rg-ai102-labs --yes --no-wait
```

> ⚠️ **Cost Warning:** Azure resources incur charges. Use F0 (free) SKUs where available and delete resources immediately after lab exercises. See [infra/README.md](infra/README.md) for cost estimates.

---

## 📖 Reference Materials

| Document | Description |
|----------|-------------|
| [ai102-objective-domain.md](docs/ai102-objective-domain.md) | Full exam objectives mapped to modules |
| [Infra README](infra/README.md) | Bicep template catalog, costs & deployment commands |
| [Scripts README](scripts/README.md) | Script inventory, setup & environment variables |

---

## 📝 Scripts Inventory

### Python SDK Samples — by Directory

| Directory | Module | Scripts |
|-----------|--------|---------|
| [services/](scripts/python/services/) | 1 — Plan & Manage | [provision-and-test.py](scripts/python/services/provision-and-test.py), [secure-access.py](scripts/python/services/secure-access.py), [content-safety.py](scripts/python/services/content-safety.py) |
| [openai/](scripts/python/openai/) | 2 — Generative AI | [chat-completions.py](scripts/python/openai/chat-completions.py), [rag-pattern.py](scripts/python/openai/rag-pattern.py), [generate-images.py](scripts/python/openai/generate-images.py) |
| [agents/](scripts/python/agents/) | 3 — Agentic | Foundry agent, multi-agent orchestration |
| [vision/](scripts/python/vision/) | 4 — Computer Vision | Image analysis, Custom Vision, Video Indexer, Face |
| [language/](scripts/python/language/) | 5 — NLP | Text analytics, translation, CLU, QnA |
| [speech/](scripts/python/speech/) | 5 — NLP | Speech-to-text, text-to-speech, SSML |
| [search/](scripts/python/search/) | 6 — Knowledge Mining | Create/query indexes, custom skills |
| [document-intelligence/](scripts/python/document-intelligence/) | 6 — Knowledge Mining | Prebuilt models, custom models, content understanding |
| [e2e-solution/](scripts/python/e2e-solution/) | All | End-to-end capstone application |

### REST API Examples

| File | Service | Module |
|------|---------|--------|
| [detect-language.http](scripts/rest-api/detect-language.http) | AI Language — detect language | 1 |
| [text-analytics.http](scripts/rest-api/text-analytics.http) | AI Language — sentiment, entities, PII | 5 |
| [vision-analyze.http](scripts/rest-api/vision-analyze.http) | AI Vision — image analysis, OCR | 4 |
| [openai-chat.http](scripts/rest-api/openai-chat.http) | Azure OpenAI — chat, embeddings | 2 |

### PowerShell Scripts

| Script | Purpose | Module |
|--------|---------|--------|
| [provision-lab-environment.ps1](scripts/powershell/provision-lab-environment.ps1) | Deploy all AI resources | Setup |
| [cleanup-lab-environment.ps1](scripts/powershell/cleanup-lab-environment.ps1) | Delete all lab resources | Cleanup |
| [configure-monitoring.ps1](scripts/powershell/configure-monitoring.ps1) | Diagnostic logging & alerts | 1 |
| [deploy-container.ps1](scripts/powershell/deploy-container.ps1) | Deploy AI container to ACI | 1 |

### Bicep Infrastructure Templates

| Template | Service | Key Parameters |
|----------|---------|----------------|
| [ai-services.bicep](infra/ai-services.bicep) | AI Services (multi-service) | `resourceName`, `sku` |
| [openai.bicep](infra/openai.bicep) | Azure OpenAI + models | `resourceName`, `chatModelName` |
| [ai-search.bicep](infra/ai-search.bicep) | Azure AI Search | `searchServiceName`, `sku` |
| [document-intelligence.bicep](infra/document-intelligence.bicep) | Document Intelligence | `resourceName`, `sku` |
| [speech.bicep](infra/speech.bicep) | Speech Services | `resourceName`, `sku` |
| [vision.bicep](infra/vision.bicep) | Computer Vision | `resourceName`, `sku` |
| [ai-foundry.bicep](infra/ai-foundry.bicep) | AI Foundry hub + project | `hubName`, `projectName` |

---

## 📊 File Size Limits Cheat Sheet

| Service | Input Limit | Notes |
|---------|-------------|-------|
| Document Intelligence | 500 MB per file (paid), 4 MB (free) | PDF, JPEG, PNG, BMP, TIFF, HEIF, DOCX, XLSX, PPTX, HTML |
| Custom Vision — Training | 6 MB per image | JPEG, PNG, BMP, GIF (first frame) |
| Custom Vision — Prediction | 4 MB per image | — |
| Azure AI Vision — Image Analysis | 20 MB per image | JPEG, PNG, GIF, BMP, ≥50×50 px |
| Azure AI Vision — OCR | 500 MB (Read API), 4 MB (analyze) | Dimensions 50×50 to 10000×10000 px |
| Speech — Real-time STT | 60 seconds per utterance | WAV (PCM), MP3, OGG, FLAC |
| Speech — Batch STT | 1 GB per file | WAV, MP3, OGG; up to 1000 files/batch |
| Speech — Custom model audio | 2 hours / 100 MB max per file | — |
| AI Search — Document | 16 MB per document (API push) | Indexer blob limit: 128 MB |
| AI Search — Skillset input | 64,000 chars for text merge | — |
| Video Indexer | 30 GB / 4 hours per file | MP4, MOV, AVI, FLV, MKV, WMV |

---

## 📋 REST Endpoint Patterns

```text
# AI Services (multi-service)
https://{resource}.cognitiveservices.azure.com/

# Azure OpenAI
https://{resource}.openai.azure.com/openai/deployments/{deployment}/chat/completions?api-version=2024-06-01

# AI Vision — Image Analysis 4.0
https://{resource}.cognitiveservices.azure.com/computervision/imageanalysis:analyze?api-version=2024-02-01

# AI Language — Text Analytics
https://{resource}.cognitiveservices.azure.com/language/:analyze-text?api-version=2023-04-01

# Speech — Speech-to-Text
https://{region}.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1

# Speech — Text-to-Speech
https://{region}.tts.speech.microsoft.com/cognitiveservices/v1

# Document Intelligence
https://{resource}.cognitiveservices.azure.com/documentintelligence/documentModels/{model}:analyze?api-version=2024-02-29-preview

# AI Search — Query Index
https://{service}.search.windows.net/indexes/{index}/docs/search?api-version=2024-07-01

# Custom Vision — Prediction
https://{resource}.cognitiveservices.azure.com/customvision/v3.0/Prediction/{projectId}/classify/iterations/{iterationName}/image

# Video Indexer
https://api.videoindexer.ai/{location}/Accounts/{accountId}/Videos/{videoId}/Index
```

---

## 🔗 Official Microsoft Resources

| Resource | Link |
|----------|------|
| AI-102 Exam Page | [learn.microsoft.com](https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-102/) |
| AI-102 Study Guide | [aka.ms/ai102-StudyGuide](https://aka.ms/ai102-StudyGuide) |
| Azure AI Services Docs | [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/) |
| Azure OpenAI Docs | [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/openai/) |
| Azure AI Search Docs | [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/search/) |
| Azure AI Vision Docs | [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/) |
| Azure AI Language Docs | [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/language-service/) |
| Azure Speech Docs | [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/) |
| Document Intelligence Docs | [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/) |
| AI Foundry Docs | [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-studio/) |
| Content Safety Docs | [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/) |
| Azure Architecture Center | [learn.microsoft.com](https://learn.microsoft.com/en-us/azure/architecture/) |
| MS Learn AI-102 Course | [learn.microsoft.com](https://learn.microsoft.com/en-us/training/courses/ai-102t00) |

---

## 📚 Community Study Resources

| Resource | Link |
|----------|------|
| Kenneth Leung — AI-102 Study Guide (GitHub) | [github.com/kennethleungty](https://github.com/kennethleungty/Azure-AI-Engineer-Associate-AI-102) |
| Folberth — AI-102 GitHub Notes | [github.com/folberth](https://github.com/folberth/AI-102-Study-Notes) |
| Arturo Quiroga — AI-102 Repo | [github.com/intelequia](https://github.com/intelequia/AI-102-AIEngineer) |
| John Savill — Azure AI-102 YouTube | [youtube.com/@NTFAQGuy](https://www.youtube.com/watch?v=I7fdWafTcPY) |
| MeasureUp — Official Practice Tests | [measureup.com](https://www.measureup.com/microsoft-practice-test-ai-102-designing-and-implementing-a-microsoft-azure-ai-solution.html) |
| Whizlabs — AI-102 Practice Tests | [whizlabs.com](https://www.whizlabs.com/microsoft-azure-certification-ai-102/) |
| SkillCertPro — AI-102 Practice Exams | [skillcertpro.com](https://skillcertpro.com/product/microsoft-ai-102-practice-exam-test/) |
| r/AzureCertification | [reddit.com](https://www.reddit.com/r/AzureCertification/) |

---

## 🛠 Your Toolkit

### VS Code Extensions

| Extension | Link |
|-----------|------|
| Python | [marketplace](https://marketplace.visualstudio.com/items?itemName=ms-python.python) |
| Jupyter | [marketplace](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) |
| REST Client | [marketplace](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) |
| Bicep | [marketplace](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-bicep) |
| Azure Account | [marketplace](https://marketplace.visualstudio.com/items?itemName=ms-vscode.azure-account) |
| GitHub Copilot | [marketplace](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) |

### CLI & Runtime

- **Python 3.10+** — [python.org](https://www.python.org/downloads/)
- **Azure CLI** — [learn.microsoft.com](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
- **Git** — [git-scm.com](https://git-scm.com/downloads)
- **Docker Desktop** — [docker.com](https://www.docker.com/products/docker-desktop/) *(for container labs)*
- **Azure Free Account** — [azure.microsoft.com](https://azure.microsoft.com/en-us/free/)

---

## 💡 Exam Day Tips

1. **Read every word** — Microsoft questions are intentionally wordy; key qualifiers hide in the details.
2. **Eliminate first** — Cross off obviously wrong answers to improve your odds on uncertain questions.
3. **Flag and move** — Don't spend more than 2 min per question; flag it and come back.
4. **Time budget** — 120 min ÷ ~58 questions ≈ 2 min each. Leave 10 min for review.
5. **Know your SDKs** — Expect Python code snippets; know the method names for each service.
6. **REST vs SDK** — Understand when the exam wants REST API patterns vs SDK calls.
7. **Responsible AI** — Several questions test Content Safety, fairness, transparency — don't skip this topic.
8. **Case studies count** — Case study sections have 4–5 linked questions; read the scenario once, answer all.
9. **No penalty for guessing** — Answer every question; unanswered = wrong.
10. **Take the free practice assessment first** — [Microsoft Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-102/practice/assessment?assessment-type=practice&assessmentId=61) mirrors the real format.

---

## 📋 Supporting Files

| File | Description |
|------|-------------|
| [CLAUDE.md](CLAUDE.md) | Claude Code project instructions & repo context |
| [CITATION.cff](CITATION.cff) | Citation metadata |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | Contributor Code of Conduct |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution guidelines |
| [LICENSE](LICENSE) | License |
| [SECURITY.md](SECURITY.md) | Security policy |
| [SUPPORT.md](SUPPORT.md) | Support information |
| [.env.template](.env.template) | Environment variable template |
| [requirements.txt](requirements.txt) | Python dependencies |
| [.markdownlint.json](.markdownlint.json) | Markdown lint configuration |

---

<p align="center">
  <strong>Good luck on your AI-102 exam! 🎉</strong><br/>
  Last updated: April 2026
</p>
