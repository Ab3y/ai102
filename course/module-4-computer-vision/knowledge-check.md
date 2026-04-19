# Module 4: Computer Vision — Knowledge Check

## Instructions

Answer all 15 questions. Each question has one correct answer unless stated otherwise. Target score: **80% or higher** (12/15).

---

### Question 1

**You are building an application that generates alt text for images on a website. The application should produce a single natural language sentence describing each image. You are using the Azure AI Vision Image Analysis 4.0 API.**

Which visual feature should you specify in your API call?

- A) `tags`
- B) `caption`
- C) `denseCaptions`
- D) `objects`

---

### Question 2

**You are developing a retail inventory application that needs to identify and locate specific products on store shelves. For each product detected, the application must return the product type and its position within the image as pixel coordinates.**

Which visual feature should you use?

- A) `tags` — returns keywords describing the image content
- B) `caption` — returns a natural language description
- C) `objects` — returns detected objects with bounding boxes
- D) `smartCrops` — returns optimal crop regions

---

### Question 3

**A developer submits the following REST API request and receives a `400 Bad Request` error:**

```http
POST https://myresource.cognitiveservices.azure.com/computervision/imageanalysis:analyze?api-version=2024-02-01&features=caption,tags
Ocp-Apim-Subscription-Key: abc123
Content-Type: application/json

{
  "url": "https://example.com/large-photo.jpg"
}
```

**The image at the URL is a valid JPEG file with dimensions of 4000×3000 pixels and a file size of 5.2 MB.**

What is the most likely cause of the error?

- A) The image dimensions exceed the maximum of 4096×4096 pixels
- B) The image file size exceeds the maximum of 4 MB
- C) The API version is incorrect
- D) JPEG format is not supported

---

### Question 4

**You receive the following partial JSON response from the Image Analysis 4.0 API. You need to extract the extracted text content.**

```json
{
  "readResult": {
    "pages": [
      {
        "lines": [
          {
            "text": "Invoice #12345",
            "words": [
              {"text": "Invoice", "confidence": 0.99},
              {"text": "#12345", "confidence": 0.97}
            ]
          },
          {
            "text": "Total: $450.00",
            "words": [
              {"text": "Total:", "confidence": 0.98},
              {"text": "$450.00", "confidence": 0.95}
            ]
          }
        ]
      }
    ]
  }
}
```

**To extract all text line by line, which code correctly iterates through the response?**

- A) `for line in result["readResult"]["lines"]:`
- B) `for page in result["readResult"]["pages"]: for line in page["lines"]:`
- C) `for word in result["readResult"]["words"]:`
- D) `for page in result["readResult"]["pages"]: for word in page["words"]:`

---

### Question 5

**You are building a document processing pipeline. Some documents contain handwritten notes alongside printed text. You need to extract both printed and handwritten text from scanned images.**

Which statement is TRUE about the Read API's handwriting support?

- A) The Read API only supports printed text; use a separate Handwriting API for handwritten text
- B) The Read API supports both printed and handwritten text, with handwriting support available for a subset of languages
- C) The Read API supports handwritten text in all 160+ supported languages
- D) Handwritten text requires the Custom Vision service with a trained model

---

### Question 6

**You are creating a quality control system for a manufacturing line. Each product image should be classified into exactly one category: "pass", "minor_defect", or "major_defect". No product can belong to more than one category.**

Which Custom Vision project type should you use?

- A) Multilabel Classification
- B) Multiclass Classification
- C) Object Detection
- D) Image Analysis 4.0 with tags

---

### Question 7

**A data scientist is training a Custom Vision model and gets the following evaluation results:**

| Tag | Precision | Recall | AP |
|-----|-----------|--------|-----|
| cat | 95% | 40% | 62% |
| dog | 92% | 88% | 90% |
| bird | 89% | 85% | 87% |

**The team reports that the model is missing many actual cat images in production — it fails to detect cats that are clearly visible.**

What should you do to improve the model's performance for the "cat" tag?

- A) Increase the probability threshold to reduce false positives
- B) Add more cat images with variety in lighting, angles, and backgrounds
- C) Remove some dog and bird images to balance the dataset
- D) Switch from multiclass to multilabel classification

---

### Question 8

**You need to deploy a Custom Vision object detection model to run on an IoT edge device that has limited internet connectivity. The model must run inference locally without calling the cloud API.**

What should you do?

- A) Use the Standard General domain and export to ONNX format
- B) Use a Compact domain and export to ONNX, TensorFlow, or CoreML format
- C) Deploy the Custom Vision prediction container using Docker
- D) Cache the cloud API responses for offline use

---

### Question 9

**You are building an automated pipeline using the Custom Vision SDK. Your code creates a project, uploads images, trains a model, and should then make it available for predictions. After training completes, predictions fail with a "Model not found" error.**

**Review the following code:**

```python
project = trainer.create_project("My Project")
apple_tag = trainer.create_tag(project.id, "apple")
# ... upload images ...
iteration = trainer.train_project(project.id)
# wait for training to complete...

# This call fails:
results = predictor.classify_image_url(
    project.id,
    "latest",
    url="https://example.com/test.jpg"
)
```

What is the most likely cause of the error?

- A) The prediction key is incorrect
- B) The iteration was not published before attempting prediction
- C) The training has not completed yet
- D) The project type is incorrect for classification

---

### Question 10

**A Custom Vision object detection model returns the following prediction:**

```json
{
  "predictions": [
    {
      "probability": 0.92,
      "tagName": "helmet",
      "boundingBox": {
        "left": 0.25,
        "top": 0.10,
        "width": 0.15,
        "height": 0.20
      }
    }
  ]
}
```

**The source image is 800×600 pixels. What are the pixel coordinates of the top-left corner of the bounding box?**

- A) left=25px, top=10px
- B) left=200px, top=60px
- C) left=0.25px, top=0.10px
- D) left=250px, top=100px

---

### Question 11

**You are building a media management application that needs to automatically generate searchable metadata from uploaded videos. The metadata should include a transcript of spoken content, identified topics, detected brands, and on-screen text (OCR).**

Which Azure service should you use?

- A) Azure AI Vision Image Analysis 4.0
- B) Azure AI Video Indexer
- C) Azure AI Speech with Azure AI Language
- D) Azure AI Custom Vision with video frame extraction

---

### Question 12

**A retail company wants to count the number of customers entering and exiting their store in real time using overhead security cameras. The solution must process video locally at the store to minimize bandwidth usage and latency.**

Which Azure service and deployment model should you recommend?

- A) Azure AI Video Indexer with real-time streaming
- B) Azure AI Vision Spatial Analysis running as a Docker container on an edge device
- C) Azure AI Face API with person counting
- D) Azure AI Vision Image Analysis 4.0 processing individual frames

---

### Question 13

**You are developing an application that identifies employees entering a secure area using facial recognition. You plan to create a PersonGroup, add employee photos, train the model, and then identify faces in real-time camera feeds.**

Before you can use the Face API identification feature, what additional step is required?

- A) Purchase an Enterprise Agreement license for Azure AI Services
- B) Apply for and receive Limited Access approval from Microsoft
- C) Upgrade to the S0 (Standard) pricing tier
- D) Enable the facial recognition feature in the Azure portal resource settings

---

### Question 14

**A developer uploads a 3 GB MP4 video file to Azure AI Video Indexer and receives an error.**

What is the most likely cause?

- A) MP4 format is not supported by Video Indexer
- B) The video file exceeds the maximum size of 2 GB
- C) The video exceeds the maximum duration of 2 hours
- D) The account has reached the maximum number of indexed videos

---

### Question 15

**You are building a Face API application and want to use the latest and most accurate models for a new project. You need to detect faces and later identify them (after receiving Limited Access approval).**

Which combination of models should you specify?

- A) `detection_01` and `recognition_01`
- B) `detection_02` and `recognition_03`
- C) `detection_03` and `recognition_04`
- D) `detection_03` and `recognition_01`

---

## Answers

### Question 1

**Correct Answer: B**

**Explanation:** The `caption` feature returns a single natural language sentence describing the entire image, which is ideal for generating alt text. `tags` returns keywords (not sentences), `denseCaptions` returns multiple region-based captions (more than needed for alt text), and `objects` returns detected objects with bounding boxes. For a single descriptive sentence, `caption` is the correct choice.

---

### Question 2

**Correct Answer: C**

**Explanation:** The `objects` feature returns detected objects with bounding box coordinates (x, y, width, height), which provides both the object type and its position within the image. `tags` returns keywords without location information. `caption` returns a text description. `smartCrops` returns optimal crop regions for thumbnails, not object detection.

---

### Question 3

**Correct Answer: B**

**Explanation:** The Image Analysis 4.0 API has a maximum file size of **4 MB**. The image in the question is 5.2 MB, which exceeds this limit. The dimensions (4000×3000) are within the allowed range of 50×50 to 16,000×16,000 pixels. JPEG is a supported format, and the API version `2024-02-01` is valid.

---

### Question 4

**Correct Answer: B**

**Explanation:** The Read API response structure is hierarchical: `readResult` → `pages[]` → `lines[]` → `words[]`. To extract text line by line, you must first iterate through pages, then iterate through lines within each page. Option A skips the pages level. Options C and D extract individual words rather than lines.

---

### Question 5

**Correct Answer: B**

**Explanation:** The Read API supports both printed and handwritten text in a single call. However, handwritten text recognition is available for a subset of languages (primarily English and a few others), not all 160+ supported print languages. There is no separate Handwriting API, and Custom Vision is not needed for handwriting recognition.

---

### Question 6

**Correct Answer: B**

**Explanation:** Multiclass classification assigns exactly **one tag per image**, which matches the requirement that each product belongs to exactly one category (pass, minor_defect, or major_defect). Multilabel classification allows multiple tags per image, which is not desired here. Object detection is for locating objects with bounding boxes. Image Analysis 4.0 provides generic tags, not custom categories.

---

### Question 7

**Correct Answer: B**

**Explanation:** The "cat" tag has high precision (95%) but very low recall (40%). Low recall means the model is **missing many actual cat images** (high false negatives). To improve recall, add more positive examples (cat images) with greater variety in lighting, angles, backgrounds, and occlusion. Increasing the threshold would make recall worse. Simply removing other class images doesn't address the lack of varied cat training data.

---

### Question 8

**Correct Answer: B**

**Explanation:** To run a Custom Vision model offline on an edge device, you must use a **compact domain** during training, which produces a smaller model that can be exported. Export formats include ONNX, TensorFlow, TensorFlow Lite, CoreML, and Docker. Standard (non-compact) domains cannot be exported — they only work via the cloud API. This is a key exam concept.

---

### Question 9

**Correct Answer: B**

**Explanation:** After training completes, you must explicitly **publish** the iteration before it can be used for predictions. The code attempts to predict using `"latest"` as the publish name, but no iteration has been published. The fix is to call `trainer.publish_iteration(project.id, iteration.id, "latest", prediction_resource_id)` before making predictions.

---

### Question 10

**Correct Answer: B**

**Explanation:** Custom Vision object detection returns **normalized bounding box coordinates** (0.0–1.0). To convert to pixel coordinates, multiply by the image dimensions:
- left: 0.25 × 800 = **200 px**
- top: 0.10 × 600 = **60 px**

The normalized coordinates represent percentages of the image dimensions, not pixel values.

---

### Question 11

**Correct Answer: B**

**Explanation:** Azure AI Video Indexer is specifically designed to extract multi-modal insights from video content, including transcripts (from speech), topics, brands (visual and audio), and OCR (on-screen text) — all in a single indexing operation. Image Analysis 4.0 works on images, not video. Using Speech + Language separately would require building the integration yourself. Custom Vision with frame extraction is unnecessarily complex.

---

### Question 12

**Correct Answer: B**

**Explanation:** Spatial Analysis runs as a Docker container on an edge device with an NVIDIA GPU and processes video locally, minimizing bandwidth and latency. It supports person counting and line crossing operations ideal for tracking store entry/exit. Video Indexer is for video content analysis, not real-time spatial monitoring. Face API doesn't have person counting. Processing individual frames with Image Analysis would be inefficient and require cloud connectivity.

---

### Question 13

**Correct Answer: B**

**Explanation:** Face **identification** (matching a detected face against a PersonGroup) is a restricted feature under Microsoft's **Limited Access** policy. You must submit an application form and receive approval from Microsoft before using identification, verification, find similar, or face grouping features. This is a Responsible AI requirement, not a pricing tier or portal setting issue.

---

### Question 14

**Correct Answer: B**

**Explanation:** Azure AI Video Indexer has a maximum file size of **2 GB**. The 3 GB file exceeds this limit. MP4 is a supported format. The maximum video duration is 4 hours (not 2 hours). While there may be account-level limits on video count, the file size is the most likely cause given the scenario.

---

### Question 15

**Correct Answer: C**

**Explanation:** For new projects, Microsoft recommends using the latest models: **detection_03** (most accurate face detection) and **recognition_04** (most accurate face recognition). Earlier model versions are available for backward compatibility but offer lower accuracy. It's important that the detection and recognition models are compatible — detection_03 works with recognition_03 and recognition_04.

---

## Score Interpretation

| Score | Interpretation | Recommendation |
|-------|---------------|----------------|
| 13–15 (87–100%) | Excellent | Ready for Module 5 |
| 12 (80%) | Good | Review missed topics, then proceed |
| 9–11 (60–73%) | Needs improvement | Re-read relevant lessons before proceeding |
| Below 9 (<60%) | Significant gaps | Review all three lessons thoroughly |
