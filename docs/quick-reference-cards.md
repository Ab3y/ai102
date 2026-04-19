# AI-102 Quick Reference Cards & Cheat Sheets

> Comprehensive comparison tables, decision trees, and rapid-lookup references for the Azure AI Engineer Associate exam.

---

## 1. Azure AI Services Decision Tree

| Scenario | Recommended Service | Why |
|----------|-------------------|-----|
| Extract sentiment, key phrases, or entities from text | **Azure AI Language** | Pre-built NLP models for common text analytics tasks |
| Translate text between languages in real time | **Azure AI Translator** | Supports 100+ languages, auto-detection, dictionary lookup |
| Convert speech to text or text to speech | **Azure AI Speech** | Real-time & batch transcription, neural TTS voices |
| Classify or detect objects in images | **Azure AI Vision** (Image Analysis) | Pre-built & custom models for tagging, captioning, detection |
| Read printed/handwritten text from images | **Azure AI Vision** (OCR / Read API) | High-accuracy OCR across 164 languages |
| Extract structured data from invoices, receipts, IDs | **Document Intelligence** | Pre-built models for common document types with field extraction |
| Build a searchable index over documents | **Azure AI Search** | Full-text, vector, semantic, and hybrid search with AI enrichment |
| Extract custom fields from domain-specific forms | **Document Intelligence** (Custom models) | Train on your own labeled documents |
| Generate text, code, or summarize content | **Azure OpenAI Service** | GPT-4o, GPT-4, GPT-3.5-Turbo for generative tasks |
| Build conversational Q&A over your data | **Azure OpenAI** + **AI Search** (RAG) | On Your Data feature grounds responses in your content |
| Detect harmful content in text or images | **Azure AI Content Safety** | Multi-category severity scoring for moderation |
| Build autonomous AI agents with tool use | **Azure AI Foundry** (Agents) | Orchestrate models with tools, code interpreter, file search |
| Identify speakers in a conversation | **Azure AI Speech** (Speaker Recognition) | Text-independent/dependent verification & identification |
| Analyze video for insights and transcription | **Azure Video Indexer** | Extracts faces, topics, sentiments, OCR, transcripts from video |
| Moderate or classify custom text categories | **Azure AI Language** (Custom text classification) | Train single-label or multi-label classifiers on your data |
| Understand conversational intent and entities | **Azure AI Language** (CLU) | Replaces LUIS — intent classification + entity extraction |

---

## 2. Service Comparison Matrix

| Service | Key Capabilities | SDK Package (.NET) | REST Endpoint Pattern | Pricing Tier Options |
|---------|-----------------|-------------------|----------------------|---------------------|
| **Azure AI Language** | Sentiment, NER, key phrases, PII detection, CLU, summarization, custom text classification, custom NER | `Azure.AI.TextAnalytics` | `https://<resource>.cognitiveservices.azure.com/language/` | Free (F0), Standard (S) |
| **Azure AI Vision** | Image Analysis 4.0, OCR/Read, Face detection, custom image classification/detection | `Azure.AI.Vision.ImageAnalysis` | `https://<resource>.cognitiveservices.azure.com/vision/` | Free (F0), Standard (S1) |
| **Azure AI Speech** | STT, TTS, translation, speaker recognition, pronunciation assessment, keyword recognition | `Microsoft.CognitiveServices.Speech` | `https://<region>.api.cognitive.microsoft.com/speechtotext/` | Free (F0), Standard (S0) |
| **Azure OpenAI** | GPT-4o, GPT-4, GPT-3.5-Turbo, DALL·E, Whisper, embeddings | `Azure.AI.OpenAI` | `https://<resource>.openai.azure.com/openai/deployments/<deployment>/` | Standard (S0), Provisioned (PTU) |
| **Azure AI Search** | Full-text search, vector search, semantic ranking, AI enrichment (skillsets), knowledge store | `Azure.Search.Documents` | `https://<service>.search.windows.net/indexes/<index>/` | Free, Basic, Standard (S1-S3), Storage Optimized (L1-L2) |
| **Document Intelligence** | Pre-built (invoice, receipt, ID, W-2, health insurance, etc.), custom, composed models, layout | `Azure.AI.FormRecognizer` | `https://<resource>.cognitiveservices.azure.com/formrecognizer/` | Free (F0), Standard (S0) |
| **Content Safety** | Text moderation, image moderation, prompt shields, groundedness detection, protected material detection | `Azure.AI.ContentSafety` | `https://<resource>.cognitiveservices.azure.com/contentsafety/` | Free (F0), Standard (S0) |
| **AI Foundry** | Model catalog, prompt flow, agents, evaluations, deployments, fine-tuning, tracing | `azure-ai-projects` (Python) | `https://<project>.services.ai.azure.com/` | Pay-per-use (varies by model) |

> **Multi-service resource**: A single `Cognitive Services` resource (`kind: CognitiveServices`) provides keys that work across Language, Vision, Speech, Translator, and more. Endpoint pattern: `https://<resource>.cognitiveservices.azure.com/`

---

## 3. File Size & Format Limits (EXAM-TESTED!)

### Document Intelligence

| Aspect | Free Tier (F0) | Standard Tier (S0) |
|--------|---------------|-------------------|
| Max file size | **4 MB** | **500 MB** |
| Max pages (per invocation) | 2 pages | 2,000 pages |
| Min image size | 50 × 50 pixels | 50 × 50 pixels |
| Supported formats | PDF, JPEG, PNG, BMP, TIFF, HEIF, DOCX, XLSX, PPTX | Same |
| Custom model training docs | 6 documents | Unlimited |
| Max custom models | 500 | 500 |
| Composed model limit | 5 sub-models | 200 sub-models |

### Custom Vision

| Aspect | Limit |
|--------|-------|
| Max image file size | **6 MB** |
| Min training images per tag | **15 images** |
| Max tags per project | 500 (Classification), 100 (Detection) |
| Max images per project | 100,000 |
| Supported formats | JPEG, PNG, BMP, GIF |
| Max image dimensions (training) | 10,240 × 10,240 pixels |
| Min image dimensions | 256 × 256 pixels (auto-resized if smaller) |

### Azure AI Vision (Image Analysis 4.0)

| Aspect | Limit |
|--------|-------|
| Max file size | **4 MB** |
| Max image dimensions | **20 megapixels** |
| Min image dimensions | 50 × 50 pixels |
| Supported formats | JPEG, PNG, GIF, BMP, WEBP, ICO, TIFF |
| Max images per request | 1 |

### Azure AI Speech

| Aspect | Real-Time STT | Batch Transcription |
|--------|--------------|-------------------|
| Max file size | **25 MB** (REST) | **1 GB** |
| Max audio duration | **60 seconds** (default REST), continuous via SDK | **24 hours** |
| Supported formats | WAV (PCM), OGG (Opus), FLAC, MP3, ALAW, MULAW | WAV, MP3, OGG, FLAC, WMA, AAC, ALAW, MULAW |
| Sample rates | 8 kHz or 16 kHz | 8 kHz to 48 kHz |
| Channels | Mono or Stereo | Mono or Stereo (per-channel transcription) |
| Streaming chunk size | Up to 1 MB per chunk | N/A (file-based) |

### Azure AI Search

| Aspect | Limit |
|--------|-------|
| Max document size (push API) | **16 MB** |
| Max characters per field | **32,766 characters** (UTF-8) |
| Max fields per index | 1,000 |
| Max indexes | Varies by tier (3 for Free, 50-200 for Standard) |
| Max document count (Free) | 10,000 |
| Max index size (Free) | 50 MB |
| Indexer blob size limit | 256 MB (Standard), 16 MB (Free) |
| Skillset execution timeout | 230 seconds per document |

### Video Indexer

| Aspect | Limit |
|--------|-------|
| Max file size | **2 GB** |
| Max video duration | **4 hours** |
| Supported formats | MP4, MOV, AVI, FLV, MKV, WMV, WebM, and more |
| Max videos per account | 25,000 (paid) |
| Max concurrent indexing jobs | 10 (paid) |

---

## 4. REST API Endpoint Patterns

### Azure AI Language

```http
POST https://<resource>.cognitiveservices.azure.com/language/:analyze-text?api-version=2024-11-15-preview
Content-Type: application/json
Ocp-Apim-Subscription-Key: <api-key>

{
  "kind": "SentimentAnalysis",
  "parameters": { "modelVersion": "latest" },
  "analysisInput": {
    "documents": [
      { "id": "1", "language": "en", "text": "The service was excellent." }
    ]
  }
}
```

### Azure AI Vision (Image Analysis 4.0)

```http
POST https://<resource>.cognitiveservices.azure.com/computervision/imageanalysis:analyze?api-version=2024-02-01&features=caption,tags,objects,read
Content-Type: application/json
Ocp-Apim-Subscription-Key: <api-key>

{
  "url": "https://example.com/image.jpg"
}
```

### Azure AI Speech (Speech-to-Text REST)

```http
POST https://<region>.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1?language=en-US
Content-Type: audio/wav
Ocp-Apim-Subscription-Key: <api-key>

<binary audio data>
```

### Azure OpenAI (Chat Completions)

```http
POST https://<resource>.openai.azure.com/openai/deployments/<deployment-name>/chat/completions?api-version=2024-10-21
Content-Type: application/json
api-key: <api-key>

{
  "messages": [
    { "role": "system", "content": "You are a helpful assistant." },
    { "role": "user", "content": "What is Azure AI?" }
  ],
  "temperature": 0.7,
  "max_tokens": 800
}
```

### Azure AI Search (Query)

```http
POST https://<service>.search.windows.net/indexes/<index>/docs/search?api-version=2024-07-01
Content-Type: application/json
api-key: <admin-or-query-key>

{
  "search": "cloud computing",
  "filter": "category eq 'Technology'",
  "select": "title,content,category",
  "top": 10,
  "queryType": "semantic",
  "semanticConfiguration": "my-semantic-config"
}
```

### Document Intelligence (Analyze Document)

```http
POST https://<resource>.cognitiveservices.azure.com/formrecognizer/documentModels/<model-id>:analyze?api-version=2024-11-30
Content-Type: application/json
Ocp-Apim-Subscription-Key: <api-key>

{
  "urlSource": "https://example.com/invoice.pdf"
}
# Returns Operation-Location header → poll for results with GET
```

### Content Safety (Text Analysis)

```http
POST https://<resource>.cognitiveservices.azure.com/contentsafety/text:analyze?api-version=2024-09-01
Content-Type: application/json
Ocp-Apim-Subscription-Key: <api-key>

{
  "text": "Text to analyze for safety.",
  "categories": ["Hate", "Violence", "Sexual", "SelfHarm"],
  "outputType": "FourSeverityLevels"
}
```

---

## 5. Authentication Methods Comparison

| Method | When to Use | Implementation |
|--------|------------|----------------|
| **API Key** | Development, testing, quick prototyping | Header: `Ocp-Apim-Subscription-Key: <key>` or `api-key: <key>` (for Search / OpenAI) |
| **Managed Identity** | Production apps on Azure (App Service, Functions, VMs, Container Apps) | Assign system/user-assigned identity → grant RBAC role → use `DefaultAzureCredential` in SDK |
| **Microsoft Entra ID Token** | Service-to-service auth, user-delegated access, CI/CD pipelines | Obtain token from `https://login.microsoftonline.com/<tenant>/oauth2/v2.0/token` with scope `https://cognitiveservices.azure.com/.default` → Header: `Authorization: Bearer <token>` |
| **Key Vault Integration** | Store/rotate keys securely, compliance requirements | Store API key as Key Vault secret → reference via `@Microsoft.KeyVault(SecretUri=...)` in App Settings or retrieve programmatically |
| **Multi-service Key** | Single key for multiple AI services from one resource | Create `CognitiveServices` (multi-service) resource → same key works for Language, Vision, Speech, etc. |

**RBAC Roles for Azure AI Services:**

| Role | Permissions |
|------|-------------|
| `Cognitive Services User` | Call prediction APIs (most common for apps) |
| `Cognitive Services Contributor` | Create/manage resources + call APIs |
| `Cognitive Services OpenAI User` | Call OpenAI completion & embedding APIs |
| `Cognitive Services OpenAI Contributor` | Manage deployments + call APIs |
| `Search Index Data Reader` | Query search indexes |
| `Search Index Data Contributor` | Read/write index data (push documents) |
| `Search Service Contributor` | Manage search service (create/delete indexes) |

---

## 6. Prebuilt vs Custom Model Decision Matrix

### Vision

| Aspect | Prebuilt (Image Analysis 4.0) | Custom (Custom Vision / Florence) |
|--------|------------------------------|----------------------------------|
| **When to use** | General tagging, captioning, object detection for common objects, OCR | Domain-specific classification/detection (e.g., product defects, medical imaging) |
| **Training required** | None | Minimum **15 images per tag** (50+ recommended) |
| **Setup time** | Minutes | Hours to days |
| **Evaluation metrics** | N/A | Precision, Recall, mAP (mean Average Precision) |
| **Export options** | N/A | ONNX, TensorFlow, CoreML, Docker container |

### Language

| Aspect | Prebuilt (NER, Sentiment, etc.) | Custom (CLU, Custom NER, Custom Classification) |
|--------|--------------------------------|------------------------------------------------|
| **When to use** | Standard entities (person, location, org), general sentiment | Domain-specific intents/entities, custom categories |
| **Training required** | None | Labeled utterances — at least **10 per intent**, **10 entity examples** minimum |
| **Setup time** | Minutes | Hours |
| **Evaluation metrics** | N/A | Precision, Recall, F1-score (per class and micro/macro average) |
| **Deployment** | Automatic | Deploy to prediction slot → assign deployment name |

### Document Intelligence

| Aspect | Prebuilt Models | Custom Models |
|--------|----------------|---------------|
| **When to use** | Standard documents: invoices, receipts, IDs, W-2, health insurance cards, business cards | Domain-specific or unique form layouts |
| **Available prebuilt models** | `prebuilt-invoice`, `prebuilt-receipt`, `prebuilt-idDocument`, `prebuilt-tax.us.w2`, `prebuilt-layout`, `prebuilt-read` | N/A |
| **Training required** | None | Minimum **5 labeled documents** (custom template); 1 document (custom neural) |
| **Composed models** | N/A | Combine up to **200** custom models into one composed model; routes to best match |
| **Evaluation metrics** | N/A | Accuracy, field-level confidence |
| **Model types** | Pre-defined fields per doc type | Template (fixed layout) or Neural (variable layout) |

---

## 7. Azure OpenAI Parameters Quick Reference

| Parameter | Range | Default | Effect |
|-----------|-------|---------|--------|
| `temperature` | 0.0 – 2.0 | 1.0 | Controls randomness. Lower = more deterministic, higher = more creative |
| `top_p` | 0.0 – 1.0 | 1.0 | Nucleus sampling. 0.1 = only top 10% probability mass. **Don't combine with temperature** |
| `max_tokens` | 1 – model max | Model-dependent | Maximum tokens in the completion. Does **not** include prompt tokens |
| `frequency_penalty` | -2.0 – 2.0 | 0 | Penalizes tokens proportional to frequency in text so far. Higher = less repetition |
| `presence_penalty` | -2.0 – 2.0 | 0 | Penalizes tokens that have appeared at all. Higher = more topic diversity |
| `stop` | Up to 4 sequences | None | Sequences where the model stops generating. E.g., `["\n", "END"]` |
| `n` | 1 – 128 | 1 | Number of completions to generate per request |
| `logit_bias` | -100 – 100 | None | JSON map of token ID to bias value. -100 = ban token, 100 = force token |
| `response_format` | `text`, `json_object` | `text` | Force JSON output (must also instruct model to output JSON in the prompt) |
| `seed` | Integer | None | For deterministic outputs. Same seed + same params = same result (best effort) |

**Token Limits by Model (approximate):**

| Model | Context Window | Max Output Tokens |
|-------|---------------|-------------------|
| GPT-4o | 128,000 | 16,384 |
| GPT-4o-mini | 128,000 | 16,384 |
| GPT-4 Turbo | 128,000 | 4,096 |
| GPT-4 (32K) | 32,768 | 8,192 |
| GPT-3.5-Turbo (16K) | 16,384 | 4,096 |
| text-embedding-ada-002 | 8,191 | N/A (embeddings) |
| text-embedding-3-small | 8,191 | N/A (1,536 dims) |
| text-embedding-3-large | 8,191 | N/A (3,072 dims) |

---

## 8. SSML Quick Reference (EXAM-TESTED!)

### Basic Structure

```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
       xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
  <voice name="en-US-JennyNeural">
    Hello, welcome to Azure AI.
  </voice>
</speak>
```

### Common SSML Elements

| Element | Purpose | Example |
|---------|---------|---------|
| `<voice>` | Select a specific voice | `<voice name="en-US-GuyNeural">Hello</voice>` |
| `<prosody>` | Control rate, pitch, volume | `<prosody rate="slow" pitch="high" volume="loud">Emphasized text</prosody>` |
| `<break>` | Insert a pause | `<break time="500ms"/>` or `<break strength="strong"/>` |
| `<emphasis>` | Emphasize a word | `<emphasis level="strong">important</emphasis>` |
| `<say-as>` | Control pronunciation | `<say-as interpret-as="date" format="mdy">03/15/2025</say-as>` |
| `<audio>` | Insert pre-recorded audio | `<audio src="https://example.com/chime.wav"/>` |
| `<sub>` | Substitute pronunciation | `<sub alias="World Wide Web Consortium">W3C</sub>` |
| `<phoneme>` | Specify exact phonetic pronunciation | `<phoneme alphabet="ipa" ph="təˈmeɪ.toʊ">tomato</phoneme>` |
| `<mstts:express-as>` | Apply speaking style (MS extension) | `<mstts:express-as style="cheerful">Great news!</mstts:express-as>` |
| `<mstts:silence>` | Fine-grained silence control | `<mstts:silence type="Leading" value="200ms"/>` |
| `<bookmark>` | Mark a point in the audio for events | `<bookmark mark="section1"/>` |
| `<lang>` | Switch language mid-utterance | `<lang xml:lang="fr-FR">Bonjour</lang>` |

### Prosody Attribute Values

| Attribute | Named Values | Relative | Absolute |
|-----------|-------------|----------|----------|
| `rate` | `x-slow`, `slow`, `medium`, `fast`, `x-fast` | `+20%`, `-30%` | N/A |
| `pitch` | `x-low`, `low`, `medium`, `high`, `x-high` | `+10%`, `-5%` | `200Hz` |
| `volume` | `silent`, `x-soft`, `soft`, `medium`, `loud`, `x-loud` | `+10%`, `-20%` | N/A |

### `say-as` interpret-as Values

| Value | Use Case | Example Input |
|-------|----------|---------------|
| `date` | Read as a date | `<say-as interpret-as="date" format="mdy">03/15/2025</say-as>` |
| `time` | Read as a time | `<say-as interpret-as="time" format="hms12">2:30pm</say-as>` |
| `telephone` | Read as a phone number | `<say-as interpret-as="telephone">+1-425-555-0100</say-as>` |
| `cardinal` | Read as a cardinal number | `<say-as interpret-as="cardinal">42</say-as>` |
| `ordinal` | Read as an ordinal | `<say-as interpret-as="ordinal">3</say-as>` → "third" |
| `characters` | Spell out each character | `<say-as interpret-as="characters">ABC</say-as>` |
| `address` | Read as a street address | `<say-as interpret-as="address">123 Main St</say-as>` |

### SSML Example — Combined Elements

```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
       xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
  <voice name="en-US-JennyNeural">
    <mstts:express-as style="friendly">
      Welcome to your daily briefing.
    </mstts:express-as>
    <break time="750ms"/>
    <prosody rate="-10%" pitch="+5%">
      Today is <say-as interpret-as="date" format="mdy">01/15/2025</say-as>.
    </prosody>
    <break strength="medium"/>
    You have <emphasis level="strong">3</emphasis> meetings scheduled.
    <break time="500ms"/>
    <voice name="en-GB-RyanNeural">
      <lang xml:lang="en-GB">Here are the details.</lang>
    </voice>
  </voice>
</speak>
```

---

## 9. AI Search Query Syntax

### OData Filter Expressions (`$filter`)

```
# Equality
$filter=category eq 'Technology'

# Comparison
$filter=rating gt 4

# Logical operators
$filter=category eq 'Tech' and rating ge 4
$filter=category eq 'Tech' or category eq 'Science'
$filter=not (category eq 'Sports')

# Collection filters (any/all)
$filter=tags/any(t: t eq 'azure')
$filter=authors/all(a: a ne 'unknown')

# Geo-spatial
$filter=geo.distance(location, geography'POINT(-122.131577 47.678581)') le 10

# String functions
$filter=search.ismatch('wifi', 'amenities')
$filter=search.ismatchscoring('luxury', 'description', 'full', 'any')
```

### Select, OrderBy, Top, Skip

```
# Select specific fields
$select=title,content,category,rating

# Order results
$orderby=rating desc,title asc

# Pagination
$top=10&$skip=20

# Count total results
$count=true
```

### Search Modes & Query Types

| Parameter | Values | Description |
|-----------|--------|-------------|
| `searchMode` | `any` (default), `all` | `any`: OR between terms; `all`: AND between terms |
| `queryType` | `simple` (default), `full`, `semantic` | `simple`: basic search; `full`: Lucene syntax; `semantic`: AI-ranked |

### Lucene Query Syntax (`queryType=full`)

```
# Phrase search
"cloud computing"

# Wildcards
comp*          (prefix)
comput?r       (single char)

# Fuzzy search
computer~1     (edit distance 1)
computer~2     (edit distance 2)

# Proximity search
"cloud computing"~5   (within 5 words)

# Boosting
cloud^4 computing     (boost "cloud" 4x)

# Field-scoped search
title:azure AND content:"machine learning"

# Regular expressions
/[a-z]{3}[0-9]{4}/
```

### Semantic Search Configuration

```json
{
  "search": "how does renewable energy work?",
  "queryType": "semantic",
  "semanticConfiguration": "my-semantic-config",
  "captions": "extractive",
  "answers": "extractive|count-3",
  "queryLanguage": "en-us"
}
```

### Vector Search

```json
{
  "vectorQueries": [
    {
      "kind": "vector",
      "vector": [0.01, -0.03, 0.12, "..."],
      "fields": "contentVector",
      "k": 5,
      "exhaustive": false
    }
  ],
  "select": "title,content"
}
```

### Hybrid Search (Text + Vector)

```json
{
  "search": "renewable energy",
  "vectorQueries": [
    {
      "kind": "vector",
      "vector": [0.01, -0.03, 0.12, "..."],
      "fields": "contentVector",
      "k": 5
    }
  ],
  "queryType": "semantic",
  "semanticConfiguration": "my-semantic-config"
}
```

---

## 10. Content Safety Severity Levels

### Output Type: FourSeverityLevels

| Severity | Value | Description |
|----------|-------|-------------|
| Safe | **0** | Content is safe — no harmful content detected |
| Low | **2** | Minor or indirect references — low risk |
| Medium | **4** | Explicit references but not graphic — moderate risk |
| High | **6** | Graphic, explicit, or severe content — high risk |

### Categories

| Category | What It Detects | Examples |
|----------|----------------|---------|
| **Hate** | Hate speech, discrimination, slurs, stereotyping based on protected attributes | Racial slurs, derogatory language about groups |
| **Violence** | Violent content, threats, descriptions of physical harm | Graphic injury descriptions, threats of harm |
| **Sexual** | Sexual content, explicit material, sexual solicitation | Explicit descriptions, inappropriate content |
| **Self-Harm** | Self-injury, suicide ideation, eating disorders | Instructions for self-harm, glorification of suicide |

### Decision Logic Example

```
IF any category severity >= threshold THEN reject/flag content

Recommended thresholds:
  - Strict:   reject if severity >= 2 (any non-safe content)
  - Moderate: reject if severity >= 4 (medium and above)
  - Lenient:  reject if severity >= 6 (only high severity)
```

### Additional Content Safety Features

| Feature | Purpose |
|---------|---------|
| **Prompt Shields** | Detect jailbreak attempts and indirect prompt injection |
| **Groundedness Detection** | Check if AI output is grounded in source material |
| **Protected Material Detection** | Identify known copyrighted text in AI output |
| **Custom Categories** | Define your own moderation categories with examples |

---

## 11. Container Deployment Environment Variables

### Required for ALL Azure AI Containers

| Variable | Description | Example |
|----------|-------------|---------|
| `ApiKey` | Your Azure AI resource API key | `ApiKey=abc123def456` |
| `Billing` | The resource endpoint URI (for billing — no data leaves the container, but billing still requires connectivity) | `Billing=https://myresource.cognitiveservices.azure.com` |
| `Eula` | Must be set to `accept` to run | `Eula=accept` |

### Docker Run Example

```bash
docker run --rm -it -p 5000:5000 \
  --memory 8g --cpus 4 \
  mcr.microsoft.com/azure-cognitive-services/textanalytics/sentiment:latest \
  Eula=accept \
  Billing=https://myresource.cognitiveservices.azure.com \
  ApiKey=<your-api-key>
```

### Optional / Service-Specific Settings

| Variable | Applies To | Description |
|----------|-----------|-------------|
| `Logging:Console:LogLevel:Default` | All | Set logging level (`Information`, `Warning`, `Error`, `Debug`) |
| `Mounts:Input` | Speech, Vision | Mount for input data |
| `Mounts:Output` | Speech, Vision | Mount for output data |
| `ApplicationInsights:InstrumentationKey` | All | Enable telemetry to App Insights |
| `CloudAI:Storage:StorageScenario` | Language (connected) | Required for connected containers |
| `DownloadRecipe` | Disconnected | Recipe for disconnected container model download |

### Container Types

| Type | Internet Requirement | Use Case |
|------|---------------------|----------|
| **Standard (Connected)** | Requires internet for billing | On-prem with internet — data stays local, billing calls go out |
| **Disconnected** | Air-gapped (no internet after download) | Fully offline; requires commitment plan purchase and license download |

### Available Containers (Key Ones)

| Container | Image |
|-----------|-------|
| Sentiment Analysis | `mcr.microsoft.com/azure-cognitive-services/textanalytics/sentiment` |
| Language Detection | `mcr.microsoft.com/azure-cognitive-services/textanalytics/language` |
| Key Phrase Extraction | `mcr.microsoft.com/azure-cognitive-services/textanalytics/keyphrase` |
| NER | `mcr.microsoft.com/azure-cognitive-services/textanalytics/ner` |
| Speech-to-Text | `mcr.microsoft.com/azure-cognitive-services/speechservices/speech-to-text` |
| Text-to-Speech | `mcr.microsoft.com/azure-cognitive-services/speechservices/text-to-speech` |
| Read OCR | `mcr.microsoft.com/azure-cognitive-services/vision/read` |
| Document Intelligence (Layout) | `mcr.microsoft.com/azure-cognitive-services/form-recognizer/layout` |

---

## 12. Key Azure CLI Commands

### Resource Group & AI Services

```bash
# Create a resource group
az group create --name myResourceGroup --location eastus

# Create a multi-service AI resource
az cognitiveservices account create \
  --name myAIResource \
  --resource-group myResourceGroup \
  --kind CognitiveServices \
  --sku S0 \
  --location eastus

# Get keys
az cognitiveservices account keys list \
  --name myAIResource \
  --resource-group myResourceGroup

# Get endpoint
az cognitiveservices account show \
  --name myAIResource \
  --resource-group myResourceGroup \
  --query "properties.endpoint" -o tsv
```

### Azure OpenAI

```bash
# Create an Azure OpenAI resource
az cognitiveservices account create \
  --name myOpenAIResource \
  --resource-group myResourceGroup \
  --kind OpenAI \
  --sku S0 \
  --location eastus

# Deploy a model
az cognitiveservices account deployment create \
  --name myOpenAIResource \
  --resource-group myResourceGroup \
  --deployment-name gpt4o-deploy \
  --model-name gpt-4o \
  --model-version "2024-08-06" \
  --model-format OpenAI \
  --sku-capacity 10 \
  --sku-name Standard
```

### Azure AI Search

```bash
# Create a search service
az search service create \
  --name mySearchService \
  --resource-group myResourceGroup \
  --sku standard \
  --location eastus

# Get admin keys
az search admin-key show \
  --service-name mySearchService \
  --resource-group myResourceGroup

# Get query keys
az search query-key list \
  --service-name mySearchService \
  --resource-group myResourceGroup
```

### Deployment & Cleanup

```bash
# Deploy a Bicep template
az deployment group create \
  --resource-group myResourceGroup \
  --template-file main.bicep \
  --parameters @params.json

# Delete resource group (cleanup)
az group delete --name myResourceGroup --yes --no-wait

# List all AI resources in a subscription
az cognitiveservices account list -o table
```

### RBAC Role Assignment

```bash
# Assign Cognitive Services User role
az role assignment create \
  --assignee <principal-id-or-email> \
  --role "Cognitive Services User" \
  --scope /subscriptions/<sub-id>/resourceGroups/<rg>/providers/Microsoft.CognitiveServices/accounts/<resource>
```

---

## 13. Confidence Score Thresholds

| Service / Feature | Score Range | Recommended Threshold | Guidance |
|------------------|-------------|----------------------|----------|
| **Language — Sentiment** | 0.0 – 1.0 (per sentiment class) | ≥ 0.75 for positive/negative classification | Scores close to 0.5 = mixed/ambiguous; treat with caution |
| **Language — NER** | 0.0 – 1.0 (confidence per entity) | ≥ 0.8 for high-confidence entity extraction | Lower scores often indicate ambiguous entity boundaries |
| **Language — CLU (Intents)** | 0.0 – 1.0 | ≥ 0.7 top intent; consider "None" if below threshold | Use `confidenceScoreThreshold` in prediction API |
| **Language — CLU (Entities)** | 0.0 – 1.0 | ≥ 0.5 | Learned entities may have lower confidence than list/prebuilt |
| **Vision — Image Analysis (Tags)** | 0.0 – 1.0 | ≥ 0.7 for reliable tags | Tags below 0.5 are speculative |
| **Vision — Object Detection** | 0.0 – 1.0 | ≥ 0.6 for detection; ≥ 0.8 for automation | Lower threshold = more detections but more false positives |
| **Custom Vision — Classification** | 0.0 – 1.0 (probability) | ≥ 0.5 default; ≥ 0.7 for production | Adjustable probability threshold at prediction time |
| **Custom Vision — Detection** | 0.0 – 1.0 (probability) | ≥ 0.5 (overlap threshold ≥ 0.3) | Two thresholds: probability threshold + IoU (overlap) threshold |
| **Document Intelligence** | 0.0 – 1.0 (per field) | ≥ 0.8 for automated processing | Fields below threshold → route to human review |
| **Face — Verification** | 0.0 – 1.0 (confidence) | ≥ 0.5 (identical) | Higher threshold = fewer false positives but more false negatives |
| **Speech — STT** | 0.0 – 1.0 (per word confidence) | ≥ 0.7 for word-level | N-best results available; confidence varies by audio quality |
| **AI Search — Semantic Reranker** | 0.0 – 4.0 (`@search.rerankerScore`) | ≥ 1.5 for relevant results | Not a 0–1 probability; relative ranking score |
| **Content Safety** | 0, 2, 4, 6 (severity) | Policy-dependent (see Section 10) | Set thresholds per category based on your use case |

---

## 14. Exam Day Quick Tips

1. **Read the scenario carefully** — Many questions test *which service* to use. Focus on the specific requirement (cost, latency, compliance, customization) before picking an answer.

2. **"Least effort" / "Minimum code changes"** — When the question says this, choose prebuilt models and managed services over custom solutions.

3. **Responsible AI is always relevant** — If an answer choice includes content filtering, human review loops, or transparency, it's often correct for responsible AI questions.

4. **Know your limits (Section 3)** — File sizes, minimum training samples, and tier differences appear in multiple question formats.

5. **Managed Identity > API Key** — For any production/security question, managed identity with RBAC is the preferred authentication method.

6. **Containers still need billing** — Even when deploying on-premises with Docker containers, the `Billing` endpoint must be set. Data stays local; metering calls go to Azure (unless disconnected container).

7. **SSML details matter** — Be comfortable with `<prosody>`, `<break>`, `<say-as>`, and `<mstts:express-as>` elements and their attribute values.

8. **AI Search enrichment pipeline** — Know the flow: Data Source → Indexer → Skillset (built-in + custom skills) → Index. Skillsets attach to indexers, not indexes.

9. **Azure OpenAI ≠ OpenAI** — Azure OpenAI uses your Azure subscription, runs in Azure regions, supports managed identity, content filtering is always on, and endpoints use `/openai/deployments/<name>/`.

10. **Elimination strategy** — On case-study questions, eliminate answers that introduce unnecessary complexity. Azure certifications reward solutions that use platform-managed features over custom infrastructure.

---

> **Last updated**: Reference material for AI-102 exam preparation. Always verify against [official Microsoft documentation](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-engineer/) for the latest service capabilities and exam objectives.
