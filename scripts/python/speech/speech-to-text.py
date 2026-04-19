"""
AI-102 Lab 5.3: Speech to Text
================================
Exam Objective: Implement natural language processing solutions
  - Implement speech-to-text
  - Configure speech recognition
  - Implement continuous recognition for long audio

This script demonstrates:
  1. Recognize speech from an audio file (single-shot)
  2. Continuous recognition for long audio
  3. Configuration options (language, profanity filter, etc.)

Prerequisites:
  - pip install azure-cognitiveservices-speech python-dotenv
  - An Azure Speech resource
  - .env file with SPEECH_KEY and SPEECH_REGION
  - An audio file in WAV format for testing
"""

import os
import time
import threading
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
load_dotenv()

SPEECH_KEY = os.getenv("SPEECH_KEY")
SPEECH_REGION = os.getenv("SPEECH_REGION", "eastus")

if not SPEECH_KEY:
    raise EnvironmentError("Set SPEECH_KEY in your .env file.")

SAMPLE_AUDIO = os.path.join(os.path.dirname(__file__), "sample-audio.wav")


# ===========================================================================
# 1. Single-shot recognition from audio file
# ===========================================================================
def recognize_from_file():
    """
    Recognize speech from an audio file (single utterance).

    EXAM TIP: Single-shot recognition stops after silence is detected
    or 15 seconds of audio, whichever comes first. Use continuous
    recognition for longer audio.
    """
    print("=" * 60)
    print("1. SINGLE-SHOT RECOGNITION (from audio file)")
    print("=" * 60)

    # Configure speech service
    speech_config = speechsdk.SpeechConfig(
        subscription=SPEECH_KEY,
        region=SPEECH_REGION,
    )

    # Set recognition language
    speech_config.speech_recognition_language = "en-US"

    # Optional: enable profanity filtering
    speech_config.set_profanity(speechsdk.ProfanityOption.Masked)

    # Optional: request word-level timestamps
    speech_config.request_word_level_timestamps()

    # Configure audio input from file
    if not os.path.exists(SAMPLE_AUDIO):
        print(f"  ⚠️  Audio file not found: {SAMPLE_AUDIO}")
        print("  Place a WAV file at this path to test file recognition.")
        print("  Demonstrating with microphone input instead...\n")
        # Fall back to default microphone
        audio_config = speechsdk.AudioConfig(use_default_microphone=True)
    else:
        audio_config = speechsdk.AudioConfig(filename=SAMPLE_AUDIO)

    # Create recognizer
    recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config,
        audio_config=audio_config,
    )

    try:
        print("  Recognizing speech...")
        result = recognizer.recognize_once()

        # Handle the result based on reason
        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print(f"  ✅ Recognized: \"{result.text}\"")
            print(f"  Duration: {result.duration / 10_000_000:.2f}s")
            print(f"  Offset: {result.offset / 10_000_000:.2f}s")

        elif result.reason == speechsdk.ResultReason.NoMatch:
            no_match = result.no_match_details
            print(f"  ⚠️  No match – Reason: {no_match.reason}")

        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation = result.cancellation_details
            print(f"  ❌ Canceled – Reason: {cancellation.reason}")
            if cancellation.reason == speechsdk.CancellationReason.Error:
                print(f"  Error: {cancellation.error_details}")

    except Exception as exc:
        print(f"  Error: {exc}")


# ===========================================================================
# 2. Continuous recognition (for long audio)
# ===========================================================================
def continuous_recognition():
    """
    Continuous recognition processes audio until explicitly stopped.
    Ideal for long audio files, real-time transcription, or meetings.

    EXAM TIP: Continuous recognition uses event callbacks:
      - recognizing: interim/partial results
      - recognized: final results for each utterance
      - canceled: recognition was canceled
      - session_stopped: session ended
    """
    print("\n" + "=" * 60)
    print("2. CONTINUOUS RECOGNITION")
    print("=" * 60)

    speech_config = speechsdk.SpeechConfig(
        subscription=SPEECH_KEY,
        region=SPEECH_REGION,
    )
    speech_config.speech_recognition_language = "en-US"

    # Enable detailed output format for more information
    speech_config.output_format = speechsdk.OutputFormat.Detailed

    if not os.path.exists(SAMPLE_AUDIO):
        print("  ⚠️  Audio file not found. Skipping continuous recognition demo.\n")
        print("  In production, continuous recognition would be set up like this:")
        print("    recognizer.recognized.connect(callback)")
        print("    recognizer.start_continuous_recognition()")
        print("    # ... wait for completion ...")
        print("    recognizer.stop_continuous_recognition()\n")
        return

    audio_config = speechsdk.AudioConfig(filename=SAMPLE_AUDIO)
    recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config,
        audio_config=audio_config,
    )

    # Use an event to signal when recognition is done
    done_event = threading.Event()
    all_results = []

    def on_recognizing(evt):
        """Called with partial/interim results."""
        print(f"    [Partial] {evt.result.text}")

    def on_recognized(evt):
        """Called with final results for each utterance."""
        if evt.result.reason == speechsdk.ResultReason.RecognizedSpeech:
            all_results.append(evt.result.text)
            print(f"    [Final]   {evt.result.text}")

    def on_canceled(evt):
        """Called when recognition is canceled."""
        print(f"    [Canceled] {evt.cancellation_details.reason}")
        done_event.set()

    def on_session_stopped(evt):
        """Called when the session ends."""
        print("    [Session stopped]")
        done_event.set()

    # Connect event handlers
    recognizer.recognizing.connect(on_recognizing)
    recognizer.recognized.connect(on_recognized)
    recognizer.canceled.connect(on_canceled)
    recognizer.session_stopped.connect(on_session_stopped)

    try:
        print("  Starting continuous recognition...")
        recognizer.start_continuous_recognition()

        # Wait for completion (timeout after 60 seconds)
        done_event.wait(timeout=60)

        recognizer.stop_continuous_recognition()

        print(f"\n  Full transcript ({len(all_results)} utterances):")
        print(f"  {' '.join(all_results)}\n")

    except Exception as exc:
        print(f"  Error: {exc}")


# ===========================================================================
# 3. Configuration options reference
# ===========================================================================
def show_configuration_options():
    """
    Reference for common speech recognition configuration options.
    """
    print("=" * 60)
    print("3. CONFIGURATION OPTIONS REFERENCE")
    print("=" * 60)

    print("""
  Language options:
    speech_config.speech_recognition_language = "en-US"
    speech_config.speech_recognition_language = "es-ES"
    speech_config.speech_recognition_language = "ja-JP"

  Auto language detection (up to 4 languages):
    auto_detect = speechsdk.AutoDetectSourceLanguageConfig(
        languages=["en-US", "es-ES", "fr-FR", "de-DE"]
    )

  Profanity handling:
    speech_config.set_profanity(speechsdk.ProfanityOption.Raw)     # No filter
    speech_config.set_profanity(speechsdk.ProfanityOption.Masked)  # ****
    speech_config.set_profanity(speechsdk.ProfanityOption.Removed) # Removed

  Audio formats:
    WAV (PCM, 16-bit, mono, 16kHz) – default/recommended
    MP3, OGG/Opus, FLAC – also supported
    Compressed audio needs: speechsdk.AudioStreamFormat

  Custom speech models:
    speech_config.endpoint_id = "<custom-model-endpoint-id>"
    """)


# ===========================================================================
# Main
# ===========================================================================
if __name__ == "__main__":
    print("\nAI-102 Lab 5.3 – Speech to Text\n")

    recognize_from_file()
    continuous_recognition()
    show_configuration_options()

    # EXAM TIPS:
    # ──────────
    # • Single-shot: recognize_once() – one utterance, max ~15s.
    # • Continuous: start/stop_continuous_recognition() – long audio.
    # • Audio input: microphone, file, or stream.
    # • Default audio format: WAV PCM 16-bit mono 16kHz.
    # • Auto language detection: up to 4 candidate languages.
    # • Custom Speech: train custom models for domain-specific vocabulary.
    # • Word-level timestamps available via request_word_level_timestamps().
    # • Pronunciation assessment available for language learning scenarios.
    # • Real-time transcription uses WebSocket under the hood.

    # CLEANUP NOTE:
    # Speech service charges per audio hour. Delete the resource when done.
