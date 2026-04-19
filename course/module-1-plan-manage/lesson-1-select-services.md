# Lesson 1: Select the Appropriate Azure AI Service

## Learning Objectives

- Identify the full landscape of Azure AI services
- Determine when to use multi-service vs. single-service resources
- Apply decision trees to select the right service for a given scenario
- Differentiate between generative AI, vision, NLP, speech, search, and document extraction services

---

## Azure AI Service Landscape

Azure AI services are organized into several categories. Understanding which service solves which problem is **critical** for the exam.

### Service Categories Overview

| Category | Services | Key Use Cases |
|----------|----------|---------------|
| **Generative AI** | Azure OpenAI Service, Microsoft Foundry | Text generation, chat, code generation, image generation, embeddings |
| **Vision** | Computer Vision, Custom Vision, Face API, Video Indexer | Image analysis, OCR, object detection, facial recognition, video analysis |
| **Language** | Language Service, Translator, Immersive Reader | Sentiment analysis, NER, key phrase extraction, translation, summarization |
| **Speech** | Speech Service | Speech-to-text, text-to-speech, speech translation, speaker recognition |
| **Search** | Azure AI Search | Full-text search, vector search, semantic ranking, hybrid search, RAG |
| **Document** | Document Intelligence (formerly Form Recognizer) | Form extraction, receipt/invoice processing, ID document reading, custom models |
| **Decision** | Content Safety, Personalizer (deprecated) | Content moderation, personalized experiences |

---

## Multi-Service vs. Single-Service Resources

### Multi-Service Resource (Azure AI Services)

A single resource that provides access to **multiple** Azure AI services under one endpoint and key.

```
Resource type: Microsoft.CognitiveServices/accounts
Kind: CognitiveServices
```

**When to use:**
- You need multiple AI capabilities (e.g., Vision + Language)
- You want simplified billing and key management
- You're building a solution that combines services

**What's included:** Vision, Language, Speech, Translator, Document Intelligence, Content Safety

**What's NOT included:** Azure OpenAI (separate resource), Azure AI Search (separate resource)

### Single-Service Resource

A dedicated resource for one specific AI service.

```
Resource type: Microsoft.CognitiveServices/accounts
Kind: TextAnalytics (or ComputerVision, Face, SpeechServices, etc.)
```

**When to use:**
- You need isolated billing per service
- Different security/access requirements per service
- Compliance requires resource-level isolation
- Using Azure OpenAI or AI Search (always single-service)

> ### 📝 Exam Tip
> The exam frequently tests whether you know which services are available in a multi-service resource vs. which require their own resource. **Azure OpenAI** and **Azure AI Search** always require dedicated resources.

---

## Decision Tree: Selecting the Right Service

### Step 1: What type of data are you working with?

```
Input Data
├── Text
│   ├── Generate/transform text → Azure OpenAI Service
│   ├── Analyze text (sentiment, entities, key phrases) → Language Service
│   ├── Translate text → Translator Service
│   └── Summarize text → Language Service or Azure OpenAI
├── Images
│   ├── General image analysis → Computer Vision
│   ├── Custom object detection → Custom Vision
│   ├── Face detection/identification → Face API
│   ├── Generate images → Azure OpenAI (DALL-E)
│   └── Read text from images (OCR) → Computer Vision or Document Intelligence
├── Documents (structured/semi-structured)
│   ├── Invoices, receipts, IDs → Document Intelligence (prebuilt models)
│   ├── Custom forms → Document Intelligence (custom models)
│   └── General document analysis → Document Intelligence (layout model)
├── Audio/Speech
│   ├── Transcribe speech → Speech Service (STT)
│   ├── Generate speech → Speech Service (TTS)
│   ├── Translate speech → Speech Service (translation)
│   └── Identify speakers → Speech Service (speaker recognition)
├── Video
│   └── Analyze video content → Video Indexer
└── Search scenarios
    ├── Full-text search over documents → Azure AI Search
    ├── Vector/semantic search → Azure AI Search
    └── RAG (Retrieval-Augmented Generation) → Azure AI Search + Azure OpenAI
```

### Step 2: Do you need a prebuilt or custom model?

| Requirement | Service | Model Type |
|-------------|---------|------------|
| General image classification | Computer Vision | Prebuilt |
| Domain-specific image classification | Custom Vision | Custom trained |
| Standard form extraction (invoices, receipts) | Document Intelligence | Prebuilt |
| Custom form extraction | Document Intelligence | Custom trained |
| General text analysis | Language Service | Prebuilt |
| Custom text classification or NER | Language Service | Custom trained |
| General chat/completion | Azure OpenAI | Prebuilt (GPT-4o) |
| Domain-specific chat | Azure OpenAI | Fine-tuned |

---

## Service Comparison Tables

### Text Analysis: Language Service vs. Azure OpenAI

| Feature | Language Service | Azure OpenAI |
|---------|-----------------|--------------|
| Sentiment analysis | ✅ Built-in | ✅ Via prompt |
| Named Entity Recognition | ✅ Built-in | ✅ Via prompt |
| Key phrase extraction | ✅ Built-in | ✅ Via prompt |
| Text summarization | ✅ Extractive & abstractive | ✅ Abstractive |
| Custom classification | ✅ Train custom models | ✅ Few-shot or fine-tune |
| Text generation | ❌ | ✅ Core capability |
| Structured output | ❌ | ✅ JSON mode |
| Cost model | Per transaction | Per token |
| Latency | Low | Variable |
| **Best for** | Specific NLP tasks at scale | Flexible, generative scenarios |

### Document Processing: Computer Vision OCR vs. Document Intelligence

| Feature | Computer Vision (OCR) | Document Intelligence |
|---------|----------------------|----------------------|
| General text extraction | ✅ | ✅ |
| Handwritten text | ✅ | ✅ |
| Structured form extraction | ❌ | ✅ Prebuilt & custom |
| Table extraction | Basic | ✅ Advanced |
| Invoice/receipt processing | ❌ | ✅ Prebuilt models |
| ID document reading | ❌ | ✅ Prebuilt model |
| Custom model training | ❌ | ✅ |
| **Best for** | Simple OCR tasks | Structured document processing |

### Search: Azure AI Search vs. Database Full-Text

| Feature | Azure AI Search | Database Full-Text Search |
|---------|----------------|--------------------------|
| Vector search | ✅ | Limited |
| Semantic ranking | ✅ | ❌ |
| AI enrichment pipeline | ✅ (skillsets) | ❌ |
| Hybrid search (keyword + vector) | ✅ | ❌ |
| RAG integration | ✅ Native | Manual |
| Faceted navigation | ✅ | ❌ |
| **Best for** | AI-powered search & RAG | Simple keyword search |

> ### 📝 Exam Tip
> Know the difference between **extractive summarization** (Language Service — selects key sentences) and **abstractive summarization** (Language Service or Azure OpenAI — generates new summary text). The exam tests this distinction.

---

## Common Exam Scenarios

### Scenario 1: "Extract data from thousands of invoices"
**Answer:** Document Intelligence with the prebuilt invoice model. Not Computer Vision OCR (lacks structure), not Azure OpenAI (not optimized for high-volume structured extraction).

### Scenario 2: "Build a chatbot that answers questions from company documents"
**Answer:** Azure AI Search (index documents) + Azure OpenAI (generate answers) = RAG pattern. Not Language Service QnA alone (limited to FAQ-style).

### Scenario 3: "Detect if uploaded images contain inappropriate content"
**Answer:** Content Safety service (image moderation). Not Computer Vision (analyzes content, doesn't moderate). Not Custom Vision (not designed for moderation).

### Scenario 4: "Transcribe customer service calls and analyze sentiment"
**Answer:** Speech Service (speech-to-text) → Language Service (sentiment analysis). Two services, can use multi-service resource.

### Scenario 5: "Classify support tickets into categories specific to your business"
**Answer:** Language Service with custom text classification. Not Azure OpenAI (possible but Language Service is purpose-built for classification). Consider Azure OpenAI if categories change frequently (few-shot prompting).

---

## Code Example: Listing Available Services

### Python SDK — Check available features of a multi-service resource

```python
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Multi-service resource endpoint serves multiple APIs
endpoint = "https://<your-resource>.cognitiveservices.azure.com/"
key = "<your-key>"

# Same endpoint, different client for each service
text_client = TextAnalyticsClient(endpoint, AzureKeyCredential(key))
```

### REST — Discover endpoint capabilities

```http
GET https://<your-resource>.cognitiveservices.azure.com/
     text/analytics/v3.1/languages
Content-Type: application/json
Ocp-Apim-Subscription-Key: <your-key>
```

---

## Key Takeaways

1. **Multi-service resources** bundle Vision, Language, Speech, Translator, Document Intelligence, and Content Safety under one endpoint — but **not** Azure OpenAI or Azure AI Search.
2. Use **decision trees** based on input data type (text, image, document, audio, video) to narrow down the right service.
3. **Document Intelligence** is for structured document extraction; **Computer Vision OCR** is for simple text reading from images.
4. The **RAG pattern** (Azure AI Search + Azure OpenAI) is the recommended approach for grounded Q&A over enterprise data.
5. **Language Service** is best for well-defined NLP tasks (sentiment, NER, classification); **Azure OpenAI** is best for flexible, generative scenarios.

---

## Further Reading

- [What are Azure AI services?](https://learn.microsoft.com/en-us/azure/ai-services/what-are-ai-services)
- [Azure AI services pricing](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/)
- [Multi-service resource overview](https://learn.microsoft.com/en-us/azure/ai-services/multi-service-resource)
- [Azure OpenAI service models](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models)
