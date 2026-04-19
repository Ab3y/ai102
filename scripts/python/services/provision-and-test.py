"""
AI-102 Lab 1.1: Provision and Test Azure AI Services
=====================================================
Exam Objective: Plan and manage an Azure AI solution
  - Create and manage an Azure AI Services resource
  - Configure diagnostic logging
  - Manage costs for Azure AI Services

This script demonstrates two ways to call Azure AI Services:
  1. Using the Python SDK (azure-ai-textanalytics)
  2. Using the REST API directly (requests library)

Prerequisites:
  - pip install azure-ai-textanalytics python-dotenv requests
  - An Azure AI Services (multi-service) or Language resource
  - .env file with AI_SERVICES_ENDPOINT and AI_SERVICES_KEY
"""

import os
import json
import requests
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# ---------------------------------------------------------------------------
# Configuration – load credentials from .env
# ---------------------------------------------------------------------------
load_dotenv()

ENDPOINT = os.getenv("AI_SERVICES_ENDPOINT")
API_KEY = os.getenv("AI_SERVICES_KEY")

if not ENDPOINT or not API_KEY:
    raise EnvironmentError(
        "Set AI_SERVICES_ENDPOINT and AI_SERVICES_KEY in your .env file."
    )

# Sample texts in different languages for language detection
SAMPLE_TEXTS = [
    "Hello, how are you today?",
    "Bonjour, comment allez-vous aujourd'hui?",
    "Hola, ¿cómo estás hoy?",
    "こんにちは、お元気ですか？",
    "Hallo, wie geht es Ihnen heute?",
]


# ===========================================================================
# APPROACH 1: Python SDK (recommended for production)
# ===========================================================================
def detect_language_sdk():
    """Use the azure-ai-textanalytics SDK to detect language."""
    print("=" * 60)
    print("APPROACH 1: Python SDK (azure-ai-textanalytics)")
    print("=" * 60)

    # Create the client with endpoint + key credential
    credential = AzureKeyCredential(API_KEY)
    client = TextAnalyticsClient(endpoint=ENDPOINT, credential=credential)

    try:
        # detect_language accepts a list of strings or DetectLanguageInput
        results = client.detect_language(documents=SAMPLE_TEXTS)

        for idx, result in enumerate(results):
            if result.is_error:
                print(f"  Document {idx}: ERROR – {result.error.message}")
                continue

            lang = result.primary_language
            print(
                f"  Text: {SAMPLE_TEXTS[idx][:40]}...\n"
                f"    Language : {lang.name} ({lang.iso6391_name})\n"
                f"    Confidence: {lang.confidence_score:.2%}\n"
            )

    except Exception as exc:
        print(f"SDK error: {exc}")


# ===========================================================================
# APPROACH 2: REST API (useful for understanding what the SDK does)
# ===========================================================================
def detect_language_rest():
    """Call the Language Detection REST API directly with requests."""
    print("=" * 60)
    print("APPROACH 2: REST API (requests library)")
    print("=" * 60)

    # EXAM TIP: The REST endpoint path for language detection
    url = f"{ENDPOINT}/text/analytics/v3.1/languages"

    headers = {
        "Ocp-Apim-Subscription-Key": API_KEY,
        "Content-Type": "application/json",
    }

    # Build the request body – each document needs an id and text
    body = {
        "documents": [
            {"id": str(i + 1), "text": text}
            for i, text in enumerate(SAMPLE_TEXTS)
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=body, timeout=30)
        response.raise_for_status()

        data = response.json()

        for doc in data.get("documents", []):
            doc_idx = int(doc["id"]) - 1
            lang = doc["detectedLanguage"]
            print(
                f"  Text: {SAMPLE_TEXTS[doc_idx][:40]}...\n"
                f"    Language : {lang['name']} ({lang['iso6391Name']})\n"
                f"    Confidence: {lang['confidenceScore']:.2%}\n"
            )

        # Show any errors
        for err in data.get("errors", []):
            print(f"  Document {err['id']}: ERROR – {err['error']['message']}")

    except requests.exceptions.RequestException as exc:
        print(f"REST API error: {exc}")


# ===========================================================================
# Main
# ===========================================================================
if __name__ == "__main__":
    print("\nAI-102 Lab 1.1 – Provision and Test Azure AI Services\n")
    detect_language_sdk()
    print()
    detect_language_rest()

    # EXAM TIP:
    # - A multi-service resource uses a single endpoint/key for many services.
    # - A single-service resource (e.g., Language) has its own endpoint/key.
    # - Both approaches (SDK vs REST) hit the same underlying API.
    # - SDK handles retries, serialization, and auth automatically.

    # CLEANUP NOTE:
    # Delete the Azure AI Services resource when no longer needed to avoid
    # charges.  Resources can be soft-deleted and purged from the portal.
