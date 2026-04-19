"""
AI-102 Lab 2.4: DALL-E Image Generation
=========================================
Exam Objective: Implement generative AI solutions with Azure OpenAI Service
  - Generate images using DALL-E models
  - Configure image generation parameters
  - Handle content filter responses

This script demonstrates:
  1. Basic image generation with DALL-E
  2. Different size and quality options
  3. Handling content filter rejections

Prerequisites:
  - pip install openai python-dotenv
  - An Azure OpenAI resource with a DALL-E model deployed (e.g., dall-e-3)
  - .env file with AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_KEY
"""

import os
from dotenv import load_dotenv
from openai import AzureOpenAI, BadRequestError

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
load_dotenv()

ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
API_KEY = os.getenv("AZURE_OPENAI_KEY")
DALLE_DEPLOYMENT = os.getenv("AZURE_OPENAI_DALLE_DEPLOYMENT", "dall-e-3")
API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-06-01")

if not ENDPOINT or not API_KEY:
    raise EnvironmentError(
        "Set AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_KEY in your .env file."
    )

client = AzureOpenAI(
    azure_endpoint=ENDPOINT,
    api_key=API_KEY,
    api_version=API_VERSION,
)


# ===========================================================================
# 1. Basic image generation
# ===========================================================================
def generate_basic_image():
    """
    Generate an image with a text prompt.

    EXAM TIP: DALL-E 3 sizes: 1024x1024, 1024x1792, 1792x1024
              DALL-E 2 sizes: 256x256, 512x512, 1024x1024
    """
    print("=" * 60)
    print("1. BASIC IMAGE GENERATION")
    print("=" * 60)

    prompt = (
        "A futuristic data center in the clouds with glowing blue servers, "
        "digital art style, clean and professional"
    )

    try:
        response = client.images.generate(
            model=DALLE_DEPLOYMENT,
            prompt=prompt,
            n=1,                  # Number of images (DALL-E 3: only n=1)
            size="1024x1024",     # Image dimensions
            quality="standard",   # "standard" or "hd" (DALL-E 3 only)
            style="vivid",        # "vivid" or "natural" (DALL-E 3 only)
        )

        image_url = response.data[0].url
        revised_prompt = response.data[0].revised_prompt

        print(f"\n  Prompt:  {prompt[:60]}...")
        print(f"  Revised: {revised_prompt[:80]}...")
        print(f"  URL:     {image_url[:80]}...")
        print(f"  ✅ Image generated successfully.\n")

    except BadRequestError as exc:
        print(f"  Content filter triggered: {exc.message}\n")
    except Exception as exc:
        print(f"  Error: {exc}\n")


# ===========================================================================
# 2. Different size and quality options
# ===========================================================================
def generate_with_options():
    """
    Show different configuration options for image generation.

    EXAM TIP:
      - quality="hd" costs more tokens but produces higher detail
      - style="natural" produces more photorealistic images
      - DALL-E 3 always returns 1 image per request (n=1)
      - DALL-E 2 can return up to 10 (n=1..10)
    """
    print("=" * 60)
    print("2. SIZE AND QUALITY OPTIONS")
    print("=" * 60)

    configurations = [
        {"size": "1024x1024", "quality": "standard", "style": "vivid"},
        {"size": "1792x1024", "quality": "hd", "style": "natural"},
    ]

    prompt = "A simple diagram showing cloud computing architecture"

    for config in configurations:
        desc = f"{config['size']}, {config['quality']}, {config['style']}"
        print(f"\n  Config: {desc}")

        try:
            response = client.images.generate(
                model=DALLE_DEPLOYMENT,
                prompt=prompt,
                n=1,
                **config,
            )

            image_url = response.data[0].url
            print(f"  ✅ Generated: {image_url[:70]}...")

        except BadRequestError as exc:
            print(f"  ⚠️  Content filter: {exc.message}")
        except Exception as exc:
            print(f"  Error: {exc}")


# ===========================================================================
# 3. Handling content filter responses
# ===========================================================================
def handle_content_filter():
    """
    Demonstrate how content filter rejections are handled.

    EXAM TIP: Azure OpenAI applies content filters to DALL-E prompts and
    generated images. A BadRequestError with code 'contentFilter' is
    returned when the prompt or output is flagged.
    """
    print("\n" + "=" * 60)
    print("3. CONTENT FILTER HANDLING")
    print("=" * 60)

    # A safe prompt to demonstrate the try/except pattern
    safe_prompt = "A friendly robot teaching a class of students"

    print(f"\n  Testing safe prompt: \"{safe_prompt}\"")

    try:
        response = client.images.generate(
            model=DALLE_DEPLOYMENT,
            prompt=safe_prompt,
            n=1,
            size="1024x1024",
        )
        print(f"  ✅ Image generated successfully.")
        print(f"  URL: {response.data[0].url[:70]}...")

    except BadRequestError as exc:
        # Check if it's a content filter rejection
        error_body = getattr(exc, "body", {}) or {}
        error_code = error_body.get("code", "") if isinstance(error_body, dict) else ""

        if "content" in str(exc).lower() or error_code == "contentFilter":
            print("  🚫 Content filter rejected the request.")
            print(f"  Reason: {exc.message}")
            print("  Action: Modify the prompt to avoid flagged content.")
        else:
            print(f"  Bad request: {exc.message}")

    except Exception as exc:
        print(f"  Unexpected error: {exc}")

    # Pattern for production: retry with modified prompt
    print("\n  Production pattern for content filter handling:")
    print("    1. Catch BadRequestError")
    print("    2. Check for contentFilter error code")
    print("    3. Log the rejection for review")
    print("    4. Return a user-friendly message")
    print("    5. Optionally retry with a sanitized prompt\n")


# ===========================================================================
# Main
# ===========================================================================
if __name__ == "__main__":
    print("\nAI-102 Lab 2.4 – DALL-E Image Generation\n")

    generate_basic_image()
    generate_with_options()
    handle_content_filter()

    # EXAM TIPS:
    # ──────────
    # • DALL-E 3: 1024x1024, 1024x1792, 1792x1024 (no 256/512).
    # • DALL-E 3: n=1 only; DALL-E 2: n=1..10.
    # • DALL-E 3 may revise your prompt for better results (revised_prompt).
    # • quality="hd" increases detail and cost.
    # • style="vivid" = hyper-real; "natural" = photorealistic.
    # • Content filters apply to both input prompts and output images.
    # • Generated image URLs are temporary – download/store if needed.
    # • Pricing is per image, varies by size and quality.

    # CLEANUP NOTE:
    # DALL-E charges per image generated. Delete the deployment if no
    # longer needed to avoid accidental charges.
