"""
AI-102 Lab 4.1: Analyze Images with Azure AI Vision
=====================================================
Exam Objective: Implement computer vision solutions
  - Analyze images using Azure AI Vision
  - Extract text from images using OCR (Read)
  - Detect objects and people in images
  - Generate captions and tags

This script demonstrates:
  1. Image analysis with multiple visual features
  2. Caption generation (dense captions)
  3. Object detection with bounding boxes
  4. Tag extraction with confidence scores
  5. OCR / Read text from images
  6. People detection

Prerequisites:
  - pip install azure-ai-vision-imageanalysis python-dotenv
  - An Azure AI Vision (or multi-service) resource
  - .env file with VISION_ENDPOINT and VISION_KEY

EXAM TIP: File limits –
  - Max file size: 4 MB
  - Max image dimensions: 20 megapixels
  - Min dimensions: 50 x 50 pixels
  - Supported formats: JPEG, PNG, GIF, BMP, TIFF, ICO, WEBP
"""

import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
load_dotenv()

ENDPOINT = os.getenv("VISION_ENDPOINT")
API_KEY = os.getenv("VISION_KEY")

if not ENDPOINT or not API_KEY:
    raise EnvironmentError(
        "Set VISION_ENDPOINT and VISION_KEY in your .env file."
    )

client = ImageAnalysisClient(
    endpoint=ENDPOINT,
    credential=AzureKeyCredential(API_KEY),
)

# Sample image URL (publicly accessible)
SAMPLE_IMAGE_URL = (
    "https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/"
    "media/quickstarts/presentation.png"
)


# ===========================================================================
# 1. Full image analysis
# ===========================================================================
def analyze_image():
    """
    Analyze an image with multiple visual features in a single call.

    EXAM TIP: You can request multiple features in one API call.
    Each feature adds to the cost but reduces latency vs. separate calls.
    """
    print("=" * 60)
    print("1. FULL IMAGE ANALYSIS")
    print("=" * 60)

    try:
        result = client.analyze_from_url(
            image_url=SAMPLE_IMAGE_URL,
            visual_features=[
                VisualFeatures.CAPTION,
                VisualFeatures.DENSE_CAPTIONS,
                VisualFeatures.TAGS,
                VisualFeatures.OBJECTS,
                VisualFeatures.READ,
                VisualFeatures.PEOPLE,
                VisualFeatures.SMART_CROPS,
            ],
            gender_neutral_caption=True,  # Use gender-neutral language
            smart_crops_aspect_ratios=[0.9, 1.33],
        )

        # --- Caption ---
        print("\n  📝 CAPTION:")
        if result.caption:
            print(f"    \"{result.caption.text}\"")
            print(f"    Confidence: {result.caption.confidence:.2%}")

        # --- Dense Captions ---
        print("\n  📝 DENSE CAPTIONS:")
        if result.dense_captions:
            for caption in result.dense_captions.list[:5]:
                bbox = caption.bounding_box
                print(
                    f"    \"{caption.text}\" "
                    f"(confidence: {caption.confidence:.2%}, "
                    f"bbox: [{bbox.x}, {bbox.y}, {bbox.width}, {bbox.height}])"
                )

        # --- Tags ---
        print("\n  🏷️  TAGS:")
        if result.tags:
            for tag in result.tags.list:
                print(f"    {tag.name:<25} confidence: {tag.confidence:.2%}")

        # --- Objects ---
        print("\n  📦 OBJECTS:")
        if result.objects:
            for obj in result.objects.list:
                bbox = obj.bounding_box
                print(
                    f"    {obj.tags[0].name:<20} "
                    f"confidence: {obj.tags[0].confidence:.2%}  "
                    f"bbox: [{bbox.x}, {bbox.y}, {bbox.width}, {bbox.height}]"
                )
        else:
            print("    No objects detected.")

        # --- Read (OCR) ---
        print("\n  📖 READ (OCR):")
        if result.read and result.read.blocks:
            for block in result.read.blocks:
                for line in block.lines:
                    print(f"    \"{line.text}\"")
                    # Each line has bounding polygon and word-level details
        else:
            print("    No text detected.")

        # --- People ---
        print("\n  👤 PEOPLE:")
        if result.people:
            for person in result.people.list:
                bbox = person.bounding_box
                print(
                    f"    Person detected – "
                    f"confidence: {person.confidence:.2%}  "
                    f"bbox: [{bbox.x}, {bbox.y}, {bbox.width}, {bbox.height}]"
                )
        else:
            print("    No people detected.")

        # --- Smart Crops ---
        print("\n  ✂️  SMART CROPS:")
        if result.smart_crops:
            for crop in result.smart_crops.list:
                bbox = crop.bounding_box
                print(
                    f"    Aspect ratio: {crop.aspect_ratio}  "
                    f"bbox: [{bbox.x}, {bbox.y}, {bbox.width}, {bbox.height}]"
                )

    except Exception as exc:
        print(f"  Error: {exc}")


# ===========================================================================
# 2. Analyze from a local file
# ===========================================================================
def analyze_local_image(image_path: str):
    """
    Analyze a local image file instead of a URL.

    EXAM TIP: Use analyze() for local files, analyze_from_url() for URLs.
    """
    print("\n" + "=" * 60)
    print("2. ANALYZE LOCAL IMAGE")
    print("=" * 60)

    if not os.path.exists(image_path):
        print(f"  Skipped – File not found: {image_path}\n")
        return

    try:
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()

        result = client.analyze(
            image_data=image_data,
            visual_features=[VisualFeatures.CAPTION, VisualFeatures.TAGS],
        )

        if result.caption:
            print(f"  Caption: \"{result.caption.text}\" ({result.caption.confidence:.2%})")

        if result.tags:
            tags = ", ".join(f"{t.name} ({t.confidence:.0%})" for t in result.tags.list[:5])
            print(f"  Top tags: {tags}")

    except Exception as exc:
        print(f"  Error: {exc}")


# ===========================================================================
# Main
# ===========================================================================
if __name__ == "__main__":
    print("\nAI-102 Lab 4.1 – Analyze Images with Azure AI Vision\n")

    analyze_image()
    analyze_local_image("sample-image.jpg")

    # EXAM TIPS:
    # ──────────
    # • Max file size: 4 MB, max dimensions: 20 megapixels.
    # • Supported formats: JPEG, PNG, GIF, BMP, TIFF, ICO, WEBP.
    # • Caption vs Dense Captions: caption = one sentence for whole image,
    #   dense captions = multiple captions for regions.
    # • Objects include bounding boxes (x, y, width, height).
    # • Read (OCR) returns blocks → lines → words with bounding polygons.
    # • Smart crops suggest optimal crop regions for given aspect ratios.
    # • gender_neutral_caption=True avoids gender assumptions.
    # • Use the 4.0 API (azure-ai-vision-imageanalysis) not the older
    #   azure-cognitiveservices-vision-computervision.

    # CLEANUP NOTE:
    # Azure AI Vision charges per transaction. Delete the resource when done.
