# Lesson 2: Speech Services

## Learning Objectives

After completing this lesson, you will be able to:

- Implement speech-to-text with real-time and continuous recognition
- Configure batch transcription for large audio files
- Implement text-to-speech with neural voices
- Write and customize SSML for fine-grained speech synthesis control
- Build custom speech models for domain-specific scenarios
- Integrate speech with intent recognition (CLU)
- Implement keyword recognition for wake-word detection
- Configure speech translation for real-time multilingual scenarios

---

## Azure AI Speech Service Overview

Azure AI Speech is part of Azure AI Services and provides speech-to-text, text-to-speech, speech translation, and speaker recognition capabilities.

**SDK:** `azure-cognitiveservices-speech` (Python) / `Microsoft.CognitiveServices.Speech` (C#)

**Authentication:**

```python
import azure.cognitiveservices.speech as speechsdk

speech_config = speechsdk.SpeechConfig(
    subscription="<api-key>",
    region="<region>"
)
```

> **EXAM TIP:** The Speech SDK uses `SpeechConfig` with a **subscription key and region** — NOT an endpoint URL. This is different from other Azure AI SDKs that typically use an endpoint + key.

---

## Speech-to-Text (STT)

Speech-to-text converts spoken audio into text. It supports real-time recognition (streaming) and batch transcription.

### Real-Time Recognition

For short utterances (single sentences or commands):

```python
import azure.cognitiveservices.speech as speechsdk

speech_config = speechsdk.SpeechConfig(subscription="<key>", region="<region>")
speech_config.speech_recognition_language = "en-US"

# From microphone
audio_config = speechsdk.AudioConfig(use_default_microphone=True)

# From file
# audio_config = speechsdk.AudioConfig(filename="audio.wav")

recognizer = speechsdk.SpeechRecognizer(
    speech_config=speech_config,
    audio_config=audio_config
)

# Single recognition — stops after first utterance
result = recognizer.recognize_once()

if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print(f"Recognized: {result.text}")
elif result.reason == speechsdk.ResultReason.NoMatch:
    print(f"No speech recognized: {result.no_match_details}")
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation = result.cancellation_details
    print(f"Canceled: {cancellation.reason}")
    if cancellation.reason == speechsdk.CancellationReason.Error:
        print(f"Error: {cancellation.error_details}")
```

### RecognitionResult Properties

| Property | Description |
|----------|-------------|
| `reason` | `RecognizedSpeech`, `NoMatch`, `Canceled` |
| `text` | The recognized text |
| `duration` | Duration of recognized speech |
| `offset` | Offset from start of audio |
| `no_match_details` | Details when no speech matched |
| `cancellation_details` | Details when recognition was canceled |

### Continuous Recognition

For long audio files, meetings, or real-time transcription:

```python
import azure.cognitiveservices.speech as speechsdk
import time

speech_config = speechsdk.SpeechConfig(subscription="<key>", region="<region>")
audio_config = speechsdk.AudioConfig(filename="long_meeting.wav")

recognizer = speechsdk.SpeechRecognizer(
    speech_config=speech_config,
    audio_config=audio_config
)

all_results = []
done = False

def on_recognized(evt):
    all_results.append(evt.result.text)
    print(f"RECOGNIZED: {evt.result.text}")

def on_session_stopped(evt):
    nonlocal done
    done = True

recognizer.recognized.connect(on_recognized)
recognizer.session_stopped.connect(on_session_stopped)
recognizer.canceled.connect(on_session_stopped)

recognizer.start_continuous_recognition()

while not done:
    time.sleep(0.5)

recognizer.stop_continuous_recognition()

full_transcript = " ".join(all_results)
print(f"\nFull transcript: {full_transcript}")
```

### Audio Formats Supported

| Format | Extension | Notes |
|--------|-----------|-------|
| WAV | .wav | Recommended: 16-bit, 16 KHz, mono PCM |
| MP3 | .mp3 | Supported |
| OGG | .ogg | Opus codec |
| FLAC | .flac | Lossless compression |
| WMA | .wma | Windows Media Audio |

> **EXAM TIP:** `recognize_once()` recognizes a **single utterance** and then stops. For continuous audio (meetings, lectures), use `start_continuous_recognition()` with event handlers. The exam will test whether you know which method to use for different scenarios.

---

## Batch Transcription

Batch transcription is designed for transcribing large amounts of audio asynchronously.

### Limits

| Parameter | Limit |
|-----------|-------|
| Max file size | 1 GB |
| Max audio duration | 24 hours per file |
| Max concurrent requests | 300 |
| Storage | Azure Blob Storage required |

### Workflow

1. Upload audio files to Azure Blob Storage
2. Create a transcription job via REST API
3. Poll for job status (or use webhook)
4. Download results when complete

### REST Example — Create Batch Transcription

```http
POST https://<region>.api.cognitive.microsoft.com/speechtotext/v3.1/transcriptions
Content-Type: application/json
Ocp-Apim-Subscription-Key: <key>

{
  "displayName": "Meeting Transcription",
  "locale": "en-US",
  "contentUrls": [
    "https://<storage>.blob.core.windows.net/audio/meeting.wav?<SAS>"
  ],
  "properties": {
    "wordLevelTimestampsEnabled": true,
    "punctuationMode": "DictatedAndAutomatic",
    "profanityFilterMode": "Masked",
    "diarizationEnabled": true,
    "timeToLive": "PT12H"
  }
}
```

**Response:**

```json
{
  "self": "https://<region>.api.cognitive.microsoft.com/speechtotext/v3.1/transcriptions/<id>",
  "status": "NotStarted",
  "displayName": "Meeting Transcription"
}
```

### Poll for Status

```http
GET https://<region>.api.cognitive.microsoft.com/speechtotext/v3.1/transcriptions/<id>
Ocp-Apim-Subscription-Key: <key>
```

Status values: `NotStarted` → `Running` → `Succeeded` / `Failed`

### Batch Transcription Properties

| Property | Description |
|----------|-------------|
| `wordLevelTimestampsEnabled` | Include word-level timing |
| `diarizationEnabled` | Speaker separation |
| `punctuationMode` | `None`, `Dictated`, `Automatic`, `DictatedAndAutomatic` |
| `profanityFilterMode` | `None`, `Removed`, `Tags`, `Masked` |
| `timeToLive` | Auto-delete results after duration (e.g., `PT12H`) |

> **EXAM TIP:** Batch transcription supports files up to **1 GB** and **24 hours** duration. It requires audio in Azure **Blob Storage** with SAS tokens. It's an **asynchronous** operation — you poll for status. This is different from real-time recognition which is synchronous and streaming.

---

## Text-to-Speech (TTS)

Text-to-speech converts text into spoken audio using neural voices.

### Basic TTS

```python
import azure.cognitiveservices.speech as speechsdk

speech_config = speechsdk.SpeechConfig(subscription="<key>", region="<region>")
speech_config.speech_synthesis_voice_name = "en-US-JennyNeural"

# Output to default speaker
synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

result = synthesizer.speak_text("Hello, welcome to Azure AI Speech Services!")

if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesis succeeded.")
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation = result.cancellation_details
    print(f"Canceled: {cancellation.reason}")
```

### Save to Audio File

```python
audio_config = speechsdk.AudioConfig(filename="output.wav")

synthesizer = speechsdk.SpeechSynthesizer(
    speech_config=speech_config,
    audio_config=audio_config
)

result = synthesizer.speak_text("This will be saved to a file.")
```

### Suppress Audio Output (Get Audio Data Only)

```python
synthesizer = speechsdk.SpeechSynthesizer(
    speech_config=speech_config,
    audio_config=None  # No speaker output
)

result = synthesizer.speak_text("Silent synthesis")
audio_data = result.audio_data  # Raw audio bytes
```

### Voice Selection

Neural voices are identified by locale and name:

| Voice Name | Language | Gender |
|------------|----------|--------|
| en-US-JennyNeural | English (US) | Female |
| en-US-GuyNeural | English (US) | Male |
| en-US-AriaNeural | English (US) | Female |
| en-GB-SoniaNeural | English (UK) | Female |
| de-DE-KatjaNeural | German | Female |
| fr-FR-DeniseNeural | French | Female |
| ja-JP-NanamiNeural | Japanese | Female |
| zh-CN-XiaoxiaoNeural | Chinese | Female |

> **EXAM TIP:** Use `speech_config.speech_synthesis_voice_name` to set the voice in code, or use the `<voice>` element in SSML. Neural voices provide the most natural-sounding speech. Voice names follow the pattern `{locale}-{Name}Neural`.

---

## SSML Deep Dive — CRITICAL FOR THE EXAM

**Speech Synthesis Markup Language (SSML)** provides fine-grained control over speech synthesis. This is one of the most heavily tested topics on the AI-102 exam.

### Basic SSML Structure

Every SSML document must have a `<speak>` root element with the XML namespace:

```xml
<speak version="1.0"
       xmlns="http://www.w3.org/2001/10/synthesis"
       xmlns:mstts="https://www.w3.org/2001/mstts"
       xml:lang="en-US">
    <voice name="en-US-JennyNeural">
        Hello, this is a basic SSML example.
    </voice>
</speak>
```

### SSML Elements Reference

| Element | Purpose | Key Attributes |
|---------|---------|----------------|
| `<speak>` | Root element | `version`, `xmlns`, `xml:lang` |
| `<voice>` | Select voice | `name` |
| `<prosody>` | Control rate, pitch, volume | `rate`, `pitch`, `volume` |
| `<emphasis>` | Emphasize words | `level` |
| `<break>` | Insert pause | `time`, `strength` |
| `<say-as>` | Control pronunciation | `interpret-as`, `format` |
| `<mstts:express-as>` | Emotional styles | `style`, `styledegree` |
| `<phoneme>` | Phonetic pronunciation | `alphabet`, `ph` |
| `<sub>` | Substitution/alias | `alias` |
| `<audio>` | Insert audio clip | `src` |
| `<p>`, `<s>` | Paragraph and sentence | — |
| `<bookmark>` | Named bookmark events | `mark` |

---

### `<voice>` — Selecting a Voice

```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
    <voice name="en-US-JennyNeural">
        This is Jenny speaking.
    </voice>
    <voice name="en-US-GuyNeural">
        And this is Guy speaking.
    </voice>
</speak>
```

You can switch voices within a single SSML document to simulate a conversation.

---

### `<prosody>` — Rate, Pitch, and Volume

Controls the speed, pitch, and loudness of speech.

#### Rate Values

| Value | Description |
|-------|-------------|
| `x-slow` | Very slow |
| `slow` | Slow |
| `medium` | Normal (default) |
| `fast` | Fast |
| `x-fast` | Very fast |
| `+50%` / `-30%` | Percentage adjustment |
| `1.5` | Absolute multiplier |

#### Pitch Values

| Value | Description |
|-------|-------------|
| `x-low` | Very low pitch |
| `low` | Low pitch |
| `medium` | Normal (default) |
| `high` | High pitch |
| `x-high` | Very high pitch |
| `+10Hz` / `-5Hz` | Hz adjustment |
| `+20%` / `-10%` | Percentage adjustment |

#### Volume Values

| Value | Description |
|-------|-------------|
| `silent` | No sound |
| `x-soft` | Very quiet |
| `soft` | Quiet |
| `medium` | Normal (default) |
| `loud` | Loud |
| `x-loud` | Very loud |
| `+20%` / `-30%` | Percentage adjustment |
| `50` | Absolute value (0–100) |

```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
    <voice name="en-US-JennyNeural">
        <prosody rate="slow" pitch="low" volume="soft">
            This is spoken slowly, with a low pitch, and quietly.
        </prosody>
        <prosody rate="fast" pitch="high" volume="loud">
            This is spoken quickly, with a high pitch, and loudly!
        </prosody>
        <prosody rate="+30%" pitch="-2st" volume="80">
            This uses percentage and semitone adjustments.
        </prosody>
    </voice>
</speak>
```

> **EXAM TIP:** `<prosody>` attributes are **rate**, **pitch**, and **volume**. The exam will test you on valid attribute values. Remember the named values (x-slow, slow, medium, fast, x-fast) AND percentage adjustments. The default for all three is `medium`.

---

### `<emphasis>` — Emphasize Words

| Level | Description |
|-------|-------------|
| `strong` | Strong emphasis |
| `moderate` | Moderate emphasis (default) |
| `reduced` | De-emphasize |
| `none` | No emphasis |

```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
    <voice name="en-US-JennyNeural">
        This is <emphasis level="strong">extremely</emphasis> important.
        This is <emphasis level="reduced">somewhat</emphasis> less critical.
    </voice>
</speak>
```

---

### `<break>` — Insert Pauses

#### Time Attribute

Specify an exact duration:

```xml
<break time="500ms"/>   <!-- 500 milliseconds -->
<break time="2s"/>      <!-- 2 seconds -->
```

#### Strength Attribute

Use predefined pause strengths:

| Strength | Duration |
|----------|----------|
| `none` | No pause (0 ms) |
| `x-weak` | ~250 ms |
| `weak` | ~500 ms |
| `medium` | ~750 ms |
| `strong` | ~1000 ms |
| `x-strong` | ~1250 ms |

```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
    <voice name="en-US-JennyNeural">
        Welcome to the presentation. <break time="1s"/>
        Let's begin with the first topic. <break strength="strong"/>
        Here are the key points.
    </voice>
</speak>
```

> **EXAM TIP:** `<break>` uses either `time` (exact duration like "500ms" or "2s") OR `strength` (named value like "strong"). Do NOT confuse with `<prosody rate>` — rate controls speaking speed, while `<break>` inserts a silent pause.

---

### `<say-as>` — Control Pronunciation

The `interpret-as` attribute tells the synthesizer how to pronounce specific text.

| interpret-as | Description | Example Input | Spoken As |
|--------------|-------------|---------------|-----------|
| `cardinal` | Number | "123" | "one hundred twenty-three" |
| `ordinal` | Ordinal number | "3" | "third" |
| `characters` | Spell out | "ABC" | "A B C" |
| `date` | Date (with format) | "2024-01-15" | Depends on format |
| `time` | Time | "13:30" | "one thirty PM" |
| `telephone` | Phone number | "5550100" | "five five five zero one zero zero" |
| `address` | Street address | — | Spoken as address |
| `fraction` | Fraction | "3/4" | "three quarters" |
| `currency` | Currency | "$19.99" | "nineteen dollars and ninety-nine cents" |

#### Date Formats

| Format | Example | Spoken As |
|--------|---------|-----------|
| `mdy` | 01/15/2024 | "January fifteenth, twenty twenty-four" |
| `dmy` | 15/01/2024 | "the fifteenth of January, twenty twenty-four" |
| `ymd` | 2024-01-15 | "twenty twenty-four, January fifteenth" |
| `md` | 01/15 | "January fifteenth" |
| `dm` | 15/01 | "the fifteenth of January" |
| `ym` | 2024-01 | "January twenty twenty-four" |
| `my` | 01/2024 | "January twenty twenty-four" |
| `y` | 2024 | "twenty twenty-four" |

```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
    <voice name="en-US-JennyNeural">
        Your order number is <say-as interpret-as="characters">ABC123</say-as>.
        You placed it on <say-as interpret-as="date" format="mdy">01/15/2024</say-as>.
        The total was <say-as interpret-as="currency">$49.99</say-as>.
        Call us at <say-as interpret-as="telephone">1-800-555-0199</say-as>.
        You are customer number <say-as interpret-as="ordinal">3</say-as> in line.
    </voice>
</speak>
```

> **EXAM TIP:** `<say-as>` is heavily tested. Know the `interpret-as` values — especially `cardinal` vs `ordinal`, `characters` for spelling out, and `date` with its `format` attribute (mdy, dmy, ymd, etc.). The exam will present SSML snippets and ask what the output will sound like.

---

### `<mstts:express-as>` — Emotional Styles

This is a Microsoft-specific extension that adds emotional expression to neural voices. Requires the `mstts` namespace.

| Style | Description |
|-------|-------------|
| `cheerful` | Happy, upbeat tone |
| `sad` | Melancholy tone |
| `angry` | Annoyed, displeased tone |
| `excited` | Enthusiastic, energetic |
| `friendly` | Warm, approachable |
| `terrified` | Frightened, panicked |
| `shouting` | Loud, commanding |
| `whispering` | Soft, secretive |
| `hopeful` | Optimistic, encouraging |
| `narration-professional` | Clear, authoritative |
| `newscast` | News anchor style |
| `customer-service` | Polite, professional |

```xml
<speak version="1.0"
       xmlns="http://www.w3.org/2001/10/synthesis"
       xmlns:mstts="https://www.w3.org/2001/mstts"
       xml:lang="en-US">
    <voice name="en-US-JennyNeural">
        <mstts:express-as style="cheerful">
            Great news! Your order has been shipped!
        </mstts:express-as>
        <mstts:express-as style="sad">
            Unfortunately, we had to cancel your reservation.
        </mstts:express-as>
        <mstts:express-as style="customer-service">
            How may I help you today? I'd be happy to assist.
        </mstts:express-as>
    </voice>
</speak>
```

#### Style Degree

Control the intensity of the style (0.01 to 2.0, default 1.0):

```xml
<mstts:express-as style="cheerful" styledegree="2">
    This is EXTREMELY cheerful!
</mstts:express-as>
```

> **EXAM TIP:** `<mstts:express-as>` requires the `xmlns:mstts` namespace declaration. Not all voices support all styles — Jenny and Aria support the most styles. The `styledegree` attribute ranges from 0.01 to 2.0 (1.0 is default). The exam may ask which namespace is needed for emotional styles.

---

### `<phoneme>` — Phonetic Pronunciation

Specify exact pronunciation using the International Phonetic Alphabet (IPA) or Speech API (SAPI) phonetic alphabet.

| Alphabet | Description |
|----------|-------------|
| `ipa` | International Phonetic Alphabet |
| `sapi` | Microsoft Speech API |
| `ups` | Universal Phone Set |

```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
    <voice name="en-US-JennyNeural">
        The word <phoneme alphabet="ipa" ph="təˈmɑːtoʊ">tomato</phoneme> can also be
        pronounced <phoneme alphabet="ipa" ph="təˈmeɪtoʊ">tomato</phoneme>.
    </voice>
</speak>
```

---

### `<sub>` — Substitution/Alias

Replace text with an alternate pronunciation:

```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
    <voice name="en-US-JennyNeural">
        <sub alias="artificial intelligence">AI</sub> is transforming healthcare.
        My favorite element is <sub alias="aluminum">Al</sub>.
        The <sub alias="World Health Organization">WHO</sub> released new guidelines.
    </voice>
</speak>
```

The displayed text is the content, but the spoken text uses the `alias`.

---

### `<audio>` — Insert Audio Clips

Insert pre-recorded audio into the synthesized speech:

```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
    <voice name="en-US-JennyNeural">
        <audio src="https://example.com/notification.wav">
            Fallback text if audio cannot be played.
        </audio>
        You have a new notification.
    </voice>
</speak>
```

Audio file requirements: WAV format, mono, 16-bit, 8/16/24 KHz sample rate, max 2 minutes.

---

### Complete SSML Examples

#### Example 1: Customer Service Greeting

```xml
<speak version="1.0"
       xmlns="http://www.w3.org/2001/10/synthesis"
       xmlns:mstts="https://www.w3.org/2001/mstts"
       xml:lang="en-US">
    <voice name="en-US-JennyNeural">
        <mstts:express-as style="customer-service">
            <prosody rate="medium" pitch="medium">
                Thank you for calling Contoso Support.
                <break time="500ms"/>
                Your call is important to us.
                <break time="300ms"/>
                Please hold while I look up your account.
            </prosody>
        </mstts:express-as>
    </voice>
</speak>
```

#### Example 2: News Broadcast with Multiple Voices

```xml
<speak version="1.0"
       xmlns="http://www.w3.org/2001/10/synthesis"
       xmlns:mstts="https://www.w3.org/2001/mstts"
       xml:lang="en-US">
    <voice name="en-US-GuyNeural">
        <mstts:express-as style="newscast">
            Good evening. Here are tonight's top stories.
            <break time="1s"/>
        </mstts:express-as>
    </voice>
    <voice name="en-US-JennyNeural">
        <mstts:express-as style="newscast">
            The stock market closed at
            <say-as interpret-as="cardinal">15432</say-as> points today,
            up <say-as interpret-as="cardinal">2</say-as> percent from yesterday.
            <break time="500ms"/>
            In other news, temperatures will reach
            <say-as interpret-as="cardinal">85</say-as> degrees
            on <say-as interpret-as="date" format="md">07/15</say-as>.
        </mstts:express-as>
    </voice>
</speak>
```

#### Example 3: IVR Phone System with Spelled-Out Input

```xml
<speak version="1.0"
       xmlns="http://www.w3.org/2001/10/synthesis"
       xmlns:mstts="https://www.w3.org/2001/mstts"
       xml:lang="en-US">
    <voice name="en-US-AriaNeural">
        <mstts:express-as style="friendly">
            Welcome to Contoso Airlines.
            <break time="500ms"/>
        </mstts:express-as>
        <prosody rate="slow">
            Your confirmation code is
            <say-as interpret-as="characters">BKG742</say-as>.
            <break time="1s"/>
            Your flight departs on
            <say-as interpret-as="date" format="mdy">03/22/2024</say-as>
            at <say-as interpret-as="time">14:30</say-as>.
            <break time="500ms"/>
            For assistance, call
            <say-as interpret-as="telephone">1-800-555-0199</say-as>.
        </prosody>
    </voice>
</speak>
```

#### Example 4: Dramatic Reading with Emphasis and Pauses

```xml
<speak version="1.0"
       xmlns="http://www.w3.org/2001/10/synthesis"
       xmlns:mstts="https://www.w3.org/2001/mstts"
       xml:lang="en-US">
    <voice name="en-US-JennyNeural">
        <prosody rate="slow" pitch="-5%">
            It was a dark and stormy night.
            <break time="2s"/>
            <emphasis level="strong">Suddenly</emphasis>,
            a door creaked open.
            <break strength="strong"/>
            <prosody volume="x-soft" rate="x-slow">
                Footsteps echoed through the empty hallway.
            </prosody>
            <break time="1s"/>
            <prosody volume="loud" rate="fast">
                And then — silence.
            </prosody>
        </prosody>
    </voice>
</speak>
```

#### Example 5: Multilingual with Abbreviations and Phonemes

```xml
<speak version="1.0"
       xmlns="http://www.w3.org/2001/10/synthesis"
       xmlns:mstts="https://www.w3.org/2001/mstts"
       xml:lang="en-US">
    <voice name="en-US-GuyNeural">
        The <sub alias="World Health Organization">WHO</sub>
        announced that <sub alias="artificial intelligence">AI</sub>
        research has grown by <say-as interpret-as="cardinal">300</say-as> percent.
        <break time="500ms"/>
    </voice>
    <voice name="fr-FR-DeniseNeural">
        <prosody rate="medium">
            Bonjour, bienvenue à la conférence internationale.
        </prosody>
    </voice>
    <voice name="en-US-JennyNeural">
        <mstts:express-as style="hopeful">
            The future of <phoneme alphabet="ipa" ph="ˌɑːr.tɪˈfɪʃ.əl">artificial</phoneme>
            intelligence looks <emphasis level="strong">very</emphasis> promising.
        </mstts:express-as>
    </voice>
</speak>
```

---

### Synthesizing SSML with the SDK

```python
import azure.cognitiveservices.speech as speechsdk

speech_config = speechsdk.SpeechConfig(subscription="<key>", region="<region>")

synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

ssml = """
<speak version="1.0"
       xmlns="http://www.w3.org/2001/10/synthesis"
       xmlns:mstts="https://www.w3.org/2001/mstts"
       xml:lang="en-US">
    <voice name="en-US-JennyNeural">
        <mstts:express-as style="cheerful">
            <prosody rate="medium" pitch="+5%">
                Welcome! Today is <say-as interpret-as="date" format="mdy">01/15/2024</say-as>.
                <break time="500ms"/>
                Let's get started!
            </prosody>
        </mstts:express-as>
    </voice>
</speak>
"""

# Use speak_ssml_async for SSML input
result = synthesizer.speak_ssml(ssml)

if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("SSML synthesis succeeded!")
```

> **EXAM TIP:** To synthesize SSML in the SDK, use `speak_ssml()` or `speak_ssml_async()` — NOT `speak_text()`. The `speak_text()` method takes plain text, while `speak_ssml()` takes an SSML document. The exam will test this distinction.

---

## Custom Speech Models

Custom Speech allows you to train models that perform better for specific domains or acoustic environments.

### Custom Acoustic Models

Improve recognition in challenging audio conditions:

| Scenario | Use Case |
|----------|----------|
| Noisy factory | Background noise adaptation |
| Call center | Phone audio quality |
| Accented speech | Regional accent adaptation |

**Training data:** 1–20 hours of labeled audio + transcripts

### Custom Language Models

Improve recognition for domain-specific vocabulary:

| Scenario | Use Case |
|----------|----------|
| Medical dictation | Medical terminology |
| Legal transcription | Legal jargon |
| Technical support | Product-specific terms |

**Training data:** Plain text files with domain vocabulary and sentences (50 KB to 1.5 GB)

### Custom Speech Workflow

1. Create a Custom Speech project in Speech Studio
2. Upload training data (audio + transcripts or text)
3. Train the model
4. Test with test datasets
5. Deploy to a custom endpoint
6. Use the endpoint ID in `SpeechConfig`

### Using a Custom Endpoint

```python
speech_config = speechsdk.SpeechConfig(subscription="<key>", region="<region>")
speech_config.endpoint_id = "<custom-endpoint-id>"

recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
result = recognizer.recognize_once()
```

> **EXAM TIP:** Custom speech models need a **deployed endpoint** specified via `endpoint_id`. The endpoint incurs hosting costs even when not processing audio. Custom language models use **plain text** training data; custom acoustic models use **audio files with transcripts**.

---

## Intent Recognition

Intent recognition combines Speech-to-Text with Conversational Language Understanding (CLU) to detect user intent from spoken language.

### Pattern

```
Audio Input → Speech-to-Text → CLU → Intent + Entities
```

### Setup with CLU

```python
import azure.cognitiveservices.speech as speechsdk

speech_config = speechsdk.SpeechConfig(subscription="<key>", region="<region>")

# Configure CLU connection
clu_model = speechsdk.languageconfig.LanguageUnderstandingModel(
    app_id="<clu-project-name>",
    endpoint="https://<language-resource>.cognitiveservices.azure.com/",
    subscription_key="<language-key>"
)

intent_recognizer = speechsdk.IntentRecognizer(speech_config=speech_config)
intent_recognizer.add_all_intents(clu_model)

result = intent_recognizer.recognize_once()

if result.reason == speechsdk.ResultReason.RecognizedIntent:
    print(f"Intent: {result.intent_id}")
    print(f"Text: {result.text}")
    print(f"Confidence: {result.intent_json}")
elif result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print(f"Speech recognized but no intent matched: {result.text}")
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech recognized")
```

> **EXAM TIP:** Intent recognition uses `IntentRecognizer` (not `SpeechRecognizer`). You add a CLU model to the recognizer, and it returns BOTH the recognized text AND the detected intent. If speech is recognized but no intent matches, the reason is `RecognizedSpeech` (not `RecognizedIntent`).

---

## Keyword Recognition

Keyword recognition (wake word detection) listens for a specific trigger phrase before activating full speech recognition.

### How It Works

1. Create a custom keyword model in Speech Studio (.table file)
2. Load the keyword model in your application
3. The app listens continuously for the keyword
4. Once detected, switch to full speech recognition

### Implementation

```python
import azure.cognitiveservices.speech as speechsdk

speech_config = speechsdk.SpeechConfig(subscription="<key>", region="<region>")
audio_config = speechsdk.AudioConfig(use_default_microphone=True)

recognizer = speechsdk.SpeechRecognizer(
    speech_config=speech_config,
    audio_config=audio_config
)

# Load keyword model
keyword_model = speechsdk.KeywordRecognitionModel("hey_contoso.table")

def on_recognized(evt):
    if evt.result.reason == speechsdk.ResultReason.RecognizedKeyword:
        print(f"Keyword detected! Now listening for command...")

recognizer.recognized.connect(on_recognized)

# Start keyword recognition
result = recognizer.recognize_once_async()
```

### Keyword Model File

- Created in Speech Studio
- Downloaded as a `.table` file
- Runs **on-device** (no cloud call needed for keyword detection)
- Full recognition after keyword uses cloud

> **EXAM TIP:** Keyword recognition runs **locally on the device** — it does NOT send audio to the cloud until the keyword is detected. The keyword model is a `.table` file. This reduces bandwidth and improves privacy.

---

## Speech Translation

Speech translation converts spoken audio from one language to text or speech in another language.

### Setup

```python
import azure.cognitiveservices.speech as speechsdk

# Use SpeechTranslationConfig (not SpeechConfig)
translation_config = speechsdk.translation.SpeechTranslationConfig(
    subscription="<key>",
    region="<region>"
)

# Set source language
translation_config.speech_recognition_language = "en-US"

# Add target languages (can add multiple)
translation_config.add_target_language("fr")
translation_config.add_target_language("de")
translation_config.add_target_language("es")

# Optional: set a voice for synthesized translation output
translation_config.voice_name = "fr-FR-DeniseNeural"

audio_config = speechsdk.AudioConfig(use_default_microphone=True)

# Use TranslationRecognizer
recognizer = speechsdk.translation.TranslationRecognizer(
    translation_config=translation_config,
    audio_config=audio_config
)

result = recognizer.recognize_once()

if result.reason == speechsdk.ResultReason.TranslatedSpeech:
    print(f"Recognized: {result.text}")
    for lang, translation in result.translations.items():
        print(f"  → {lang}: {translation}")
```

**Sample output:**

```
Recognized: Hello, how are you today?
  → fr: Bonjour, comment allez-vous aujourd'hui?
  → de: Hallo, wie geht es Ihnen heute?
  → es: Hola, ¿cómo estás hoy?
```

### Key Differences from Standard STT

| Feature | SpeechRecognizer | TranslationRecognizer |
|---------|------------------|-----------------------|
| Config class | `SpeechConfig` | `SpeechTranslationConfig` |
| Recognizer class | `SpeechRecognizer` | `TranslationRecognizer` |
| Output | Recognized text | Recognized text + translations |
| Target languages | N/A | `add_target_language()` |
| Voice output | N/A | `voice_name` for spoken translation |

### Synthesized Translation (Voice Output)

To get spoken output in the target language:

```python
translation_config.voice_name = "de-DE-KatjaNeural"

def on_synthesizing(evt):
    audio = evt.result.audio
    # Play or save the translated audio
    if audio and len(audio) > 0:
        print(f"Received {len(audio)} bytes of translated audio")

recognizer.synthesizing.connect(on_synthesizing)
```

> **EXAM TIP:** Speech translation uses `SpeechTranslationConfig` and `TranslationRecognizer` — NOT `SpeechConfig` and `SpeechRecognizer`. You can translate to **multiple languages simultaneously** using `add_target_language()`. Set `voice_name` to get spoken audio output of the translation.

---

## File Size Limits Summary

| Feature | Limit |
|---------|-------|
| Real-time STT | Streaming — no hard file limit |
| Batch transcription file size | 1 GB |
| Batch transcription duration | 24 hours per file |
| TTS SSML input | 400 KB or ~65,000 characters |
| Audio clip in SSML `<audio>` | 2 minutes |
| Custom keyword model | On-device, ~1 MB |

> **EXAM TIP:** Know these limits — the exam frequently asks about maximum file sizes and durations for batch transcription (1 GB, 24 hours) vs real-time recognition (streaming).

---

## Key Takeaways

1. **Speech-to-text** offers `recognize_once()` for single utterances and `start_continuous_recognition()` for long audio with event handlers.
2. **Batch transcription** handles files up to 1 GB / 24 hours via an asynchronous REST API with Blob Storage.
3. **Text-to-speech** uses neural voices set via `speech_synthesis_voice_name` or SSML `<voice>` elements.
4. **SSML is heavily tested.** Master these elements: `<voice>`, `<prosody>` (rate/pitch/volume), `<break>` (time/strength), `<say-as>` (interpret-as with format), `<mstts:express-as>` (style), `<emphasis>`, `<sub>`, `<phoneme>`.
5. Use `speak_ssml()` (not `speak_text()`) to synthesize SSML in the SDK.
6. `<mstts:express-as>` requires the `mstts` namespace declaration and supports emotional styles like cheerful, sad, angry, newscast, and customer-service.
7. **Custom speech** models improve recognition for noisy environments (acoustic) or domain vocabulary (language). Deploy to a custom endpoint.
8. **Intent recognition** uses `IntentRecognizer` + CLU model to detect intent from speech.
9. **Keyword recognition** runs on-device using a `.table` file — no cloud call until the keyword is detected.
10. **Speech translation** uses `SpeechTranslationConfig` + `TranslationRecognizer`. It supports multiple target languages simultaneously.

---

## Microsoft Documentation

- [Speech service overview](https://learn.microsoft.com/azure/ai-services/speech-service/overview)
- [Speech-to-text quickstart](https://learn.microsoft.com/azure/ai-services/speech-service/get-started-speech-to-text)
- [Text-to-speech quickstart](https://learn.microsoft.com/azure/ai-services/speech-service/get-started-text-to-speech)
- [SSML reference](https://learn.microsoft.com/azure/ai-services/speech-service/speech-synthesis-markup)
- [SSML prosody element](https://learn.microsoft.com/azure/ai-services/speech-service/speech-synthesis-markup-voice#adjust-prosody)
- [Batch transcription](https://learn.microsoft.com/azure/ai-services/speech-service/batch-transcription)
- [Custom speech](https://learn.microsoft.com/azure/ai-services/speech-service/custom-speech-overview)
- [Speech translation](https://learn.microsoft.com/azure/ai-services/speech-service/get-started-speech-translation)
- [Keyword recognition](https://learn.microsoft.com/azure/ai-services/speech-service/keyword-recognition-overview)
