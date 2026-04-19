# Lesson 1: Analyze Images with Azure AI Vision

## Learning Objectives

After completing this lesson, you will be able to:

- Understand the Image Analysis 4.0 API and the Florence foundation model
- Configure endpoint authentication using subscription keys and Microsoft Entra ID
- Extract visual features including tags, captions, objects, people, and smart crops
- Perform optical character recognition (OCR) using the Read API
- Interpret JSON responses from Image Analysis calls
- Know image file limits and supported formats for the exam
- Write code to analyze images using both the Python SDK and REST API

---

## 1. Image Analysis 4.0 API Overview

### The Florence Foundation Model

Azure AI Vision 4.0 is powered by **Florence**, Microsoft's large-scale vision foundation model. Florence was trained on billions of image-text pairs and provides state-of-the-art performance across a wide range of visual tasks.

Key advantages of the Florence-based Image Analysis 4.0 API:

| Feature | Description |
|---------|-------------|
| **Unified API** | A single endpoint handles captions, tags, objects, OCR, people, and smart crops |
| **Improved accuracy** | Florence significantly outperforms older Computer Vision 3.2 models |
| **Dense captions** | Generate captions for multiple regions, not just the whole image |
| **Custom models** | Combine prebuilt features with custom-trained models in one call |
| **Caption generation** | Natural language captions powered by the Florence model |

> **EXAM TIP:** The AI-102 exam focuses on Image Analysis 4.0 (api-version `2024-02-01`). The older Computer Vision 3.2 API is being retired. Know the 4.0 visual features: `tags`, `caption`, `denseCaptions`, `objects`, `people`, `read`, `smartCrops`.

### Service Endpoint and Resource

To use the Image Analysis 4.0 API, you need an **Azure AI Vision** resource or a **multi-service Azure AI Services** resource.

The base endpoint format:

```
https://<your-resource-name>.cognitiveservices.azure.com
```

The full Image Analysis endpoint:

```
POST {endpoint}/computervision/imageanalysis:analyze?api-version=2024-02-01&features={features}
```

---

## 2. Authentication

### Subscription Key Authentication

Pass the key in the `Ocp-Apim-Subscription-Key` header:

```http
POST https://myresource.cognitiveservices.azure.com/computervision/imageanalysis:analyze?api-version=2024-02-01&features=caption,tags
Ocp-Apim-Subscription-Key: <your-key>
Content-Type: application/json

{
  "url": "https://example.com/image.jpg"
}
```

### Microsoft Entra ID (Azure AD) Authentication

Use a bearer token from `DefaultAzureCredential` or a service principal:

```http
POST https://myresource.cognitiveservices.azure.com/computervision/imageanalysis:analyze?api-version=2024-02-01&features=caption,tags
Authorization: Bearer <access-token>
Content-Type: application/json
```

> **EXAM TIP:** Both subscription key and Microsoft Entra ID authentication are supported. For production, Entra ID with managed identity is the recommended approach. The required scope for Entra ID is `https://cognitiveservices.azure.com/.default`.

---

## 3. Visual Features

The Image Analysis 4.0 API supports the following visual features, specified via the `features` query parameter:

| Feature | Description | Example Use Case |
|---------|-------------|-----------------|
| `caption` | A single natural language sentence describing the image | Alt text generation |
| `denseCaptions` | Captions for multiple regions within the image | Detailed image descriptions |
| `tags` | Keywords/labels for the image content | Content categorization |
| `objects` | Detected objects with bounding boxes | Object localization |
| `people` | Detected people with bounding boxes | People counting |
| `read` | Extracted text via OCR | Document digitization |
| `smartCrops` | Suggested crop regions that preserve content | Thumbnail generation |

### Specifying Features in API Calls

You can request multiple features in a single call by comma-separating them:

```
?features=caption,tags,objects,read
```

### Confidence Scores and Thresholds

Every result includes a **confidence score** between 0.0 and 1.0:

- **Tags**: Each tag has a confidence score; filter by threshold (e.g., > 0.7)
- **Caption**: The generated caption has a single confidence value
- **Objects**: Each detected object has a confidence score
- **People**: Each detected person has a confidence score

> **EXAM TIP:** The API does NOT automatically filter by confidence threshold. You must implement threshold filtering in your own code. The default is to return all results regardless of confidence.

---

## 4. Tags (Image Classification)

Tags represent keywords or labels that describe the content of an image. They are NOT localized — they describe what is **in** the image but not **where**.

### Request

```
GET /computervision/imageanalysis:analyze?features=tags&api-version=2024-02-01
```

### Response Structure

```json
{
  "tagsResult": {
    "values": [
      {
        "name": "outdoor",
        "confidence": 0.9876
      },
      {
        "name": "mountain",
        "confidence": 0.9542
      },
      {
        "name": "sky",
        "confidence": 0.9318
      },
      {
        "name": "snow",
        "confidence": 0.8901
      },
      {
        "name": "nature",
        "confidence": 0.8754
      }
    ]
  }
}
```

### Key Points

- Tags are returned in **descending order of confidence**
- Each tag has a `name` (string) and `confidence` (float 0–1)
- Tags cover objects, actions, scenery, and settings
- No bounding box information is provided — that's what `objects` is for

---

## 5. Image Descriptions (Captions)

### Caption vs Dense Captions

| Feature | `caption` | `denseCaptions` |
|---------|-----------|-----------------|
| **Output** | Single sentence describing the whole image | Multiple captions for different regions |
| **Count** | Always 1 caption | Multiple (controlled by `denseCaptions` settings) |
| **Bounding box** | No | Yes — each dense caption includes a bounding box |
| **Use case** | Alt text, simple description | Detailed accessibility, region-level descriptions |

### Caption Response

```json
{
  "captionResult": {
    "text": "a person hiking on a snowy mountain trail",
    "confidence": 0.8921
  }
}
```

### Dense Captions Response

```json
{
  "denseCaptionsResult": {
    "values": [
      {
        "text": "a person hiking on a snowy mountain trail",
        "confidence": 0.8921,
        "boundingBox": {
          "x": 0, "y": 0, "w": 800, "h": 600
        }
      },
      {
        "text": "a person wearing a red jacket and backpack",
        "confidence": 0.8456,
        "boundingBox": {
          "x": 200, "y": 100, "w": 200, "h": 350
        }
      },
      {
        "text": "snow-covered mountain peaks under a blue sky",
        "confidence": 0.8312,
        "boundingBox": {
          "x": 0, "y": 0, "w": 800, "h": 250
        }
      }
    ]
  }
}
```

> **EXAM TIP:** `caption` returns ONE sentence for the entire image. `denseCaptions` returns MULTIPLE captions each with a bounding box region. If a question asks about describing **regions** of an image, the answer is `denseCaptions`.

---

## 6. Object Detection

Object detection identifies objects in an image AND provides their **bounding box** coordinates for localization.

### Bounding Box Format

Each detected object includes:

| Field | Description |
|-------|-------------|
| `x` | Left edge of the bounding box (pixels from left) |
| `y` | Top edge of the bounding box (pixels from top) |
| `w` | Width of the bounding box in pixels |
| `h` | Height of the bounding box in pixels |

### Response Structure

```json
{
  "objectsResult": {
    "values": [
      {
        "boundingBox": {
          "x": 120,
          "y": 80,
          "w": 250,
          "h": 400
        },
        "tags": [
          {
            "name": "person",
            "confidence": 0.9654
          }
        ]
      },
      {
        "boundingBox": {
          "x": 450,
          "y": 200,
          "w": 100,
          "h": 150
        },
        "tags": [
          {
            "name": "backpack",
            "confidence": 0.8821
          }
        ]
      }
    ]
  }
}
```

### Tags vs Objects: Key Differences

| Aspect | Tags (`tags`) | Objects (`objects`) |
|--------|---------------|---------------------|
| **What it provides** | Keywords/labels for the whole image | Specific objects with bounding boxes |
| **Localization** | No — just labels | Yes — bounding box coordinates |
| **Granularity** | Broad concepts (outdoor, nature, sky) | Specific objects (person, car, dog) |
| **Use case** | Categorization, search indexing | Localization, counting, spatial analysis |

> **EXAM TIP:** If an exam question asks about *locating* or *finding where* an object is in an image, the answer is `objects` (not `tags`). Tags tell you **what** is in the image; objects tell you **what** and **where**.

---

## 7. People Detection

The `people` feature detects people in an image and returns bounding boxes. It is optimized for detecting people specifically and typically performs better than generic object detection for this purpose.

### Response Structure

```json
{
  "peopleResult": {
    "values": [
      {
        "boundingBox": {
          "x": 120,
          "y": 50,
          "w": 180,
          "h": 420
        },
        "confidence": 0.9812
      },
      {
        "boundingBox": {
          "x": 400,
          "y": 80,
          "w": 160,
          "h": 380
        },
        "confidence": 0.9543
      }
    ]
  }
}
```

> **EXAM TIP:** The `people` feature in Image Analysis 4.0 detects people with bounding boxes but does NOT identify or recognize who they are. For face identification, you need the separate **Face API** (which requires Limited Access approval).

---

## 8. Smart Crops

Smart cropping suggests optimal crop regions that preserve the most important content in the image, useful for generating thumbnails at specific aspect ratios.

### Request with Aspect Ratios

```
?features=smartCrops&smartcrops-aspect-ratios=1.0,1.5,0.75
```

### Response Structure

```json
{
  "smartCropsResult": {
    "values": [
      {
        "aspectRatio": 1.0,
        "boundingBox": {
          "x": 100, "y": 50, "w": 400, "h": 400
        }
      },
      {
        "aspectRatio": 1.5,
        "boundingBox": {
          "x": 50, "y": 80, "w": 600, "h": 400
        }
      }
    ]
  }
}
```

---

## 9. OCR / Read API

The **Read** feature (`read`) extracts printed and handwritten text from images using OCR (Optical Character Recognition).

### Synchronous vs Asynchronous Calls

| Mode | API | Use Case |
|------|-----|----------|
| **Synchronous** | Image Analysis 4.0 `?features=read` | Single images, quick results |
| **Asynchronous** | Legacy Read API (3.2) POST + GET | Large documents, multi-page PDFs |

In Image Analysis 4.0, the `read` feature is **synchronous** — results are returned in the same response.

> **EXAM TIP:** In the older Read API (3.2), you submit a POST request and then poll with GET until results are ready (async pattern). In Image Analysis 4.0 with `?features=read`, OCR is synchronous. Know both patterns for the exam.

### Response Structure: Pages → Lines → Words

The OCR response is hierarchical:

```
readResult
  └── pages[]
        ├── lines[]
        │     ├── text (full line text)
        │     ├── boundingPolygon (coordinates of the line)
        │     └── words[]
        │           ├── text (individual word)
        │           ├── boundingPolygon (coordinates of the word)
        │           └── confidence (float 0–1)
        └── words[] (flat list of all words on the page)
```

### Full OCR Response Example

```json
{
  "readResult": {
    "pages": [
      {
        "height": 1200,
        "width": 800,
        "angle": 0.0,
        "pageNumber": 1,
        "lines": [
          {
            "text": "Welcome to Azure AI",
            "boundingPolygon": [
              {"x": 50, "y": 30},
              {"x": 400, "y": 30},
              {"x": 400, "y": 70},
              {"x": 50, "y": 70}
            ],
            "words": [
              {
                "text": "Welcome",
                "boundingPolygon": [
                  {"x": 50, "y": 30},
                  {"x": 160, "y": 30},
                  {"x": 160, "y": 70},
                  {"x": 50, "y": 70}
                ],
                "confidence": 0.9921
              },
              {
                "text": "to",
                "boundingPolygon": [
                  {"x": 170, "y": 30},
                  {"x": 210, "y": 30},
                  {"x": 210, "y": 70},
                  {"x": 170, "y": 70}
                ],
                "confidence": 0.9987
              },
              {
                "text": "Azure",
                "boundingPolygon": [
                  {"x": 220, "y": 30},
                  {"x": 310, "y": 30},
                  {"x": 310, "y": 70},
                  {"x": 220, "y": 70}
                ],
                "confidence": 0.9945
              },
              {
                "text": "AI",
                "boundingPolygon": [
                  {"x": 320, "y": 30},
                  {"x": 360, "y": 30},
                  {"x": 360, "y": 70},
                  {"x": 320, "y": 70}
                ],
                "confidence": 0.9978
              }
            ]
          },
          {
            "text": "Vision Services",
            "boundingPolygon": [
              {"x": 50, "y": 90},
              {"x": 300, "y": 90},
              {"x": 300, "y": 130},
              {"x": 50, "y": 130}
            ],
            "words": [
              {
                "text": "Vision",
                "boundingPolygon": [
                  {"x": 50, "y": 90},
                  {"x": 150, "y": 90},
                  {"x": 150, "y": 130},
                  {"x": 50, "y": 130}
                ],
                "confidence": 0.9912
              },
              {
                "text": "Services",
                "boundingPolygon": [
                  {"x": 160, "y": 90},
                  {"x": 300, "y": 90},
                  {"x": 300, "y": 130},
                  {"x": 160, "y": 130}
                ],
                "confidence": 0.9876
              }
            ]
          }
        ]
      }
    ]
  }
}
```

### Language Support

The Read API supports **over 160 languages** for printed text and a subset for handwritten text. Common supported languages include English, Chinese, Japanese, Korean, French, German, Spanish, Portuguese, Italian, Dutch, and Arabic.

To specify a language:

```
?features=read&language=en
```

> **EXAM TIP:** The Read API supports both **printed** and **handwritten** text. Handwritten text support is available for a subset of languages (primarily English). Know that the response hierarchy is **pages → lines → words**.

---

## 10. File Limits and Requirements

| Constraint | Value |
|------------|-------|
| **Maximum file size** | 4 MB |
| **Minimum dimensions** | 50 × 50 pixels |
| **Maximum dimensions** | 16,000 × 16,000 pixels |
| **Supported formats** | JPEG, PNG, GIF, BMP, WEBP, ICO, TIFF |
| **Input methods** | URL (JSON body) or binary upload (octet-stream) |

### URL Input

```json
{
  "url": "https://example.com/image.jpg"
}
```

Content-Type: `application/json`

### Binary Upload

Send the raw image bytes directly in the request body.

Content-Type: `application/octet-stream`

> **EXAM TIP:** Know the file limits: **4 MB max**, dimensions between **50×50** and **16,000×16,000**. If a question mentions an image larger than 4 MB or smaller than 50×50, it will fail. Supported formats: JPEG, PNG, GIF, BMP, WEBP, ICO, TIFF.

---

## 11. Code Examples

### Python SDK: Analyze Image for Tags and Captions

**Install the SDK:**

```bash
pip install azure-ai-vision-imageanalysis
```

**Analyze an image:**

```python
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

# Create client
endpoint = "https://myresource.cognitiveservices.azure.com"
key = "your-subscription-key"
client = ImageAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Analyze image from URL
result = client.analyze_from_url(
    image_url="https://example.com/mountain.jpg",
    visual_features=[
        VisualFeatures.CAPTION,
        VisualFeatures.TAGS,
        VisualFeatures.OBJECTS,
        VisualFeatures.PEOPLE,
        VisualFeatures.READ
    ]
)

# --- Caption ---
if result.caption is not None:
    print(f"Caption: '{result.caption.text}' "
          f"(confidence: {result.caption.confidence:.4f})")

# --- Tags ---
if result.tags is not None:
    print("Tags:")
    for tag in result.tags.list:
        print(f"  '{tag.name}' (confidence: {tag.confidence:.4f})")

# --- Objects ---
if result.objects is not None:
    print("Objects:")
    for obj in result.objects.list:
        print(f"  '{obj.tags[0].name}' at "
              f"[x={obj.bounding_box.x}, y={obj.bounding_box.y}, "
              f"w={obj.bounding_box.width}, h={obj.bounding_box.height}] "
              f"(confidence: {obj.tags[0].confidence:.4f})")

# --- People ---
if result.people is not None:
    print(f"People detected: {len(result.people.list)}")
    for person in result.people.list:
        print(f"  Person at "
              f"[x={person.bounding_box.x}, y={person.bounding_box.y}, "
              f"w={person.bounding_box.width}, h={person.bounding_box.height}] "
              f"(confidence: {person.confidence:.4f})")

# --- Read / OCR ---
if result.read is not None:
    print("Text:")
    for page in result.read.pages:
        for line in page.lines:
            print(f"  Line: '{line.text}'")
            for word in line.words:
                print(f"    Word: '{word.text}' "
                      f"(confidence: {word.confidence:.4f})")
```

### Python SDK with Entra ID Authentication

```python
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.identity import DefaultAzureCredential

endpoint = "https://myresource.cognitiveservices.azure.com"
client = ImageAnalysisClient(
    endpoint=endpoint,
    credential=DefaultAzureCredential()
)

result = client.analyze_from_url(
    image_url="https://example.com/photo.jpg",
    visual_features=[VisualFeatures.CAPTION, VisualFeatures.TAGS]
)

print(f"Caption: {result.caption.text}")
```

### Python SDK: Analyze Local Image File

```python
with open("local-image.jpg", "rb") as image_file:
    image_data = image_file.read()

result = client.analyze(
    image_data=image_data,
    visual_features=[
        VisualFeatures.CAPTION,
        VisualFeatures.TAGS,
        VisualFeatures.OBJECTS
    ]
)
```

### REST API: Analyze Image for Tags and Captions

```http
POST https://myresource.cognitiveservices.azure.com/computervision/imageanalysis:analyze?api-version=2024-02-01&features=caption,tags
Ocp-Apim-Subscription-Key: <your-key>
Content-Type: application/json

{
  "url": "https://example.com/mountain.jpg"
}
```

**Response:**

```json
{
  "captionResult": {
    "text": "a person hiking on a snowy mountain trail",
    "confidence": 0.8921
  },
  "tagsResult": {
    "values": [
      {"name": "outdoor", "confidence": 0.9876},
      {"name": "mountain", "confidence": 0.9542},
      {"name": "snow", "confidence": 0.8901},
      {"name": "person", "confidence": 0.8654},
      {"name": "hiking", "confidence": 0.7823}
    ]
  }
}
```

### REST API: Object Detection

```http
POST https://myresource.cognitiveservices.azure.com/computervision/imageanalysis:analyze?api-version=2024-02-01&features=objects
Ocp-Apim-Subscription-Key: <your-key>
Content-Type: application/json

{
  "url": "https://example.com/street-scene.jpg"
}
```

**Response:**

```json
{
  "objectsResult": {
    "values": [
      {
        "boundingBox": {"x": 50, "y": 100, "w": 200, "h": 350},
        "tags": [{"name": "person", "confidence": 0.9712}]
      },
      {
        "boundingBox": {"x": 400, "y": 150, "w": 300, "h": 200},
        "tags": [{"name": "car", "confidence": 0.9534}]
      },
      {
        "boundingBox": {"x": 350, "y": 50, "w": 50, "h": 80},
        "tags": [{"name": "traffic light", "confidence": 0.8876}]
      }
    ]
  }
}
```

### REST API: OCR / Read Text Extraction

```http
POST https://myresource.cognitiveservices.azure.com/computervision/imageanalysis:analyze?api-version=2024-02-01&features=read&language=en
Ocp-Apim-Subscription-Key: <your-key>
Content-Type: application/json

{
  "url": "https://example.com/document.jpg"
}
```

### REST API: Binary Image Upload

```bash
curl -X POST "https://myresource.cognitiveservices.azure.com/computervision/imageanalysis:analyze?api-version=2024-02-01&features=caption,tags" \
  -H "Ocp-Apim-Subscription-Key: <your-key>" \
  -H "Content-Type: application/octet-stream" \
  --data-binary @local-image.jpg
```

### Python: REST API with `requests`

```python
import requests
import json

endpoint = "https://myresource.cognitiveservices.azure.com"
key = "your-subscription-key"

analyze_url = (
    f"{endpoint}/computervision/imageanalysis:analyze"
    f"?api-version=2024-02-01&features=caption,tags,objects,read"
)

headers = {
    "Ocp-Apim-Subscription-Key": key,
    "Content-Type": "application/json"
}

body = {
    "url": "https://example.com/mountain.jpg"
}

response = requests.post(analyze_url, headers=headers, json=body)
response.raise_for_status()
result = response.json()

# Parse caption
caption = result.get("captionResult", {})
print(f"Caption: {caption.get('text')} "
      f"(confidence: {caption.get('confidence', 0):.4f})")

# Parse tags
tags = result.get("tagsResult", {}).get("values", [])
for tag in tags:
    print(f"Tag: {tag['name']} (confidence: {tag['confidence']:.4f})")

# Parse objects
objects = result.get("objectsResult", {}).get("values", [])
for obj in objects:
    box = obj["boundingBox"]
    tag_name = obj["tags"][0]["name"]
    confidence = obj["tags"][0]["confidence"]
    print(f"Object: {tag_name} at [{box['x']},{box['y']},{box['w']},{box['h']}] "
          f"(confidence: {confidence:.4f})")

# Parse OCR text
read_result = result.get("readResult", {})
for page in read_result.get("pages", []):
    for line in page.get("lines", []):
        print(f"Line: {line['text']}")
```

---

## 12. Full Annotated Response Example

Here is a complete response when requesting all major features:

```http
POST /computervision/imageanalysis:analyze?api-version=2024-02-01&features=caption,denseCaptions,tags,objects,people,read,smartCrops&smartcrops-aspect-ratios=1.0
```

```json
{
  "modelVersion": "2024-02-01",
  "metadata": {
    "width": 800,
    "height": 600
  },
  "captionResult": {
    "text": "a person sitting at a desk working on a laptop",
    "confidence": 0.9102
  },
  "denseCaptionsResult": {
    "values": [
      {
        "text": "a person sitting at a desk working on a laptop",
        "confidence": 0.9102,
        "boundingBox": {"x": 0, "y": 0, "w": 800, "h": 600}
      },
      {
        "text": "a silver laptop on a wooden desk",
        "confidence": 0.8654,
        "boundingBox": {"x": 200, "y": 250, "w": 350, "h": 250}
      }
    ]
  },
  "tagsResult": {
    "values": [
      {"name": "person", "confidence": 0.9876},
      {"name": "computer", "confidence": 0.9654},
      {"name": "laptop", "confidence": 0.9543},
      {"name": "indoor", "confidence": 0.9321},
      {"name": "desk", "confidence": 0.8987}
    ]
  },
  "objectsResult": {
    "values": [
      {
        "boundingBox": {"x": 100, "y": 50, "w": 300, "h": 450},
        "tags": [{"name": "person", "confidence": 0.9712}]
      },
      {
        "boundingBox": {"x": 200, "y": 280, "w": 350, "h": 220},
        "tags": [{"name": "laptop", "confidence": 0.9534}]
      }
    ]
  },
  "peopleResult": {
    "values": [
      {
        "boundingBox": {"x": 100, "y": 50, "w": 300, "h": 450},
        "confidence": 0.9812
      }
    ]
  },
  "readResult": {
    "pages": [
      {
        "height": 600,
        "width": 800,
        "angle": 0.0,
        "pageNumber": 1,
        "lines": [
          {
            "text": "Azure AI Vision",
            "boundingPolygon": [
              {"x": 250, "y": 310}, {"x": 500, "y": 310},
              {"x": 500, "y": 340}, {"x": 250, "y": 340}
            ],
            "words": [
              {"text": "Azure", "confidence": 0.9912,
               "boundingPolygon": [{"x":250,"y":310},{"x":320,"y":310},{"x":320,"y":340},{"x":250,"y":340}]},
              {"text": "AI", "confidence": 0.9978,
               "boundingPolygon": [{"x":330,"y":310},{"x":370,"y":310},{"x":370,"y":340},{"x":330,"y":340}]},
              {"text": "Vision", "confidence": 0.9945,
               "boundingPolygon": [{"x":380,"y":310},{"x":500,"y":310},{"x":500,"y":340},{"x":380,"y":340}]}
            ]
          }
        ]
      }
    ]
  },
  "smartCropsResult": {
    "values": [
      {
        "aspectRatio": 1.0,
        "boundingBox": {"x": 100, "y": 50, "w": 450, "h": 450}
      }
    ]
  }
}
```

---

## 13. Background Removal (Deprecated Note)

The Image Analysis 4.0 API previously included a **background removal / foreground matting** feature. This feature has been deprecated as of early 2025.

> **EXAM TIP:** If you see references to background removal in older study materials, be aware it was deprecated. It is unlikely to appear on current exams, but if it does, know it was a feature of Image Analysis 4.0 that generated a foreground matte or removed the background.

---

## 14. Microsoft Documentation

| Resource | Link |
|----------|------|
| Image Analysis overview | [Docs](https://learn.microsoft.com/azure/ai-services/computer-vision/overview-image-analysis) |
| Image Analysis 4.0 quickstart | [Docs](https://learn.microsoft.com/azure/ai-services/computer-vision/quickstarts-sdk/image-analysis-client-library-40) |
| Image Analysis REST API reference | [Docs](https://learn.microsoft.com/rest/api/computervision/image-analysis/analyze-image) |
| Python SDK reference | [Docs](https://learn.microsoft.com/python/api/azure-ai-vision-imageanalysis/) |
| Supported languages for OCR | [Docs](https://learn.microsoft.com/azure/ai-services/computer-vision/language-support) |

---

## Key Takeaways

1. **Image Analysis 4.0** is powered by the Florence foundation model and provides a unified API for captions, tags, objects, people detection, OCR, and smart crops.

2. **Visual features** are specified via the `features` query parameter — you can request multiple in a single call (e.g., `?features=caption,tags,objects,read`).

3. **Tags** classify the image content (no location); **objects** localize detected items with bounding boxes (`x`, `y`, `w`, `h`).

4. **Caption** gives one sentence for the whole image; **denseCaptions** give multiple captions with bounding boxes for regions.

5. **OCR (Read)** extracts text in a hierarchical structure: **pages → lines → words**, each with bounding polygons and confidence scores.

6. **File limits**: max **4 MB**, dimensions **50×50 to 16,000×16,000**, formats JPEG/PNG/GIF/BMP/WEBP/ICO/TIFF.

7. **Authentication** supports both subscription keys (`Ocp-Apim-Subscription-Key` header) and Microsoft Entra ID (bearer token). Entra ID with managed identity is recommended for production.

---

[← Back to Module Overview](overview.md) | [Next: Custom Vision →](lesson-2-custom-vision.md)
