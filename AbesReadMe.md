# Abe's AI-102 Repo Navigation Guide

> **Exam:** AI-102 — Designing and Implementing a Microsoft Azure AI Solution  
> **Passing Score:** 700 / 1000 | **Questions:** ~58 | **Duration:** 120 min  
> **Skills Measured Version:** December 23, 2025 (Microsoft Foundry branding)  
> **Retires:** June 30, 2026

---

## Repo Map at a Glance

```
AI102/
├── AbesReadMe.md              ← YOU ARE HERE
├── course/                    ← Self-paced training course (start here)
│   ├── syllabus.md            ← Course entry point, 12-week study plan
│   ├── module-1-plan-manage/
│   ├── module-2-generative-ai/
│   ├── module-3-agentic-solutions/
│   ├── module-4-computer-vision/
│   ├── module-5-nlp/
│   └── module-6-knowledge-mining/
├── docs/                      ← Exam reference materials
│   ├── ai102-objective-domain.md
│   ├── quick-reference-cards.md
│   └── reference-architectures.md
├── infra/                     ← Bicep IaC templates (7 templates)
│   ├── ai-services.bicep
│   ├── openai.bicep
│   ├── ai-foundry.bicep
│   ├── vision.bicep
│   ├── speech.bicep
│   ├── ai-search.bicep
│   ├── document-intelligence.bicep
│   ├── modules/               ← Reusable Bicep modules
│   └── parameters/            ← Parameter files
├── scripts/                   ← Runnable scripts by language
│   ├── python/        (12+ scripts across 7 service areas)
│   ├── powershell/    (4 scripts)
│   ├── rest-api/      (4 .http files)
│   └── csharp/        (planned)
├── images/                    ← Architecture diagrams
├── ai102-course-flow.md       ← 6-segment live instructor schedule
├── ai102-punchlist.md         ← Demo punchlist for live sessions
├── CLAUDE.md                  ← AI assistant guidance for this repo
├── requirements.txt           ← Python dependencies
└── README.md                  ← Original repo README
```

---

## Exam Domain Weights

| # | Domain | Weight | Course Module |
|---|--------|--------|---------------|
| 1 | Plan and manage an Azure AI solution | 20–25% | [Module 1](course/module-1-plan-manage/) |
| 2 | Implement generative AI solutions | 15–20% | [Module 2](course/module-2-generative-ai/) |
| 3 | Implement an agentic solution | 5–10% | [Module 3](course/module-3-agentic-solutions/) |
| 4 | Implement computer vision solutions | 10–15% | [Module 4](course/module-4-computer-vision/) |
| 5 | Implement NLP solutions | 15–20% | [Module 5](course/module-5-nlp/) |
| 6 | Implement knowledge mining & info extraction | 15–20% | [Module 6](course/module-6-knowledge-mining/) |

---

## Step-by-Step Study Plan

### Phase 0 — Orient (Day 1)

1. **Read this file** to understand the repo layout.
2. **Open [`course/syllabus.md`](course/syllabus.md)** — your course home page with the 12-week study plan, module links, and MS Learn paths.
3. **Skim [`docs/ai102-objective-domain.md`](docs/ai102-objective-domain.md)** to see every exam objective in one place.
4. **Bookmark the official practice assessment:** <https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-102/practice/assessment?assessment-type=practice&assessmentId=61>

---

### Phase 1 — Module 1: Plan & Manage Azure AI Solutions (Weeks 1–2)

**Exam weight: 20–25%** — Covers AI Services provisioning, SDK vs REST, security, containers, monitoring, and cost management.

| Order | File | What You'll Learn |
|-------|------|-------------------|
| 1 | [`overview.md`](course/module-1-plan-manage/overview.md) | Module objectives, MS Learn links, service landscape |
| 2 | [`lesson-1-provision-manage.md`](course/module-1-plan-manage/lesson-1-provision-manage.md) | Multi-service vs single-service resources, SDK vs REST patterns |
| 3 | [`lesson-2-security.md`](course/module-1-plan-manage/lesson-2-security.md) | Managed identity, Key Vault integration, network security |
| 4 | [`lesson-3-containers.md`](course/module-1-plan-manage/lesson-3-containers.md) | Docker deployment, container env vars (ApiKey, Billing, Eula) |
| 5 | [`lesson-4-monitoring.md`](course/module-1-plan-manage/lesson-4-monitoring.md) | Diagnostic settings, Log Analytics, alerts, cost management |
| 6 | [`knowledge-check.md`](course/module-1-plan-manage/knowledge-check.md) | Scenario-based questions with answers |

**Bicep labs to deploy:**

| Bicep Template | What It Provisions |
|----------------|-------------------|
| [`infra/ai-services.bicep`](infra/ai-services.bicep) | Multi-service AI resource |
| [`infra/ai-services-secure.bicep`](infra/ai-services-secure.bicep) | AI Services with Key Vault + managed identity |

**Python scripts to run:**

| Script | What It Does |
|--------|-------------|
| [`scripts/python/services/provision-and-test.py`](scripts/python/services/provision-and-test.py) | Provision and call AI Services via SDK |
| [`scripts/python/services/secure-access.py`](scripts/python/services/secure-access.py) | Authenticate with managed identity / Key Vault |
| [`scripts/python/services/content-safety.py`](scripts/python/services/content-safety.py) | Analyze text for harmful content |

**PowerShell scripts:**

| Script | What It Does |
|--------|-------------|
| [`scripts/powershell/configure-monitoring.ps1`](scripts/powershell/configure-monitoring.ps1) | Configure diagnostic settings and alerts |
| [`scripts/powershell/deploy-container.ps1`](scripts/powershell/deploy-container.ps1) | Deploy AI Services in a Docker container |

---

### Phase 2 — Module 2: Generative AI Solutions (Weeks 3–4)

**Exam weight: 15–20%** — Covers Azure OpenAI, prompt engineering, RAG, DALL·E, fine-tuning, and AI Foundry.

| Order | File | What You'll Learn |
|-------|------|-------------------|
| 1 | [`overview.md`](course/module-2-generative-ai/overview.md) | Module objectives, model catalog, deployment options |
| 2 | [`lesson-1-openai.md`](course/module-2-generative-ai/lesson-1-openai.md) | Azure OpenAI, chat completions, prompt engineering |
| 3 | [`lesson-2-rag.md`](course/module-2-generative-ai/lesson-2-rag.md) | RAG pattern, grounding, data integration |
| 4 | [`lesson-3-images-finetune.md`](course/module-2-generative-ai/lesson-3-images-finetune.md) | DALL·E image generation, fine-tuning models |
| 5 | [`knowledge-check.md`](course/module-2-generative-ai/knowledge-check.md) | Scenario-based questions with answers |

**Bicep labs to deploy:**

| Bicep Template | What It Provisions |
|----------------|-------------------|
| [`infra/openai.bicep`](infra/openai.bicep) | Azure OpenAI resource with model deployments |
| [`infra/ai-foundry.bicep`](infra/ai-foundry.bicep) | AI Foundry hub + project |

**Python scripts to run:**

| Script | What It Does |
|--------|-------------|
| [`scripts/python/openai/chat-completions.py`](scripts/python/openai/chat-completions.py) | Chat completions with system/user messages |
| [`scripts/python/openai/rag-pattern.py`](scripts/python/openai/rag-pattern.py) | RAG — ground answers with your own data |
| [`scripts/python/openai/generate-images.py`](scripts/python/openai/generate-images.py) | Generate images with DALL·E |
| [`scripts/python/openai/fine-tune.py`](scripts/python/openai/fine-tune.py) | Fine-tune a model with custom training data |

---

### Phase 3 — Module 3: Agentic Solutions (Week 5)

**Exam weight: 5–10%** — Covers AI Foundry agents, tool use, multi-agent orchestration.

| Order | File | What You'll Learn |
|-------|------|-------------------|
| 1 | [`overview.md`](course/module-3-agentic-solutions/overview.md) | Module objectives, agent architecture patterns |
| 2 | [`lesson-1-agents.md`](course/module-3-agentic-solutions/lesson-1-agents.md) | Foundry agents, function calling, tool use |
| 3 | [`knowledge-check.md`](course/module-3-agentic-solutions/knowledge-check.md) | Scenario-based questions with answers |

**Python scripts to run:**

| Script | What It Does |
|--------|-------------|
| [`scripts/python/agents/foundry-agent.py`](scripts/python/agents/foundry-agent.py) | Build and run an AI Foundry agent |
| [`scripts/python/agents/multi-agent-orchestration.py`](scripts/python/agents/multi-agent-orchestration.py) | Multi-agent orchestration pattern |

---

### Phase 4 — Module 4: Computer Vision Solutions (Weeks 6–7)

**Exam weight: 10–15%** — Covers Image Analysis, Custom Vision, Video Indexer, and Face API.

| Order | File | What You'll Learn |
|-------|------|-------------------|
| 1 | [`overview.md`](course/module-4-computer-vision/overview.md) | Module objectives, Vision service capabilities |
| 2 | [`lesson-1-image-analysis.md`](course/module-4-computer-vision/lesson-1-image-analysis.md) | Image Analysis 4.0, captions, tags, objects, OCR |
| 3 | [`lesson-2-custom-vision.md`](course/module-4-computer-vision/lesson-2-custom-vision.md) | Custom Vision training, classification, object detection |
| 4 | [`lesson-3-video-face.md`](course/module-4-computer-vision/lesson-3-video-face.md) | Video Indexer insights, Face API detection & verification |
| 5 | [`knowledge-check.md`](course/module-4-computer-vision/knowledge-check.md) | Scenario-based questions with answers |

**Bicep labs to deploy:**

| Bicep Template | What It Provisions |
|----------------|-------------------|
| [`infra/vision.bicep`](infra/vision.bicep) | Computer Vision resource |

**Python scripts to run:**

| Script | What It Does |
|--------|-------------|
| [`scripts/python/vision/analyze-image.py`](scripts/python/vision/analyze-image.py) | Analyze image — captions, tags, objects |
| [`scripts/python/vision/custom-vision-train.py`](scripts/python/vision/custom-vision-train.py) | Train a Custom Vision classifier |
| [`scripts/python/vision/video-indexer.py`](scripts/python/vision/video-indexer.py) | Extract insights from video with Video Indexer |
| [`scripts/python/vision/face-detection.py`](scripts/python/vision/face-detection.py) | Detect and verify faces with Face API |

---

### Phase 5 — Module 5: Natural Language Processing (Weeks 8–9)

**Exam weight: 15–20%** — Covers Text Analytics, Translator, Speech Services, CLU, and Question Answering.

| Order | File | What You'll Learn |
|-------|------|-------------------|
| 1 | [`overview.md`](course/module-5-nlp/overview.md) | Module objectives, NLP service landscape |
| 2 | [`lesson-1-text-analytics.md`](course/module-5-nlp/lesson-1-text-analytics.md) | Sentiment, key phrases, entities, PII, language detection |
| 3 | [`lesson-2-translation.md`](course/module-5-nlp/lesson-2-translation.md) | Text translation, custom translator, document translation |
| 4 | [`lesson-3-speech.md`](course/module-5-nlp/lesson-3-speech.md) | Speech-to-text, text-to-speech, pronunciation assessment |
| 5 | [`lesson-4-clu-qna.md`](course/module-5-nlp/lesson-4-clu-qna.md) | Conversational Language Understanding, Question Answering |
| 6 | [`knowledge-check.md`](course/module-5-nlp/knowledge-check.md) | Scenario-based questions with answers |

**Bicep labs to deploy:**

| Bicep Template | What It Provisions |
|----------------|-------------------|
| [`infra/speech.bicep`](infra/speech.bicep) | Speech Services resource |

**Python scripts to run:**

| Script | What It Does |
|--------|-------------|
| [`scripts/python/language/text-analytics.py`](scripts/python/language/text-analytics.py) | Sentiment, key phrases, entities, PII detection |
| [`scripts/python/language/translate-text.py`](scripts/python/language/translate-text.py) | Translate text across languages |
| [`scripts/python/speech/speech-to-text.py`](scripts/python/speech/speech-to-text.py) | Transcribe audio to text |
| [`scripts/python/speech/text-to-speech.py`](scripts/python/speech/text-to-speech.py) | Synthesize speech from text |
| [`scripts/python/language/clu-client.py`](scripts/python/language/clu-client.py) | Conversational Language Understanding client |
| [`scripts/python/language/qna-client.py`](scripts/python/language/qna-client.py) | Question Answering client |

---

### Phase 6 — Module 6: Knowledge Mining & Information Extraction (Weeks 10–11)

**Exam weight: 15–20%** — Covers AI Search, skillsets, indexers, Document Intelligence, and custom skills.

| Order | File | What You'll Learn |
|-------|------|-------------------|
| 1 | [`overview.md`](course/module-6-knowledge-mining/overview.md) | Module objectives, knowledge mining pipeline |
| 2 | [`lesson-1-ai-search.md`](course/module-6-knowledge-mining/lesson-1-ai-search.md) | Index design, skillsets, indexers, semantic ranking |
| 3 | [`lesson-2-document-intelligence.md`](course/module-6-knowledge-mining/lesson-2-document-intelligence.md) | Prebuilt models, custom models, document processing |
| 4 | [`knowledge-check.md`](course/module-6-knowledge-mining/knowledge-check.md) | Scenario-based questions with answers |

**Bicep labs to deploy:**

| Bicep Template | What It Provisions |
|----------------|-------------------|
| [`infra/ai-search.bicep`](infra/ai-search.bicep) | Azure AI Search service |
| [`infra/document-intelligence.bicep`](infra/document-intelligence.bicep) | Document Intelligence resource |

**Python scripts to run:**

| Script | What It Does |
|--------|-------------|
| [`scripts/python/search/create-index.py`](scripts/python/search/create-index.py) | Create a search index with skillset |
| [`scripts/python/search/query-index.py`](scripts/python/search/query-index.py) | Query a search index (full-text, filters, facets) |
| [`scripts/python/document-intelligence/prebuilt-invoice.py`](scripts/python/document-intelligence/prebuilt-invoice.py) | Extract fields from invoices with prebuilt model |
| [`scripts/python/document-intelligence/custom-model.py`](scripts/python/document-intelligence/custom-model.py) | Train and use a custom Document Intelligence model |

---

### Phase 7 — Review & Exam Prep (Week 12)

1. **Re-take all knowledge checks** — aim for 90%+ on every module.
2. **Review quick reference cards:** [`docs/quick-reference-cards.md`](docs/quick-reference-cards.md) — comparison tables, cheat sheets, and decision trees.
3. **Study reference architectures:** [`docs/reference-architectures.md`](docs/reference-architectures.md) — key architectures mapped to exam objectives.
4. **Drill practice questions:** [`docs/practice-questions.md`](docs/practice-questions.md) — scenario-based questions with explanations.
5. **Take the official practice assessment:** <https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-102/practice/assessment?assessment-type=practice&assessmentId=61>
6. **Run the end-to-end lab:** [`scripts/python/e2e-solution/`](scripts/python/e2e-solution/) — ties together all six domains in a single pipeline.

---

## How to Deploy Bicep Labs

Every Bicep template in `infra/` can be deployed standalone. Deploy with:

```bash
# 1. Log in
az login

# 2. Create a resource group
az group create --name ai102-labs-rg --location eastus

# 3. Deploy a template
az deployment group create \
  --resource-group ai102-labs-rg \
  --template-file infra/<template-name>.bicep

# 4. Clean up when done (IMPORTANT — avoid charges)
az group delete --name ai102-labs-rg --yes --no-wait
```

> **Cost tip:** Always delete your resource group when you're done with a lab. Use the Azure Cost Management blade to monitor spending. Most AI Services have a free tier — leverage it.

---

## Supporting Files Reference

| File | Purpose |
|------|---------|
| [`ai102-course-flow.md`](ai102-course-flow.md) | 6-segment live instructor schedule with demos |
| [`ai102-punchlist.md`](ai102-punchlist.md) | Demo punchlist for live sessions |
| [`course/syllabus.md`](course/syllabus.md) | Course entry point — 12-week plan, module links, MS Learn paths |
| [`docs/ai102-objective-domain.md`](docs/ai102-objective-domain.md) | Complete exam objective domain |
| [`docs/quick-reference-cards.md`](docs/quick-reference-cards.md) | Comparison tables and cheat sheets |
| [`docs/reference-architectures.md`](docs/reference-architectures.md) | Key architectures mapped to exam objectives |
| [`CLAUDE.md`](CLAUDE.md) | AI assistant guidance for this repo |
| [`infra/README.md`](infra/README.md) | Bicep template catalog and usage notes |
| [`scripts/README.md`](scripts/README.md) | Script inventory and execution guide |

---

## Scripts Inventory

### Python Scripts by Directory (`scripts/python/`)

| Directory | Script | Module |
|-----------|--------|--------|
| `services/` | [`provision-and-test.py`](scripts/python/services/provision-and-test.py) | Module 1 |
| `services/` | [`secure-access.py`](scripts/python/services/secure-access.py) | Module 1 |
| `services/` | [`content-safety.py`](scripts/python/services/content-safety.py) | Module 1 |
| `openai/` | [`chat-completions.py`](scripts/python/openai/chat-completions.py) | Module 2 |
| `openai/` | [`rag-pattern.py`](scripts/python/openai/rag-pattern.py) | Module 2 |
| `openai/` | [`generate-images.py`](scripts/python/openai/generate-images.py) | Module 2 |
| `openai/` | [`fine-tune.py`](scripts/python/openai/fine-tune.py) | Module 2 |
| `agents/` | [`foundry-agent.py`](scripts/python/agents/foundry-agent.py) | Module 3 |
| `agents/` | [`multi-agent-orchestration.py`](scripts/python/agents/multi-agent-orchestration.py) | Module 3 |
| `vision/` | [`analyze-image.py`](scripts/python/vision/analyze-image.py) | Module 4 |
| `vision/` | [`custom-vision-train.py`](scripts/python/vision/custom-vision-train.py) | Module 4 |
| `vision/` | [`video-indexer.py`](scripts/python/vision/video-indexer.py) | Module 4 |
| `vision/` | [`face-detection.py`](scripts/python/vision/face-detection.py) | Module 4 |
| `language/` | [`text-analytics.py`](scripts/python/language/text-analytics.py) | Module 5 |
| `language/` | [`translate-text.py`](scripts/python/language/translate-text.py) | Module 5 |
| `speech/` | [`speech-to-text.py`](scripts/python/speech/speech-to-text.py) | Module 5 |
| `speech/` | [`text-to-speech.py`](scripts/python/speech/text-to-speech.py) | Module 5 |
| `language/` | [`clu-client.py`](scripts/python/language/clu-client.py) | Module 5 |
| `language/` | [`qna-client.py`](scripts/python/language/qna-client.py) | Module 5 |
| `search/` | [`create-index.py`](scripts/python/search/create-index.py) | Module 6 |
| `search/` | [`query-index.py`](scripts/python/search/query-index.py) | Module 6 |
| `document-intelligence/` | [`prebuilt-invoice.py`](scripts/python/document-intelligence/prebuilt-invoice.py) | Module 6 |
| `document-intelligence/` | [`custom-model.py`](scripts/python/document-intelligence/custom-model.py) | Module 6 |

### REST API Files (`scripts/rest-api/`)

| File | Service |
|------|---------|
| [`detect-language.http`](scripts/rest-api/detect-language.http) | Language Detection |
| [`openai-chat.http`](scripts/rest-api/openai-chat.http) | Azure OpenAI Chat |
| [`text-analytics.http`](scripts/rest-api/text-analytics.http) | Text Analytics |
| [`vision-analyze.http`](scripts/rest-api/vision-analyze.http) | Image Analysis |

### PowerShell Scripts (`scripts/powershell/`)

| Script | Purpose |
|--------|---------|
| [`provision-lab-environment.ps1`](scripts/powershell/provision-lab-environment.ps1) | Provision full lab environment |
| [`configure-monitoring.ps1`](scripts/powershell/configure-monitoring.ps1) | Configure diagnostic settings & alerts |
| [`deploy-container.ps1`](scripts/powershell/deploy-container.ps1) | Deploy AI Services in Docker container |
| [`cleanup-lab-environment.ps1`](scripts/powershell/cleanup-lab-environment.ps1) | Tear down all lab resources |

---

## Official Microsoft Resources

| Resource | Link |
|----------|------|
| AI-102 Exam Page | <https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-102/> |
| Official Practice Assessment | <https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-102/practice/assessment?assessment-type=practice&assessmentId=61> |
| AI-102 Study Guide | <https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-102> |
| MS Learn: Plan & Manage AI Solutions | <https://learn.microsoft.com/en-us/training/paths/plan-manage-azure-ai-solution/> |
| MS Learn: Generative AI Solutions | <https://learn.microsoft.com/en-us/training/paths/create-azure-openai-solution/> |
| MS Learn: Computer Vision Solutions | <https://learn.microsoft.com/en-us/training/paths/create-computer-vision-solutions-azure-cognitive-services/> |
| MS Learn: NLP Solutions | <https://learn.microsoft.com/en-us/training/paths/explore-natural-language-processing/> |
| MS Learn: Knowledge Mining | <https://learn.microsoft.com/en-us/training/paths/implement-knowledge-mining-azure-cognitive-search/> |
| Azure AI Services Documentation | <https://learn.microsoft.com/en-us/azure/ai-services/> |
| Azure OpenAI Documentation | <https://learn.microsoft.com/en-us/azure/ai-services/openai/> |

---

## Community Resources

| Resource | Link |
|----------|------|
| John Savill's AI-102 Study Cram | <https://www.youtube.com/results?search_query=john+savill+ai-102> |
| Microsoft AI-102 GitHub Labs | <https://microsoftlearning.github.io/mslearn-ai-services/> |
| AI-102 Exam Readiness Zone | <https://learn.microsoft.com/en-us/shows/exam-readiness-zone/?terms=ai-102> |
| Azure AI Community Hub | <https://techcommunity.microsoft.com/category/azure-ai-services/> |
| r/AzureCertification | <https://www.reddit.com/r/AzureCertification/> |

---

## Quick Tips for Exam Day

1. **Read every word** — AI-102 questions hinge on subtle requirements like "minimize latency" vs. "minimize cost" vs. "minimize development effort."
2. **Know which service to pick** — The exam loves "which Azure AI service should you use?" questions. Know the decision tree: AI Services vs. OpenAI vs. Custom Vision vs. AI Search vs. Document Intelligence.
3. **SDK vs REST** — Understand when to use each. SDK for production apps, REST for quick testing and language-agnostic integration.
4. **Managed Identity always** — Default answer for any "how should the app authenticate to AI Services" question.
5. **Container deployment** — Know the three required env vars: `ApiKey`, `Billing` (endpoint URL), `Eula=accept`.
6. **RAG pattern** — Retrieval-Augmented Generation is heavily tested. Know the architecture: AI Search → retrieve → OpenAI → generate.
7. **Skillset pipeline** — Understand the AI Search enrichment pipeline: data source → indexer → skillset → index.
8. **Custom vs prebuilt models** — Know when to use prebuilt Document Intelligence models (invoice, receipt, ID) vs. training a custom model.
9. **Content Safety** — Know how to configure content filters on Azure OpenAI deployments and when to use the Content Safety API.
10. **Flag and review** — Flag uncertain questions immediately. You'll have time at the end to revisit. Don't waste 5 minutes on one question early.

---

*Last updated: April 2026*
