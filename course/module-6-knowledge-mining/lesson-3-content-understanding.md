# Lesson 3: Azure AI Content Understanding

## Learning Objectives

After completing this lesson, you will be able to:

- Explain what Azure AI Content Understanding is and its role in the Azure AI ecosystem
- Configure OCR pipelines for high-quality text extraction from images and documents
- Implement document summarization and classification workflows
- Use attribute detection for document quality assessment and content type identification
- Extract entities, tables, and key-value pairs from complex documents
- Process video and audio content for transcription and analysis
- Choose the right Azure AI service for different content extraction scenarios

---

## 1. Overview of Azure AI Content Understanding

Azure AI Content Understanding is a unified Azure AI service designed to extract, classify, and summarize structured information from a wide range of content types—including documents, images, video, and audio. It brings together multiple AI capabilities into a single, streamlined service for building intelligent content processing pipelines.

### What Is Content Understanding?

Content Understanding provides a **single API surface** for:

- Extracting text, tables, and entities from documents and images
- Classifying documents by type
- Summarizing document content
- Detecting attributes like handwriting vs. printed text
- Processing multimedia content (video and audio)

Unlike Document Intelligence (which focuses on form/field extraction with prebuilt and custom models), Content Understanding is designed for broader, more flexible content analysis across multiple modalities.

### Relationship to Other Azure AI Services

| Service | Focus | Strengths |
|---------|-------|-----------|
| **Content Understanding** | Unified multimodal content extraction and analysis | Single API for documents, images, video, audio; summarization; flexible extraction |
| **Document Intelligence** | Structured document field extraction | Prebuilt models for invoices/receipts/IDs; custom form models; composed models |
| **Azure AI Vision (OCR)** | Image and video analysis | Real-time image analysis; spatial analysis; optical character recognition |
| **Azure AI Language** | Text analytics and NLP | Sentiment analysis; NER; text summarization; question answering |
| **Azure AI Speech** | Speech processing | Speech-to-text; text-to-speech; speech translation |

### Preview Status and Availability

- Content Understanding is currently in **public preview**.
- Available in select Azure regions (check the documentation for current availability).
- Preview APIs may change before general availability.
- Not recommended for production workloads until GA.

> **EXAM TIP:** Content Understanding is a newer service that unifies capabilities from multiple Azure AI services. For the exam, understand its key differentiators: **multimodal support** (documents + video + audio), **summarization**, and **flexible extraction**. Know when to choose it over Document Intelligence or AI Vision OCR.

### Core Architecture

Content Understanding uses an **analyzer-based** architecture:

1. **Create an analyzer** — Define the content type (document, image, video, audio) and the extraction tasks (OCR, summarization, entity extraction, etc.).
2. **Submit content** — Send your document, image, video, or audio file to the analyzer.
3. **Get results** — Retrieve structured extraction results in JSON format.

```
Content → Analyzer → Extraction Pipeline → Structured Results (JSON)
```

---

## 2. OCR Pipeline for Text Extraction

Content Understanding includes a powerful OCR pipeline for extracting text from images, scanned documents, and PDFs.

### High-Quality Text Extraction

The OCR pipeline handles:

- **Printed text** — Standard typed text in documents, signs, labels
- **Handwritten text** — Handwriting recognition across many scripts
- **Multi-language documents** — Automatic language detection and mixed-language support
- **Complex layouts** — Multi-column documents, forms, tables

### Layout Analysis

Content Understanding performs layout analysis to understand document structure:

| Feature | Description |
|---------|-------------|
| **Reading order** | Determines the correct sequence of text blocks for natural reading flow |
| **Column detection** | Identifies multi-column layouts and processes them correctly |
| **Header/footer detection** | Recognizes page headers and footers |
| **Section identification** | Identifies document sections and their hierarchy |
| **Table detection** | Locates and structures tabular data |
| **Figure/image regions** | Identifies embedded images and figures |

### Handwritten vs Printed Text

Content Understanding can differentiate between handwritten and printed text within the same document:

```json
{
  "content": "Patient Name: John Smith",
  "spans": [
    {
      "offset": 0,
      "length": 14,
      "attributes": {
        "textType": "printed"
      }
    },
    {
      "offset": 15,
      "length": 10,
      "attributes": {
        "textType": "handwritten"
      }
    }
  ]
}
```

### OCR Configuration (REST)

```http
PUT https://{endpoint}/contentunderstanding/analyzers/{analyzerName}?api-version=2024-12-01-preview
Content-Type: application/json
Ocp-Apim-Subscription-Key: {key}

{
  "description": "Document OCR analyzer",
  "scenario": "document",
  "config": {
    "returnDetails": true
  },
  "fieldSchema": {
    "fields": {
      "content": {
        "type": "string",
        "description": "Full extracted text content"
      }
    }
  }
}
```

### Comparison of OCR Services

| Feature | Content Understanding OCR | Document Intelligence OCR | AI Vision Read API |
|---------|--------------------------|--------------------------|-------------------|
| **Text extraction** | ✅ High quality | ✅ High quality | ✅ High quality |
| **Handwriting** | ✅ | ✅ | ✅ |
| **Layout analysis** | ✅ Advanced | ✅ Advanced | ❌ Basic |
| **Reading order** | ✅ | ✅ | ✅ |
| **Multi-language** | ✅ | ✅ | ✅ |
| **Table extraction** | ✅ | ✅ | ❌ |
| **Form field extraction** | Via custom schema | ✅ Prebuilt + custom | ❌ |
| **Summarization** | ✅ | ❌ | ❌ |
| **Video/audio OCR** | ✅ | ❌ | ✅ (images/video frames) |

> **EXAM TIP:** All three OCR services (Content Understanding, Document Intelligence, and AI Vision Read API) provide high-quality text extraction. The key differentiator is that Document Intelligence excels at **structured field extraction** (invoices, receipts), while Content Understanding adds **summarization and multimodal capabilities**. AI Vision Read API is best for simple, fast OCR on images.

---

## 3. Document Summarization and Classification

Content Understanding can automatically classify documents and generate summaries, reducing manual processing effort.

### Document Classification

Automatic classification identifies the type of document being processed:

- **Invoice**, **receipt**, **contract**, **letter**, **report**, **resume**, **form**
- Custom classification categories through analyzer configuration

#### Classification Use Cases

| Scenario | Description |
|----------|-------------|
| **Mailroom automation** | Sort incoming documents by type for routing |
| **Compliance processing** | Identify document types for regulatory workflows |
| **Records management** | Categorize and organize digital archives |
| **Claims processing** | Route insurance claims to appropriate queues |

### Document Summarization

Content Understanding supports both extractive and abstractive summarization:

| Type | Description | Output |
|------|-------------|--------|
| **Extractive** | Selects the most important sentences from the original text | Key sentences verbatim |
| **Abstractive** | Generates new sentences that capture the main ideas | Paraphrased summary |

#### Configuring Summarization

```http
PUT https://{endpoint}/contentunderstanding/analyzers/{analyzerName}?api-version=2024-12-01-preview
Content-Type: application/json
Ocp-Apim-Subscription-Key: {key}

{
  "description": "Document summarization analyzer",
  "scenario": "document",
  "fieldSchema": {
    "fields": {
      "summary": {
        "type": "string",
        "method": "generate",
        "description": "A concise summary of the document content"
      },
      "documentType": {
        "type": "string",
        "method": "classify",
        "description": "The type of document",
        "enum": ["invoice", "receipt", "contract", "report", "letter", "other"]
      },
      "keyTopics": {
        "type": "array",
        "items": { "type": "string" },
        "method": "generate",
        "description": "The main topics discussed in the document"
      }
    }
  }
}
```

### Key Information Extraction

Beyond raw text, Content Understanding can extract structured key information:

- **Dates and deadlines** — Important dates mentioned in contracts, reports
- **Monetary values** — Amounts, totals, budgets
- **People and organizations** — Named entities referenced in the document
- **Action items** — Tasks, obligations, requirements

> **EXAM TIP:** Content Understanding's summarization uses AI-generated output (powered by large language models), making it distinct from Document Intelligence's field extraction approach. If a question asks about **summarizing** or **classifying** documents (not extracting specific form fields), Content Understanding is the better choice.

---

## 4. Attribute Detection

Content Understanding can detect various attributes of the content being analyzed, providing metadata about document quality and characteristics.

### Handwritten vs Printed Text Differentiation

The service can classify text segments as handwritten or printed:

| Attribute | Description | Use Case |
|-----------|-------------|----------|
| `handwritten` | Text appears to be handwritten | Flag for manual review; different OCR confidence thresholds |
| `printed` | Text is machine-printed | High-confidence automated processing |
| `mixed` | Document contains both types | Apply different processing pipelines |

### Document Quality Assessment

Content Understanding evaluates document quality factors:

| Quality Attribute | Description | Impact |
|-------------------|-------------|--------|
| **Resolution** | Image DPI and clarity | Low resolution → lower OCR accuracy |
| **Contrast** | Text-to-background contrast | Poor contrast → missed text |
| **Skew** | Page rotation angle | Large skew → layout analysis errors |
| **Noise** | Background noise, artifacts | Noisy images → more OCR errors |
| **Blur** | Image sharpness | Blurry images → lower extraction accuracy |

### Page Orientation and Rotation Detection

The service automatically detects and corrects page orientation:

- **0°** — Normal orientation
- **90°** — Rotated clockwise
- **180°** — Upside down
- **270°** — Rotated counterclockwise

```json
{
  "pages": [
    {
      "pageNumber": 1,
      "angle": -2.3,
      "width": 8.5,
      "height": 11,
      "unit": "inch",
      "attributes": {
        "orientation": "portrait",
        "textType": "printed",
        "qualityScore": 0.92
      }
    }
  ]
}
```

### Content Type Identification

Content Understanding identifies the type of content on each page:

| Content Type | Description |
|-------------|-------------|
| **Text page** | Primarily text content |
| **Form page** | Structured form with fields and values |
| **Table page** | Primarily tabular data |
| **Image page** | Primarily photographic or graphic content |
| **Mixed** | Combination of content types |
| **Blank** | Empty or nearly empty page |

---

## 5. Entity and Table Extraction

Content Understanding provides sophisticated extraction capabilities for entities, tables, and key-value pairs from complex documents.

### Named Entity Extraction

The service extracts named entities from document content:

| Entity Type | Examples |
|-------------|---------|
| **Person** | "John Smith", "Dr. Jane Doe" |
| **Organization** | "Microsoft", "Contoso Ltd." |
| **Location** | "Seattle, WA", "123 Main St" |
| **Date/Time** | "March 15, 2024", "next Tuesday" |
| **Money/Currency** | "$1,500.00", "€200" |
| **Percentage** | "15%", "0.5%" |
| **Phone number** | "(206) 555-0100" |
| **Email** | "john@contoso.com" |

#### Configuring Entity Extraction

```http
PUT https://{endpoint}/contentunderstanding/analyzers/{analyzerName}?api-version=2024-12-01-preview
Content-Type: application/json
Ocp-Apim-Subscription-Key: {key}

{
  "description": "Entity extraction analyzer",
  "scenario": "document",
  "fieldSchema": {
    "fields": {
      "people": {
        "type": "array",
        "items": { "type": "string" },
        "method": "extract",
        "description": "All person names mentioned in the document"
      },
      "organizations": {
        "type": "array",
        "items": { "type": "string" },
        "method": "extract",
        "description": "All organization names mentioned in the document"
      },
      "totalAmount": {
        "type": "number",
        "method": "extract",
        "description": "The total monetary amount in the document"
      },
      "effectiveDate": {
        "type": "string",
        "method": "extract",
        "description": "The effective date of the agreement or document"
      }
    }
  }
}
```

### Table Detection and Structured Extraction

Content Understanding detects tables within documents and extracts them as structured data:

| Capability | Description |
|-----------|-------------|
| **Simple tables** | Standard row/column grids with headers |
| **Complex tables** | Merged cells, multi-row headers, nested tables |
| **Borderless tables** | Tables without visible grid lines |
| **Cross-page tables** | Tables that span multiple pages |

#### Table Extraction Result Structure

```json
{
  "tables": [
    {
      "rowCount": 5,
      "columnCount": 4,
      "cells": [
        {
          "rowIndex": 0,
          "columnIndex": 0,
          "content": "Product",
          "kind": "columnHeader",
          "spans": [{ "offset": 0, "length": 7 }]
        },
        {
          "rowIndex": 0,
          "columnIndex": 1,
          "content": "Quantity",
          "kind": "columnHeader"
        },
        {
          "rowIndex": 1,
          "columnIndex": 0,
          "content": "Widget A",
          "kind": "content"
        },
        {
          "rowIndex": 1,
          "columnIndex": 1,
          "content": "100",
          "kind": "content"
        }
      ],
      "boundingRegions": [
        { "pageNumber": 1, "polygon": [1.0, 3.0, 7.5, 3.0, 7.5, 6.5, 1.0, 6.5] }
      ]
    }
  ]
}
```

### Key-Value Pair Extraction

For semi-structured documents, Content Understanding can extract key-value pairs:

```json
{
  "keyValuePairs": [
    {
      "key": { "content": "Invoice Number" },
      "value": { "content": "INV-2024-001" },
      "confidence": 0.95
    },
    {
      "key": { "content": "Date" },
      "value": { "content": "March 15, 2024" },
      "confidence": 0.93
    }
  ]
}
```

### Image and Figure Extraction

Content Understanding can identify and extract embedded images and figures from documents:

- **Photographs** — Embedded photos within reports
- **Charts and graphs** — Bar charts, pie charts, line graphs
- **Diagrams** — Flow charts, architecture diagrams
- **Logos** — Company logos and watermarks
- **Signatures** — Signature blocks and handwritten signatures

> **EXAM TIP:** Content Understanding extracts entities using an AI-driven approach with a flexible schema you define, while Document Intelligence uses prebuilt models with **fixed, known field schemas** (e.g., "VendorName" on invoices). If you need to extract custom entities from arbitrary documents without training a model, Content Understanding's schema-based approach is more flexible.

---

## 6. Processing Video and Audio

One of Content Understanding's key differentiators is its ability to process multimedia content—video and audio files—alongside documents.

### Video Content Analysis

Content Understanding can analyze video content to extract:

| Capability | Description |
|-----------|-------------|
| **Keyframe extraction** | Identifies the most representative frames from scenes |
| **Scene detection** | Segments video into distinct scenes based on visual changes |
| **Transcript generation** | Extracts spoken text from video audio tracks |
| **Visual text extraction** | OCR on text visible in video frames (signs, captions, slides) |
| **Content summarization** | Generates a summary of the video's content |

#### Video Analyzer Configuration

```http
PUT https://{endpoint}/contentunderstanding/analyzers/{analyzerName}?api-version=2024-12-01-preview
Content-Type: application/json
Ocp-Apim-Subscription-Key: {key}

{
  "description": "Video content analyzer",
  "scenario": "video",
  "fieldSchema": {
    "fields": {
      "summary": {
        "type": "string",
        "method": "generate",
        "description": "A concise summary of the video content"
      },
      "topics": {
        "type": "array",
        "items": { "type": "string" },
        "method": "generate",
        "description": "Main topics discussed in the video"
      },
      "speakers": {
        "type": "array",
        "items": { "type": "string" },
        "method": "extract",
        "description": "Names of speakers identified in the video"
      }
    }
  }
}
```

### Audio Processing

Content Understanding processes audio content to extract:

| Capability | Description |
|-----------|-------------|
| **Transcription** | Converts spoken language to text |
| **Speaker diarization** | Identifies and labels different speakers |
| **Language detection** | Identifies the spoken language(s) |
| **Content summarization** | Generates a summary of the audio content |
| **Entity extraction** | Identifies named entities from the transcript |

#### Audio Analyzer Configuration

```http
PUT https://{endpoint}/contentunderstanding/analyzers/{analyzerName}?api-version=2024-12-01-preview
Content-Type: application/json
Ocp-Apim-Subscription-Key: {key}

{
  "description": "Audio content analyzer",
  "scenario": "audio",
  "fieldSchema": {
    "fields": {
      "transcript": {
        "type": "string",
        "method": "extract",
        "description": "Full transcript of the audio content"
      },
      "summary": {
        "type": "string",
        "method": "generate",
        "description": "A concise summary of the audio content"
      },
      "actionItems": {
        "type": "array",
        "items": { "type": "string" },
        "method": "generate",
        "description": "Action items mentioned in the conversation"
      }
    }
  }
}
```

### Multimodal Content Understanding

Content Understanding can combine analysis across modalities:

- **Video with slides** — Extract both spoken words and on-screen text from presentation recordings
- **Training videos** — Generate summaries combining visual demonstrations and narration
- **Meeting recordings** — Transcribe audio, extract action items, and capture whiteboard content

#### Submitting Content for Analysis

```http
POST https://{endpoint}/contentunderstanding/analyzers/{analyzerName}:analyze?api-version=2024-12-01-preview
Content-Type: application/json
Ocp-Apim-Subscription-Key: {key}

{
  "url": "https://storage.blob.core.windows.net/media/training-video.mp4"
}
```

**Response (polling pattern, similar to Document Intelligence):**

```http
HTTP/1.1 202 Accepted
Operation-Location: https://{endpoint}/contentunderstanding/analyzers/{analyzerName}/results/{resultId}?api-version=2024-12-01-preview
```

```http
GET https://{endpoint}/contentunderstanding/analyzers/{analyzerName}/results/{resultId}?api-version=2024-12-01-preview
Ocp-Apim-Subscription-Key: {key}
```

```json
{
  "status": "succeeded",
  "result": {
    "analyzerId": "video-analyzer",
    "contentType": "video",
    "contents": [
      {
        "markdown": "## Video Transcript\n\nSpeaker 1: Welcome to today's training...",
        "fields": {
          "summary": {
            "type": "string",
            "valueString": "A training video covering Azure AI services, including Document Intelligence and Content Understanding."
          },
          "topics": {
            "type": "array",
            "valueArray": [
              { "type": "string", "valueString": "Azure AI services" },
              { "type": "string", "valueString": "Document Intelligence" },
              { "type": "string", "valueString": "Content Understanding" }
            ]
          },
          "speakers": {
            "type": "array",
            "valueArray": [
              { "type": "string", "valueString": "Dr. Jane Smith" }
            ]
          }
        }
      }
    ]
  }
}
```

> **EXAM TIP:** Content Understanding is the **only** Azure AI service in the AI-102 scope that provides **unified video and audio processing** alongside document analysis. If a question mentions processing video or audio content for text extraction, summarization, or entity extraction, Content Understanding is the answer.

---

## 7. When to Use Which Service

Choosing the right service is a critical exam skill. Here is a comprehensive comparison:

### Detailed Comparison Table

| Feature | Content Understanding | Document Intelligence | AI Vision (OCR/Read) | AI Language |
|---------|----------------------|----------------------|---------------------|-------------|
| **Text extraction (OCR)** | ✅ | ✅ | ✅ | ❌ |
| **Handwriting recognition** | ✅ | ✅ | ✅ | ❌ |
| **Table extraction** | ✅ | ✅ | ❌ | ❌ |
| **Form field extraction** | ✅ (custom schema) | ✅ (prebuilt + custom) | ❌ | ❌ |
| **Prebuilt document models** | ❌ | ✅ (invoice, receipt, ID, etc.) | ❌ | ❌ |
| **Custom trained models** | ✅ (schema-driven) | ✅ (template + neural) | ❌ | ✅ (NER) |
| **Composed models** | ❌ | ✅ (up to 200 models) | ❌ | ❌ |
| **Document classification** | ✅ | ✅ (classifier model) | ❌ | ✅ (text classification) |
| **Document summarization** | ✅ | ❌ | ❌ | ✅ (text summarization) |
| **Entity extraction** | ✅ | ❌ | ❌ | ✅ (NER) |
| **Video processing** | ✅ | ❌ | ✅ (frame analysis) | ❌ |
| **Audio processing** | ✅ | ❌ | ❌ | ❌ |
| **Speaker diarization** | ✅ | ❌ | ❌ | ❌ |
| **Multimodal analysis** | ✅ | ❌ | Partial | ❌ |
| **Knowledge store integration** | Via AI Search | Via AI Search | Via AI Search | Via AI Search |

### Decision Guide

| Scenario | Recommended Service | Reason |
|----------|-------------------|--------|
| Extract invoice fields (vendor, total, line items) | **Document Intelligence** | Prebuilt invoice model with known field schema |
| Extract receipt details for expense reports | **Document Intelligence** | Prebuilt receipt model |
| Verify identity from passport/driver's license | **Document Intelligence** | Prebuilt ID document model |
| Summarize a 50-page legal contract | **Content Understanding** | Document summarization capability |
| Classify incoming mail into categories | **Content Understanding** | Document classification without training |
| Extract text from a photograph of a sign | **AI Vision Read API** | Simple, fast OCR for images |
| Transcribe and summarize a meeting recording | **Content Understanding** | Audio transcription + summarization |
| Process video lectures for searchable transcripts | **Content Understanding** | Video transcription + entity extraction |
| Build a composed model for mixed document types | **Document Intelligence** | Composed model with automatic routing |
| Extract entities from plain text (not a document) | **AI Language** | NER on text input |
| Extract data from forms with a fixed layout | **Document Intelligence** | Template custom model for fixed layouts |
| Analyze documents of varying format without training | **Content Understanding** | Schema-driven extraction, no labeling required |

> **EXAM TIP:** The exam will present scenarios where you must choose between these services. Remember: **Document Intelligence** is best for structured forms with known fields. **Content Understanding** is best for summarization, classification, and multimedia. **AI Vision Read** is best for simple image OCR. **AI Language** is best for text-only NLP tasks.

---

## 8. Code Examples

### Python: Analyze a Document with Content Understanding

```python
import requests
import time

endpoint = "https://my-content-understanding.cognitiveservices.azure.com"
api_key = "<your-key>"
analyzer_name = "document-analyzer"
api_version = "2024-12-01-preview"

# Step 1: Submit analysis request
analyze_url = f"{endpoint}/contentunderstanding/analyzers/{analyzer_name}:analyze?api-version={api_version}"

headers = {
    "Ocp-Apim-Subscription-Key": api_key,
    "Content-Type": "application/json"
}

body = {
    "url": "https://storage.blob.core.windows.net/documents/contract.pdf"
}

response = requests.post(analyze_url, headers=headers, json=body)
operation_url = response.headers["Operation-Location"]

# Step 2: Poll for results
while True:
    result_response = requests.get(operation_url, headers={"Ocp-Apim-Subscription-Key": api_key})
    result = result_response.json()

    if result["status"] == "succeeded":
        break
    elif result["status"] == "failed":
        print(f"Analysis failed: {result.get('error', 'Unknown error')}")
        break

    time.sleep(2)

# Step 3: Process results
if result["status"] == "succeeded":
    analysis = result["result"]
    for content in analysis["contents"]:
        print("--- Extracted Content ---")
        print(content.get("markdown", ""))

        fields = content.get("fields", {})
        for field_name, field_value in fields.items():
            print(f"{field_name}: {field_value.get('valueString', field_value.get('valueArray', 'N/A'))}")
```

### REST: Create an Analyzer

```http
PUT https://{endpoint}/contentunderstanding/analyzers/my-doc-analyzer?api-version=2024-12-01-preview
Content-Type: application/json
Ocp-Apim-Subscription-Key: {key}

{
  "description": "Comprehensive document analyzer",
  "scenario": "document",
  "fieldSchema": {
    "fields": {
      "documentType": {
        "type": "string",
        "method": "classify",
        "description": "Type of document",
        "enum": ["invoice", "contract", "report", "memo", "other"]
      },
      "summary": {
        "type": "string",
        "method": "generate",
        "description": "Brief summary of the document (2-3 sentences)"
      },
      "keyEntities": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": { "type": "string" },
            "type": { "type": "string" },
            "role": { "type": "string" }
          }
        },
        "method": "extract",
        "description": "Key people and organizations mentioned"
      },
      "importantDates": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "date": { "type": "string" },
            "description": { "type": "string" }
          }
        },
        "method": "extract",
        "description": "Important dates referenced in the document"
      }
    }
  }
}
```

### REST: Analyze Content and Retrieve Results

```http
POST https://{endpoint}/contentunderstanding/analyzers/my-doc-analyzer:analyze?api-version=2024-12-01-preview
Content-Type: application/json
Ocp-Apim-Subscription-Key: {key}

{
  "url": "https://storage.blob.core.windows.net/documents/quarterly-report.pdf"
}
```

**Poll and retrieve:**

```http
GET https://{endpoint}/contentunderstanding/analyzers/my-doc-analyzer/results/{resultId}?api-version=2024-12-01-preview
Ocp-Apim-Subscription-Key: {key}
```

**Response:**

```json
{
  "status": "succeeded",
  "result": {
    "analyzerId": "my-doc-analyzer",
    "contentType": "application/pdf",
    "contents": [
      {
        "markdown": "# Quarterly Report Q1 2024\n\n## Executive Summary\n\nRevenue increased by 15%...",
        "fields": {
          "documentType": {
            "type": "string",
            "valueString": "report"
          },
          "summary": {
            "type": "string",
            "valueString": "Q1 2024 quarterly report showing 15% revenue growth driven by cloud services expansion. Key initiatives include AI platform launch and European market entry."
          },
          "keyEntities": {
            "type": "array",
            "valueArray": [
              {
                "type": "object",
                "valueObject": {
                  "name": { "type": "string", "valueString": "Contoso Corp" },
                  "type": { "type": "string", "valueString": "Organization" },
                  "role": { "type": "string", "valueString": "Reporting company" }
                }
              }
            ]
          },
          "importantDates": {
            "type": "array",
            "valueArray": [
              {
                "type": "object",
                "valueObject": {
                  "date": { "type": "string", "valueString": "2024-03-31" },
                  "description": { "type": "string", "valueString": "End of Q1 reporting period" }
                }
              }
            ]
          }
        }
      }
    ]
  }
}
```

### Python: Process Video Content

```python
import requests
import time

endpoint = "https://my-content-understanding.cognitiveservices.azure.com"
api_key = "<your-key>"
analyzer_name = "video-analyzer"
api_version = "2024-12-01-preview"

# Submit video for analysis
analyze_url = f"{endpoint}/contentunderstanding/analyzers/{analyzer_name}:analyze?api-version={api_version}"

headers = {
    "Ocp-Apim-Subscription-Key": api_key,
    "Content-Type": "application/json"
}

body = {
    "url": "https://storage.blob.core.windows.net/media/training-session.mp4"
}

response = requests.post(analyze_url, headers=headers, json=body)
operation_url = response.headers["Operation-Location"]

# Poll for results (video analysis may take longer)
max_retries = 60
for i in range(max_retries):
    result_response = requests.get(
        operation_url,
        headers={"Ocp-Apim-Subscription-Key": api_key}
    )
    result = result_response.json()

    if result["status"] in ("succeeded", "failed"):
        break

    time.sleep(10)  # Video processing takes longer than documents

if result["status"] == "succeeded":
    analysis = result["result"]
    for content in analysis["contents"]:
        fields = content.get("fields", {})

        summary = fields.get("summary", {}).get("valueString", "N/A")
        print(f"Video Summary: {summary}")

        topics = fields.get("topics", {}).get("valueArray", [])
        print("Topics:")
        for topic in topics:
            print(f"  - {topic.get('valueString', 'N/A')}")

        speakers = fields.get("speakers", {}).get("valueArray", [])
        print("Speakers:")
        for speaker in speakers:
            print(f"  - {speaker.get('valueString', 'N/A')}")
```

---

## 9. Integration with Azure AI Search

Content Understanding can be integrated with Azure AI Search as a custom skill in an enrichment pipeline:

### Architecture

```
Data Source → Indexer → Skillset (Content Understanding skill) → Search Index
                                                              → Knowledge Store
```

### Custom Skill Integration

You can create an Azure Function that calls Content Understanding and expose it as a custom skill:

```python
import azure.functions as func
import requests
import time
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    values = req.get_json().get("values", [])
    results = []

    for record in values:
        record_id = record["recordId"]
        document_url = record["data"]["documentUrl"]

        # Call Content Understanding analyzer
        analysis_result = analyze_document(document_url)

        results.append({
            "recordId": record_id,
            "data": {
                "summary": analysis_result.get("summary", ""),
                "documentType": analysis_result.get("documentType", ""),
                "entities": analysis_result.get("entities", [])
            },
            "errors": [],
            "warnings": []
        })

    return func.HttpResponse(
        json.dumps({"values": results}),
        mimetype="application/json"
    )
```

> **EXAM TIP:** Content Understanding uses the same **async polling pattern** as Document Intelligence (POST to analyze → poll Operation-Location). If you see a question about processing multimedia content (video/audio) for search indexing, think Content Understanding as a custom skill in an AI Search enrichment pipeline.

---

## Key Takeaways

1. **Unified Service** — Content Understanding provides a single API for documents, images, video, and audio analysis. It unifies capabilities from multiple Azure AI services.

2. **Analyzer-Based Architecture** — Create an analyzer with a field schema, submit content, and retrieve structured results. The schema-driven approach is flexible and doesn't require training labeled data.

3. **OCR Excellence** — High-quality text extraction supporting handwritten and printed text, multi-language documents, and complex layouts. Comparable quality to Document Intelligence OCR.

4. **Summarization and Classification** — Unique capability among document-focused services. Generates extractive and abstractive summaries and classifies documents without training.

5. **Entity and Table Extraction** — Flexible schema-driven entity extraction. Detects and structures tables including complex, borderless, and cross-page tables.

6. **Multimedia Processing** — Video analysis (keyframes, scenes, transcription) and audio processing (transcription, speaker diarization) are key differentiators from Document Intelligence.

7. **Service Selection** — Use Document Intelligence for structured forms with prebuilt models. Use Content Understanding for summarization, classification, and multimedia. Use AI Vision Read API for simple image OCR.

8. **Preview Status** — Content Understanding is in public preview. APIs may change before GA.

9. **Integration** — Works with Azure AI Search as a custom skill for building enriched search indexes from multimedia content.

---

## Further Reading

- [Azure AI Content Understanding documentation](https://learn.microsoft.com/azure/ai-services/content-understanding/)
- [Content Understanding overview](https://learn.microsoft.com/azure/ai-services/content-understanding/overview)
- [Content Understanding quickstart](https://learn.microsoft.com/azure/ai-services/content-understanding/quickstart)
- [Analyzer concepts](https://learn.microsoft.com/azure/ai-services/content-understanding/concepts/analyzers)
- [Document Intelligence vs Content Understanding](https://learn.microsoft.com/azure/ai-services/document-intelligence/)
- [Azure AI Search custom skills](https://learn.microsoft.com/azure/search/cognitive-search-custom-skill-web-api)
