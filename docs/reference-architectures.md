# AI-102 Reference Architectures

> Key architectural patterns for the Microsoft AI-102 exam.
> Each section includes a Mermaid diagram, component breakdown, and exam-relevant notes.

---

## 1. RAG (Retrieval Augmented Generation) Architecture

Retrieval Augmented Generation grounds LLM responses in your own data, reducing hallucinations and enabling domain-specific answers without fine-tuning.

```mermaid
flowchart LR
    User([User]) --> App[Application Layer]
    App -->|query + chat history| AOAI[Azure OpenAI<br/>GPT-4 / GPT-4o]
    AOAI -->|system prompt<br/>+ grounding context| App
    App -->|search query /<br/>vector embedding| Search[Azure AI Search<br/>Vector + Semantic]
    Search -->|ranked results<br/>+ captions| App
    Search -->|indexer pulls<br/>documents| Blob[(Azure Blob Storage<br/>Documents / PDFs)]
    App -->|embedding request| Embed[Azure OpenAI<br/>Embedding Model]
    Embed -->|vector| App

    style AOAI fill:#4B8BBE,color:#fff
    style Search fill:#E97132,color:#fff
    style Blob fill:#0078D4,color:#fff
    style Embed fill:#4B8BBE,color:#fff
```

### How It Works

1. User submits a question via the application.
2. The app generates a vector embedding of the query using an Azure OpenAI embedding model.
3. Azure AI Search performs **hybrid retrieval** (vector similarity + keyword BM25) with optional **semantic ranking**.
4. Top-ranked document chunks are injected into the **system prompt** as grounding context.
5. Azure OpenAI generates a response constrained to the retrieved context.

### Key Components

| Component | Purpose |
|---|---|
| **Azure OpenAI (Chat)** | Generates natural language answers grounded in context |
| **Azure OpenAI (Embedding)** | Converts queries and documents into vectors (text-embedding-ada-002 / text-embedding-3-large) |
| **Azure AI Search** | Stores vectors and text; performs hybrid + semantic retrieval |
| **Blob Storage** | Source document store (PDF, DOCX, HTML, etc.) |
| **Integrated Vectorization** | Search-managed chunking and embedding at index time |

### Key Exam Points

- **"On Your Data"** feature in Azure OpenAI connects directly to AI Search — no custom code needed for basic RAG.
- Hybrid search (vector + keyword) with semantic ranker provides the best relevance.
- `role: "system"` messages carry the grounding context; `role: "user"` carries the question.
- **Temperature = 0** is recommended for factual/grounded responses.
- Chunking strategy (size, overlap) directly impacts retrieval quality.
- Citations can be returned by instructing the model to reference `[docN]` source IDs.

### Exam Objectives

- *Plan and manage an Azure AI solution* — selecting appropriate services for RAG
- *Implement Azure AI Search solutions* — indexing, querying, vectorization
- *Create solutions with Azure OpenAI* — completions API, system messages, grounding

### Relevant Labs

- Lab: Implement RAG with Azure OpenAI and Azure AI Search
- Lab: Use your own data with Azure OpenAI

---

## 2. Azure AI Search Enrichment Pipeline

The AI enrichment pipeline transforms raw, unstructured content into searchable, structured data by applying cognitive skills during indexing.

```mermaid
flowchart LR
    DS[(Data Source<br/>Blob / SQL / Cosmos)] -->|connect| Indexer[Indexer<br/>Scheduling & Tracking]
    Indexer -->|document cracking| Skillset

    subgraph Skillset[Skillset]
        direction TB
        BI[Built-in Skills<br/>OCR · Entity Recognition<br/>Key Phrases · Translation<br/>Sentiment · PII Detection]
        Custom[Custom Skills<br/>Azure Function<br/>Web API]
        BI --> Merge[Merge / Shaper<br/>Skills]
        Custom --> Merge
    end

    Skillset -->|enriched documents| Index[(Search Index<br/>Fields & Scoring Profiles)]
    Skillset -->|projections| KS[(Knowledge Store<br/>Tables · Objects · Files)]

    style DS fill:#0078D4,color:#fff
    style Indexer fill:#E97132,color:#fff
    style Index fill:#50E6FF,color:#000
    style KS fill:#50E6FF,color:#000
```

### How It Works

1. A **data source** connection points the indexer to raw content (Blob, SQL, Cosmos DB, etc.).
2. The **indexer** cracks documents (extracts text/images), tracks change detection, and orchestrates the pipeline.
3. The **skillset** applies a chain of AI transformations (built-in or custom) to each document.
4. Enriched output is mapped to **index fields** via `outputFieldMappings`.
5. Optionally, enriched data is projected into a **knowledge store** for downstream analytics.

### Built-in vs Custom Skills

| Built-in Skills | Custom Skills |
|---|---|
| OCR, Image Analysis, Entity Recognition, Key Phrase Extraction, Language Detection, Translation, Sentiment, PII Detection, Text Split | Any logic hosted as an **Azure Function** or **Web API** conforming to the custom skill interface |
| No additional deployment needed | Requires implementing the `WebApiSkill` JSON contract (records in → records out) |
| Billed per AI Services transaction | Billed per Function execution + AI Services if used internally |

### Knowledge Store Projections

| Projection Type | Storage Target | Use Case |
|---|---|---|
| **Table** | Azure Table Storage | Structured analytics, Power BI |
| **Object** | Azure Blob Storage (JSON) | Full enrichment tree for downstream apps |
| **File** | Azure Blob Storage (binary) | Normalized images extracted via OCR |

### Key Exam Points

- A skillset must be attached to an **AI Services multi-service resource** (not a free tier) for production workloads.
- Custom skills use the `WebApiSkill` type; the function must accept and return the standard `{ "values": [...] }` JSON format.
- The **Shaper skill** creates complex types for knowledge store projections.
- `fieldMappings` map source fields → index; `outputFieldMappings` map enrichment output → index.
- Incremental enrichment caches skill output to avoid reprocessing unchanged documents.
- **Debug sessions** in the portal allow step-through inspection of the enrichment pipeline.

### Exam Objectives

- *Implement knowledge mining and document intelligence solutions* — skillsets, indexers, knowledge store
- *Implement Azure AI Search solutions* — index schema, field mappings, custom skills

### Relevant Labs

- Lab: Create an Azure AI Search solution
- Lab: Create a custom skill for Azure AI Search
- Lab: Create a knowledge store with Azure AI Search

---

## 3. Document Processing Pipeline

Azure AI Document Intelligence extracts structured data from documents at scale, feeding downstream search and application layers.

```mermaid
flowchart LR
    Docs([Documents<br/>PDF · Invoice · Receipt<br/>ID · Form]) -->|upload| Blob[(Azure Blob Storage)]
    Blob -->|SAS URI or<br/>managed identity| DI[Azure AI<br/>Document Intelligence]

    subgraph DI[Document Intelligence]
        direction TB
        Pre[Prebuilt Models<br/>Invoice · Receipt · ID<br/>W-2 · Health Insurance<br/>Layout · Read]
        Cust[Custom Models<br/>Template · Neural<br/>Composed]
        Pre ~~~ Cust
    end

    DI -->|structured JSON<br/>key-value pairs<br/>tables · fields| Search[(Azure AI Search<br/>Index)]
    DI -->|direct API| App[Application]
    Search --> App

    style Docs fill:#FFB900,color:#000
    style Blob fill:#0078D4,color:#fff
    style Search fill:#E97132,color:#fff
```

### Prebuilt vs Custom Model Decision

| Factor | Prebuilt | Custom (Template) | Custom (Neural) |
|---|---|---|---|
| **When to use** | Standard document types (invoices, receipts, IDs) | Fixed-layout forms unique to your org | Variable-layout forms |
| **Training data** | None required | ≥ 5 labeled samples | ≥ 5 labeled samples |
| **Layout sensitivity** | N/A | Exact layout match needed | Handles layout variation |
| **Composed model** | N/A | ✅ Combine up to 200 models | ✅ Can be composed |

### Composed Models

- A **composed model** routes incoming documents to the appropriate sub-model automatically.
- Use `docType` confidence to determine which sub-model matched.
- Maximum of **200** component models per composed model.

### Key Exam Points

- **Read model** → plain text + handwriting; **Layout model** → text + tables + structure; **Prebuilt** → specific document types with named fields.
- Custom template models require documents with **consistent layout** (same form version).
- Custom neural models handle **varying layouts** and are more flexible but take longer to train.
- Document Intelligence Studio provides labeling UI for training custom models.
- API versions: use `2024-11-30` (GA) or later for latest features.
- Results include `confidence` scores — exam may test threshold decisions.

### Exam Objectives

- *Implement knowledge mining and document intelligence solutions* — model selection, training, composed models
- *Implement Azure AI Search solutions* — using Document Intelligence as a data source or custom skill

### Relevant Labs

- Lab: Extract data from forms with Azure AI Document Intelligence
- Lab: Create a composed Document Intelligence model

---

## 4. Computer Vision Pipeline

Azure AI Vision services analyze images and video for classification, detection, OCR, and rich media indexing.

```mermaid
flowchart TB
    Input([Images / Video]) --> Vision

    subgraph Vision[Azure AI Vision]
        direction TB
        Analyze[Image Analysis 4.0<br/>Captions · Tags · Objects<br/>People · Smart Crops]
        OCR2[OCR / Read API<br/>Printed & Handwritten Text]
        Spatial[Spatial Analysis<br/>People Counting · Zones]
    end

    Input --> CustomV

    subgraph CustomV[Custom Vision / Florence]
        direction TB
        Classify[Image Classification<br/>Multi-class · Multi-label]
        Detect[Object Detection<br/>Bounding Boxes]
    end

    Input --> Video[Azure Video Indexer<br/>Faces · Topics · Transcript<br/>Scenes · OCR · Labels]

    Vision --> App([Application])
    CustomV --> App
    Video --> App

    style Vision fill:#4B8BBE,color:#fff
    style CustomV fill:#E97132,color:#fff
    style Video fill:#50E6FF,color:#000
```

### Service Selection Guide

| Need | Service | Key Feature |
|---|---|---|
| General image analysis | **AI Vision — Image Analysis** | Captions, tags, objects, people, colors |
| Read text from images | **AI Vision — Read / OCR** | Async batch or sync single-page |
| Domain-specific classification | **Custom Vision** or **Florence fine-tuning** | Train with your own labeled images |
| Object detection with bounding boxes | **Custom Vision** or **Image Analysis** (custom model) | Locate specific objects |
| Video content understanding | **Azure Video Indexer** | Transcripts, faces, topics, scenes, brands |
| Spatial / in-store analytics | **AI Vision — Spatial Analysis** | Edge container, zone counting |

### Key Exam Points

- Image Analysis 4.0 uses **Florence** foundation model — supports both prebuilt and custom training via few-shot.
- **Read API** is the recommended OCR approach (replaces older Computer Vision OCR endpoints).
- Custom Vision supports **export to ONNX, TensorFlow, CoreML** for edge/offline scenarios.
- Custom Vision training: **Quick Training** (fast, fewer iterations) vs **Advanced Training** (specify budget in hours).
- Custom Vision has two project types: **Classification** (multi-class or multi-label) and **Object Detection**.
- Video Indexer supports **custom language models**, **custom brands models**, and **custom person models**.
- **Multi-modal embeddings** (vectorize images + text into the same space) enable image retrieval via text queries.

### Exam Objectives

- *Implement computer vision solutions* — Image Analysis, OCR, Custom Vision
- *Implement Azure AI Search solutions* — using vision skills in enrichment pipeline
- *Create solutions with Azure AI Video Indexer*

### Relevant Labs

- Lab: Analyze images with Azure AI Vision
- Lab: Read text with Azure AI Vision
- Lab: Classify images with Custom Vision
- Lab: Detect objects with Custom Vision
- Lab: Analyze video with Video Indexer

---

## 5. Speech Application Architecture

Azure AI Speech services enable real-time and batch speech processing, translation, and natural-sounding synthesis.

```mermaid
flowchart LR
    Audio([Audio Input<br/>Microphone / File]) -->|streaming /<br/>batch| STT[Speech-to-Text<br/>Real-time · Batch]
    STT -->|transcript +<br/>intent| LU[Language<br/>Understanding<br/>CLU / LUIS]
    LU -->|intent +<br/>entities| BL[Business Logic]
    BL -->|response text| TTS[Text-to-Speech<br/>Neural Voices · SSML]
    TTS -->|synthesized audio| Output([Audio Output<br/>Speaker / File])

    Audio -->|translation mode| Trans[Speech Translation<br/>Real-time]
    Trans -->|translated text<br/>or audio| Output

    STT -.->|Custom Speech| CSM[Custom Model<br/>Acoustic + Language<br/>Adaptation]

    style STT fill:#4B8BBE,color:#fff
    style TTS fill:#E97132,color:#fff
    style Trans fill:#50E6FF,color:#000
    style LU fill:#FFB900,color:#000
```

### Key Components

| Component | Purpose |
|---|---|
| **Speech-to-Text** | Convert audio to text; supports real-time streaming and batch transcription |
| **Text-to-Speech** | Generate speech from text; neural voices with SSML for prosody control |
| **Speech Translation** | Real-time speech-to-speech or speech-to-text translation |
| **Custom Speech** | Adapt acoustic/language models with your own data for domain-specific recognition |
| **Custom Neural Voice** | Create a branded voice with ≤ 1 hour of training audio (requires approval) |
| **Intent Recognition** | Direct integration of Speech SDK with CLU for single-step speech-to-intent |

### SSML (Speech Synthesis Markup Language)

```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
       xmlns:mstts="http://www.w3.org/2001/mstts" xml:lang="en-US">
  <voice name="en-US-JennyNeural">
    <mstts:express-as style="cheerful" styledegree="1.5">
      Welcome to the demo!
    </mstts:express-as>
    <break time="500ms"/>
    <prosody rate="-10%" pitch="+5%">
      Let me show you the features.
    </prosody>
  </voice>
</speak>
```

### Key Exam Points

- **SpeechConfig** + **AudioConfig** are the two required objects for any Speech SDK operation.
- `SpeechRecognizer.recognized` event fires after final recognition; `recognizing` fires for interim results.
- Batch transcription uses a REST API (not the SDK) and requires audio in Blob Storage.
- Speech Translation `TranslationRecognizer` can output to multiple target languages simultaneously.
- Custom Speech models improve accuracy for domain-specific vocabulary, accents, and noisy environments.
- SSML controls: `<voice>`, `<prosody>` (rate, pitch, volume), `<break>`, `<mstts:express-as>` (style), `<say-as>` (interpret-as).
- **Pronunciation Assessment** evaluates accuracy, fluency, completeness, and prosody.

### Exam Objectives

- *Implement natural language processing solutions* — speech recognition, synthesis, translation
- *Create solutions with Azure OpenAI* — integrating speech with GPT for voice assistants

### Relevant Labs

- Lab: Recognize and synthesize speech
- Lab: Translate speech
- Lab: Create a custom speech model (if available in course)

---

## 6. Conversational AI Architecture

Azure Bot Framework combined with Conversational Language Understanding (CLU) and custom question answering enables intelligent, multi-turn conversational experiences.

```mermaid
flowchart TB
    User([User]) -->|message| Channel[Channels<br/>Web Chat · Teams<br/>Direct Line · Slack]
    Channel -->|Activity| Bot[Azure Bot Service<br/>Bot Framework SDK]

    Bot -->|utterance| CLU[CLU<br/>Intents + Entities]
    CLU -->|intent: GetWeather<br/>entity: city=Seattle| Bot

    Bot -->|question| QA[Custom Question<br/>Answering<br/>Knowledge Base]
    QA -->|answer +<br/>follow-up prompts| Bot

    Bot -->|multi-turn context| Dialog[Dialog Manager<br/>Waterfall · Adaptive]
    Dialog -->|gather slots| Bot

    Bot -->|response| Channel
    Channel -->|reply| User

    Bot -.->|complex queries| AOAI[Azure OpenAI<br/>Orchestration]

    style Bot fill:#4B8BBE,color:#fff
    style CLU fill:#E97132,color:#fff
    style QA fill:#50E6FF,color:#000
    style AOAI fill:#FFB900,color:#000
```

### Multi-Turn Conversation Flow

```mermaid
sequenceDiagram
    participant U as User
    participant B as Bot
    participant C as CLU
    participant Q as QA

    U->>B: "I need help with billing"
    B->>C: Recognize intent
    C->>B: Intent: Billing (0.92)
    B->>U: "What billing topic? (view balance, payment, dispute)"
    U->>B: "View my balance"
    B->>Q: Follow-up prompt matched
    Q->>B: Answer + context
    B->>U: "Your balance is $42.50. Need anything else?"
    U->>B: "No thanks"
    B->>U: "Goodbye!"
```

### Key Components

| Component | Purpose |
|---|---|
| **CLU (Conversational Language Understanding)** | Intent classification and entity extraction — replaces LUIS |
| **Custom Question Answering** | FAQ-style Q&A from documents, URLs, or manual entries — replaces QnA Maker |
| **Bot Framework SDK** | Conversation management, dialog flows, state management |
| **Azure Bot Service** | Hosting, channel registration, authentication |
| **Adaptive Dialogs** | Declarative, event-driven dialog management |

### Key Exam Points

- **CLU** is the successor to LUIS; both may appear on the exam but CLU is the current recommendation.
- CLU is authored in **Language Studio** and deployed to a **Language resource** prediction endpoint.
- Custom Question Answering uses **precise answering** (short answer extraction) and **follow-up prompts** for multi-turn.
- Confidence threshold: default is 0.5; adjust to control answer precision vs recall.
- **Orchestration workflow** in CLU can route between CLU projects and QA projects in a single call.
- Bot state: **UserState** (persists across conversations), **ConversationState** (single conversation), **PrivateConversationState** (per user per conversation).
- `Activity.type` — "message", "conversationUpdate", "event", etc. The `OnMembersAdded` handler sends welcome messages.
- Active learning in QA suggests alternate questions based on user traffic.

### Exam Objectives

- *Implement natural language processing solutions* — CLU, question answering, orchestration
- *Create conversational AI solutions* — Bot Framework, dialogs, state management

### Relevant Labs

- Lab: Create a question answering solution
- Lab: Create a conversational language understanding model
- Lab: Create a bot with the Bot Framework SDK
- Lab: Create a Bot Framework Composer bot (if included)

---

## 7. AI Foundry (Microsoft Foundry) Project Architecture

Azure AI Foundry (formerly Azure AI Studio) provides a unified platform for building, evaluating, and deploying generative AI solutions.

```mermaid
flowchart TB
    subgraph Hub[AI Foundry Hub]
        direction TB
        SharedRes[Shared Resources<br/>Networking · Policies<br/>Connections · Compute]
    end

    Hub --> ProjA[Project A]
    Hub --> ProjB[Project B]

    subgraph ProjA[Project A]
        direction TB
        Models[Model Deployments<br/>GPT-4o · GPT-4 · Phi<br/>Managed / Serverless]
        PF[Prompt Flow<br/>Authoring · Testing<br/>Chains · Tools]
        Eval[Evaluation<br/>Groundedness · Relevance<br/>Coherence · Fluency]
    end

    ProjA -->|deploy endpoint| App([Application<br/>via SDK / REST])

    subgraph Support[Supporting Resources]
        direction LR
        Storage[(Azure Storage)]
        KV[Key Vault]
        AppIns[Application Insights]
        CR[Container Registry]
    end

    Hub --- Support

    style Hub fill:#0078D4,color:#fff
    style ProjA fill:#4B8BBE,color:#fff
    style Support fill:#E6E6E6,color:#000
```

### Hub vs Project

| Concept | Scope | Purpose |
|---|---|---|
| **Hub** | Organization-level | Shared connections, networking, policies, compute pools |
| **Project** | Team / app-level | Model deployments, prompt flows, evaluations, data, experiments |

### Prompt Flow

- Visual DAG editor for building LLM chains (prompt → LLM → output).
- Node types: **LLM**, **Python**, **Prompt**, **Tool** (search, DALL-E, etc.).
- Supports **batch runs** for evaluation over test datasets.
- Deploy as a **managed online endpoint** for production serving.

### Key Exam Points

- Each **hub** has exactly one associated Azure AI Services multi-service resource.
- Projects inherit hub connections but can add project-specific connections.
- **Model catalog** offers Azure OpenAI models, open-source models (Llama, Mistral), and model-as-a-service (MaaS) via serverless API.
- **Managed compute** deployments bill by token usage; **serverless API** deployments bill per transaction.
- Evaluation metrics: **groundedness**, **relevance**, **coherence**, **fluency**, **similarity**, **F1**.
- Content safety evaluations run automatically during model evaluation.
- Prompt flow supports **connection** objects for API keys / endpoints — secrets stored in Key Vault.
- **Tracing** with Application Insights provides end-to-end observability of prompt flow runs.

### Exam Objectives

- *Plan and manage an Azure AI solution* — hub/project structure, resource management
- *Create solutions with Azure OpenAI* — model deployment, evaluation, prompt engineering
- *Implement generative AI solutions* — prompt flow, RAG orchestration

### Relevant Labs

- Lab: Explore Azure AI Foundry
- Lab: Create a prompt flow in Azure AI Foundry
- Lab: Evaluate generative AI models

---

## 8. Agentic AI Architecture

Agentic AI uses autonomous agents that can plan, use tools, and complete multi-step tasks — powered by the Azure OpenAI Assistants API or Semantic Kernel.

```mermaid
flowchart TB
    User([User]) -->|task / question| Agent

    subgraph Agent[AI Agent]
        direction TB
        Plan[Planner<br/>Decompose task<br/>into steps]
        Plan --> Execute
        Execute[Executor<br/>Call tools in sequence<br/>Evaluate results]
        Execute --> Plan
    end

    Agent -->|function_call| Tools

    subgraph Tools[Agent Tools]
        direction TB
        Code[Code Interpreter<br/>Run Python<br/>Generate charts]
        FileSearch[File Search<br/>Vector store over<br/>uploaded files]
        Func[Function Calling<br/>Custom API calls<br/>Database queries]
    end

    Agent <-->|completions API| AOAI[Azure OpenAI<br/>GPT-4o]
    Func -->|HTTP| ExtAPI[External APIs<br/>& Services]

    style Agent fill:#4B8BBE,color:#fff
    style Tools fill:#E97132,color:#fff
    style AOAI fill:#FFB900,color:#000
```

### Multi-Agent Orchestration

```mermaid
flowchart LR
    User([User]) --> Orchestrator[Orchestrator Agent<br/>Routes & coordinates]
    Orchestrator --> Research[Research Agent<br/>File Search + Web]
    Orchestrator --> Analysis[Analysis Agent<br/>Code Interpreter]
    Orchestrator --> Writer[Writer Agent<br/>Report Generation]
    Research -->|findings| Orchestrator
    Analysis -->|charts + data| Orchestrator
    Writer -->|final report| Orchestrator
    Orchestrator -->|combined result| User

    style Orchestrator fill:#0078D4,color:#fff
    style Research fill:#4B8BBE,color:#fff
    style Analysis fill:#E97132,color:#fff
    style Writer fill:#50E6FF,color:#000
```

### Key Components

| Component | Purpose |
|---|---|
| **Assistants API** | Manages threads, runs, and tool execution for stateful agents |
| **Code Interpreter** | Sandboxed Python execution for math, data analysis, chart generation |
| **File Search** | Built-in RAG over uploaded files (auto-chunks, embeds, and retrieves) |
| **Function Calling** | Agent invokes developer-defined functions; app executes and returns results |
| **Threads** | Persistent conversation state with automatic context window management |

### Key Exam Points

- **Assistants API** objects: `Assistant` → `Thread` → `Message` → `Run` → `RunStep`.
- A **Run** can have status: `queued`, `in_progress`, `requires_action` (function call), `completed`, `failed`.
- When status is `requires_action`, the app must execute the function and submit tool outputs via `submit_tool_outputs`.
- **Code Interpreter** supports file uploads (CSV, XLSX, images) and produces downloadable output files.
- **File Search** uses a vector store; supports up to 10,000 files per vector store.
- Function calling uses a JSON Schema definition for parameters — the model decides when to call which function.
- **Parallel function calling**: model can request multiple function calls in a single turn.
- Agents vs Completions: Agents maintain state server-side; Completions are stateless.

### Exam Objectives

- *Create solutions with Azure OpenAI* — Assistants API, function calling, tool use
- *Implement generative AI solutions* — agentic patterns, orchestration

### Relevant Labs

- Lab: Implement function calling with Azure OpenAI
- Lab: Use the Assistants API with Azure OpenAI (if available)

---

## 9. End-to-End Secure AI Solution

A Zero Trust architecture for AI services ensures data never traverses the public internet and all access is identity-authenticated.

```mermaid
flowchart TB
    subgraph VNet[Azure Virtual Network]
        direction TB
        subgraph AppSubnet[App Subnet]
            AppSvc[App Service<br/>VNet Integration]
        end

        subgraph PESubnet[Private Endpoint Subnet]
            PE_AI[Private Endpoint<br/>AI Services]
            PE_Search[Private Endpoint<br/>AI Search]
            PE_Storage[Private Endpoint<br/>Storage Account]
            PE_KV[Private Endpoint<br/>Key Vault]
            PE_AOAI[Private Endpoint<br/>Azure OpenAI]
        end

        AppSvc -->|private IP| PE_AI
        AppSvc -->|private IP| PE_Search
        AppSvc -->|private IP| PE_Storage
        AppSvc -->|private IP| PE_KV
        AppSvc -->|private IP| PE_AOAI
    end

    MI[Managed Identity<br/>System-assigned] -.->|RBAC| PE_AI
    MI -.->|RBAC| PE_Search
    MI -.->|RBAC| PE_Storage
    MI -.->|RBAC| PE_KV
    MI -.->|RBAC| PE_AOAI
    AppSvc --- MI

    DNS[Azure Private<br/>DNS Zones] -.->|name resolution| PESubnet

    style VNet fill:#E6E6E6,color:#000
    style AppSubnet fill:#C8E6C9,color:#000
    style PESubnet fill:#FFECB3,color:#000
    style MI fill:#4B8BBE,color:#fff
```

### Zero Trust Pattern for AI Services

| Layer | Implementation |
|---|---|
| **Network** | Private endpoints; disable public network access on all AI resources |
| **Identity** | Managed identity (system-assigned) — no API keys in code |
| **Data** | Customer-managed keys (CMK) for encryption at rest; TLS 1.2+ in transit |
| **Access Control** | Azure RBAC: `Cognitive Services User`, `Search Index Data Reader`, etc. |
| **Monitoring** | Diagnostic settings → Log Analytics; Azure Monitor alerts |
| **Secrets** | Key Vault for any required secrets; never store in app config |

### Key RBAC Roles for AI

| Role | Purpose |
|---|---|
| `Cognitive Services OpenAI User` | Call Azure OpenAI completions/embeddings APIs |
| `Cognitive Services User` | Call AI Services APIs (Vision, Language, etc.) |
| `Search Index Data Contributor` | Read/write search index data |
| `Storage Blob Data Reader` | Read blobs (for indexer data source) |
| `Key Vault Secrets User` | Read secrets from Key Vault |

### Key Exam Points

- **Managed identity** is the recommended authentication — use `DefaultAzureCredential` in code.
- `DefaultAzureCredential` tries (in order): environment → managed identity → Visual Studio → Azure CLI → Interactive.
- Private endpoints create a **network interface** in your VNet with a private IP for the AI service.
- Each private endpoint requires a **Private DNS Zone** for correct name resolution (e.g., `privatelink.cognitiveservices.azure.com`).
- Disable public network access: set `publicNetworkAccess: Disabled` on AI resources.
- **Customer-managed keys** require Key Vault with soft-delete and purge protection enabled.
- **Virtual network rules** and **IP firewall rules** can be used instead of (or with) private endpoints.
- **Diagnostic settings** should send to Log Analytics for auditing API calls.

### Exam Objectives

- *Plan and manage an Azure AI solution* — networking, authentication, key management
- *Implement security for Azure AI solutions* — managed identity, RBAC, private endpoints, CMK

### Relevant Labs

- Lab: Manage Azure AI Services security
- Lab: Configure private endpoints for Azure AI Services (if available)

---

## 10. Content Safety Pipeline

Azure AI Content Safety provides layered filtering for both inputs and outputs of generative AI applications.

```mermaid
flowchart LR
    User([User Input]) --> PS[Prompt Shields<br/>Jailbreak Detection<br/>Indirect Attacks]
    PS -->|safe| CF_In[Input Content Filters<br/>Hate · Sexual · Violence<br/>Self-harm]
    PS -->|blocked| Blocked1([Blocked Response])
    CF_In -->|passes threshold| BL[Blocklists<br/>Custom Terms<br/>Regex Patterns]
    CF_In -->|exceeds threshold| Blocked1
    BL -->|clean| AOAI[Azure OpenAI<br/>Model Processing]
    BL -->|match| Blocked1
    AOAI -->|generated text| CF_Out[Output Content Filters<br/>Hate · Sexual · Violence<br/>Self-harm]
    CF_Out -->|passes| GD[Groundedness<br/>Detection]
    CF_Out -->|exceeds threshold| Blocked2([Blocked Response])
    GD -->|grounded| Response([Safe Response<br/>to User])
    GD -->|ungrounded| Blocked2

    style PS fill:#E97132,color:#fff
    style CF_In fill:#4B8BBE,color:#fff
    style CF_Out fill:#4B8BBE,color:#fff
    style BL fill:#FFB900,color:#000
    style AOAI fill:#50E6FF,color:#000
    style GD fill:#C8E6C9,color:#000
```

### Filter Severity Levels

| Category | Severity Levels | Action Options |
|---|---|---|
| **Hate** | Safe (0) · Low (2) · Medium (4) · High (6) | Allow, Filter, or Annotate at each level |
| **Sexual** | Safe (0) · Low (2) · Medium (4) · High (6) | Allow, Filter, or Annotate at each level |
| **Violence** | Safe (0) · Low (2) · Medium (4) · High (6) | Allow, Filter, or Annotate at each level |
| **Self-harm** | Safe (0) · Low (2) · Medium (4) · High (6) | Allow, Filter, or Annotate at each level |

### Content Safety Features

| Feature | Purpose |
|---|---|
| **Content Filters** | Severity-based filtering for 4 harm categories on both input and output |
| **Prompt Shields** | Detect jailbreak attempts and indirect prompt injection from documents |
| **Blocklists** | Custom term lists and regex patterns for domain-specific blocking |
| **Protected Material Detection** | Detect known copyrighted text in model output |
| **Groundedness Detection** | Verify model output is grounded in provided source documents |

### Key Exam Points

- Content filters are configured per **deployment** in Azure OpenAI — each deployment can have different filter settings.
- Default filter configuration blocks content at **Medium** severity and above.
- **Prompt Shields** are separate from content filters; they detect adversarial prompt manipulation.
- **Blocklists** support both exact match and regex patterns; up to 10,000 terms per list.
- The Content Safety API can be called **standalone** (not just through Azure OpenAI) for pre/post-processing.
- `annotations` in the API response show which filter triggered and at what severity.
- When a filter blocks content, the API returns a `finish_reason: "content_filter"` with a `content_filter_results` object.
- **Groundedness detection** compares model output against source documents to detect hallucinations.
- Configure filters via Azure OpenAI Studio → Deployments → Content Filters, or via REST API.

### Exam Objectives

- *Create solutions with Azure OpenAI* — content filter configuration, responsible AI
- *Implement responsible AI practices* — harm mitigation, content safety configuration

### Relevant Labs

- Lab: Configure content filters in Azure OpenAI
- Lab: Explore Azure AI Content Safety (if available)

---

## Quick Reference: Architecture Selection

| Scenario | Primary Architecture | Key Services |
|---|---|---|
| Chat with enterprise docs | RAG (#1) | Azure OpenAI + AI Search + Blob |
| Extract data from scanned forms | Document Processing (#3) | Document Intelligence |
| Enrich & search unstructured content | Enrichment Pipeline (#2) | AI Search + Skillset |
| Classify product images | Computer Vision (#4) | Custom Vision / AI Vision |
| Voice-enabled assistant | Speech (#5) + Conversational AI (#6) | Speech SDK + Bot Framework + CLU |
| FAQ chatbot | Conversational AI (#6) | Custom Question Answering + Bot |
| Multi-step task automation | Agentic AI (#8) | Assistants API + Function Calling |
| Secure production deployment | Secure AI (#9) | VNet + Private Endpoints + MI |
| Content moderation for GenAI | Content Safety (#10) | Content Filters + Prompt Shields |
| End-to-end GenAI project | AI Foundry (#7) | Hub + Project + Prompt Flow |

---

*Last updated: July 2025 — aligned with AI-102 exam objectives and Azure AI services GA features.*
