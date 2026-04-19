"""
AI-102 Lab 5.3: Text to Speech
================================
Exam Objective: Implement natural language processing solutions
  - Implement text-to-speech
  - Configure speech synthesis
  - Use SSML for advanced control

This script demonstrates:
  1. Basic text-to-speech synthesis
  2. SSML-based synthesis with prosody, emphasis, breaks, and voice selection
  3. Saving speech output to audio files

Prerequisites:
  - pip install azure-cognitiveservices-speech python-dotenv
  - An Azure Speech resource
  - .env file with SPEECH_KEY and SPEECH_REGION
"""

import os
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


# ===========================================================================
# 1. Basic text-to-speech
# ===========================================================================
def basic_tts():
    """
    Synthesize speech from plain text.

    EXAM TIP: Default voice varies by language. You can choose from
    hundreds of neural voices across 100+ languages.
    """
    print("=" * 60)
    print("1. BASIC TEXT-TO-SPEECH")
    print("=" * 60)

    speech_config = speechsdk.SpeechConfig(
        subscription=SPEECH_KEY,
        region=SPEECH_REGION,
    )

    # Select a neural voice
    speech_config.speech_synthesis_voice_name = "en-US-JennyNeural"

    # Output to a WAV file instead of speakers
    output_file = os.path.join(os.path.dirname(__file__), "output-basic.wav")
    audio_config = speechsdk.AudioConfig(filename=output_file)

    synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config,
        audio_config=audio_config,
    )

    text = (
        "Welcome to the AI-102 certification preparation lab. "
        "Today we will learn about Azure AI Speech services."
    )

    try:
        print(f"  Synthesizing: \"{text[:50]}...\"")
        result = synthesizer.speak_text(text)

        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print(f"  ✅ Audio saved to: {output_file}")
            duration_ms = result.audio_duration.total_seconds() * 1000
            print(f"  Duration: {duration_ms:.0f}ms")

        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation = result.cancellation_details
            print(f"  ❌ Canceled: {cancellation.reason}")
            if cancellation.reason == speechsdk.CancellationReason.Error:
                print(f"  Error: {cancellation.error_details}")

    except Exception as exc:
        print(f"  Error: {exc}")


# ===========================================================================
# 2. SSML-based text-to-speech
# ===========================================================================
def ssml_tts():
    """
    Use Speech Synthesis Markup Language (SSML) for fine-grained control.

    EXAM TIP: SSML elements you should know:
      <speak>     – Root element with xml:lang
      <voice>     – Select voice (can switch mid-speech)
      <prosody>   – Control rate, pitch, volume
      <emphasis>  – Add emphasis (strong, moderate, reduced)
      <break>     – Insert pauses (time="500ms" or strength="medium")
      <say-as>    – Control pronunciation (date, number, telephone, etc.)
      <phoneme>   – Specify exact pronunciation with IPA/SAPI
      <mstts:express-as> – Emotional styles (cheerful, sad, etc.)
    """
    print("\n" + "=" * 60)
    print("2. SSML-BASED TEXT-TO-SPEECH")
    print("=" * 60)

    speech_config = speechsdk.SpeechConfig(
        subscription=SPEECH_KEY,
        region=SPEECH_REGION,
    )

    output_file = os.path.join(os.path.dirname(__file__), "output-ssml.wav")
    audio_config = speechsdk.AudioConfig(filename=output_file)

    synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config,
        audio_config=audio_config,
    )

    # SSML with multiple features demonstrated
    ssml = """
    <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
           xmlns:mstts="http://www.w3.org/2001/mstts"
           xml:lang="en-US">

        <!-- Voice selection -->
        <voice name="en-US-JennyNeural">

            <!-- Prosody: control rate and pitch -->
            <prosody rate="medium" pitch="default">
                Welcome to the Azure AI certification lab.
            </prosody>

            <!-- Break: insert a pause -->
            <break time="750ms"/>

            <!-- Emphasis -->
            Today we will focus on <emphasis level="strong">speech services</emphasis>,
            which is a key topic on the exam.

            <break time="500ms"/>

            <!-- Prosody: slow down for important info -->
            <prosody rate="slow" pitch="low">
                Remember: the Speech SDK supports both speech-to-text
                and text-to-speech in a single library.
            </prosody>

            <break time="500ms"/>

            <!-- Say-as: control how text is spoken -->
            The exam date is <say-as interpret-as="date" format="mdy">12/15/2024</say-as>.
            Call us at <say-as interpret-as="telephone">1-800-555-0199</say-as>.
            The cost is <say-as interpret-as="currency">$29.99</say-as>.

        </voice>

        <break time="1s"/>

        <!-- Switch to a different voice -->
        <voice name="en-US-GuyNeural">
            <prosody rate="fast" pitch="high">
                And now a different voice is speaking!
                This demonstrates voice switching within SSML.
            </prosody>
        </voice>

    </speak>
    """

    try:
        print("  Synthesizing SSML...")
        result = synthesizer.speak_ssml(ssml)

        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print(f"  ✅ Audio saved to: {output_file}")
            duration_ms = result.audio_duration.total_seconds() * 1000
            print(f"  Duration: {duration_ms:.0f}ms")
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation = result.cancellation_details
            print(f"  ❌ Canceled: {cancellation.reason}")
            if cancellation.reason == speechsdk.CancellationReason.Error:
                print(f"  Error: {cancellation.error_details}")

    except Exception as exc:
        print(f"  Error: {exc}")


# ===========================================================================
# 3. SSML with emotional styles
# ===========================================================================
def emotional_styles_ssml():
    """
    Demonstrate emotional speaking styles with mstts:express-as.

    EXAM TIP: Not all voices support all styles. Neural voices like
    en-US-JennyNeural support styles such as: cheerful, sad, angry,
    excited, friendly, terrified, shouting, whispering, hopeful.
    """
    print("\n" + "=" * 60)
    print("3. EMOTIONAL STYLES (mstts:express-as)")
    print("=" * 60)

    speech_config = speechsdk.SpeechConfig(
        subscription=SPEECH_KEY,
        region=SPEECH_REGION,
    )

    output_file = os.path.join(os.path.dirname(__file__), "output-emotional.wav")
    audio_config = speechsdk.AudioConfig(filename=output_file)

    synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config,
        audio_config=audio_config,
    )

    ssml = """
    <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
           xmlns:mstts="http://www.w3.org/2001/mstts"
           xml:lang="en-US">
        <voice name="en-US-JennyNeural">

            <mstts:express-as style="cheerful">
                Congratulations on starting your AI-102 preparation!
                This is going to be a great learning journey.
            </mstts:express-as>

            <break time="1s"/>

            <mstts:express-as style="empathetic">
                I understand that certification exams can be challenging.
                Take your time and study consistently.
            </mstts:express-as>

            <break time="1s"/>

            <!-- Style with degree control (0.01 to 2.0) -->
            <mstts:express-as style="excited" styledegree="2">
                You passed the exam! Amazing work!
            </mstts:express-as>

        </voice>
    </speak>
    """

    try:
        print("  Synthesizing emotional styles...")
        result = synthesizer.speak_ssml(ssml)

        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print(f"  ✅ Audio saved to: {output_file}")
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation = result.cancellation_details
            print(f"  ❌ Canceled: {cancellation.reason}")
            if cancellation.reason == speechsdk.CancellationReason.Error:
                print(f"  Error: {cancellation.error_details}")

    except Exception as exc:
        print(f"  Error: {exc}")


# ===========================================================================
# 4. Available voices reference
# ===========================================================================
def list_voices():
    """List available voices for a language."""
    print("\n" + "=" * 60)
    print("4. AVAILABLE VOICES (en-US sample)")
    print("=" * 60)

    speech_config = speechsdk.SpeechConfig(
        subscription=SPEECH_KEY,
        region=SPEECH_REGION,
    )

    synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config,
        audio_config=None,  # No audio output
    )

    try:
        voices_result = synthesizer.get_voices_async("en-US").get()

        if voices_result.reason == speechsdk.ResultReason.VoicesListRetrieved:
            print(f"  Found {len(voices_result.voices)} en-US voices. First 10:")
            for voice in voices_result.voices[:10]:
                styles = ", ".join(voice.style_list) if voice.style_list else "none"
                print(
                    f"    {voice.short_name:<30} "
                    f"Gender: {voice.gender.name:<8} "
                    f"Styles: {styles[:40]}"
                )
        else:
            print(f"  Could not retrieve voices: {voices_result.reason}")

    except Exception as exc:
        print(f"  Error: {exc}")


# ===========================================================================
# Main
# ===========================================================================
if __name__ == "__main__":
    print("\nAI-102 Lab 5.3 – Text to Speech\n")

    basic_tts()
    ssml_tts()
    emotional_styles_ssml()
    list_voices()

    # EXAM TIPS:
    # ──────────
    # • SSML elements: <speak>, <voice>, <prosody>, <break>, <emphasis>,
    #   <say-as>, <phoneme>, <mstts:express-as>.
    # • speak_text() for plain text; speak_ssml() for SSML input.
    # • Neural voices (recommended): higher quality, more natural.
    # • Not all voices support all emotional styles – check docs.
    # • Output formats: WAV (default), MP3, OGG, raw PCM.
    # • Custom Neural Voice: train a custom voice with your own recordings.
    # • Audio output: speakers, file, or memory stream.
    # • Viseme events available for lip-sync animations.
    # • Batch synthesis API available for processing large text volumes.

    # CLEANUP NOTE:
    # Speech service charges per character synthesized (neural pricing).
    # Delete generated audio files and the resource when done.
