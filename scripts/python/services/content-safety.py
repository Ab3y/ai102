"""
AI-102 Lab 1.5: Content Safety
================================
Exam Objective: Plan and manage an Azure AI solution
  - Implement responsible AI practices
  - Configure content filters and safety settings

This script demonstrates:
  1. Text content analysis across four harm categories
  2. Understanding severity levels (0–6)
  3. Creating and using a blocklist

Prerequisites:
  - pip install azure-ai-contentsafety python-dotenv
  - An Azure Content Safety resource
  - .env file with CONTENT_SAFETY_ENDPOINT and CONTENT_SAFETY_KEY
"""

import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import HttpResponseError
from azure.ai.contentsafety import ContentSafetyClient, BlocklistClient
from azure.ai.contentsafety.models import (
    AnalyzeTextOptions,
    TextCategory,
    TextBlocklistMatch,
    AddOrUpdateTextBlocklistItemsOptions,
    TextBlocklistItem,
)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
load_dotenv()

ENDPOINT = os.getenv("CONTENT_SAFETY_ENDPOINT")
API_KEY = os.getenv("CONTENT_SAFETY_KEY")

if not ENDPOINT or not API_KEY:
    raise EnvironmentError(
        "Set CONTENT_SAFETY_ENDPOINT and CONTENT_SAFETY_KEY in your .env file."
    )

credential = AzureKeyCredential(API_KEY)

# Severity level descriptions for reference
SEVERITY_DESCRIPTIONS = {
    0: "Safe – no harmful content detected",
    2: "Low – minor concern",
    4: "Medium – moderate concern",
    6: "High – severe harmful content",
}


# ===========================================================================
# 1. Analyze text for harmful content
# ===========================================================================
def analyze_text():
    """
    Analyze text across four harm categories:
      - Hate and fairness
      - Violence
      - Sexual
      - Self-harm

    EXAM TIP: Severity levels are 0, 2, 4, 6 (even numbers only).
    Each category is scored independently.
    """
    print("=" * 60)
    print("1. TEXT CONTENT ANALYSIS")
    print("=" * 60)

    client = ContentSafetyClient(ENDPOINT, credential)

    # Sample texts to analyze (benign examples for testing)
    test_texts = [
        "The weather is beautiful today and I love spending time with friends.",
        "The villain in the movie threatened to destroy the entire city.",
        "The documentary explored the historical impact of armed conflict.",
    ]

    for text in test_texts:
        print(f"\n  Text: \"{text[:60]}...\"" if len(text) > 60 else f"\n  Text: \"{text}\"")

        try:
            request = AnalyzeTextOptions(text=text)
            response = client.analyze_text(request)

            # Print results for each harm category
            categories = {
                "Hate":      response.categories_analysis[0] if len(response.categories_analysis) > 0 else None,
                "SelfHarm":  response.categories_analysis[1] if len(response.categories_analysis) > 1 else None,
                "Sexual":    response.categories_analysis[2] if len(response.categories_analysis) > 2 else None,
                "Violence":  response.categories_analysis[3] if len(response.categories_analysis) > 3 else None,
            }

            for result in response.categories_analysis:
                severity = result.severity
                desc = SEVERITY_DESCRIPTIONS.get(severity, "Unknown")
                print(f"    {result.category:<12} severity={severity}  ({desc})")

        except HttpResponseError as exc:
            print(f"    Error: {exc.message}")
        except Exception as exc:
            print(f"    Error: {exc}")


# ===========================================================================
# 2. Create and use a blocklist
# ===========================================================================
def blocklist_example():
    """
    Blocklists let you define custom terms that should always be flagged,
    regardless of the model's assessment.

    EXAM TIP: Blocklists are useful for brand-specific or domain-specific
    terms that the general model may not flag.
    """
    print("\n" + "=" * 60)
    print("2. BLOCKLIST EXAMPLE")
    print("=" * 60)

    blocklist_name = "ai102-demo-blocklist"
    blocklist_client = BlocklistClient(ENDPOINT, credential)
    content_client = ContentSafetyClient(ENDPOINT, credential)

    try:
        # Step 1: Create a blocklist
        print(f"\n  Creating blocklist: {blocklist_name}")
        blocklist_client.create_or_update_text_blocklist(
            blocklist_name=blocklist_name,
            options={"blocklistName": blocklist_name, "description": "AI-102 demo blocklist"},
        )
        print("  ✅ Blocklist created.")

        # Step 2: Add items to the blocklist
        block_items = [
            TextBlocklistItem(text="forbidden-term-alpha", description="Demo term 1"),
            TextBlocklistItem(text="forbidden-term-beta", description="Demo term 2"),
        ]

        blocklist_client.add_or_update_blocklist_items(
            blocklist_name=blocklist_name,
            options=AddOrUpdateTextBlocklistItemsOptions(blocklist_items=block_items),
        )
        print(f"  ✅ Added {len(block_items)} items to blocklist.")

        # Step 3: Analyze text with the blocklist
        test_text = "This message contains forbidden-term-alpha in the middle."
        print(f"\n  Analyzing: \"{test_text}\"")

        request = AnalyzeTextOptions(
            text=test_text,
            blocklist_names=[blocklist_name],
            halt_on_blocklist_hit=False,  # True = stop analysis on first match
        )
        response = content_client.analyze_text(request)

        if response.blocklists_match:
            for match in response.blocklists_match:
                print(
                    f"    🚫 Blocklist hit: '{match.blocklist_item_text}' "
                    f"(blocklist: {match.blocklist_name})"
                )
        else:
            print("    No blocklist matches found.")

    except HttpResponseError as exc:
        print(f"  Error: {exc.message}")
    except Exception as exc:
        print(f"  Error: {exc}")

    finally:
        # Cleanup: delete the demo blocklist
        try:
            blocklist_client.delete_text_blocklist(blocklist_name=blocklist_name)
            print(f"\n  🧹 Cleaned up blocklist: {blocklist_name}")
        except Exception:
            pass


# ===========================================================================
# Main
# ===========================================================================
if __name__ == "__main__":
    print("\nAI-102 Lab 1.5 – Content Safety\n")

    analyze_text()
    blocklist_example()

    # EXAM TIPS:
    # ──────────
    # • Four categories: Hate, Violence, Sexual, Self-Harm.
    # • Severity levels: 0 (safe), 2 (low), 4 (medium), 6 (high).
    # • Blocklists add custom term matching on top of model analysis.
    # • halt_on_blocklist_hit=True stops analysis on first blocklist match.
    # • Content Safety is separate from Azure OpenAI content filters.
    # • Text limit: 10,000 characters per request.
    # • Image analysis also available (AnalyzeImageOptions).

    # CLEANUP NOTE:
    # The blocklist is deleted automatically above. Delete the Content
    # Safety resource if no longer needed.
