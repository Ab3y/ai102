# Lesson 3: Video Analysis — Video Indexer, Spatial Analysis, and Face API

## Learning Objectives

After completing this lesson, you will be able to:

- Describe Azure AI Video Indexer capabilities and architecture
- Differentiate between ARM-connected and classic Video Indexer accounts
- Upload and index videos using the Video Indexer portal and API
- Extract insights from video including transcripts, topics, faces, emotions, and brands
- Embed Video Indexer widgets in custom applications
- Implement spatial analysis for people counting and movement tracking
- Use the Face API for detection, identification, and verification
- Understand Responsible AI restrictions and the Limited Access policy for facial recognition

---

## 1. Azure AI Video Indexer Overview

Azure AI Video Indexer is an AI-powered service that extracts deep insights from video and audio content. It combines multiple Azure AI services (Speech, Language, Vision) into a single unified indexing pipeline.

### Capabilities

Video Indexer extracts the following insights from video content:

| Category | Insights |
|----------|----------|
| **Audio/Speech** | Transcript, language detection, speaker identification (diarization), audio effects |
| **Text/NLP** | Keywords, topics, named entities, sentiment, key phrases, text-based emotion |
| **Visual** | Face detection, celebrity recognition, OCR (on-screen text), labels, scene/shot detection, keyframe extraction |
| **Content** | Brands (visual + audio mentions), content moderation |
| **Structural** | Scene segmentation, shot detection, keyframe selection, black frame detection |
| **Metadata** | Thumbnail generation, observed people, matched person, detected clothing |

### What Makes Video Indexer Different

| Feature | Video Indexer | Custom Solution |
|---------|--------------|-----------------|
| **Multi-modal** | Audio + video + text combined | Must integrate separate services |
| **Pre-built models** | Ready to use, no training | Requires training for each model |
| **Timeline correlation** | All insights mapped to timestamps | Must build correlation logic |
| **Portal + API** | Visual portal for exploration, API for automation | API only |
| **Widgets** | Embeddable player, insights, and editor widgets | Must build custom UI |

---

## 2. Account Types

### ARM-Connected Accounts (Recommended)

ARM (Azure Resource Manager) connected accounts are the modern standard:

| Aspect | Details |
|--------|---------|
| **Management** | Managed as an Azure resource (ARM) |
| **Billing** | Standard Azure billing |
| **RBAC** | Azure role-based access control |
| **Networking** | Virtual network and private endpoint support |
| **Scale** | Enterprise-grade SLAs |
| **Integration** | Connected to Azure AI Services for enhanced models |

### Classic Accounts (Legacy)

| Aspect | Details |
|--------|---------|
| **Management** | Standalone, not an Azure resource |
| **Billing** | Separate billing model |
| **RBAC** | API key-based access only |
| **Limitation** | Being deprecated; migrate to ARM-connected |

> **EXAM TIP:** ARM-connected accounts are the recommended account type. Classic accounts are legacy and being deprecated. For the exam, know that ARM-connected accounts support Azure RBAC, virtual networks, and are managed through the Azure portal like any other Azure resource.

### Connecting to Azure AI Services

An ARM-connected Video Indexer account can be linked to an Azure AI Services resource to unlock enhanced capabilities:

- Improved speech-to-text accuracy
- More language support
- Custom speech models
- Increased scale

---

## 3. Video Indexer Portal

The Video Indexer portal provides a no-code interface for uploading, indexing, and exploring video insights.

**Portal URL:** [https://www.videoindexer.ai](https://www.videoindexer.ai)

### Portal Workflow

1. **Upload** a video file or provide a URL
2. **Configure** indexing options (source language, privacy, streaming preset)
3. **Wait** for indexing to complete
4. **Explore** insights in the visual timeline

### Indexing Options

| Option | Description |
|--------|-------------|
| **Source language** | Language of the audio (auto-detect or specify) |
| **Privacy** | Private (only you) or Public (anyone with link) |
| **Streaming preset** | Encoding quality for playback |
| **Video indexing preset** | Default, Audio only, Video only, Advanced audio, Advanced video, Advanced audio + video, Basic audio, Basic video |
| **People model** | Custom people model for face identification |
| **Brands model** | Custom brands model for brand detection |
| **Custom language model** | Custom language model for transcription |

---

## 4. Video Indexer API

The Video Indexer API allows programmatic access to all indexing capabilities.

### API Authentication

Video Indexer uses **access tokens** for API authentication:

1. **Account-level access token**: Full access to the account
2. **Video-level access token**: Access to a specific video only
3. Token types: Reader, Contributor, Owner

### Getting an Access Token

```http
POST https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VideoIndexer/accounts/{accountName}/generateAccessToken?api-version=2024-01-01
Authorization: Bearer <ARM-token>
Content-Type: application/json

{
  "permissionType": "Contributor",
  "scope": "Account"
}
```

Response:

```json
{
  "accessToken": "eyJ0eXAiOiJK..."
}
```

### Upload and Index a Video

```http
POST https://api.videoindexer.ai/{location}/Accounts/{accountId}/Videos?name={videoName}&accessToken={accessToken}
Content-Type: multipart/form-data

<video file binary>
```

Or provide a URL:

```http
POST https://api.videoindexer.ai/{location}/Accounts/{accountId}/Videos?name={videoName}&videoUrl={encodedUrl}&accessToken={accessToken}
```

### Query Parameters for Upload

| Parameter | Description |
|-----------|-------------|
| `name` | Display name for the video |
| `videoUrl` | URL to the video file (alternative to upload) |
| `language` | Source language (e.g., `en-US`, `auto`) |
| `privacy` | `Private` or `Public` |
| `indexingPreset` | `Default`, `AudioOnly`, `VideoOnly`, `AdvancedAudio`, `AdvancedVideo` |
| `sendSuccessEmail` | Send email when indexing completes |
| `callbackUrl` | Webhook URL for completion notification |

### Get Video Index (Insights)

```http
GET https://api.videoindexer.ai/{location}/Accounts/{accountId}/Videos/{videoId}/Index?accessToken={accessToken}
```

### Python: Upload and Get Insights

```python
import requests
import time

account_id = "your-account-id"
location = "trial"  # or your Azure region
access_token = "your-access-token"
api_url = "https://api.videoindexer.ai"

# ============================================================
# Step 1: Upload a video
# ============================================================
upload_url = (
    f"{api_url}/{location}/Accounts/{account_id}/Videos"
    f"?name=SampleVideo"
    f"&privacy=Private"
    f"&language=en-US"
    f"&accessToken={access_token}"
)

# Upload from URL
params = {"videoUrl": "https://example.com/video.mp4"}
response = requests.post(upload_url, params=params)
response.raise_for_status()
video_id = response.json()["id"]
print(f"Video uploaded. ID: {video_id}")

# ============================================================
# Step 2: Wait for indexing to complete
# ============================================================
while True:
    index_url = (
        f"{api_url}/{location}/Accounts/{account_id}"
        f"/Videos/{video_id}/Index"
        f"?accessToken={access_token}"
    )
    response = requests.get(index_url)
    result = response.json()
    state = result.get("state")
    print(f"Indexing state: {state}")

    if state == "Processed":
        break
    elif state == "Failed":
        print("Indexing failed!")
        break

    time.sleep(30)

# ============================================================
# Step 3: Extract insights
# ============================================================
insights = result.get("videos", [{}])[0].get("insights", {})

# Transcript
transcript = insights.get("transcript", [])
for entry in transcript:
    text = entry.get("text", "")
    start = entry["instances"][0]["start"] if entry.get("instances") else ""
    print(f"[{start}] {text}")

# Topics
topics = insights.get("topics", [])
for topic in topics:
    print(f"Topic: {topic['name']} "
          f"(confidence: {topic.get('confidence', 0):.2f})")

# Keywords
keywords = insights.get("keywords", [])
for kw in keywords:
    print(f"Keyword: {kw['name']}")

# Faces
faces = insights.get("faces", [])
for face in faces:
    print(f"Face: {face.get('name', 'Unknown')} "
          f"(appearances: {len(face.get('instances', []))})")

# Sentiments
sentiments = insights.get("sentiments", [])
for sentiment in sentiments:
    print(f"Sentiment: {sentiment['sentimentType']} "
          f"(avg score: {sentiment.get('averageScore', 0):.2f})")

# Labels (visual)
labels = insights.get("labels", [])
for label in labels:
    print(f"Label: {label['name']}")

# Brands
brands = insights.get("brands", [])
for brand in brands:
    print(f"Brand: {brand['name']} "
          f"(type: {brand.get('referenceType', 'N/A')})")

# Named entities
named_entities = insights.get("namedPeople", [])
for entity in named_entities:
    print(f"Named person: {entity['name']}")

# OCR (on-screen text)
ocr = insights.get("ocr", [])
for text_block in ocr:
    print(f"OCR: {text_block['text']}")
```

### File Limits

| Constraint | Value |
|------------|-------|
| **Maximum file size** | 2 GB |
| **Maximum video duration** | 4 hours |
| **Supported formats** | MP4, MOV, WMV, AVI, MKV, FLV, ASF, M4V, MPEG, MPG, TS, 3GP, WebM |
| **Maximum concurrent uploads** | 4 per account |

> **EXAM TIP:** Video Indexer limits: **2 GB** max file size and **4 hours** max duration. Compare with Image Analysis which is **4 MB** max. Supported video formats include MP4, MOV, WMV, AVI, MKV, and FLV.

---

## 5. Video Indexer Insights JSON Structure

The insights JSON contains hierarchical data mapped to timestamps:

```json
{
  "videos": [
    {
      "insights": {
        "transcript": [
          {
            "id": 1,
            "text": "Welcome to our product demo.",
            "confidence": 0.95,
            "speakerId": 1,
            "language": "en-US",
            "instances": [
              {
                "start": "0:00:01.500",
                "end": "0:00:04.200"
              }
            ]
          }
        ],
        "topics": [
          {
            "id": 1,
            "name": "Technology",
            "referenceUrl": "https://en.wikipedia.org/wiki/Technology",
            "confidence": 0.87,
            "instances": [
              {"start": "0:00:00", "end": "0:02:30"}
            ]
          }
        ],
        "keywords": [
          {
            "id": 1,
            "name": "artificial intelligence",
            "instances": [
              {"start": "0:00:15", "end": "0:00:18"}
            ]
          }
        ],
        "faces": [
          {
            "id": 1,
            "name": "Speaker 1",
            "confidence": 0.92,
            "thumbnailId": "thumb-001",
            "instances": [
              {"start": "0:00:01", "end": "0:01:30"}
            ]
          }
        ],
        "labels": [
          {
            "id": 1,
            "name": "computer",
            "instances": [
              {
                "confidence": 0.88,
                "start": "0:00:05",
                "end": "0:00:30"
              }
            ]
          }
        ],
        "scenes": [
          {
            "id": 1,
            "instances": [
              {"start": "0:00:00", "end": "0:01:15"}
            ]
          }
        ],
        "shots": [
          {
            "id": 1,
            "keyFrames": [
              {
                "id": 1,
                "instances": [
                  {"start": "0:00:00", "end": "0:00:00"}
                ]
              }
            ],
            "instances": [
              {"start": "0:00:00", "end": "0:00:08"}
            ]
          }
        ],
        "sentiments": [
          {
            "id": 1,
            "sentimentType": "Positive",
            "averageScore": 0.78,
            "instances": [
              {"start": "0:00:00", "end": "0:01:00"}
            ]
          }
        ],
        "emotions": [
          {
            "id": 1,
            "type": "Joy",
            "instances": [
              {"start": "0:00:30", "end": "0:00:45"}
            ]
          }
        ],
        "brands": [
          {
            "id": 1,
            "name": "Microsoft",
            "referenceType": "Wiki",
            "referenceUrl": "https://en.wikipedia.org/wiki/Microsoft",
            "confidence": 0.95,
            "instances": [
              {"start": "0:00:20", "end": "0:00:25"}
            ]
          }
        ],
        "ocr": [
          {
            "id": 1,
            "text": "Azure AI Services",
            "confidence": 0.97,
            "instances": [
              {"start": "0:00:10", "end": "0:00:15"}
            ]
          }
        ]
      }
    }
  ]
}
```

---

## 6. Video Indexer Widgets

Video Indexer provides embeddable widgets for custom web applications:

### Widget Types

| Widget | Purpose | Embed Method |
|--------|---------|-------------|
| **Player** | Video playback with insights overlay | `<iframe>` |
| **Insights** | Timeline of all extracted insights | `<iframe>` |
| **Editor** | Clip and edit video based on insights | `<iframe>` |

### Embedding Widgets

```html
<!-- Player Widget -->
<iframe
  src="https://www.videoindexer.ai/embed/player/{accountId}/{videoId}/?accessToken={token}"
  width="800"
  height="450"
  frameborder="0"
  allowfullscreen>
</iframe>

<!-- Insights Widget -->
<iframe
  src="https://www.videoindexer.ai/embed/insights/{accountId}/{videoId}/?accessToken={token}"
  width="400"
  height="600"
  frameborder="0">
</iframe>
```

### Widget Communication

The player and insights widgets can communicate when embedded on the same page — clicking an insight jumps the player to that timestamp, and vice versa.

```html
<!-- Both widgets communicate via postMessage API -->
<script>
  // Listen for cross-widget events
  window.addEventListener("message", function(event) {
    if (event.data.type === "seekTo") {
      console.log("Jump to time: " + event.data.time);
    }
  });
</script>
```

> **EXAM TIP:** Video Indexer widgets can be embedded in custom apps using `<iframe>`. The **player** and **insights** widgets communicate automatically when on the same page — clicking a topic/keyword/face in the insights widget jumps the player to the relevant timestamp.

---

## 7. Spatial Analysis

Spatial analysis uses computer vision to understand how people move through and interact with physical spaces. It is deployed as a Docker container running on an edge device with a connected camera.

### Capabilities

| Operation | Description |
|-----------|-------------|
| **Person counting** | Count people entering/exiting a zone |
| **Person crossing line** | Detect when people cross a virtual line |
| **Person in zone / dwell time** | Track time spent in a defined zone |
| **Person distance** | Measure distance between people |
| **Person movement direction** | Determine direction of movement |

### Architecture

```
Camera → Edge Device (Docker Container) → Azure IoT Hub → Cloud Processing
                    ↓
         Spatial Analysis Container
         (AI model runs locally)
```

### Zone and Line Configuration

Zones and lines are defined using polygon coordinates:

```json
{
  "zones": [
    {
      "name": "checkout-zone",
      "polygon": [
        [0.1, 0.5], [0.1, 0.9],
        [0.5, 0.9], [0.5, 0.5]
      ]
    }
  ],
  "lines": [
    {
      "name": "entrance-line",
      "line": {
        "start": {"x": 0.0, "y": 0.5},
        "end": {"x": 1.0, "y": 0.5}
      }
    }
  ]
}
```

### Use Cases

| Industry | Use Case | Operation |
|----------|----------|-----------|
| **Retail** | Count shoppers entering/leaving store | Person counting |
| **Retail** | Monitor checkout queue length | Person in zone |
| **Workplace** | Enforce occupancy limits | Person counting |
| **Workplace** | Monitor social distancing | Person distance |
| **Security** | Detect restricted area entry | Person crossing line |
| **Healthcare** | Monitor waiting room occupancy | Person in zone / dwell time |
| **Transportation** | Track passenger flow | Person movement direction |

### Deployment Requirements

| Requirement | Details |
|-------------|---------|
| **Edge device** | NVIDIA GPU (T4, Xavier, Jetson) |
| **Container runtime** | NVIDIA Docker |
| **Camera** | RTSP stream support |
| **Connectivity** | Azure IoT Hub connection |
| **Resolution** | Minimum 15 FPS at 1080p recommended |

> **EXAM TIP:** Spatial analysis runs as a **Docker container on an edge device** — it does NOT run in the cloud. It requires an **NVIDIA GPU** and connects to **Azure IoT Hub** for event reporting. Know the key operations: person counting, line crossing, zone dwell time, and distance measurement.

---

## 8. Face API

The Azure AI Face API provides face detection, identification, verification, and analysis capabilities.

### Capabilities Overview

| Capability | Description | Limited Access Required? |
|------------|-------------|------------------------|
| **Face detection** | Detect faces and return bounding boxes | No |
| **Face attributes** | Age, gender, emotion, glasses, head pose, blur, exposure, noise, occlusion, facial hair, makeup, accessories | **Partially** — some attributes retired |
| **Face identification** | Identify who a person is from a trained person group | **Yes** |
| **Face verification** | Verify if two faces belong to the same person | **Yes** |
| **Face grouping** | Group similar faces together | **Yes** |
| **Find similar** | Find faces similar to a reference face | **Yes** |

### Face Detection

Face detection is available without Limited Access approval and returns:

- **Bounding box** (faceRectangle): top, left, width, height
- **Face ID**: temporary ID valid for 24 hours
- **Face landmarks**: 27 key facial points (eyes, nose, mouth, etc.)
- **Head pose**: roll, yaw, pitch angles
- **Quality for recognition**: low, medium, high

### Face Detection Request

```http
POST https://myresource.cognitiveservices.azure.com/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=true&returnFaceAttributes=headPose,qualityForRecognition
Ocp-Apim-Subscription-Key: <your-key>
Content-Type: application/json

{
  "url": "https://example.com/photo.jpg"
}
```

### Face Detection Response

```json
[
  {
    "faceId": "c5c24a82-6845-4031-9d5d-978df9175426",
    "faceRectangle": {
      "top": 114,
      "left": 183,
      "width": 162,
      "height": 162
    },
    "faceLandmarks": {
      "pupilLeft": {"x": 210.5, "y": 155.3},
      "pupilRight": {"x": 310.2, "y": 152.8},
      "noseTip": {"x": 260.1, "y": 200.5},
      "mouthLeft": {"x": 215.3, "y": 235.7},
      "mouthRight": {"x": 305.8, "y": 233.2}
    },
    "faceAttributes": {
      "headPose": {
        "pitch": -2.5,
        "roll": 1.2,
        "yaw": -3.8
      },
      "qualityForRecognition": "high"
    }
  }
]
```

### Python SDK: Face Detection

```python
from azure.ai.vision.face import FaceClient
from azure.ai.vision.face.models import (
    FaceDetectionModel,
    FaceRecognitionModel,
    FaceAttributeTypeDetection03
)
from azure.core.credentials import AzureKeyCredential

endpoint = "https://myresource.cognitiveservices.azure.com"
key = "your-subscription-key"

client = FaceClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

# Detect faces from URL
url = "https://example.com/group-photo.jpg"

result = client.detect_from_url(
    url=url,
    detection_model=FaceDetectionModel.DETECTION_03,
    recognition_model=FaceRecognitionModel.RECOGNITION_04,
    return_face_id=True,
    return_face_landmarks=True,
    return_face_attributes=[
        FaceAttributeTypeDetection03.HEAD_POSE,
        FaceAttributeTypeDetection03.QUALITY_FOR_RECOGNITION
    ]
)

for face in result:
    rect = face.face_rectangle
    print(f"Face detected at: "
          f"top={rect.top}, left={rect.left}, "
          f"width={rect.width}, height={rect.height}")
    print(f"  Face ID: {face.face_id}")
    if face.face_attributes:
        pose = face.face_attributes.head_pose
        print(f"  Head pose: pitch={pose.pitch:.1f}, "
              f"roll={pose.roll:.1f}, yaw={pose.yaw:.1f}")
        print(f"  Quality: "
              f"{face.face_attributes.quality_for_recognition}")
```

### Python SDK: Detect Faces in Local Image

```python
with open("local-photo.jpg", "rb") as image_file:
    image_data = image_file.read()

result = client.detect(
    image_content=image_data,
    detection_model=FaceDetectionModel.DETECTION_03,
    recognition_model=FaceRecognitionModel.RECOGNITION_04,
    return_face_id=True
)

print(f"Detected {len(result)} face(s)")
```

---

## 9. Responsible AI and Limited Access Policy

### What Is Limited Access?

Microsoft restricts access to certain Face API features to prevent misuse and ensure responsible AI practices. The **Limited Access** policy requires customers to apply and be approved before using certain capabilities.

### Features Requiring Limited Access Approval

| Feature | Requires Approval | Status |
|---------|-------------------|--------|
| Face detection (bounding boxes) | No | Available to all |
| Face landmarks | No | Available to all |
| Head pose | No | Available to all |
| Quality for recognition | No | Available to all |
| Blur, exposure, noise, occlusion | No | Available to all |
| **Face identification** | **Yes** | Must apply |
| **Face verification** | **Yes** | Must apply |
| **Find similar** | **Yes** | Must apply |
| **Face grouping** | **Yes** | Must apply |
| Age, gender, emotion, smile | **Retired** | No longer available |

### How to Apply

1. Complete the [Limited Access application form](https://aka.ms/facerecognition)
2. Describe your use case and responsible AI practices
3. Microsoft reviews and approves/denies the application
4. Approval grants access to identification and verification features

### PersonGroup and FaceList Concepts

These concepts are relevant only with Limited Access approval:

| Concept | Description |
|---------|-------------|
| **PersonGroup** | A container for Person objects, each with persisted face data; used for identification ("who is this?") |
| **Person** | An individual within a PersonGroup with one or more persisted face images |
| **FaceList** | A flat collection of persisted face IDs; used for "find similar" operations |
| **LargePersonGroup** | Scalable version of PersonGroup for up to 1,000,000 persons |
| **LargeFaceList** | Scalable version of FaceList for up to 1,000,000 faces |

### Identification Workflow (Limited Access Required)

```
1. Create PersonGroup → 2. Add Persons → 3. Add faces to each Person
                                                    ↓
4. Train PersonGroup → 5. Detect face in new image → 6. Identify against PersonGroup
```

```python
# This workflow requires Limited Access approval

# Step 1: Create a PersonGroup
client.create_person_group(
    person_group_id="employees",
    name="Company Employees",
    recognition_model=FaceRecognitionModel.RECOGNITION_04
)

# Step 2: Add a person
person = client.create_person_group_person(
    person_group_id="employees",
    name="Jane Smith"
)

# Step 3: Add faces to the person
with open("jane-photo1.jpg", "rb") as f:
    client.add_person_group_person_face(
        person_group_id="employees",
        person_id=person.person_id,
        image=f.read()
    )

# Step 4: Train the PersonGroup
client.train_person_group(person_group_id="employees")

# Step 5: Detect a face in a new image
with open("unknown-person.jpg", "rb") as f:
    detected_faces = client.detect(
        image_content=f.read(),
        detection_model=FaceDetectionModel.DETECTION_03,
        recognition_model=FaceRecognitionModel.RECOGNITION_04,
        return_face_id=True
    )

# Step 6: Identify
face_ids = [face.face_id for face in detected_faces]
identify_results = client.identify(
    face_ids=face_ids,
    person_group_id="employees"
)

for result in identify_results:
    if result.candidates:
        person_id = result.candidates[0].person_id
        confidence = result.candidates[0].confidence
        print(f"Identified: {person_id} "
              f"(confidence: {confidence:.2%})")
```

> **EXAM TIP:** Face **detection** (bounding boxes, landmarks, head pose) is available to all customers. Face **identification** and **verification** require **Limited Access approval**. Face attributes like age, gender, emotion, and smile have been **retired** and are no longer available. Know that Microsoft retired these attributes as part of their Responsible AI commitment.

---

## 10. Detection Models and Recognition Models

### Detection Models

| Model | Best For |
|-------|----------|
| **detection_01** | Default, general face detection |
| **detection_02** | Improved accuracy, especially for small/side/blurry faces |
| **detection_03** | Latest and most accurate; recommended for new projects |

### Recognition Models

| Model | Best For |
|-------|----------|
| **recognition_01** | Legacy |
| **recognition_02** | Improved accuracy |
| **recognition_03** | Better accuracy still |
| **recognition_04** | Latest and most accurate; recommended for new projects |

> **EXAM TIP:** For new projects, use **detection_03** and **recognition_04**. These are the latest and most accurate models. PersonGroups must be trained with a specific recognition model, and identification can only be done against faces detected with a compatible recognition model.

---

## 11. Comparing Computer Vision Services

| Service | Best For | Key Feature |
|---------|----------|-------------|
| **Image Analysis 4.0** | Prebuilt image understanding | Tags, captions, objects, OCR |
| **Custom Vision** | Domain-specific classification/detection | Custom trained models |
| **Face API** | Face-specific analysis | Detection, identification, verification |
| **Video Indexer** | Video content understanding | Multi-modal timeline insights |
| **Spatial Analysis** | Physical space monitoring | People counting, movement tracking |

### Decision Flow

```
Need to analyze images?
├── Generic image content → Image Analysis 4.0
├── Domain-specific classification → Custom Vision
├── Face-specific analysis → Face API
│   ├── Just detection → Available to all
│   └── Identification/verification → Limited Access required
└── Need text extraction → Image Analysis 4.0 (read feature)

Need to analyze video?
├── Content insights (transcript, topics, etc.) → Video Indexer
└── Real-time physical space monitoring → Spatial Analysis
```

---

## 12. REST API: Face Detection Example

```http
POST https://myresource.cognitiveservices.azure.com/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=false&returnFaceAttributes=headPose,qualityForRecognition&detectionModel=detection_03&recognitionModel=recognition_04
Ocp-Apim-Subscription-Key: <your-key>
Content-Type: application/json

{
  "url": "https://example.com/group-photo.jpg"
}
```

**Response:**

```json
[
  {
    "faceId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "faceRectangle": {
      "top": 120,
      "left": 200,
      "width": 150,
      "height": 150
    },
    "faceAttributes": {
      "headPose": {
        "pitch": -1.5,
        "roll": 0.8,
        "yaw": -2.3
      },
      "qualityForRecognition": "high"
    }
  },
  {
    "faceId": "b2c3d4e5-f6a7-8901-bcde-f23456789012",
    "faceRectangle": {
      "top": 130,
      "left": 450,
      "width": 140,
      "height": 140
    },
    "faceAttributes": {
      "headPose": {
        "pitch": 0.3,
        "roll": -0.5,
        "yaw": 5.1
      },
      "qualityForRecognition": "medium"
    }
  }
]
```

---

## 13. Microsoft Documentation

| Resource | Link |
|----------|------|
| Video Indexer overview | [Docs](https://learn.microsoft.com/azure/azure-video-indexer/video-indexer-overview) |
| Video Indexer API reference | [Docs](https://api-portal.videoindexer.ai/) |
| Video Indexer portal | [Portal](https://www.videoindexer.ai) |
| Spatial Analysis overview | [Docs](https://learn.microsoft.com/azure/ai-services/computer-vision/intro-to-spatial-analysis-public-preview) |
| Spatial Analysis operations | [Docs](https://learn.microsoft.com/azure/ai-services/computer-vision/spatial-analysis-operations) |
| Face API overview | [Docs](https://learn.microsoft.com/azure/ai-services/computer-vision/overview-identity) |
| Face API quickstart | [Docs](https://learn.microsoft.com/azure/ai-services/computer-vision/quickstarts-sdk/identity-client-library) |
| Limited Access policy | [Docs](https://learn.microsoft.com/azure/ai-services/cognitive-services-limited-access) |
| Responsible AI for Face | [Docs](https://learn.microsoft.com/azure/ai-services/computer-vision/responsible-use-of-face-service) |

---

## Key Takeaways

1. **Video Indexer** extracts multi-modal insights from video: transcripts, topics, faces, brands, sentiment, OCR, scenes, and keyframes — all mapped to timestamps. File limits are **2 GB** and **4 hours**.

2. **ARM-connected accounts** are the recommended Video Indexer account type. Classic accounts are legacy. ARM accounts support Azure RBAC and virtual networks.

3. **Video Indexer widgets** (player, insights, editor) can be embedded via `<iframe>` in custom apps. Player and insights widgets communicate automatically for timestamp-synchronized navigation.

4. **Spatial Analysis** runs as a Docker container on an **edge device** with an NVIDIA GPU. It supports person counting, line crossing, zone dwell time, and distance measurement — all processed locally with events sent to IoT Hub.

5. **Face API detection** (bounding boxes, landmarks, head pose) is available to all customers. **Face identification and verification** require **Limited Access approval**. Face attributes like age, gender, and emotion have been **retired**.

6. Use **detection_03** and **recognition_04** for new Face API projects — they are the latest and most accurate models.

7. For the exam, know which service to use: **Image Analysis 4.0** for general image understanding, **Custom Vision** for domain-specific models, **Face API** for face analysis, **Video Indexer** for video insights, and **Spatial Analysis** for physical space monitoring.

---

[← Previous: Custom Vision](lesson-2-custom-vision.md) | [Back to Module Overview →](overview.md)
