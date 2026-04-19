# AI-102 Teaching Punchlist — April 2026

**6 segments × 50 minutes | O'Reilly Live Learning | Abe Abraham**

---

## Cross-Cutting: Weave Into Every Segment

- [ ] **Responsible AI**: content safety, fairness, transparency, prompt shields, harm detection
- [ ] **Managed Identity**: use everywhere instead of API keys in code
- [ ] **Microsoft Foundry branding**: new naming as of Dec 2025 (not "Azure AI Foundry")
- [ ] **SDK vs REST**: show both for each service, know endpoint URL patterns
- [ ] **Prebuilt vs Custom**: recurring decision pattern across vision, language, doc intel
- [ ] **File size limits**: per-service limits are explicitly exam-tested
- [ ] **Container deployment**: Docker env vars (ApiKey, Billing, Eula)

---

## Segment 1: Plan & Manage Azure AI Solutions (20–25%)

### Select Appropriate Services (1.1)

- [ ] AI Services landscape: Vision, Language, Speech, OpenAI, Search, Document Intelligence, Content Safety
- [ ] Multi-service resource vs single-service resource — when and why
- [ ] Service selection decision tree for each scenario type
- [ ] Microsoft Foundry portal vs Azure Portal

### Plan, Create, Deploy (1.2)

- [ ] Create Azure AI resource (Portal, CLI, Bicep — show all 3)
- [ ] Deploy AI models — deployment options (Standard, Provisioned, Global)
- [ ] SDK installation: `pip install azure-ai-textanalytics openai azure-search-documents`
- [ ] REST API endpoint structure: `{endpoint}/{service}/{version}/{operation}`
- [ ] CI/CD integration patterns for AI solutions
- [ ] Container deployment: pull from MCR, configure billing endpoint, deploy to ACI
- [ ] **EXAM:** Know Docker run command env vars: `ApiKey`, `Billing`, `Eula=accept`

### Manage, Monitor, Secure (1.3)

- [ ] Diagnostic settings: route logs to Log Analytics, Event Hub, Storage
- [ ] Azure Monitor metrics and alerts for AI Services
- [ ] Cost management: right-size deployments, monitor token usage
- [ ] Key management: two-key rotation pattern, Key Vault integration
- [ ] Authentication: API key vs managed identity vs Entra ID token
- [ ] Network security: Private Link, service endpoints, firewall rules
- [ ] RBAC roles for AI Services (Cognitive Services Contributor, User)

### Responsible AI (1.4)

- [ ] Content moderation: text and image analysis
- [ ] Content Safety severity levels (0–6): Hate, Violence, Sexual, Self-harm
- [ ] Custom blocklists for domain-specific filtering
- [ ] Prompt shields for jailbreak/injection detection
- [ ] Content filters on Azure OpenAI deployments
- [ ] Responsible AI governance framework design

---

## Segment 2: Generative AI Solutions (15–20%)

### Microsoft Foundry Solutions (2.1)

- [ ] Hub vs Project concepts in Microsoft Foundry
- [ ] Deploy hub, project, and supporting resources
- [ ] Model catalog: explore and select models
- [ ] Prompt flow: create, test, evaluate
- [ ] RAG pattern: ground model in your data using AI Search
- [ ] Model evaluation metrics: groundedness, relevance, coherence, fluency
- [ ] Foundry SDK integration in applications
- [ ] Prompt templates: parameterized prompts for reuse

### Azure OpenAI (2.2)

- [ ] Provision Azure OpenAI resource (region availability matters!)
- [ ] Deploy models: GPT-4o (chat), text-embedding-ada-002 (embeddings), DALL-E (images)
- [ ] Chat completions API: system/user/assistant messages
- [ ] **EXAM:** Parameters — temperature, top_p, max_tokens, frequency_penalty, presence_penalty
- [ ] Token calculation and max token behavior (Folberth topic #10)
- [ ] DALL-E image generation: sizes, content filtering
- [ ] Multimodal models: image + text input
- [ ] REST endpoint: `{resource}.openai.azure.com/openai/deployments/{model}/chat/completions`

### Optimize & Operationalize (2.3)

- [ ] Parameter tuning: temperature (0=deterministic, 2=creative)
- [ ] Model monitoring and diagnostic settings
- [ ] Resource optimization: scaling, model updates
- [ ] Tracing and feedback collection
- [ ] Model reflection patterns
- [ ] Container deployment for edge/local
- [ ] Multi-model orchestration
- [ ] Prompt engineering techniques: few-shot, chain-of-thought, system prompts
- [ ] Fine-tuning: JSONL format, training workflow, when to use vs RAG

---

## Segment 3: Agentic Solutions (5–10%) + Computer Vision (10–15%)

### Custom Agents (3.1)

- [ ] Agent concepts: tools, memory, planning, orchestration
- [ ] Agent use cases and when NOT to use agents
- [ ] Microsoft Foundry Agent Service: create, configure tools (code interpreter, file search, functions)
- [ ] Microsoft Agent Framework: complex agent implementations
- [ ] Multi-agent orchestration: planner + executor patterns
- [ ] Multi-user scenarios and autonomous capabilities
- [ ] Testing, optimizing, and deploying agents

### Analyze Images (4.1)

- [ ] Image Analysis 4.0 API: visual features parameter options
- [ ] Features: tags, caption, denseCaptions, objects, people, read
- [ ] Object detection with bounding boxes
- [ ] OCR / Read API: extract printed and handwritten text
- [ ] Interpret response JSON structure and confidence scores
- [ ] **EXAM:** File limits — 4MB, 20MP, supported formats (JPEG, PNG, GIF, BMP, WEBP)

### Custom Vision Models (4.2)

- [ ] Classification (multiclass vs multilabel) vs Object Detection — decision criteria
- [ ] Label images in Custom Vision portal or via SDK
- [ ] Training: minimum images per tag (15+), training time
- [ ] Evaluation metrics: precision, recall, AP (average precision)
- [ ] Publish model to prediction endpoint
- [ ] Consume via REST and SDK
- [ ] **EXAM:** Code-first approach — build model entirely via SDK (Folberth topic #11)

### Video Analysis (4.3)

- [ ] Azure AI Video Indexer: transcript, faces, topics, emotions, OCR, brands
- [ ] Connect Video Indexer to AI Services account
- [ ] Video Indexer API for programmatic access
- [ ] Spatial Analysis: detect presence and movement of people
- [ ] **EXAM:** Video file limits — 2GB, 4 hours, MP4/MOV/WMV/AVI/MKV

---

## Segment 4: Natural Language Processing (15–20%)

### Text Analytics & Translation (5.1)

- [ ] Key phrase extraction
- [ ] Sentiment analysis (document + sentence level, confidence scores)
- [ ] Named Entity Recognition (NER)
- [ ] PII detection and redaction (categories: SSN, email, phone, address)
- [ ] Language detection
- [ ] Entity linking to Wikipedia (Folberth topic #17)
- [ ] Text translation: auto-detect source, transliterate
- [ ] Document translation (preserves formatting)
- [ ] Custom Translator: train, improve, publish custom model

### Speech Services (5.2)

- [ ] Speech-to-Text: real-time recognition, continuous recognition
- [ ] Speech-to-Text from audio file (WAV, MP3, OGG, FLAC)
- [ ] Batch transcription for large audio (up to 1GB, 24 hours)
- [ ] **EXAM — SSML deep dive** (Folberth topic #14):
  - `<voice name="...">` — select neural voice
  - `<prosody rate="..." pitch="..." volume="...">` — control delivery
  - `<emphasis level="strong|moderate|reduced">` — stress words
  - `<break time="500ms"/>` — insert pauses
  - `<say-as interpret-as="date|telephone|cardinal">` — pronunciation
  - Voice styles: `<mstts:express-as style="cheerful|sad|angry">`
- [ ] Custom speech models (acoustic + language adaptation)
- [ ] Intent recognition with Speech SDK
- [ ] Keyword recognition (wake word)
- [ ] Speech translation: speech-to-speech, speech-to-text

### Custom Language Models (5.3)

- [ ] CLU: create intents, entities, add utterances
- [ ] CLU: train, evaluate, deploy, test
- [ ] CLU: optimize, backup, recover models
- [ ] CLU: consume from client application (Python SDK)
- [ ] CLU: import/export projects (Folberth topic #18)
- [ ] Custom Question Answering: create project in Language Studio
- [ ] QnA: add pairs manually + import from FAQ URL/documents
- [ ] QnA: multi-turn conversations
- [ ] QnA: alternate phrasings and chit-chat personality
- [ ] QnA: train, test, publish knowledge base
- [ ] QnA: export knowledge base
- [ ] QnA: multi-language solution
- [ ] **EXAM:** Synonyms in responses (Folberth topic #7)

---

## Segment 5: Knowledge Mining & Information Extraction (15–20%)

### Azure AI Search (6.1)

- [ ] Provision AI Search: Free vs Basic vs Standard tier
- [ ] Index schema: fields (Edm.String, Edm.Int32, Collection), attributes (searchable, filterable, sortable, facetable)
- [ ] Data sources: Blob Storage, SQL Database, Cosmos DB, Table Storage
- [ ] Indexers: schedule, field mappings, output field mappings
- [ ] Built-in skillset: entity recognition, key phrases, OCR, image analysis, language detection
- [ ] Custom skills: Azure Function integration, Web API skill
- [ ] Knowledge store projections: file, object, table
- [ ] Query syntax: `$filter`, `$select`, `$orderby`, `$top`, `search.ismatch`, wildcards
- [ ] Semantic search configuration
- [ ] Vector search: vector fields, embedding generation, vector queries
- [ ] Hybrid search: keyword + vector combined
- [ ] **EXAM:** Indexable resource types (Folberth topic #15)

### Document Intelligence (6.2)

- [ ] Prebuilt models: invoice, receipt, ID document, business card, W-2, health insurance
- [ ] Analyze via REST (async polling pattern: POST → GET operation-location)
- [ ] Analyze via Python SDK (`begin_analyze_document`)
- [ ] Custom models: label in DI Studio, train, evaluate
- [ ] Composed models: combine multiple custom models
- [ ] **EXAM:** File limits — 4MB (Free) / 500MB (Standard), 2/2000 pages, formats
- [ ] **EXAM:** Synonyms in Document Intelligence (Folberth topic #7)

### Content Understanding (6.3)

- [ ] OCR pipeline: extract text from images and scanned documents
- [ ] Document summarization and classification
- [ ] Attribute detection (handwritten vs printed, language)
- [ ] Entity, table, and image extraction from complex documents
- [ ] Process video and audio content
- [ ] Differences from Document Intelligence — when to use which

---

## Segment 6: Review & Exam Prep

### Quick Reference Review

- [ ] Walk through service comparison matrix
- [ ] File size limits cheat sheet (all services)
- [ ] REST endpoint patterns for each service
- [ ] Authentication methods decision tree
- [ ] Prebuilt vs custom decision matrix
- [ ] SSML attribute quick reference

### Practice Questions

- [ ] Work through 10 selected scenario questions
- [ ] Discuss rationale and common traps
- [ ] Focus on "which service" decision scenarios

### Exam Strategy

- [ ] Choose Python or C# at start — cannot switch
- [ ] ~58 questions / 120 minutes — pace yourself
- [ ] MS Learn accessible but time-consuming to navigate
- [ ] Case study sections cannot be revisited after completion
- [ ] Managed identity = usually correct for auth questions
- [ ] Know service limits — file sizes explicitly tested
- [ ] Think end-to-end: ingest → process → expose → secure → monitor

---
