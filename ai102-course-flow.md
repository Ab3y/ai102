# AI-102 Designing and Implementing Azure AI Solutions — Course Flow

**Instructor:** Abe Abraham | **Platform:** O'Reilly Live Learning / Workshop
**Duration:** 6 × 50-minute segments with 10-minute breaks
**Exam Version:** Skills measured as of December 23, 2025

---

## Schedule Overview

| Time | Activity |
|------|----------|
| 9:00 AM | Segment 1 — Plan & Manage Azure AI Solutions |
| 9:50 AM | Break (10 min) |
| 10:00 AM | Segment 2 — Generative AI Solutions |
| 10:50 AM | Break (10 min) |
| 11:00 AM | Segment 3 — Agentic Solutions + Computer Vision |
| 11:50 AM | Lunch (30 min) |
| 12:20 PM | Segment 4 — Natural Language Processing |
| 1:10 PM | Break (10 min) |
| 1:20 PM | Segment 5 — Knowledge Mining & Information Extraction |
| 2:10 PM | Break (10 min) |
| 2:20 PM | Segment 6 — Review, Practice Questions & Exam Prep |
| 3:10 PM | End |

---

## Segment 1: Plan & Manage Azure AI Solutions (20–25%)

**Duration:** 50 minutes | **Module:** [module-1-plan-manage](course/module-1-plan-manage/overview.md)

### Topics (30 min)
- Azure AI Services landscape — when to use which service
- Multi-service vs single-service resource provisioning
- SDK vs REST API patterns (show both)
- Managed identity & Key Vault integration
- Container deployment (Docker env vars: ApiKey, Billing, Eula)
- Monitoring: diagnostic settings, Log Analytics, alerts
- Cost management strategies

### Demo (15 min)
1. **Provision AI Services** via Portal + CLI + Bicep (`infra/ai-services.bicep`)
2. **REST API call** — detect language (`scripts/rest-api/detect-language.http`)
3. **Python SDK call** — same operation (`scripts/python/services/provision-and-test.py`)
4. **Content Safety** — analyze text for harmful content (`scripts/python/services/content-safety.py`)

### Knowledge Check (5 min)
- 3 quick scenario questions from [knowledge-check.md](course/module-1-plan-manage/knowledge-check.md)

---

## Segment 2: Generative AI Solutions (15–20%)

**Duration:** 50 minutes | **Module:** [module-2-generative-ai](course/module-2-generative-ai/overview.md)

### Topics (25 min)
- Azure OpenAI provisioning and model deployment
- Chat completions API — parameters (temperature, top_p, max_tokens)
- Token calculation and limits
- RAG pattern: search → retrieve → augment → generate
- Microsoft Foundry: hub, project, prompt flow, evaluation
- DALL-E image generation
- Fine-tuning vs prompt engineering vs RAG decision tree
- Prompt engineering techniques

### Demo (20 min)
1. **Azure OpenAI Playground** — deploy GPT-4o, test in portal
2. **Chat Completions** — Python SDK with parameter tuning (`scripts/python/openai/chat-completions.py`)
3. **RAG Pattern** — query AI Search + ground response (`scripts/python/openai/rag-pattern.py`)
4. **REST API** — show endpoint structure (`scripts/rest-api/openai-chat.http`)

### Knowledge Check (5 min)
- 3 quick scenario questions

---

## Segment 3: Agentic Solutions (5–10%) + Computer Vision (10–15%)

**Duration:** 50 minutes | **Modules:** [module-3](course/module-3-agentic-solutions/overview.md) + [module-4](course/module-4-computer-vision/overview.md)

### Agentic Solutions (15 min)
- Agent concepts: tools, memory, orchestration
- Microsoft Foundry Agent Service vs Agent Framework
- Multi-agent orchestration patterns
- Testing and deployment

### Computer Vision (25 min)
- Image Analysis 4.0 — visual features, tags, captions, objects, OCR
- Custom Vision — classification vs object detection, training workflow
- Code-first Custom Vision (exam tested!)
- Video Indexer — insights extraction, spatial analysis
- Face API — responsible AI restrictions
- File size limits (4MB/20MP for Vision, 6MB for Custom Vision)

### Demo (10 min)
1. **Image Analysis** — analyze image with all features (`scripts/python/vision/analyze-image.py`)
2. **OCR** — extract text from handwritten image (`scripts/rest-api/vision-analyze.http`)

---

## Segment 4: Natural Language Processing (15–20%)

**Duration:** 50 minutes | **Module:** [module-5-nlp](course/module-5-nlp/overview.md)

### Topics (25 min)
- Text Analytics — sentiment, entities, key phrases, PII, language detection
- Entity linking (Wikipedia)
- Translation — text, documents, custom translator
- Speech-to-Text — real-time, batch, custom speech
- Text-to-Speech — SSML deep dive (prosody, emphasis, break, voice styles)
- Intent & keyword recognition
- Speech translation
- CLU — intents, entities, utterances, training workflow
- Custom Question Answering — knowledge base, multi-turn, chit-chat
- Import/export language projects

### Demo (20 min)
1. **Text Analytics** — sentiment + PII detection (`scripts/python/language/text-analytics.py`)
2. **SSML** — text-to-speech with styles (`scripts/python/speech/text-to-speech.py`)
3. **REST API** — text analytics endpoints (`scripts/rest-api/text-analytics.http`)

### Knowledge Check (5 min)
- 3 SSML-focused questions (heavily tested!)

---

## Segment 5: Knowledge Mining & Information Extraction (15–20%)

**Duration:** 50 minutes | **Module:** [module-6-knowledge-mining](course/module-6-knowledge-mining/overview.md)

### Topics (25 min)
- Azure AI Search — indexes, skillsets, indexers, data sources
- Built-in skills vs custom skills (Azure Functions)
- Knowledge store projections (file, object, table)
- Query syntax — $filter, $select, $orderby, wildcards, fuzzy
- Semantic search and vector search
- Document Intelligence — prebuilt models (invoice, receipt, ID)
- Custom Document Intelligence models — training, evaluation, composed models
- Content Understanding — OCR pipelines, classification, multimedia
- File size limits (4MB free / 500MB standard, supported formats)

### Demo (20 min)
1. **Create AI Search Index** — with vector fields (`scripts/python/search/create-index.py`)
2. **Query Index** — full-text + vector + hybrid (`scripts/python/search/query-index.py`)
3. **Document Intelligence** — analyze invoice (`scripts/python/document-intelligence/prebuilt-invoice.py`)

### Knowledge Check (5 min)
- 3 scenario questions on service selection

---

## Segment 6: Review, Practice & Exam Prep

**Duration:** 50 minutes

### Quick Reference Review (15 min)
- Walk through [quick-reference-cards.md](docs/quick-reference-cards.md)
- File size limits cheat sheet
- REST endpoint patterns
- Authentication methods comparison
- Prebuilt vs custom decision matrix

### Practice Questions (20 min)
- Work through 10 selected questions from [practice-questions.md](docs/practice-questions.md)
- Discuss answer rationale and common traps

### Exam Strategy (10 min)
- Choose Python or C# at start — cannot switch
- ~58 questions in 120 minutes — time management
- MS Learn accessible but time-consuming
- Case study sections cannot be revisited
- Know service limits (file sizes, quotas)
- Managed identity = usually correct for auth questions
- End-to-end thinking: ingest → process → expose → secure

### Resources (5 min)
- [Official Practice Assessment](https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-102/practice/assessment?assessment-type=practice&assessmentId=61)
- [Exam Sandbox](https://aka.ms/examdemo)
- [Kenneth Leung's GitHub Notes](https://github.com/kennethleungty/Azure-AI-Engineer-Associate-Notes)
- [John Folberth's Study Guide](https://github.com/JFolberth/Microsoft-AI-102-Study-Guide)
- [Arturo Quiroga's Exam Prep](https://github.com/Arturo-Quiroga-MSFT/AI-102-Exam-Prep)

---

## Cross-Cutting Themes (weave into every segment)

- [ ] **Responsible AI**: content safety, fairness, transparency, content filters, prompt shields
- [ ] **Managed Identity**: use for all service-to-service auth
- [ ] **Microsoft Foundry branding**: new naming (Dec 2025 update)
- [ ] **SDK vs REST**: show both approaches for each service
- [ ] **Prebuilt vs Custom**: recurring decision pattern
- [ ] **File size limits**: per-service limits are explicitly tested
- [ ] **Cost optimization**: right-size models, free vs paid tiers
