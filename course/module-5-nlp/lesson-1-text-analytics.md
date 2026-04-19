# Lesson 1: Text Analytics & Translation

## Learning Objectives

After completing this lesson, you will be able to:

- Extract key phrases from text documents
- Analyze sentiment at document and sentence level with opinion mining
- Recognize and categorize named entities (NER)
- Detect and redact personally identifiable information (PII)
- Detect the language of input text
- Link entities to Wikipedia knowledge base articles
- Translate text in real time to multiple languages
- Perform asynchronous batch document translation
- Train and deploy custom translation models

---

## Azure AI Language Service Overview

Azure AI Language consolidates multiple NLP capabilities under a single endpoint. You create a **Language resource** (or a multi-service **Azure AI Services resource**) and call various features via the unified `/text/analytics/v3.2-preview.2` REST endpoint or the Python SDK `azure-ai-textanalytics`.

**Endpoint format:**

```
https://<resource-name>.cognitiveservices.azure.com/
```

**Authentication:**

| Method | Header / Parameter |
|--------|--------------------|
| API Key | `Ocp-Apim-Subscription-Key: <key>` |
| Azure AD Token | `Authorization: Bearer <token>` |

> **EXAM TIP:** A single Azure AI Language resource provides text analytics, CLU, custom question answering, and more. You do NOT need separate resources for each feature. However, **Translator** is a separate Azure AI service with its own resource and endpoint.

---

## Key Phrase Extraction

Key phrase extraction identifies the main talking points in a document. It returns a list of strings representing the key concepts.

### How It Works

The service uses NLP models to parse the text and identify noun phrases that represent the main ideas. It does not perform summarization — it returns individual phrases.

### Use Cases

- Quickly scanning customer feedback for common themes
- Tagging documents for search indexing
- Clustering support tickets by topic

### Limits

| Parameter | Limit |
|-----------|-------|
| Max characters per document | 5,120 |
| Max documents per request | 25 |
| Max request size | 1 MB |

### Python SDK Example

```python
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint = "https://<resource>.cognitiveservices.azure.com/"
key = "<api-key>"

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

documents = [
    "The food at the hotel was excellent but the room service was slow.",
    "Azure AI services provide powerful machine learning capabilities."
]

response = client.extract_key_phrases(documents)

for idx, doc in enumerate(response):
    if not doc.is_error:
        print(f"Document {idx}: {doc.key_phrases}")
    else:
        print(f"Document {idx} error: {doc.error}")
```

**Sample output:**

```
Document 0: ['food', 'hotel', 'room service']
Document 1: ['Azure AI services', 'powerful machine learning capabilities']
```

> **EXAM TIP:** Key phrase extraction returns **strings**, not entities with categories. If the question asks about categorizing extracted information (Person, Location, Organization), that is **Named Entity Recognition**, not key phrase extraction.

---

## Sentiment Analysis

Sentiment analysis evaluates text and returns sentiment labels with confidence scores at both document and sentence levels.

### Sentiment Labels

| Label | Description |
|-------|-------------|
| **Positive** | Text expresses favorable opinion |
| **Neutral** | Text is factual or lacks emotional content |
| **Negative** | Text expresses unfavorable opinion |
| **Mixed** | Document contains both positive and negative sentences |

### Confidence Scores

Each sentiment label has a confidence score between 0 and 1. The three scores (positive, neutral, negative) sum to 1.0.

```json
{
  "sentiment": "mixed",
  "confidenceScores": {
    "positive": 0.45,
    "neutral": 0.05,
    "negative": 0.50
  },
  "sentences": [
    {
      "text": "The food was excellent.",
      "sentiment": "positive",
      "confidenceScores": { "positive": 0.98, "neutral": 0.01, "negative": 0.01 }
    },
    {
      "text": "But the service was terrible.",
      "sentiment": "negative",
      "confidenceScores": { "positive": 0.01, "neutral": 0.02, "negative": 0.97 }
    }
  ]
}
```

### Opinion Mining (Aspect-Based Sentiment)

Opinion mining is an advanced feature of sentiment analysis that provides granular insight into opinions about specific **targets** (aspects) and **assessments** (opinions about those targets).

- **Target:** The entity being discussed (e.g., "food", "staff", "room")
- **Assessment:** The opinion word (e.g., "excellent", "rude", "clean")

Enable it by passing `show_opinion_mining=True` in the SDK.

### Python SDK — Sentiment with Opinion Mining

```python
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

client = TextAnalyticsClient(
    endpoint="https://<resource>.cognitiveservices.azure.com/",
    credential=AzureKeyCredential("<api-key>")
)

documents = [
    "The food was great but the waiter was rude.",
    "The hotel room was clean and spacious."
]

response = client.analyze_sentiment(
    documents,
    show_opinion_mining=True
)

for doc in response:
    print(f"Document sentiment: {doc.sentiment}")
    for sentence in doc.sentences:
        print(f"  Sentence: '{sentence.text}' → {sentence.sentiment}")
        for mined_opinion in sentence.mined_opinions:
            target = mined_opinion.target
            print(f"    Target: '{target.text}' → {target.sentiment}")
            for assessment in mined_opinion.assessments:
                print(f"      Assessment: '{assessment.text}' → {assessment.sentiment}")
```

**Sample output:**

```
Document sentiment: mixed
  Sentence: 'The food was great but the waiter was rude.' → mixed
    Target: 'food' → positive
      Assessment: 'great' → positive
    Target: 'waiter' → negative
      Assessment: 'rude' → negative
```

> **EXAM TIP:** Opinion mining is enabled via the `show_opinion_mining=True` parameter. It breaks down sentiment to the **aspect level** — returning targets and assessments. This is different from standard sentiment analysis, which only provides document-level and sentence-level sentiment.

---

## Named Entity Recognition (NER)

NER identifies and categorizes entities in text into predefined categories.

### Entity Categories

| Category | Examples | Subcategories |
|----------|----------|---------------|
| **Person** | "Satya Nadella", "Jane Doe" | — |
| **Location** | "Seattle", "Mount Everest" | GPE, Structural, Geographic |
| **Organization** | "Microsoft", "United Nations" | Medical, Stock Exchange, Sports |
| **DateTime** | "January 2024", "next Tuesday" | Date, Time, DateRange, Duration |
| **Quantity** | "35 degrees", "10 km" | Number, Percentage, Ordinal, Age, Currency, Dimension, Temperature |
| **Email** | "user@example.com" | — |
| **URL** | "https://example.com" | — |
| **IP Address** | "192.168.1.1" | — |
| **Phone Number** | "+1-555-0100" | — |
| **Skill** | "Python programming" | — |
| **Event** | "Olympics", "World Cup" | Cultural, Natural, Sports |
| **Product** | "Surface Pro", "Xbox" | Computing |

### Response Structure

Each recognized entity includes:
- `text` — the entity as it appears in the text
- `category` — the broad category
- `subcategory` — more specific classification (if available)
- `confidenceScore` — 0.0 to 1.0
- `offset` — character position in the document
- `length` — character length of the entity

### Python SDK — NER

```python
documents = ["Microsoft was founded by Bill Gates and Paul Allen in Albuquerque, New Mexico on April 4, 1975."]

response = client.recognize_entities(documents)

for doc in response:
    for entity in doc.entities:
        print(f"  Entity: {entity.text}")
        print(f"    Category: {entity.category} / {entity.subcategory}")
        print(f"    Confidence: {entity.confidence_score:.2f}")
```

**Sample output:**

```
  Entity: Microsoft
    Category: Organization / None
    Confidence: 1.00
  Entity: Bill Gates
    Category: Person / None
    Confidence: 1.00
  Entity: Paul Allen
    Category: Person / None
    Confidence: 1.00
  Entity: Albuquerque, New Mexico
    Category: Location / GPE
    Confidence: 0.98
  Entity: April 4, 1975
    Category: DateTime / Date
    Confidence: 0.95
```

> **EXAM TIP:** NER identifies entities and assigns categories, but does NOT link them to external knowledge bases. If the question involves linking to Wikipedia or disambiguating entities, that is **Entity Linking** (covered below).

---

## PII Detection and Redaction

PII detection identifies and optionally redacts sensitive personal information from text.

### PII Categories

| Category | Examples |
|----------|----------|
| Social Security Number | 123-45-6789 |
| Credit Card Number | 4111-1111-1111-1111 |
| Email Address | user@example.com |
| Phone Number | +1-555-0100 |
| Physical Address | 123 Main St, Anytown, USA |
| IP Address | 192.168.1.1 |
| Person Name | John Doe |
| Date of Birth | 01/15/1990 |
| Passport Number | AB1234567 |
| Driver's License | DL-12345678 |
| Bank Account | 1234567890 |

### Redaction

When you call PII detection, the response includes a `redacted_text` field where each PII entity is replaced with its category label in brackets:

```
Input:  "Call John Doe at 555-0100 or email john@example.com"
Output: "Call ******** at ******** or email *****************"
```

### Domain Parameter — PHI Detection

Set `domain="phi"` to detect Protected Health Information (PHI) entities for HIPAA compliance:

```python
response = client.recognize_pii_entities(
    documents,
    domain="phi"  # Enables healthcare-specific PII detection
)
```

PHI-specific categories include: patient names, medical record numbers, diagnosis codes, treatment information.

### StringIndexType Parameter

Controls how text offsets are calculated:

| Value | Description |
|-------|-------------|
| `Utf16CodeUnit` | Default. Compatible with Python, C#, JavaScript |
| `UnicodeCodePoint` | Recommended for Python |
| `TextElements_v8` | Grapheme clusters |

### Python SDK — PII Detection

```python
documents = [
    "My SSN is 123-45-6789 and my email is jane.doe@contoso.com. Please call 555-0199."
]

response = client.recognize_pii_entities(documents)

for doc in response:
    print(f"Redacted: {doc.redacted_text}")
    for entity in doc.entities:
        print(f"  PII: '{entity.text}' → Category: {entity.category} (Confidence: {entity.confidence_score:.2f})")
```

**Sample output:**

```
Redacted: My SSN is *********** and my email is *******************. Please call ********.
  PII: '123-45-6789' → Category: USSocialSecurityNumber (Confidence: 0.85)
  PII: 'jane.doe@contoso.com' → Category: Email (Confidence: 0.99)
  PII: '555-0199' → Category: PhoneNumber (Confidence: 0.80)
```

> **EXAM TIP:** PII detection returns BOTH the list of PII entities AND a `redacted_text` version. The `domain="phi"` parameter enables healthcare-specific PII detection. Remember the `StringIndexType` parameter — the exam may ask which value to use for a specific programming language.

---

## Language Detection

Language detection identifies the primary language of input text and returns a confidence score.

### Response Fields

| Field | Description |
|-------|-------------|
| `name` | Human-readable language name (e.g., "English") |
| `iso6391Name` | ISO 639-1 code (e.g., "en") |
| `confidenceScore` | 0.0 to 1.0 |

### Unknown Language

If the language cannot be determined, the response returns:

```json
{
  "name": "(Unknown)",
  "iso6391Name": "(Unknown)",
  "confidenceScore": 0.0
}
```

### Country Hint

The `countryHint` parameter helps disambiguate similar languages:

```python
documents = [
    {"id": "1", "text": "Ce document est en français.", "countryHint": "FR"},
    {"id": "2", "text": "Este documento está en español.", "countryHint": "ES"}
]

# To disable country hint:
documents = [
    {"id": "1", "text": "Some ambiguous text.", "countryHint": ""}
]
```

### Python SDK — Language Detection

```python
documents = [
    "This is a document written in English.",
    "Dies ist ein Dokument auf Deutsch.",
    "Este es un documento en español."
]

response = client.detect_language(documents)

for doc in response:
    print(f"Language: {doc.primary_language.name} ({doc.primary_language.iso6391_name})")
    print(f"Confidence: {doc.primary_language.confidence_score:.2f}")
```

### REST Example — Language Detection

```http
POST https://<resource>.cognitiveservices.azure.com/text/analytics/v3.2-preview.2/languages
Content-Type: application/json
Ocp-Apim-Subscription-Key: <key>

{
  "documents": [
    { "id": "1", "text": "Bonjour tout le monde" },
    { "id": "2", "text": "Hola, ¿cómo estás?" }
  ]
}
```

**Response:**

```json
{
  "documents": [
    {
      "id": "1",
      "detectedLanguage": {
        "name": "French",
        "iso6391Name": "fr",
        "confidenceScore": 1.0
      }
    },
    {
      "id": "2",
      "detectedLanguage": {
        "name": "Spanish",
        "iso6391Name": "es",
        "confidenceScore": 1.0
      }
    }
  ]
}
```

> **EXAM TIP:** Use `countryHint=""` (empty string) to disable the country hint, NOT `null` or omitting the field. The exam may test this subtle distinction. Language detection supports 120+ languages.

---

## Entity Linking

Entity linking identifies entities in text and links them to corresponding entries in a well-known knowledge base (Wikipedia).

### How It Differs from NER

| Feature | NER | Entity Linking |
|---------|-----|----------------|
| Categorizes entities | ✅ Yes (Person, Location, etc.) | ❌ No categories |
| Links to knowledge base | ❌ No | ✅ Yes (Wikipedia) |
| Disambiguates entities | ❌ No | ✅ Yes |
| Returns URL | ❌ No | ✅ Yes (Wikipedia URL) |
| Returns confidence score | ✅ Yes | ✅ Yes |

### Disambiguation Example

The text "I love Mars bars" could refer to:
- **Mars (planet)** — the fourth planet
- **Mars, Inc.** — the candy company
- **Mars (mythology)** — the Roman god

Entity linking uses context to determine the correct Wikipedia article.

### Response Fields

| Field | Description |
|-------|-------------|
| `name` | Entity display name |
| `matches` | Text spans that match this entity |
| `language` | Language of the Wikipedia article |
| `url` | Wikipedia URL |
| `dataSource` | Always "Wikipedia" |
| `id` | Wikipedia page ID |
| `bingId` | Bing entity ID |

### Python SDK — Entity Linking

```python
documents = [
    "I visited the Space Needle in Seattle last weekend.",
    "Mars was named after the Roman god of war."
]

response = client.recognize_linked_entities(documents)

for doc in response:
    for entity in doc.entities:
        print(f"Entity: {entity.name}")
        print(f"  URL: {entity.url}")
        print(f"  Data Source: {entity.data_source}")
        for match in entity.matches:
            print(f"  Match: '{match.text}' (Confidence: {match.confidence_score:.2f})")
```

**Sample output:**

```
Entity: Space Needle
  URL: https://en.wikipedia.org/wiki/Space_Needle
  Data Source: Wikipedia
  Match: 'Space Needle' (Confidence: 0.95)
Entity: Seattle
  URL: https://en.wikipedia.org/wiki/Seattle
  Data Source: Wikipedia
  Match: 'Seattle' (Confidence: 0.98)
Entity: Mars
  URL: https://en.wikipedia.org/wiki/Mars_(mythology)
  Data Source: Wikipedia
  Match: 'Mars' (Confidence: 0.88)
```

> **EXAM TIP:** Entity linking provides **disambiguation** — it resolves ambiguous entity names to the correct Wikipedia article based on context. The exam loves asking about the difference between NER (categorizes entities) and entity linking (links to Wikipedia). Remember: entity linking ALWAYS uses Wikipedia as its data source.

---

## Text Translation (Azure AI Translator)

Azure AI Translator is a **separate** service from Azure AI Language. It provides real-time text translation, transliteration, and language detection.

### Key Features

| Feature | Description |
|---------|-------------|
| **Translate** | Translate text between 100+ languages |
| **Transliterate** | Convert script (e.g., Japanese Kanji → Latin) |
| **Detect** | Identify source language |
| **Dictionary Lookup** | Alternative translations for a word |
| **Dictionary Examples** | Usage examples for translations |
| **Languages** | Get list of supported languages |

### Endpoint

The Translator service uses a **global endpoint** (not a regional one like Language):

```
https://api.cognitive.microsofttranslator.com/
```

Or regional endpoints:

```
https://<region>.api.cognitive.microsofttranslator.com/
```

### REST Example — Text Translation

```http
POST https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=fr&to=de
Content-Type: application/json
Ocp-Apim-Subscription-Key: <key>
Ocp-Apim-Subscription-Region: <region>

[
  { "Text": "Hello, how are you?" },
  { "Text": "The weather is beautiful today." }
]
```

**Response:**

```json
[
  {
    "translations": [
      { "text": "Bonjour, comment allez-vous?", "to": "fr" },
      { "text": "Hallo, wie geht es Ihnen?", "to": "de" }
    ]
  },
  {
    "translations": [
      { "text": "Le temps est magnifique aujourd'hui.", "to": "fr" },
      { "text": "Das Wetter ist heute schön.", "to": "de" }
    ]
  }
]
```

### Key Parameters

| Parameter | Description |
|-----------|-------------|
| `from` | Source language code (optional — auto-detected if omitted) |
| `to` | Target language code(s) — **required**, can specify multiple |
| `textType` | `plain` (default) or `html` |
| `profanityAction` | `NoAction`, `Marked`, `Deleted` |
| `profanityMarker` | `Asterisk` (default) or `Tag` |
| `includeAlignment` | Returns alignment mapping |
| `includeSentenceLength` | Returns sentence boundaries |

### Translate to Multiple Languages

You can translate to multiple target languages in a single request by specifying multiple `to` parameters:

```
?to=fr&to=de&to=es&to=ja
```

### Transliteration

Convert text from one script to another without translation:

```http
POST https://api.cognitive.microsofttranslator.com/transliterate?api-version=3.0&language=ja&fromScript=jpan&toScript=latn

[{ "Text": "こんにちは" }]
```

Response: `[{ "text": "Kon'nichiwa", "script": "latn" }]`

### Profanity Handling

| Action | Behavior |
|--------|----------|
| `NoAction` | Profanity is translated as-is |
| `Marked` | Profanity is surrounded by markers (asterisks or XML tags) |
| `Deleted` | Profanity is removed from the output |

### Sentence Length Limits

| Limit | Value |
|-------|-------|
| Max characters per request | 50,000 |
| Max characters per element | 10,000 |
| Max text elements per request | 100 |

> **EXAM TIP:** The Translator service requires **two headers** for authentication: `Ocp-Apim-Subscription-Key` AND `Ocp-Apim-Subscription-Region`. The region header is required when using a single-service Translator resource. The source language (`from`) is optional — if omitted, the service auto-detects the language.

---

## Document Translation

Document translation provides asynchronous batch translation for entire documents while preserving their formatting and structure.

### How It Works

1. Upload source documents to an Azure Blob Storage container
2. Specify a target container for translated documents
3. Submit a translation request (asynchronous)
4. Poll for status or use webhook notifications
5. Download translated documents from the target container

### Supported Document Formats

| Format | Extensions |
|--------|------------|
| Word | .docx |
| PDF | .pdf |
| HTML | .html, .htm |
| Excel | .xlsx |
| PowerPoint | .pptx |
| Plain Text | .txt |
| Tab-Separated | .tsv |
| Comma-Separated | .csv |
| Markdown | .md |
| OpenDocument | .odt, .ods, .odp |
| Rich Text | .rtf |
| XLIFF | .xlf |
| Message | .msg |

### Storage Setup

Both source and target containers need **SAS tokens** with appropriate permissions:
- Source container: **Read** and **List** permissions
- Target container: **Write** and **List** permissions

### REST Example — Document Translation

```http
POST https://<resource>.cognitiveservices.azure.com/translator/text/batch/v1.1/batches
Content-Type: application/json
Ocp-Apim-Subscription-Key: <key>

{
  "inputs": [
    {
      "source": {
        "sourceUrl": "https://<storage>.blob.core.windows.net/source?<SAS>",
        "language": "en"
      },
      "targets": [
        {
          "targetUrl": "https://<storage>.blob.core.windows.net/target-fr?<SAS>",
          "language": "fr"
        },
        {
          "targetUrl": "https://<storage>.blob.core.windows.net/target-de?<SAS>",
          "language": "de"
        }
      ]
    }
  ]
}
```

### Glossary Files

Glossaries ensure specific terms are translated consistently:

```http
{
  "inputs": [
    {
      "source": { "sourceUrl": "..." },
      "targets": [
        {
          "targetUrl": "...",
          "language": "fr",
          "glossaries": [
            {
              "glossaryUrl": "https://<storage>.blob.core.windows.net/glossary/terms.tsv?<SAS>",
              "format": "tsv"
            }
          ]
        }
      ]
    }
  ]
}
```

**Glossary TSV format:**

```
en	fr
Azure	Azure
machine learning	apprentissage automatique
```

> **EXAM TIP:** Document translation is **asynchronous** (batch). You submit the job and poll for status. Both source and target containers need SAS tokens. Glossary files ensure consistent translation of domain-specific terms.

---

## Custom Translator

Custom Translator allows you to build customized neural machine translation (NMT) models trained on your domain-specific parallel documents.

### When to Use Custom Translator

| Scenario | Use |
|----------|-----|
| General translation | Standard Translator |
| Domain-specific terminology (legal, medical, technical) | Custom Translator |
| Consistent branding / product names | Custom Translator |
| Previously translated content available | Custom Translator |

### Training Data Requirements

| Document Type | Description |
|---------------|-------------|
| **Parallel documents** | Source + target language pairs (required) |
| **Dictionary** | Term pairs for forced translations |
| **Training** | Bulk of parallel data for model training |
| **Tuning** | Fine-tuning the model (auto-selected if not provided) |
| **Testing** | Evaluate model quality (auto-selected if not provided) |

**Minimum requirement:** 10,000 parallel sentences for training.

### BLEU Score

The **Bilingual Evaluation Understudy (BLEU)** score measures translation quality:

| BLEU Score | Interpretation |
|------------|----------------|
| < 30 | Poor quality — significant errors |
| 30–40 | Moderate quality — understandable |
| 40–50 | Good quality — near-professional |
| 50–60 | High quality — fluent translation |
| > 60 | Excellent — approaching human quality |

### Workflow

1. **Create a workspace** in Custom Translator portal
2. **Create a project** — specify source/target language pair and category
3. **Upload parallel documents** — aligned sentence pairs
4. **Train the model** — automatic training process
5. **Evaluate** — review BLEU score and sample translations
6. **Publish** — deploy to a category ID
7. **Use** — add `category` parameter to standard Translator API calls

### Using Custom Model

```http
POST https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=fr&category=<categoryId>

[{ "Text": "The patient exhibited acute myocardial infarction." }]
```

> **EXAM TIP:** Custom Translator uses **parallel documents** for training — these are matched pairs of source and target language text. The quality metric is the **BLEU score** (higher is better). You deploy a custom model and reference it via the `category` parameter in the standard Translator API.

---

## Summary: All Text Analytics Operations

| Operation | SDK Method | What It Returns |
|-----------|-----------|-----------------|
| Key Phrases | `extract_key_phrases()` | List of key phrase strings |
| Sentiment | `analyze_sentiment()` | Document + sentence sentiment labels & scores |
| Opinion Mining | `analyze_sentiment(show_opinion_mining=True)` | Targets and assessments |
| NER | `recognize_entities()` | Entities with categories and confidence |
| PII | `recognize_pii_entities()` | PII entities + redacted text |
| Language Detection | `detect_language()` | Primary language + confidence |
| Entity Linking | `recognize_linked_entities()` | Entities with Wikipedia URLs |

---

## Key Takeaways

1. **Key phrase extraction** returns important noun phrases — not categorized entities.
2. **Sentiment analysis** provides document-level and sentence-level sentiment with confidence scores. **Opinion mining** adds target-assessment pairs for aspect-based sentiment.
3. **NER** categorizes entities (Person, Location, DateTime, etc.) with confidence scores but does NOT link to external knowledge bases.
4. **PII detection** identifies sensitive data and returns `redacted_text`. Use `domain="phi"` for healthcare data.
5. **Language detection** returns the primary language with a confidence score. Use `countryHint=""` to disable hints.
6. **Entity linking** disambiguates entities and links them to **Wikipedia** articles — different from NER.
7. **Translator** is a separate service from Language. It supports translation to **multiple languages** in one request and requires the `Ocp-Apim-Subscription-Region` header.
8. **Document translation** is asynchronous and requires Azure Blob Storage with SAS tokens for source and target containers.
9. **Custom Translator** uses parallel documents and produces a BLEU score. Deploy custom models and reference them via the `category` parameter.
10. All text analytics features share the same SDK (`azure-ai-textanalytics`) and endpoint, but Translator uses a separate endpoint (`api.cognitive.microsofttranslator.com`).

---

## Microsoft Documentation

- [Text Analytics overview](https://learn.microsoft.com/azure/ai-services/language-service/overview)
- [Sentiment analysis](https://learn.microsoft.com/azure/ai-services/language-service/sentiment-opinion-mining/overview)
- [Named entity recognition](https://learn.microsoft.com/azure/ai-services/language-service/named-entity-recognition/overview)
- [PII detection](https://learn.microsoft.com/azure/ai-services/language-service/personally-identifiable-information/overview)
- [Entity linking](https://learn.microsoft.com/azure/ai-services/language-service/entity-linking/overview)
- [Language detection](https://learn.microsoft.com/azure/ai-services/language-service/language-detection/overview)
- [Translator service](https://learn.microsoft.com/azure/ai-services/translator/overview)
- [Document translation](https://learn.microsoft.com/azure/ai-services/translator/document-translation/overview)
- [Custom Translator](https://learn.microsoft.com/azure/ai-services/translator/custom-translator/overview)
