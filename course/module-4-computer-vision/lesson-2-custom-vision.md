# Lesson 2: Custom Vision — Classification and Object Detection

## Learning Objectives

After completing this lesson, you will be able to:

- Distinguish between multiclass classification, multilabel classification, and object detection
- Understand training requirements including minimum image counts and dataset balance
- Choose between quick training and advanced training
- Select the correct training domain (general, compact, specialized)
- Interpret evaluation metrics: precision, recall, and average precision (AP)
- Publish trained iterations to the prediction endpoint
- Build an end-to-end Custom Vision pipeline entirely in code (no portal required)
- Consume prediction results via SDK and REST API

---

## 1. Classification vs Object Detection

Custom Vision supports three project types. Choosing the right one depends on your scenario:

### Multiclass Classification

- **One tag per image** — the model predicts a single most likely category
- Example: "Is this a cat, dog, or bird?"
- Each image is assigned exactly one label during training

### Multilabel Classification

- **Multiple tags per image** — the model predicts all applicable categories
- Example: "This image contains a beach AND a sunset AND palm trees"
- Each image can have one or more labels during training

### Object Detection

- **Tags + bounding box regions** — the model identifies objects AND their locations
- Example: "There is a cat at [x, y, w, h] and a dog at [x, y, w, h]"
- Each image is annotated with bounding boxes around objects of interest

### Decision Table: When to Use Which

| Scenario | Project Type |
|----------|-------------|
| Classify a product as defective or non-defective | Multiclass Classification |
| Identify all ingredients visible in a food photo | Multilabel Classification |
| Locate and identify different car models in parking lot images | Object Detection |
| Sort incoming mail images by department | Multiclass Classification |
| Tag social media images with all applicable content categories | Multilabel Classification |
| Count and locate people in security camera footage | Object Detection |
| Determine if an X-ray shows a fracture or is normal | Multiclass Classification |
| Identify multiple safety violations in a construction site photo | Multilabel Classification |

### Comparison: Custom Vision vs Prebuilt Image Analysis

| Aspect | Prebuilt Image Analysis 4.0 | Custom Vision |
|--------|----------------------------|---------------|
| **Training required** | No — works out of the box | Yes — requires labeled training data |
| **Categories** | 10,000+ generic tags | Your custom categories only |
| **Accuracy for your domain** | Good for general content | Excellent for domain-specific content |
| **Bounding boxes** | Yes (objects feature) | Yes (object detection projects) |
| **Setup time** | Minutes | Hours (data collection + training) |
| **Best for** | General-purpose analysis | Domain-specific classification/detection |
| **Edge deployment** | No | Yes (compact domains) |

> **EXAM TIP:** Use **prebuilt Image Analysis** when generic tags/objects meet your needs. Use **Custom Vision** when you need domain-specific categories that the prebuilt model doesn't cover (e.g., specific product defects, custom inventory items, specialized medical conditions).

---

## 2. Training Requirements

### Minimum Image Counts

| Requirement | Value |
|-------------|-------|
| **Minimum images per tag** | 15 |
| **Recommended images per tag** | 30–50+ for good accuracy |
| **Practical recommendation** | 50+ images per tag with varied conditions |

### Image Requirements

| Constraint | Value |
|------------|-------|
| **Minimum resolution** | 256 × 256 pixels |
| **Maximum file size** | 6 MB per image |
| **Supported formats** | JPEG, PNG, BMP, GIF |
| **Maximum images per project** | 100,000 (paid tier) |
| **Maximum tags per project** | 500 |

### Dataset Balance

A balanced dataset is critical for good model performance:

- **Balanced**: Each tag has roughly the same number of images
- **Imbalanced**: Some tags have far more images than others
- Imbalanced datasets cause the model to be biased toward the over-represented class

**Example of imbalanced data (BAD):**

| Tag | Image Count | Problem |
|-----|------------|---------|
| Cat | 200 | Over-represented |
| Dog | 180 | OK |
| Bird | 15 | Under-represented — model will struggle |

**Better balanced data:**

| Tag | Image Count |
|-----|------------|
| Cat | 50 |
| Dog | 50 |
| Bird | 50 |

### Image Variety

For each tag, include images with variety in:

- **Lighting**: bright, dim, indoor, outdoor
- **Angles**: front, side, top-down, tilted
- **Backgrounds**: different settings and contexts
- **Scale**: close-up, medium, far away
- **Occlusion**: partially hidden objects

### Negative Examples

- **Negative images**: images that do NOT contain any of your tags
- Help the model learn what is NOT your target
- Especially useful for object detection to reduce false positives
- Tagged with the special "Negative" label or left untagged

> **EXAM TIP:** The minimum is **15 images per tag**, but Microsoft recommends **at least 30** for reasonable accuracy. Datasets should be **balanced** (similar counts per tag) and include **variety** in lighting, angle, and background. Images must be at least **256×256 pixels** and no larger than **6 MB**.

---

## 3. Training and Iteration

### Quick Training vs Advanced Training

| Aspect | Quick Training | Advanced Training |
|--------|---------------|-------------------|
| **Duration** | Minutes | Up to 24 hours |
| **When to use** | Initial testing, prototyping | Production models, maximum accuracy |
| **Budget** | Specify up to 1 hour | Specify 1–24 hours |
| **Result** | Good baseline accuracy | Optimized accuracy |
| **Cost** | Lower (less compute time) | Higher (more compute time) |

### Training Domains

Custom Vision offers specialized domains optimized for specific content types:

| Domain | Best For | Available In |
|--------|----------|-------------|
| **General** | Wide range of images | Classification + Detection |
| **General [A1]** | Improved general with better accuracy | Classification + Detection |
| **General [A2]** | Latest general-purpose domain | Classification + Detection |
| **Food** | Photos of dishes and ingredients | Classification |
| **Landmarks** | Natural and artificial landmarks | Classification |
| **Retail** | Product shelf and display images | Classification |
| **Logo** | Brand logos | Detection |

### Compact Domains (Edge Deployment)

Compact domains produce smaller models that can be exported and run on edge devices:

| Compact Domain | Best For | Export Formats |
|----------------|----------|----------------|
| **General (compact)** | General-purpose edge models | TensorFlow, ONNX, CoreML, Docker |
| **General (compact) [S1]** | Improved compact | TensorFlow, ONNX, CoreML, Docker |
| **Food (compact)** | Food on edge | TensorFlow, ONNX, CoreML |
| **Landmarks (compact)** | Landmarks on edge | TensorFlow, ONNX, CoreML |
| **Retail (compact)** | Retail on edge | TensorFlow, ONNX, CoreML |

> **EXAM TIP:** If an exam question asks about running a model **offline**, on an **edge device**, on **IoT**, or **without internet connectivity**, the answer involves a **compact domain** with model export. Standard (non-compact) domains can only be consumed via the cloud API.

### Iterations

- Each time you train the model, a new **iteration** is created
- Previous iterations are preserved — you can compare and roll back
- Only one iteration can be published at a time per prediction resource name
- You select which iteration to publish as the active prediction endpoint

---

## 4. Evaluation Metrics

After training, Custom Vision provides three key evaluation metrics:

### Precision

$$\text{Precision} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}}$$

- Of all items the model **predicted** as a given class, what percentage were correct?
- **High precision** = few false positives (the model rarely makes incorrect predictions)
- Example: Model predicts 100 images as "cat" — 95 actually are cats → 95% precision

### Recall

$$\text{Recall} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}}$$

- Of all items that **actually are** a given class, what percentage did the model find?
- **High recall** = few false negatives (the model rarely misses actual positives)
- Example: 100 actual cat images in the test set — model correctly identifies 90 → 90% recall

### Average Precision (AP)

- The **area under the precision-recall curve**
- A single number that summarizes model performance across all confidence thresholds
- Higher AP = better overall model quality
- Reported per-tag and as mean Average Precision (mAP) across all tags

### How to Improve Each Metric

| Problem | Metric Affected | Solution |
|---------|----------------|----------|
| Too many false positives | Low Precision | Add more negative examples; add more variety to positive examples |
| Too many false negatives | Low Recall | Add more positive examples with greater variety |
| Both metrics low | Low AP | Add more training data overall; ensure balanced dataset |
| Good on some tags, poor on others | Uneven per-tag AP | Balance the dataset; add more images for underperforming tags |

### Probability Threshold Adjustment

The probability threshold controls the minimum confidence required for a prediction:

- **Higher threshold** → fewer predictions, higher precision, lower recall
- **Lower threshold** → more predictions, lower precision, higher recall
- Default threshold varies by project; adjust based on your tolerance for errors

```
Threshold = 0.9  → Very selective: few predictions, high confidence
Threshold = 0.5  → Balanced: moderate predictions, moderate confidence
Threshold = 0.1  → Permissive: many predictions, low confidence
```

> **EXAM TIP:** Know the difference between precision and recall. **Precision** = "of what the model predicted, how many were right?" **Recall** = "of what actually exists, how many did the model find?" If the question describes missed detections, the issue is **low recall**. If the question describes too many false alarms, the issue is **low precision**.

---

## 5. Publishing and Consuming

### Publishing an Iteration

After training, you must **publish** an iteration to make it available for predictions:

1. Select the trained iteration
2. Choose a **publish name** (e.g., "production-v1")
3. Specify the **prediction resource** ID

Once published, the model is accessible via the prediction endpoint.

### Prediction Resource vs Training Resource

| Resource | Purpose |
|----------|---------|
| **Training resource** | Upload images, tag, train models, evaluate |
| **Prediction resource** | Serve predictions for published models |
| **Multi-service AI resource** | Can serve as both (for simpler setups) |

> **EXAM TIP:** In production, Microsoft recommends using **separate** training and prediction resources. The training resource handles data and model management; the prediction resource handles inference. This separation provides better access control and cost management.

### Prediction Endpoint

The prediction endpoint URL format:

```
POST https://{endpoint}/customvision/v3.0/prediction/{project-id}/classify/iterations/{published-name}/image
POST https://{endpoint}/customvision/v3.0/prediction/{project-id}/classify/iterations/{published-name}/url
POST https://{endpoint}/customvision/v3.0/prediction/{project-id}/detect/iterations/{published-name}/image
POST https://{endpoint}/customvision/v3.0/prediction/{project-id}/detect/iterations/{published-name}/url
```

- `classify` for classification projects
- `detect` for object detection projects
- `/image` for binary upload
- `/url` for image URL input

### Prediction Response Structure

**Classification response:**

```json
{
  "id": "a1b2c3d4-...",
  "project": "project-id",
  "iteration": "iteration-id",
  "created": "2024-01-15T10:30:00.000Z",
  "predictions": [
    {
      "probability": 0.9542,
      "tagId": "tag-id-1",
      "tagName": "cat",
      "tagType": "Regular"
    },
    {
      "probability": 0.0321,
      "tagId": "tag-id-2",
      "tagName": "dog",
      "tagType": "Regular"
    }
  ]
}
```

**Object detection response:**

```json
{
  "id": "a1b2c3d4-...",
  "project": "project-id",
  "iteration": "iteration-id",
  "created": "2024-01-15T10:30:00.000Z",
  "predictions": [
    {
      "probability": 0.9654,
      "tagId": "tag-id-1",
      "tagName": "cat",
      "tagType": "Regular",
      "boundingBox": {
        "left": 0.12,
        "top": 0.15,
        "width": 0.45,
        "height": 0.60
      }
    },
    {
      "probability": 0.8876,
      "tagId": "tag-id-2",
      "tagName": "dog",
      "tagType": "Regular",
      "boundingBox": {
        "left": 0.55,
        "top": 0.20,
        "width": 0.35,
        "height": 0.55
      }
    }
  ]
}
```

> **EXAM TIP:** In object detection responses, bounding box coordinates are **normalized** (0.0–1.0), NOT pixel values. `left: 0.12` means 12% from the left edge. To convert to pixels, multiply by the image width/height.

---

## 6. Code-First Approach (Programmatic Pipeline)

You can build the entire Custom Vision workflow without the portal — fully automated via the SDK.

### Install SDKs

```bash
pip install azure-cognitiveservices-vision-customvision
```

### Python SDK: Complete End-to-End Pipeline

```python
from azure.cognitiveservices.vision.customvision.training import (
    CustomVisionTrainingClient
)
from azure.cognitiveservices.vision.customvision.prediction import (
    CustomVisionPredictionClient
)
from azure.cognitiveservices.vision.customvision.training.models import (
    ImageFileCreateBatch,
    ImageFileCreateEntry,
    Region
)
from msrest.authentication import ApiKeyCredentials
import time
import os

# ============================================================
# Step 1: Configure credentials
# ============================================================
training_endpoint = "https://mycvtraining.cognitiveservices.azure.com"
training_key = "your-training-key"
prediction_endpoint = "https://mycvprediction.cognitiveservices.azure.com"
prediction_key = "your-prediction-key"
prediction_resource_id = "/subscriptions/.../resourceGroups/.../providers/Microsoft.CognitiveServices/accounts/mycvprediction"

training_credentials = ApiKeyCredentials(
    in_headers={"Training-key": training_key}
)
trainer = CustomVisionTrainingClient(
    training_endpoint, training_credentials
)

prediction_credentials = ApiKeyCredentials(
    in_headers={"Prediction-key": prediction_key}
)
predictor = CustomVisionPredictionClient(
    prediction_endpoint, prediction_credentials
)

# ============================================================
# Step 2: Create a new project
# ============================================================
project = trainer.create_project(
    name="Fruit Classifier",
    description="Classify images of fruit",
    classification_type="Multiclass"  # or "Multilabel"
    # For object detection, use:
    # domain_id=<object-detection-domain-id>
)
print(f"Project created: {project.id}")

# ============================================================
# Step 3: Create tags
# ============================================================
apple_tag = trainer.create_tag(project.id, "apple")
banana_tag = trainer.create_tag(project.id, "banana")
orange_tag = trainer.create_tag(project.id, "orange")
print("Tags created: apple, banana, orange")

# ============================================================
# Step 4: Upload and tag images
# ============================================================
image_entries = []

# Upload apple images
apple_dir = "training-images/apple"
for filename in os.listdir(apple_dir):
    filepath = os.path.join(apple_dir, filename)
    with open(filepath, "rb") as image_file:
        image_entries.append(
            ImageFileCreateEntry(
                name=filename,
                contents=image_file.read(),
                tag_ids=[apple_tag.id]
            )
        )

# Upload banana images
banana_dir = "training-images/banana"
for filename in os.listdir(banana_dir):
    filepath = os.path.join(banana_dir, filename)
    with open(filepath, "rb") as image_file:
        image_entries.append(
            ImageFileCreateEntry(
                name=filename,
                contents=image_file.read(),
                tag_ids=[banana_tag.id]
            )
        )

# Upload orange images
orange_dir = "training-images/orange"
for filename in os.listdir(orange_dir):
    filepath = os.path.join(orange_dir, filename)
    with open(filepath, "rb") as image_file:
        image_entries.append(
            ImageFileCreateEntry(
                name=filename,
                contents=image_file.read(),
                tag_ids=[orange_tag.id]
            )
        )

# Upload in batches (max 64 images per batch)
batch_size = 64
for i in range(0, len(image_entries), batch_size):
    batch = ImageFileCreateBatch(
        images=image_entries[i:i + batch_size]
    )
    upload_result = trainer.create_images_from_files(
        project.id, batch
    )
    if not upload_result.is_batch_successful:
        for image in upload_result.images:
            if image.status != "OK":
                print(f"Upload failed: {image.source_url} - {image.status}")

print(f"Uploaded {len(image_entries)} images")

# ============================================================
# Step 5: Train the model
# ============================================================
print("Training started...")
iteration = trainer.train_project(project.id)

while iteration.status != "Completed":
    iteration = trainer.get_iteration(project.id, iteration.id)
    print(f"Training status: {iteration.status}")
    time.sleep(10)

print("Training complete!")

# ============================================================
# Step 6: Evaluate the model
# ============================================================
performance = trainer.get_iteration_performance(
    project.id, iteration.id
)
print(f"Precision: {performance.precision:.2%}")
print(f"Recall:    {performance.recall:.2%}")
print(f"AP:        {performance.average_precision:.2%}")

for tag_perf in performance.per_tag_performance:
    print(f"  {tag_perf.name}: "
          f"P={tag_perf.precision:.2%}, "
          f"R={tag_perf.recall:.2%}, "
          f"AP={tag_perf.average_precision:.2%}")

# ============================================================
# Step 7: Publish the iteration
# ============================================================
publish_name = "fruit-classifier-v1"
trainer.publish_iteration(
    project.id,
    iteration.id,
    publish_name,
    prediction_resource_id
)
print(f"Model published as '{publish_name}'")

# ============================================================
# Step 8: Make predictions
# ============================================================

# Predict from URL
results = predictor.classify_image_url(
    project.id,
    publish_name,
    url="https://example.com/test-apple.jpg"
)

for prediction in results.predictions:
    print(f"  {prediction.tag_name}: {prediction.probability:.2%}")

# Predict from local file
with open("test-image.jpg", "rb") as image_file:
    results = predictor.classify_image(
        project.id,
        publish_name,
        image_file.read()
    )

for prediction in results.predictions:
    print(f"  {prediction.tag_name}: {prediction.probability:.2%}")
```

### Object Detection: Uploading Images with Bounding Boxes

For object detection projects, you must specify bounding box regions when uploading:

```python
# Create an object detection project
obj_detect_domain = next(
    d for d in trainer.get_domains()
    if d.type == "ObjectDetection" and d.name == "General"
)

project = trainer.create_project(
    name="Safety Equipment Detector",
    domain_id=obj_detect_domain.id
)

helmet_tag = trainer.create_tag(project.id, "helmet")
vest_tag = trainer.create_tag(project.id, "vest")

# Upload images with bounding box annotations
# Coordinates are normalized (0.0 to 1.0)
image_entries = []
with open("image1.jpg", "rb") as f:
    image_entries.append(
        ImageFileCreateEntry(
            name="image1.jpg",
            contents=f.read(),
            regions=[
                Region(
                    tag_id=helmet_tag.id,
                    left=0.1,    # 10% from left
                    top=0.05,    # 5% from top
                    width=0.2,   # 20% of image width
                    height=0.25  # 25% of image height
                ),
                Region(
                    tag_id=vest_tag.id,
                    left=0.08,
                    top=0.30,
                    width=0.25,
                    height=0.50
                )
            ]
        )
    )

batch = ImageFileCreateBatch(images=image_entries)
trainer.create_images_from_files(project.id, batch)
```

---

## 7. REST API for Predictions

### Classification Prediction (URL Input)

```http
POST https://mycvprediction.cognitiveservices.azure.com/customvision/v3.0/prediction/{project-id}/classify/iterations/fruit-classifier-v1/url
Prediction-Key: <your-prediction-key>
Content-Type: application/json

{
  "url": "https://example.com/test-apple.jpg"
}
```

### Classification Prediction (Binary Input)

```http
POST https://mycvprediction.cognitiveservices.azure.com/customvision/v3.0/prediction/{project-id}/classify/iterations/fruit-classifier-v1/image
Prediction-Key: <your-prediction-key>
Content-Type: application/octet-stream

<binary image data>
```

### Object Detection Prediction

```http
POST https://mycvprediction.cognitiveservices.azure.com/customvision/v3.0/prediction/{project-id}/detect/iterations/safety-detector-v1/url
Prediction-Key: <your-prediction-key>
Content-Type: application/json

{
  "url": "https://example.com/construction-site.jpg"
}
```

### REST Prediction with Python `requests`

```python
import requests

prediction_endpoint = "https://mycvprediction.cognitiveservices.azure.com"
prediction_key = "your-prediction-key"
project_id = "your-project-id"
publish_name = "fruit-classifier-v1"

# Classify from URL
url = (
    f"{prediction_endpoint}/customvision/v3.0/prediction/"
    f"{project_id}/classify/iterations/{publish_name}/url"
)
headers = {
    "Prediction-Key": prediction_key,
    "Content-Type": "application/json"
}
body = {
    "url": "https://example.com/test-apple.jpg"
}

response = requests.post(url, headers=headers, json=body)
results = response.json()

for pred in results["predictions"]:
    print(f"{pred['tagName']}: {pred['probability']:.2%}")
```

```python
# Classify from local file
url = (
    f"{prediction_endpoint}/customvision/v3.0/prediction/"
    f"{project_id}/classify/iterations/{publish_name}/image"
)
headers = {
    "Prediction-Key": prediction_key,
    "Content-Type": "application/octet-stream"
}

with open("test-image.jpg", "rb") as f:
    response = requests.post(url, headers=headers, data=f.read())

results = response.json()
for pred in results["predictions"]:
    print(f"{pred['tagName']}: {pred['probability']:.2%}")
```

---

## 8. Resource Setup Options

### Option 1: Dedicated Custom Vision Resources (Recommended)

Create two separate resources:

| Resource | SKU | Purpose |
|----------|-----|---------|
| Custom Vision Training | F0 (free) or S0 | Upload data, tag, train, evaluate |
| Custom Vision Prediction | F0 (free) or S0 | Serve prediction requests |

### Option 2: Multi-Service Azure AI Resource

- A single Azure AI Services (multi-service) resource can handle both training and prediction
- Simpler setup but less granular access control
- Good for development/testing

### Free Tier Limits

| Limit | F0 (Free) Training | F0 (Free) Prediction |
|-------|--------------------|--------------------|
| Projects | 2 | 2 |
| Training images | 5,000 per project | N/A |
| Predictions | N/A | 10,000/month |
| Tags | 50 per project | N/A |
| Iterations | 10 per project | N/A |

> **EXAM TIP:** The free tier allows **2 projects** with **5,000 images** per project and **50 tags**. For production workloads, use the S0 (Standard) tier which supports **100 projects**, **100,000 images** per project, and **500 tags**.

---

## 9. Exporting Models for Edge Deployment

When using a **compact domain**, you can export the trained model:

### Supported Export Formats

| Format | Platform |
|--------|----------|
| **TensorFlow** | Android, Linux, Raspberry Pi |
| **TensorFlow Lite** | Android, iOS, Raspberry Pi |
| **ONNX** | Windows ML, Azure ML, cross-platform |
| **CoreML** | iOS, macOS |
| **Docker** (Linux/Windows/ARM) | Containers on any platform |
| **VAIDK** | Vision AI Dev Kit |

### Export via SDK

```python
# Export a compact model to ONNX
export = trainer.export_iteration(
    project.id,
    iteration.id,
    platform="ONNX"
)

# Check export status
while export.status != "Done":
    exports = trainer.get_exports(project.id, iteration.id)
    export = next(e for e in exports if e.platform == "ONNX")
    time.sleep(5)

# Download the exported model
print(f"Download URL: {export.download_uri}")
```

> **EXAM TIP:** Only **compact domains** support model export. Standard domains are cloud-only. If you need to run inference on an edge device, IoT hub, or offline — you must train with a compact domain and export the model.

---

## 10. Custom Vision Portal vs Code-First

| Approach | Pros | Cons |
|----------|------|------|
| **Portal** (customvision.ai) | Visual UI, easy tagging, drag-and-drop | Manual, not automatable, not reproducible |
| **Code-first** (SDK/REST) | Automatable, CI/CD integration, reproducible | Requires coding, harder to visually verify tags |
| **Hybrid** | Tag in portal, train/deploy in code | Best of both worlds for many teams |

The portal URL: [https://www.customvision.ai](https://www.customvision.ai)

---

## 11. Microsoft Documentation

| Resource | Link |
|----------|------|
| Custom Vision overview | [Docs](https://learn.microsoft.com/azure/ai-services/custom-vision-service/overview) |
| Quickstart: Build a classifier | [Docs](https://learn.microsoft.com/azure/ai-services/custom-vision-service/getting-started-build-a-classifier) |
| Quickstart: Build an object detector | [Docs](https://learn.microsoft.com/azure/ai-services/custom-vision-service/get-started-build-detector) |
| Python SDK quickstart | [Docs](https://learn.microsoft.com/azure/ai-services/custom-vision-service/quickstarts/image-classification) |
| Export models to mobile | [Docs](https://learn.microsoft.com/azure/ai-services/custom-vision-service/export-your-model) |
| Training API reference | [Docs](https://learn.microsoft.com/rest/api/customvision/training/) |
| Prediction API reference | [Docs](https://learn.microsoft.com/rest/api/customvision/prediction/) |
| How to improve your model | [Docs](https://learn.microsoft.com/azure/ai-services/custom-vision-service/getting-started-improving-your-classifier) |

---

## Key Takeaways

1. **Three project types**: Multiclass classification (one tag), multilabel classification (multiple tags), and object detection (tags + bounding boxes).

2. **Minimum 15 images per tag** (30+ recommended). Images must be at least 256×256 pixels and under 6 MB. Datasets should be balanced with variety in lighting, angles, and backgrounds.

3. **Compact domains** are required for exporting models to edge devices (TensorFlow, ONNX, CoreML, Docker). Standard domains are cloud-only.

4. **Precision** measures false positive rate ("of what was predicted, how many were right?"). **Recall** measures false negative rate ("of what actually exists, how many were found?"). **AP** is the area under the precision-recall curve.

5. **Publishing** makes a trained iteration available at the prediction endpoint. Use separate training and prediction resources for production.

6. **Object detection bounding boxes** use normalized coordinates (0.0–1.0) in both training annotations and prediction responses.

7. The entire Custom Vision workflow — project creation, image upload, tagging, training, publishing, and prediction — can be automated via the **Python SDK** without the portal.

---

[← Previous: Analyze Images](lesson-1-analyze-images.md) | [Next: Video Analysis →](lesson-3-video-analysis.md)
