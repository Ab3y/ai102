# Module 5: Natural Language Processing — Knowledge Check

## Instructions

Answer all 15 questions. Each question has one correct answer unless stated otherwise. Target score: **80% or higher** (12/15).

---

### Question 1

**You are building an application that analyzes customer reviews for a hotel chain. Management wants to know not just the overall sentiment of each review, but also what specific aspects (food, staff, room) customers liked or disliked. Which feature should you use?**

- A) Sentiment analysis with `show_opinion_mining=False`
- B) Key phrase extraction
- C) Sentiment analysis with `show_opinion_mining=True`
- D) Named entity recognition

---

### Question 2

**Your application processes user-submitted text and must replace sensitive information (SSN, email, phone numbers) with asterisks before storing the text. The application also handles medical records and must comply with HIPAA. Which API call and parameter should you use?**

- A) `recognize_entities()` with `category="PII"`
- B) `recognize_pii_entities()` with `domain="phi"`
- C) `recognize_pii_entities()` with `domain="healthcare"`
- D) `analyze_sentiment()` with `show_opinion_mining=True`

---

### Question 3

**You need to disambiguate the word "Mercury" in a set of documents — determining whether each reference is about the planet, the element, or the car brand. Which Azure AI Language feature should you use?**

- A) Named entity recognition (NER)
- B) Key phrase extraction
- C) Entity linking
- D) PII detection

---

### Question 4

**You are using the Azure AI Translator service to translate text. Your REST request fails with a 401 error. You verified the API key is correct. What is the most likely cause?**

- A) The text exceeds the 10,000 character limit per element
- B) You forgot to include the `Ocp-Apim-Subscription-Region` header
- C) The target language is not supported
- D) You need to use the Language service endpoint instead of the Translator endpoint

---

### Question 5

**You need to create an SSML document that speaks a phone number digit by digit (e.g., "5-5-5-0-1-0-0" instead of "five million five hundred fifty thousand one hundred"). Which SSML element and attribute should you use?**

- A) `<say-as interpret-as="cardinal">5550100</say-as>`
- B) `<say-as interpret-as="telephone">5550100</say-as>`
- C) `<prosody rate="slow">5550100</prosody>`
- D) `<emphasis level="strong">5550100</emphasis>`

---

### Question 6

**Review the following SSML snippet. What is wrong with it?**

```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
    <voice name="en-US-JennyNeural">
        <mstts:express-as style="cheerful">
            Welcome to our store!
        </mstts:express-as>
    </voice>
</speak>
```

- A) The `<voice>` element is missing the `xml:lang` attribute
- B) The `<mstts:express-as>` namespace (`xmlns:mstts`) is not declared in the `<speak>` element
- C) The `style` attribute value "cheerful" is not valid
- D) The `<speak>` element is missing the `xmlns:mstts` attribute and the `version` should be "2.0"

---

### Question 7

**You want your TTS output to pause for exactly 1.5 seconds between two sentences, then speak the second sentence slowly. Which SSML fragment achieves this?**

- A)
```xml
<break time="1.5s"/>
<prosody rate="slow">Second sentence.</prosody>
```

- B)
```xml
<break strength="1500ms"/>
<prosody speed="slow">Second sentence.</prosody>
```

- C)
```xml
<pause duration="1.5s"/>
<prosody rate="slow">Second sentence.</prosody>
```

- D)
```xml
<break time="1500"/>
<prosody rate="slow">Second sentence.</prosody>
```

---

### Question 8

**You need to transcribe a 3-hour recorded conference call stored as a 800 MB WAV file. Which approach should you use?**

- A) `recognize_once()` with `AudioConfig(filename="conference.wav")`
- B) `start_continuous_recognition()` with `AudioConfig(filename="conference.wav")`
- C) Batch transcription REST API with the file in Azure Blob Storage
- D) Speech translation with `TranslationRecognizer`

---

### Question 9

**You are implementing speech translation. Your application must recognize English speech and output translated text in French, German, and Spanish simultaneously. Which configuration is correct?**

- A) Create three separate `SpeechConfig` objects, one per target language
- B) Use `SpeechTranslationConfig`, set `speech_recognition_language="en-US"`, and call `add_target_language()` three times for "fr", "de", and "es"
- C) Use `SpeechConfig` with `speech_recognition_language="en-US"` and set `translation_languages=["fr", "de", "es"]`
- D) Use `TranslationRecognizer` with `SpeechConfig` and specify target languages in `recognize_once()`

---

### Question 10

**You are building a CLU model for a home automation app. Users can say things like "Turn on the living room lights" and "Set the thermostat to 72 degrees." You have defined the intents `ControlLights`, `SetTemperature`, and `None`. After training, the confusion matrix shows that `ControlLights` is frequently confused with `SetTemperature`. What is the best action?**

- A) Delete the `None` intent to simplify the model
- B) Add more utterances to each intent with clearly distinguishing vocabulary
- C) Merge `ControlLights` and `SetTemperature` into a single intent
- D) Remove all entities from both intents

---

### Question 11

**In your CLU model, you need to extract order numbers that always follow the pattern "ORD-" followed by exactly 6 digits (e.g., ORD-123456). Which entity type should you use?**

- A) Learned entity
- B) List entity
- C) Prebuilt entity
- D) Regex entity

---

### Question 12

**Your team has built a CLU model in a development environment and needs to deploy it to production. The production environment uses a different Azure AI Language resource in another region. What is the correct approach?**

- A) Recreate the model from scratch in the production resource
- B) Export the project as JSON from the dev resource, then import it into the production resource
- C) Copy the Language resource using Azure Resource Mover
- D) Use the `SpeechConfig.endpoint_id` to point to the dev resource

---

### Question 13

**You call a CLU model with the utterance "What's the weather in Paris?" and receive the following response. The `topIntent` is `GetWeather` with a confidence score of 0.45. Your application's confidence threshold is 0.7. What should your application do?**

- A) Execute the `GetWeather` intent with the extracted entity "Paris"
- B) Return the default/fallback response and ask the user to rephrase
- C) Execute the `None` intent
- D) Retrain the model immediately

---

### Question 14

**You are creating a custom question answering project for a company's FAQ. You add a QA pair about the return policy with three follow-up prompts: "Electronics", "Clothing", and "Books." The "Electronics" follow-up leads to an answer about the 15-day electronics return policy. You want this electronics answer to appear ONLY when the user follows the multi-turn flow — not when they directly ask about electronics returns. Which property should you set?**

- A) `displayOrder: 0`
- B) `isContextOnly: true`
- C) `confidenceThreshold: 1.0`
- D) `isFollowUpOnly: true`

---

### Question 15

**Your custom question answering project contains the QA pair: "How do I fix my printer?" → "Try restarting the printer..." Users are also asking "How do I repair my printer?" and "How do I troubleshoot my printer?" but these are not matching. You want "fix", "repair", "troubleshoot", and "solve" to be treated as equivalent across ALL QA pairs. What should you configure?**

- A) Add alternate phrasings to this specific QA pair
- B) Add project-level synonyms: ["fix", "repair", "troubleshoot", "solve"]
- C) Enable chit-chat with the "Professional" personality
- D) Create separate QA pairs for each word variation

---

## Answers

### Question 1
**Correct Answer: C**
**Explanation:** Opinion mining (`show_opinion_mining=True`) breaks down sentiment to the aspect level, identifying specific targets (food, staff, room) and the assessments (opinions) about them. Standard sentiment analysis (A) only provides document and sentence-level sentiment. Key phrase extraction (B) returns phrases but no sentiment. NER (D) categorizes entities but doesn't analyze sentiment.

### Question 2
**Correct Answer: B**
**Explanation:** `recognize_pii_entities()` is the correct method for PII detection and redaction. The `domain="phi"` parameter enables Protected Health Information detection for HIPAA compliance. There is no `domain="healthcare"` parameter value (C). NER (A) identifies entities but doesn't specifically detect PII or provide redaction. Sentiment analysis (D) is unrelated.

### Question 3
**Correct Answer: C**
**Explanation:** Entity linking disambiguates entities by linking them to Wikipedia articles. It uses context to determine whether "Mercury" refers to the planet, element, or car brand. NER (A) would identify "Mercury" as an entity but cannot disambiguate it — it doesn't link to external knowledge bases. Key phrase extraction (B) and PII detection (D) are unrelated.

### Question 4
**Correct Answer: B**
**Explanation:** The Translator service requires TWO authentication headers: `Ocp-Apim-Subscription-Key` AND `Ocp-Apim-Subscription-Region`. A missing region header causes a 401 Unauthorized error even when the API key is correct. The character limit (A) would cause a 400 error, not 401. An unsupported language (C) would also cause a 400 error.

### Question 5
**Correct Answer: B**
**Explanation:** `<say-as interpret-as="telephone">` tells the speech synthesizer to pronounce the number as a phone number — reading each digit individually. `interpret-as="cardinal"` (A) would pronounce it as a large number ("five million..."). `<prosody>` (C) controls speaking speed, not pronunciation. `<emphasis>` (D) controls stress/emphasis.

### Question 6
**Correct Answer: B**
**Explanation:** The `<mstts:express-as>` element requires the Microsoft TTS namespace to be declared in the `<speak>` root element: `xmlns:mstts="https://www.w3.org/2001/mstts"`. Without this namespace declaration, the SSML is invalid. The `style="cheerful"` value is valid (C). Option D is partially correct about the namespace but wrong about the version.

### Question 7
**Correct Answer: A**
**Explanation:** `<break time="1.5s"/>` inserts a pause of exactly 1.5 seconds. `<prosody rate="slow">` controls speaking speed. Option B is wrong because `strength` takes named values (none, x-weak, weak, medium, strong, x-strong), not millisecond values, and the attribute is `rate` not `speed`. Option C is wrong because there is no `<pause>` element in SSML. Option D is wrong because `time` requires a unit suffix ("ms" or "s").

### Question 8
**Correct Answer: C**
**Explanation:** Batch transcription is designed for large audio files. It supports files up to 1 GB and 24 hours duration, handles the 800 MB file easily, and runs asynchronously. `recognize_once()` (A) only recognizes a single utterance. Continuous recognition (B) works but is designed for real-time streaming, not pre-recorded files of this size. Speech translation (D) is for language translation, not transcription.

### Question 9
**Correct Answer: B**
**Explanation:** Speech translation uses `SpeechTranslationConfig` (not `SpeechConfig`) with `add_target_language()` called once per target language. You can add multiple target languages to get simultaneous translation. Option A would require three separate recognizers. Option C uses the wrong config class and a non-existent property. Option D uses the wrong config class.

### Question 10
**Correct Answer: B**
**Explanation:** When intents are confused, add more utterances with distinguishing vocabulary to each intent. For `ControlLights`, add utterances with light-specific words ("dim", "brightness", "switch"). For `SetTemperature`, add utterances with temperature-specific words ("degrees", "thermostat", "heating"). Deleting `None` (A) is never appropriate — it's required. Merging (C) loses the ability to distinguish between the actions. Removing entities (D) removes useful information.

### Question 11
**Correct Answer: D**
**Explanation:** Regex entities match text using regular expression patterns. The pattern `ORD-\d{6}` precisely matches the order number format. A learned entity (A) would require many labeled examples and might not be as precise. A list entity (B) requires predefined values, which doesn't work for numeric patterns. A prebuilt entity (C) doesn't have a specific order number type.

### Question 12
**Correct Answer: B**
**Explanation:** CLU projects can be exported as JSON and imported into another Language resource. This is the standard approach for migrating between environments. Recreating from scratch (A) is wasteful and error-prone. Azure Resource Mover (C) moves resources, not model data within them. `SpeechConfig.endpoint_id` (D) is for custom speech models, not CLU.

### Question 13
**Correct Answer: B**
**Explanation:** The confidence score (0.45) is below the application's threshold (0.7). The application should NOT execute the intent — instead, it should return a fallback response and ask the user to rephrase. Executing the intent (A) risks acting on an uncertain prediction. Executing the None intent (C) is incorrect — the model did predict GetWeather, just with low confidence. Retraining (D) is not an immediate runtime action.

### Question 14
**Correct Answer: B**
**Explanation:** Setting `isContextOnly: true` on the electronics return policy answer ensures it only appears when the user follows the multi-turn flow from the parent return policy question. It won't appear as a top-level answer to direct queries. `displayOrder` (A) controls prompt ordering, not visibility. There is no `isFollowUpOnly` property (D). Setting a confidence threshold of 1.0 (C) would effectively hide the answer but is not the correct mechanism.

### Question 15
**Correct Answer: B**
**Explanation:** Project-level synonyms define word equivalences that apply across ALL QA pairs. Defining ["fix", "repair", "troubleshoot", "solve"] as synonyms means any of these words will match any QA pair containing any of the others. Alternate phrasings (A) would only help this specific QA pair, not all pairs. Chit-chat (C) is for social conversation. Creating separate QA pairs (D) creates maintenance burden and doesn't solve the vocabulary problem for other pairs.
