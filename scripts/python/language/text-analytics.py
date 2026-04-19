"""
AI-102 Lab 5.1: Text Analytics
================================
Exam Objective: Implement natural language processing solutions
  - Analyze sentiment
  - Extract key phrases
  - Recognize entities (NER)
  - Detect and redact PII
  - Detect language

This script demonstrates:
  1. Sentiment analysis (positive/negative/neutral/mixed)
  2. Key phrase extraction
  3. Named entity recognition (NER)
  4. PII detection and redaction
  5. Language detection
  6. Batch processing of multiple documents

Prerequisites:
  - pip install azure-ai-textanalytics python-dotenv
  - An Azure AI Language (or multi-service) resource
  - .env file with AI_SERVICES_ENDPOINT and AI_SERVICES_KEY
"""

import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
load_dotenv()

ENDPOINT = os.getenv("AI_SERVICES_ENDPOINT")
API_KEY = os.getenv("AI_SERVICES_KEY")

if not ENDPOINT or not API_KEY:
    raise EnvironmentError(
        "Set AI_SERVICES_ENDPOINT and AI_SERVICES_KEY in your .env file."
    )

client = TextAnalyticsClient(
    endpoint=ENDPOINT,
    credential=AzureKeyCredential(API_KEY),
)

# Sample documents for analysis
DOCUMENTS = [
    "The hotel was excellent! Great location and friendly staff. Highly recommend.",
    "The food was terrible and the service was slow. Very disappointing experience.",
    "Microsoft was founded by Bill Gates and Paul Allen in Albuquerque, New Mexico.",
    "My email is john.doe@example.com and my phone number is 555-123-4567.",
    "Je suis très content de ce produit. Il fonctionne parfaitement.",
]


# ===========================================================================
# 1. Sentiment Analysis
# ===========================================================================
def analyze_sentiment():
    """
    Analyze document-level and sentence-level sentiment.

    EXAM TIP: Sentiment values are positive, negative, neutral, or mixed.
    Each comes with confidence scores that sum to 1.0.
    "Mixed" appears at document level when sentences have different sentiments.
    """
    print("=" * 60)
    print("1. SENTIMENT ANALYSIS")
    print("=" * 60)

    docs = DOCUMENTS[:2]  # Use the review texts

    try:
        results = client.analyze_sentiment(
            documents=docs,
            show_opinion_mining=True,  # Aspect-based sentiment
        )

        for idx, result in enumerate(results):
            if result.is_error:
                print(f"  Doc {idx}: ERROR – {result.error.message}")
                continue

            print(f"\n  Document {idx}: \"{docs[idx][:50]}...\"")
            print(f"    Overall sentiment: {result.sentiment}")
            print(
                f"    Scores: pos={result.confidence_scores.positive:.2f} "
                f"neu={result.confidence_scores.neutral:.2f} "
                f"neg={result.confidence_scores.negative:.2f}"
            )

            # Sentence-level sentiment
            for sentence in result.sentences:
                print(f"    Sentence: \"{sentence.text[:40]}...\"")
                print(f"      Sentiment: {sentence.sentiment}")

                # Opinion mining (aspect-based sentiment)
                for opinion in sentence.mined_opinions:
                    target = opinion.target
                    print(f"      Target: \"{target.text}\" → {target.sentiment}")
                    for assessment in opinion.assessments:
                        print(f"        Assessment: \"{assessment.text}\" → {assessment.sentiment}")

    except Exception as exc:
        print(f"  Error: {exc}")


# ===========================================================================
# 2. Key Phrase Extraction
# ===========================================================================
def extract_key_phrases():
    """
    Extract key phrases from documents.

    EXAM TIP: Key phrases are noun phrases that represent the main topics.
    Useful for indexing, summarization, and topic modeling.
    """
    print("\n" + "=" * 60)
    print("2. KEY PHRASE EXTRACTION")
    print("=" * 60)

    try:
        results = client.extract_key_phrases(documents=DOCUMENTS[:3])

        for idx, result in enumerate(results):
            if result.is_error:
                print(f"  Doc {idx}: ERROR – {result.error.message}")
                continue

            print(f"\n  Document {idx}: \"{DOCUMENTS[idx][:50]}...\"")
            print(f"    Key phrases: {', '.join(result.key_phrases)}")

    except Exception as exc:
        print(f"  Error: {exc}")


# ===========================================================================
# 3. Named Entity Recognition (NER)
# ===========================================================================
def recognize_entities():
    """
    Recognize named entities (people, places, organizations, etc.).

    EXAM TIP: NER categories include Person, Location, Organization,
    DateTime, Quantity, URL, Email, PhoneNumber, and more.
    Entity linking resolves entities to Wikipedia.
    """
    print("\n" + "=" * 60)
    print("3. NAMED ENTITY RECOGNITION (NER)")
    print("=" * 60)

    docs = [DOCUMENTS[2]]  # Microsoft text

    try:
        results = client.recognize_entities(documents=docs)

        for idx, result in enumerate(results):
            if result.is_error:
                print(f"  Doc {idx}: ERROR – {result.error.message}")
                continue

            print(f"\n  Document: \"{docs[idx][:60]}...\"")
            for entity in result.entities:
                print(
                    f"    Entity: \"{entity.text}\" "
                    f"  Category: {entity.category}"
                    f"{'/' + entity.subcategory if entity.subcategory else ''}"
                    f"  Confidence: {entity.confidence_score:.2%}"
                    f"  Offset: {entity.offset}"
                )

    except Exception as exc:
        print(f"  Error: {exc}")


# ===========================================================================
# 4. PII Detection and Redaction
# ===========================================================================
def detect_pii():
    """
    Detect personally identifiable information (PII) and return redacted text.

    EXAM TIP: PII categories include Email, PhoneNumber, SSN, Address,
    CreditCardNumber, IPAddress, and more. The redacted_text replaces
    PII with category labels like [Email], [PhoneNumber].
    """
    print("\n" + "=" * 60)
    print("4. PII DETECTION AND REDACTION")
    print("=" * 60)

    docs = [DOCUMENTS[3]]  # Email and phone text

    try:
        results = client.recognize_pii_entities(
            documents=docs,
            categories_filter=["Email", "PhoneNumber", "Address"],
        )

        for idx, result in enumerate(results):
            if result.is_error:
                print(f"  Doc {idx}: ERROR – {result.error.message}")
                continue

            print(f"\n  Original:  \"{docs[idx]}\"")
            print(f"  Redacted:  \"{result.redacted_text}\"")

            for entity in result.entities:
                print(
                    f"    PII: \"{entity.text}\" "
                    f"  Category: {entity.category} "
                    f"  Confidence: {entity.confidence_score:.2%}"
                )

    except Exception as exc:
        print(f"  Error: {exc}")


# ===========================================================================
# 5. Language Detection
# ===========================================================================
def detect_language():
    """
    Detect the language of each document.

    EXAM TIP: Returns ISO 6391 language code and confidence score.
    Supports 120+ languages. Ambiguous or short text may have lower confidence.
    """
    print("\n" + "=" * 60)
    print("5. LANGUAGE DETECTION")
    print("=" * 60)

    try:
        results = client.detect_language(documents=DOCUMENTS)

        for idx, result in enumerate(results):
            if result.is_error:
                print(f"  Doc {idx}: ERROR – {result.error.message}")
                continue

            lang = result.primary_language
            print(
                f"  \"{DOCUMENTS[idx][:40]}...\"  →  "
                f"{lang.name} ({lang.iso6391_name}) "
                f"confidence: {lang.confidence_score:.2%}"
            )

    except Exception as exc:
        print(f"  Error: {exc}")


# ===========================================================================
# 6. Batch Processing
# ===========================================================================
def batch_processing():
    """
    Process multiple operations in a single batch using begin_analyze_actions.

    EXAM TIP: Batch processing is more efficient for large volumes.
    Each action type counts as a separate transaction for billing.
    Max 25 documents per request, max 5,120 characters per document.
    """
    print("\n" + "=" * 60)
    print("6. BATCH PROCESSING (multiple actions)")
    print("=" * 60)

    from azure.ai.textanalytics import (
        RecognizeEntitiesAction,
        ExtractKeyPhrasesAction,
        AnalyzeSentimentAction,
    )

    docs = DOCUMENTS[:3]

    try:
        poller = client.begin_analyze_actions(
            documents=docs,
            actions=[
                AnalyzeSentimentAction(),
                ExtractKeyPhrasesAction(),
                RecognizeEntitiesAction(),
            ],
        )

        results = poller.result()

        for doc_idx, action_results in enumerate(results):
            print(f"\n  Document {doc_idx}: \"{docs[doc_idx][:50]}...\"")

            for result in action_results:
                if result.is_error:
                    print(f"    ERROR: {result.error.message}")
                    continue

                kind = result.kind
                if kind == "SentimentAnalysis":
                    print(f"    Sentiment: {result.sentiment}")
                elif kind == "KeyPhraseExtraction":
                    print(f"    Key phrases: {', '.join(result.key_phrases[:3])}")
                elif kind == "EntityRecognition":
                    entities = [f"{e.text} ({e.category})" for e in result.entities[:3]]
                    print(f"    Entities: {', '.join(entities)}")

    except Exception as exc:
        print(f"  Error: {exc}")


# ===========================================================================
# Main
# ===========================================================================
if __name__ == "__main__":
    print("\nAI-102 Lab 5.1 – Text Analytics\n")

    analyze_sentiment()
    extract_key_phrases()
    recognize_entities()
    detect_pii()
    detect_language()
    batch_processing()

    # EXAM TIPS:
    # ──────────
    # • Max 25 documents per request, 5,120 characters per document.
    # • Opinion mining adds aspect-based sentiment (target + assessment).
    # • PII redaction replaces entities with category labels in redacted_text.
    # • Entity linking resolves entities to Wikipedia knowledge base.
    # • begin_analyze_actions is async (long-running operation with polling).
    # • Language detection supports 120+ languages.
    # • All text analytics features use the same TextAnalyticsClient.

    # CLEANUP NOTE:
    # Text analytics charges per text record (1 record = 1 document).
    # Delete the resource when no longer needed.
