"""
AI-102 Lab 4.2: Train a Custom Vision Model
=============================================
Exam Objective: Implement computer vision solutions
  - Create a Custom Vision project
  - Add and tag training images
  - Train and publish a model
  - Use the prediction endpoint

This script demonstrates the code-first approach to:
  1. Creating a Custom Vision project (classification or object detection)
  2. Creating tags and uploading tagged images
  3. Training the model
  4. Publishing the model to a prediction endpoint
  5. Making predictions

Prerequisites:
  - pip install azure-cognitiveservices-vision-customvision python-dotenv
  - A Custom Vision resource (Training AND Prediction)
  - .env file with the required variables (see below)
  - A folder of training images organized by category

NOTE: Custom Vision is a legacy service. For new projects, consider
using Florence-based models in Azure AI Vision (Image Analysis 4.0)
with custom models. However, Custom Vision is still on the AI-102 exam.
"""

import os
import time
from dotenv import load_dotenv
from azure.cognitiveservices.vision.customvision.training import (
    CustomVisionTrainingClient,
)
from azure.cognitiveservices.vision.customvision.prediction import (
    CustomVisionPredictionClient,
)
from azure.cognitiveservices.vision.customvision.training.models import (
    ImageFileCreateBatch,
    ImageFileCreateEntry,
    Region,
)
from msrest.authentication import ApiKeyCredentials

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
load_dotenv()

TRAINING_ENDPOINT = os.getenv("CUSTOM_VISION_TRAINING_ENDPOINT")
TRAINING_KEY = os.getenv("CUSTOM_VISION_TRAINING_KEY")
PREDICTION_ENDPOINT = os.getenv("CUSTOM_VISION_PREDICTION_ENDPOINT")
PREDICTION_KEY = os.getenv("CUSTOM_VISION_PREDICTION_KEY")
PREDICTION_RESOURCE_ID = os.getenv("CUSTOM_VISION_PREDICTION_RESOURCE_ID")

for var_name, var_val in [
    ("CUSTOM_VISION_TRAINING_ENDPOINT", TRAINING_ENDPOINT),
    ("CUSTOM_VISION_TRAINING_KEY", TRAINING_KEY),
]:
    if not var_val:
        raise EnvironmentError(f"Set {var_name} in your .env file.")


# ===========================================================================
# 1. Create a classification project
# ===========================================================================
def create_project(trainer: CustomVisionTrainingClient):
    """
    Create a Custom Vision project for image classification.

    EXAM TIP: Project types –
      - Classification: Multiclass (one tag per image) or Multilabel
      - Object Detection: locates objects with bounding boxes
    Domain options: General, Food, Landmarks, Retail, etc.
    Compact domains allow export to edge devices (ONNX, TensorFlow, etc.)
    """
    print("=" * 60)
    print("1. CREATE PROJECT")
    print("=" * 60)

    # List available domains
    domains = trainer.get_domains()
    general_domain = next(d for d in domains if d.name == "General" and not d.exportable)

    project = trainer.create_project(
        name="AI102-Fruit-Classifier",
        description="Demo classification project for AI-102",
        domain_id=general_domain.id,
        classification_type="Multiclass",  # or "Multilabel"
    )

    print(f"  Created project: {project.name} (ID: {project.id})")
    return project


# ===========================================================================
# 2. Create tags and upload images
# ===========================================================================
def upload_training_images(trainer: CustomVisionTrainingClient, project):
    """
    Create tags and upload training images.

    EXAM TIP:
      - Minimum 5 images per tag for training (15+ recommended).
      - Images should represent real-world variety (angles, lighting, etc.).
      - Max batch upload: 64 images per call.
      - Supported formats: JPEG, PNG, BMP, GIF (first frame).
    """
    print("\n" + "=" * 60)
    print("2. CREATE TAGS AND UPLOAD IMAGES")
    print("=" * 60)

    # Create tags
    apple_tag = trainer.create_tag(project.id, "Apple")
    banana_tag = trainer.create_tag(project.id, "Banana")
    orange_tag = trainer.create_tag(project.id, "Orange")

    print(f"  Created tags: Apple, Banana, Orange")

    tags = {"apple": apple_tag, "banana": banana_tag, "orange": orange_tag}

    # Upload images from a local folder structure:
    #   training-images/
    #     apple/  → image1.jpg, image2.jpg, ...
    #     banana/ → image1.jpg, image2.jpg, ...
    #     orange/ → image1.jpg, image2.jpg, ...
    training_dir = os.path.join(os.path.dirname(__file__), "training-images")

    if not os.path.exists(training_dir):
        print(f"  ⚠️  Training images directory not found: {training_dir}")
        print("  Create the directory with subfolders per category to upload images.")
        print("  Skipping upload – project created with tags only.\n")
        return tags

    for tag_name, tag_obj in tags.items():
        tag_dir = os.path.join(training_dir, tag_name)
        if not os.path.isdir(tag_dir):
            print(f"  ⚠️  Skipping tag '{tag_name}' – folder not found.")
            continue

        image_entries = []
        for filename in os.listdir(tag_dir):
            filepath = os.path.join(tag_dir, filename)
            if not os.path.isfile(filepath):
                continue
            with open(filepath, "rb") as f:
                image_entries.append(
                    ImageFileCreateEntry(
                        name=filename,
                        contents=f.read(),
                        tag_ids=[tag_obj.id],
                    )
                )

        # Upload in batches of 64
        for i in range(0, len(image_entries), 64):
            batch = ImageFileCreateBatch(images=image_entries[i : i + 64])
            result = trainer.create_images_from_files(project.id, batch)
            ok = sum(1 for img in result.images if img.status == "OK")
            print(f"  Uploaded {ok} images for tag '{tag_name}'")

    return tags


# ===========================================================================
# 3. Train the model
# ===========================================================================
def train_model(trainer: CustomVisionTrainingClient, project):
    """
    Train the Custom Vision model.

    EXAM TIP:
      - Training creates an "iteration" (version of the model).
      - Quick Training is default; Advanced Training takes longer but may
        be more accurate (set training_type="Advanced", budget hours).
      - Each training run produces performance metrics (precision, recall, AP).
    """
    print("=" * 60)
    print("3. TRAIN MODEL")
    print("=" * 60)

    try:
        iteration = trainer.train_project(project.id)
        print(f"  Training started: iteration {iteration.id}")
        print("  Waiting for training to complete...")

        while iteration.status != "Completed":
            iteration = trainer.get_iteration(project.id, iteration.id)
            print(f"    Status: {iteration.status}")

            if iteration.status == "Failed":
                print("  ❌ Training failed. Ensure at least 5 images per tag.")
                return None

            time.sleep(5)

        print(f"  ✅ Training completed!")

        # Get performance metrics
        performance = trainer.get_iteration_performance(project.id, iteration.id)
        print(f"    Precision:  {performance.precision:.2%}")
        print(f"    Recall:     {performance.recall:.2%}")
        print(f"    AP (mAP):   {performance.average_precision:.2%}")

        return iteration

    except Exception as exc:
        print(f"  Error: {exc}")
        return None


# ===========================================================================
# 4. Publish the model
# ===========================================================================
def publish_model(trainer: CustomVisionTrainingClient, project, iteration):
    """
    Publish the trained iteration to a prediction endpoint.

    EXAM TIP: You must publish an iteration before you can use it for
    predictions. The publish name is used as the model name in prediction calls.
    """
    print("\n" + "=" * 60)
    print("4. PUBLISH MODEL")
    print("=" * 60)

    if not PREDICTION_RESOURCE_ID:
        print("  Skipped – CUSTOM_VISION_PREDICTION_RESOURCE_ID not set.\n")
        return None

    publish_name = "fruit-classifier-v1"

    try:
        trainer.publish_iteration(
            project.id,
            iteration.id,
            publish_name,
            PREDICTION_RESOURCE_ID,
        )
        print(f"  ✅ Published as: {publish_name}")
        return publish_name

    except Exception as exc:
        print(f"  Error: {exc}")
        return None


# ===========================================================================
# 5. Make predictions
# ===========================================================================
def predict_image(publish_name: str, project_id: str):
    """
    Use the prediction endpoint to classify a new image.

    EXAM TIP: Two prediction methods –
      - classify_image_url / detect_image_url: image from URL
      - classify_image / detect_image: image from file bytes
    """
    print("\n" + "=" * 60)
    print("5. MAKE PREDICTIONS")
    print("=" * 60)

    if not PREDICTION_ENDPOINT or not PREDICTION_KEY:
        print("  Skipped – prediction endpoint/key not set.\n")
        return

    credentials = ApiKeyCredentials(
        in_headers={"Prediction-key": PREDICTION_KEY}
    )
    predictor = CustomVisionPredictionClient(PREDICTION_ENDPOINT, credentials)

    test_image_url = "https://example.com/test-apple.jpg"

    try:
        results = predictor.classify_image_url(
            project_id,
            publish_name,
            url=test_image_url,
        )

        print(f"  Predictions for: {test_image_url}")
        for prediction in results.predictions:
            print(
                f"    {prediction.tag_name:<15} "
                f"probability: {prediction.probability:.2%}"
            )

    except Exception as exc:
        print(f"  Error: {exc}")
        print("  Hint: Ensure the test image URL is publicly accessible.\n")


# ===========================================================================
# Main
# ===========================================================================
if __name__ == "__main__":
    print("\nAI-102 Lab 4.2 – Train Custom Vision Model\n")

    credentials = ApiKeyCredentials(
        in_headers={"Training-key": TRAINING_KEY}
    )
    trainer = CustomVisionTrainingClient(TRAINING_ENDPOINT, credentials)

    # Run the full workflow
    project = create_project(trainer)
    tags = upload_training_images(trainer, project)

    # Only train if images were uploaded
    print("\n  ℹ️  To train: add images to training-images/<category>/ folders")
    print("  and re-run this script.\n")

    # Uncomment when training images are available:
    # iteration = train_model(trainer, project)
    # if iteration:
    #     publish_name = publish_model(trainer, project, iteration)
    #     if publish_name:
    #         predict_image(publish_name, project.id)

    # EXAM TIPS:
    # ──────────
    # • Min 5 images per tag (15+ recommended for quality).
    # • Compact domains export to ONNX, CoreML, TensorFlow, etc.
    # • General (non-compact) domains run only in the cloud.
    # • Training types: Quick (default) or Advanced (budget in hours).
    # • Publish an iteration to make it available for predictions.
    # • Two resources needed: Training and Prediction (can be same multi).
    # • Performance metrics: Precision, Recall, Average Precision (AP).
    # • For new projects, consider Azure AI Vision custom models instead.

    # CLEANUP NOTE:
    # Delete the Custom Vision project when done:
    #   trainer.delete_project(project.id)
    # Also delete the Custom Vision resources to stop charges.
