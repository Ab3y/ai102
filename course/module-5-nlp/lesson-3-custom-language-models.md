# Lesson 3: Custom Language Models — CLU & Custom Question Answering

## Learning Objectives

After completing this lesson, you will be able to:

- Define intents, entities, and utterances for a CLU model
- Train, evaluate, and deploy a CLU model
- Consume CLU from a client application
- Export and import CLU projects for backup and CI/CD
- Create and configure a custom question answering project
- Add QA pairs from multiple sources (manual, URL, documents)
- Configure multi-turn conversations with follow-up prompts
- Use synonyms, alternate phrasings, and chit-chat personalities
- Publish and query a custom question answering knowledge base

---

## PART 1: Conversational Language Understanding (CLU)

CLU (Conversational Language Understanding) is the successor to LUIS (Language Understanding Intelligent Service). It enables you to build custom NLP models that extract intents and entities from user utterances.

### Core Architecture

```
User Utterance → CLU Model → Intent (what the user wants)
                            → Entities (parameters/details)
```

**Example:**

```
Input:  "Book a flight from Seattle to Tokyo on March 15"
Output: Intent: BookFlight
        Entities:
          - Origin: Seattle
          - Destination: Tokyo
          - DepartureDate: March 15
```

---

### Core Concepts

#### Intents

An intent represents the **user's goal** — what they want to accomplish.

| Concept | Description |
|---------|-------------|
| Definition | A category that represents a user's purpose |
| Examples | `BookFlight`, `GetWeather`, `CheckBalance`, `CancelOrder` |
| Minimum utterances | 5 per intent (recommended: 15+) |
| "None" intent | **Required** — catches irrelevant/out-of-scope input |

The **None intent** is automatically created and must contain example utterances of things users might say that are NOT relevant to your application. This prevents the model from forcing every input into a defined intent.

```
None intent examples:
- "What time is it?"
- "Tell me a joke"
- "Who won the Super Bowl?"
- "Hello"
```

> **EXAM TIP:** The **None intent** is required and should contain at least 10% of your total utterances. Every CLU project has it. If a question asks which intent handles irrelevant user input, the answer is the **None** intent.

#### Entities

Entities are **parameters or details** extracted from utterances. CLU supports four entity types:

| Entity Type | Description | Example |
|-------------|-------------|---------|
| **Learned** | Model extracts from labeled examples | City names, product names |
| **List** | Predefined set of values with synonyms | Room types: "suite", "deluxe", "standard" |
| **Prebuilt** | Built-in recognizers | DateTime, Number, Temperature, Age, Currency, Email, Phone |
| **Regex** | Regular expression patterns | Order numbers: `ORD-\d{6}` |

##### Learned Entities

Trained from labeled examples in utterances. The model learns to identify them from context:

```
Utterance: "Book a flight from [Seattle](Origin) to [Tokyo](Destination)"
Utterance: "I need to fly from [London](Origin) to [Paris](Destination)"
```

##### List Entities

Defined as a set of values with optional synonyms:

```json
{
  "name": "RoomType",
  "sublists": [
    {
      "listKey": "Standard",
      "synonyms": ["standard", "regular", "basic", "economy"]
    },
    {
      "listKey": "Deluxe",
      "synonyms": ["deluxe", "premium", "upgraded"]
    },
    {
      "listKey": "Suite",
      "synonyms": ["suite", "executive suite", "presidential"]
    }
  ]
}
```

##### Prebuilt Entities

Ready-to-use entities that don't need training:

| Prebuilt Entity | Recognizes |
|-----------------|------------|
| `DateTime` | Dates, times, durations, date ranges |
| `Number` | Numeric values |
| `Ordinal` | First, second, third... |
| `Temperature` | "72 degrees", "30°C" |
| `Currency` | "$49.99", "100 euros" |
| `Age` | "25 years old" |
| `Percentage` | "50%", "half" |
| `Email` | Email addresses |
| `Phone Number` | Phone numbers |
| `URL` | Web addresses |

##### Regex Entities

Match patterns using regular expressions:

```
Entity: OrderNumber
Pattern: ORD-\d{6}
Matches: ORD-123456, ORD-789012
```

#### Utterances

Utterances are **example phrases** that users might say, labeled with intents and entities.

**Best practices for utterances:**

| Guideline | Details |
|-----------|---------|
| Minimum per intent | 5 (recommended: 15–30) |
| Variety | Include different phrasings of the same intent |
| Length variety | Mix short and long utterances |
| Entity coverage | Label all entities in every utterance |
| Balance | Roughly equal number of utterances across intents |
| Real-world examples | Use actual customer language when possible |

```
Intent: BookFlight
  - "Book a flight from Seattle to Tokyo"
  - "I need to fly to London next Tuesday"
  - "Can you get me a plane ticket from JFK to LAX on December 3rd?"
  - "Flying from Chicago to Miami"
  - "Reserve a seat on a flight from Denver to Atlanta for tomorrow"
```

> **EXAM TIP:** More utterances improve model quality. The exam may ask about the **minimum** (5 per intent) and **recommended** (15+) number of utterances. Always include varied phrasings and label ALL entities in every utterance.

---

### Building a CLU Model

#### Step-by-Step Workflow

1. **Create a Language resource** in Azure Portal
2. **Open Language Studio** (language.cognitive.azure.com)
3. **Create a CLU project**
   - Name the project
   - Set the primary language
   - Optionally enable multiple languages
4. **Define intents**
   - Add intents (e.g., BookFlight, GetWeather, CancelOrder)
   - The None intent is created automatically
5. **Define entities**
   - Add learned, list, prebuilt, or regex entities
6. **Add utterances**
   - Type or paste example utterances for each intent
   - Label entities within utterances by selecting text
7. **Train the model**
   - Select training mode (standard or advanced)
   - Start training
8. **Evaluate the model**
   - Review precision, recall, and F1 scores
   - Analyze the confusion matrix
9. **Deploy the model**
   - Deploy to a named slot (e.g., "production")
10. **Test and integrate**
    - Test in Language Studio
    - Call from your application via SDK or REST

---

### Training and Evaluation

#### Training Modes

| Mode | Description | Use Case |
|------|-------------|----------|
| **Standard** | Faster, simpler training | Development/testing |
| **Advanced** | Deeper training, better quality | Production |

#### Evaluation Metrics

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| **Precision** | TP / (TP + FP) | Of all predictions for this intent, how many were correct? |
| **Recall** | TP / (TP + FN) | Of all actual instances of this intent, how many were found? |
| **F1 Score** | 2 × (P × R) / (P + R) | Harmonic mean of precision and recall |

- **TP** = True Positive (correctly predicted)
- **FP** = False Positive (incorrectly predicted as this intent)
- **FN** = False Negative (this intent was missed)

#### Confusion Matrix

The confusion matrix shows where the model confuses intents:

```
                Predicted
               Book  Weather  Cancel  None
Actual  Book    45      2       1      2
       Weather   1     38       0      1
       Cancel    3      0      35      2
       None      0      1       1     18
```

- Diagonal = correct predictions
- Off-diagonal = misclassifications
- Look for patterns to add more training data where confusion occurs

#### Improving Model Quality

| Issue | Solution |
|-------|----------|
| Low precision for an intent | Add more None examples; make intent boundaries clearer |
| Low recall for an intent | Add more utterance variations for that intent |
| Two intents confused | Add distinguishing utterances; consider merging if too similar |
| Entity not recognized | Add more labeled examples with varied context |
| Overall low scores | Increase utterance count to 30+ per intent |

> **EXAM TIP:** Know the difference between precision (fewer false positives) and recall (fewer false negatives). If the exam describes a scenario where the model predicts an intent incorrectly too often, **precision** is the problem. If it fails to detect an intent, **recall** is the problem. The **F1 score** is the balanced measure.

---

### Deployment and Testing

#### Deploy to a Slot

```
Project: FlightBooking
Model: model-v2
Deployment Name: production
```

Multiple deployment slots allow A/B testing and staged rollouts.

#### API Endpoint Structure

```
POST https://<resource>.cognitiveservices.azure.com/language/:analyze-conversations?api-version=2023-04-01
```

#### REST Example — Analyze Conversation

```http
POST https://<resource>.cognitiveservices.azure.com/language/:analyze-conversations?api-version=2023-04-01
Content-Type: application/json
Ocp-Apim-Subscription-Key: <key>

{
  "kind": "Conversation",
  "analysisInput": {
    "conversationItem": {
      "id": "1",
      "text": "Book a flight from Seattle to Tokyo on March 15",
      "modality": "text",
      "language": "en",
      "participantId": "user1"
    }
  },
  "parameters": {
    "projectName": "FlightBooking",
    "deploymentName": "production",
    "stringIndexType": "TextElement_v8"
  }
}
```

**Response:**

```json
{
  "kind": "ConversationResult",
  "result": {
    "query": "Book a flight from Seattle to Tokyo on March 15",
    "prediction": {
      "topIntent": "BookFlight",
      "projectKind": "Conversation",
      "intents": [
        { "category": "BookFlight", "confidenceScore": 0.95 },
        { "category": "None", "confidenceScore": 0.03 },
        { "category": "GetWeather", "confidenceScore": 0.02 }
      ],
      "entities": [
        {
          "category": "Origin",
          "text": "Seattle",
          "offset": 22,
          "length": 7,
          "confidenceScore": 0.92
        },
        {
          "category": "Destination",
          "text": "Tokyo",
          "offset": 33,
          "length": 5,
          "confidenceScore": 0.94
        },
        {
          "category": "DepartureDate",
          "text": "March 15",
          "offset": 42,
          "length": 8,
          "confidenceScore": 0.89
        }
      ]
    }
  }
}
```

---

### Client App Consumption (Python SDK)

```python
from azure.ai.language.conversations import ConversationAnalysisClient
from azure.core.credentials import AzureKeyCredential

endpoint = "https://<resource>.cognitiveservices.azure.com/"
key = "<api-key>"
project_name = "FlightBooking"
deployment_name = "production"

client = ConversationAnalysisClient(endpoint, AzureKeyCredential(key))

result = client.analyze_conversation(
    task={
        "kind": "Conversation",
        "analysisInput": {
            "conversationItem": {
                "id": "1",
                "text": "Book a flight from Seattle to Tokyo on March 15",
                "modality": "text",
                "language": "en",
                "participantId": "user1"
            }
        },
        "parameters": {
            "projectName": project_name,
            "deploymentName": deployment_name,
            "stringIndexType": "TextElement_v8"
        }
    }
)

prediction = result["result"]["prediction"]

# Get the top intent
top_intent = prediction["topIntent"]
confidence = next(
    i["confidenceScore"]
    for i in prediction["intents"]
    if i["category"] == top_intent
)

print(f"Top Intent: {top_intent} (Confidence: {confidence:.2f})")

# Extract entities
for entity in prediction["entities"]:
    print(f"  Entity: {entity['category']} = '{entity['text']}' "
          f"(Confidence: {entity['confidenceScore']:.2f})")

# Confidence threshold pattern
if confidence >= 0.7:
    if top_intent == "BookFlight":
        # Extract entities and process booking
        entities = {e["category"]: e["text"] for e in prediction["entities"]}
        origin = entities.get("Origin", "unknown")
        destination = entities.get("Destination", "unknown")
        date = entities.get("DepartureDate", "unknown")
        print(f"Booking flight: {origin} → {destination} on {date}")
    elif top_intent == "CancelOrder":
        # Handle cancellation
        pass
else:
    print("Low confidence — asking user to rephrase.")
```

> **EXAM TIP:** Use `ConversationAnalysisClient` from `azure.ai.language.conversations` to consume CLU models. Always check the `confidenceScore` and implement a threshold (typically 0.7) — if confidence is too low, ask the user to rephrase instead of acting on an uncertain prediction.

---

### Import/Export

CLU projects can be exported as JSON for backup, version control, or migration between environments.

#### Export

```http
POST https://<resource>.cognitiveservices.azure.com/language/authoring/analyze-conversations/projects/{projectName}/:export?api-version=2023-04-01&stringIndexType=Utf16CodeUnit
Ocp-Apim-Subscription-Key: <key>
```

The export includes:
- Project metadata (name, language, description)
- All intents
- All entities (with list values, regex patterns)
- All utterances with entity labels
- Model training configuration

#### Import

```http
POST https://<resource>.cognitiveservices.azure.com/language/authoring/analyze-conversations/projects/{projectName}/:import?api-version=2023-04-01
Content-Type: application/json
Ocp-Apim-Subscription-Key: <key>

{
  "projectFileVersion": "2023-04-01",
  "stringIndexType": "Utf16CodeUnit",
  "metadata": {
    "projectKind": "Conversation",
    "projectName": "FlightBooking",
    "multilingual": false,
    "language": "en-us"
  },
  "assets": {
    "projectKind": "Conversation",
    "intents": [
      { "category": "BookFlight" },
      { "category": "GetWeather" },
      { "category": "None" }
    ],
    "entities": [
      { "category": "Origin" },
      { "category": "Destination" },
      { "category": "DepartureDate", "prebuilts": ["DateTime.Date"] }
    ],
    "utterances": [
      {
        "text": "Book a flight from Seattle to Tokyo",
        "language": "en-us",
        "intent": "BookFlight",
        "entities": [
          { "category": "Origin", "offset": 22, "length": 7 },
          { "category": "Destination", "offset": 33, "length": 5 }
        ]
      }
    ]
  }
}
```

#### Use Cases for Import/Export

| Scenario | Approach |
|----------|----------|
| **Backup** | Regularly export project JSON |
| **CI/CD** | Store exported JSON in Git; import during deployment |
| **Environment migration** | Export from dev, import to production Language resource |
| **Versioning** | Export after each training cycle with version tags |
| **Team collaboration** | Share project files via source control |

> **EXAM TIP:** CLU projects are exported as **JSON**. You can import the exported JSON into another Language resource to replicate the project. This is essential for **disaster recovery** and **CI/CD pipelines**. The export includes everything — intents, entities, utterances, and configuration.

---

### Optimize, Backup, and Recover

#### Model Versioning

- Each training run creates a named model version
- Keep previous versions for rollback
- Compare metrics across versions

#### Disaster Recovery Strategy

1. **Export regularly** — automate JSON export after each training
2. **Store in version control** — commit exported JSON to Git
3. **Secondary region** — import into a Language resource in another region
4. **Dual deployment** — deploy to both primary and secondary regions

#### Retraining Strategies

| Strategy | When to Use |
|----------|------------|
| Add more utterances | Model accuracy is low |
| Rebalance intents | One intent has far more utterances than others |
| Merge similar intents | Confusion matrix shows consistent misclassification |
| Split broad intents | One intent handles too many different scenarios |
| Add more entity labels | Entities are not being extracted consistently |

---

## PART 2: Custom Question Answering

Custom question answering enables you to create a knowledge base of QA pairs that can respond to user questions with natural language matching.

### Overview

| Feature | Description |
|---------|-------------|
| Service | Azure AI Language (with custom QA feature enabled) |
| Portal | Language Studio |
| Input sources | Manual entry, URLs, documents |
| Matching | Semantic matching (not just keyword) |
| Responses | Text answers with confidence scores |

---

### Create a Project

#### Prerequisites

1. Create an **Azure AI Language** resource
2. Enable the **Custom question answering** feature during creation
3. Link an **Azure Cognitive Search** resource (required for indexing QA pairs)

#### Project Settings

| Setting | Description |
|---------|-------------|
| Name | Project identifier |
| Language | Primary language (or enable multi-language) |
| Default answer | Response when no match is found |
| Description | Optional project description |

> **EXAM TIP:** Custom question answering requires BOTH an **Azure AI Language** resource AND an **Azure Cognitive Search** resource. The Search resource stores the QA index. Without Search, you cannot create a custom QA project.

---

### Add QA Pairs

#### Manual Entry

Add questions and answers directly in Language Studio:

```
Question: What are your business hours?
Answer: We are open Monday through Friday, 9 AM to 5 PM Eastern Time.

Alternative questions:
  - When are you open?
  - What time do you close?
  - Are you open on weekends?
```

#### Import from URLs

Provide FAQ page URLs and the service extracts QA pairs automatically:

```
Source URL: https://www.contoso.com/faq
Source URL: https://www.contoso.com/support/common-questions
```

Supported page types:
- Standard FAQ pages (Q&A format)
- Product support pages
- Policy pages with clear question/answer structures

#### Import from Documents

Upload files to extract QA pairs:

| Format | Extension |
|--------|-----------|
| PDF | .pdf |
| Word | .docx |
| Excel | .xlsx |
| Text | .txt |
| TSV | .tsv |
| HTML | .html |

#### Structured QA Pairs with Metadata

Add metadata to QA pairs for filtering:

```json
{
  "question": "How do I reset my password?",
  "answer": "Go to Settings > Security > Reset Password and follow the prompts.",
  "metadata": {
    "category": "account",
    "product": "web-app",
    "difficulty": "easy"
  }
}
```

Metadata can be used to filter answers at query time.

---

### Multi-Turn Conversations

Multi-turn conversations enable follow-up prompts that guide the user through a series of related questions.

#### How It Works

```
User: How do I return an item?
Bot: What type of item are you returning?
     → [Electronics]  → "Electronics must be returned within 15 days..."
     → [Clothing]     → "Clothing can be returned within 30 days..."
     → [Books]        → "Books are non-returnable..."
```

#### Configuration

Each QA pair can have **follow-up prompts**:

| Property | Description |
|----------|-------------|
| `displayText` | Text shown on the button/link |
| `qnaId` | Links to another QA pair |
| `contextOnly` | If true, answer only appears in this context |

```json
{
  "question": "How do I return an item?",
  "answer": "What type of item are you returning?",
  "context": {
    "isContextOnly": false,
    "prompts": [
      {
        "displayOrder": 1,
        "displayText": "Electronics",
        "qnaId": 10
      },
      {
        "displayOrder": 2,
        "displayText": "Clothing",
        "qnaId": 11
      },
      {
        "displayOrder": 3,
        "displayText": "Books",
        "qnaId": 12
      }
    ]
  }
}
```

#### Context-Only Answers

When `isContextOnly: true`, the answer only appears as part of a multi-turn flow — it won't be returned for top-level queries.

```json
{
  "id": 10,
  "question": "Electronics return policy",
  "answer": "Electronics must be returned within 15 days in original packaging with receipt.",
  "context": {
    "isContextOnly": true,
    "prompts": []
  }
}
```

> **EXAM TIP:** Multi-turn conversations use **follow-up prompts** that link to other QA pairs. The `isContextOnly` property determines whether an answer appears only in context (true) or also as a standalone answer (false). The exam may present a scenario where answers should NOT appear without context.

---

### Alternate Phrasings

Adding multiple question variations improves matching accuracy:

```
Primary question: "What are your business hours?"
Alternate phrasings:
  - "When are you open?"
  - "What time do you close?"
  - "Are you open on weekends?"
  - "Operating hours"
  - "When can I visit?"
  - "Store hours"
  - "What days are you open?"
```

Best practices:
- Add 5–10 alternate phrasings per QA pair
- Include informal and formal variations
- Include different word orders
- Include abbreviations and full forms

---

### Chit-Chat Personality

Add built-in social conversation capabilities to make your bot more engaging.

#### Available Personalities

| Personality | Tone | Example Response to "Tell me a joke" |
|-------------|------|--------------------------------------|
| **Professional** | Formal, business-like | "I'm focused on helping you with your questions." |
| **Friendly** | Warm, casual | "Sure! Why did the developer go broke? Because he used up all his cache!" |
| **Witty** | Humorous, clever | "I'm not great at jokes, but I'm pretty good at answers!" |
| **Caring** | Empathetic, supportive | "I'd love to make you smile! Here's a fun fact instead..." |
| **Enthusiastic** | Energetic, excited | "Oh, I love jokes! Here's one that always gets me..." |

#### Adding Chit-Chat

In Language Studio:
1. Go to your QA project
2. Select "Add source"
3. Choose "Chit-chat"
4. Select a personality

Chit-chat adds pre-built QA pairs for common social interactions:
- Greetings ("Hi", "Hello", "How are you?")
- Goodbyes ("Bye", "See you later")
- Gratitude ("Thank you", "Thanks")
- Small talk ("Tell me a joke", "What's your name?")

> **EXAM TIP:** Chit-chat is added as a **data source** — it's a set of pre-built QA pairs, not a separate model. You select ONE personality per project. Chit-chat QA pairs can be edited or deleted like any other QA pair.

---

### Synonyms

Synonyms expand the matching capability by telling the service that certain words are interchangeable.

#### How Synonyms Work

Synonyms are defined at the **project level** (not per QA pair). When a user's question contains a synonym, the service treats it as equivalent to the original term.

```json
{
  "synonyms": [
    {
      "alterations": ["fix", "solve", "resolve", "troubleshoot", "repair"]
    },
    {
      "alterations": ["cost", "price", "fee", "charge", "rate"]
    },
    {
      "alterations": ["PC", "computer", "laptop", "desktop", "machine"]
    }
  ]
}
```

#### Synonyms vs Alternate Phrasings

| Feature | Synonyms | Alternate Phrasings |
|---------|----------|---------------------|
| Scope | Project-level (all QA pairs) | Per QA pair |
| Granularity | Single word/term | Full question |
| Use case | Interchangeable terms | Different ways of asking |
| Example | "fix" ↔ "solve" ↔ "repair" | "How do I fix it?" ↔ "What's the solution?" |

> **EXAM TIP:** Synonyms work at the **project level** and apply to ALL QA pairs. They handle single-word substitutions. Alternate phrasings are **per QA pair** and handle different sentence structures. Use synonyms for vocabulary expansion and alternate phrasings for structural variations.

---

### Train, Test, and Publish

#### Testing in Language Studio

1. Click "Test" in Language Studio
2. Enter a question
3. Review the top answer, confidence score, and source
4. Check if follow-up prompts appear (for multi-turn)
5. Inspect alternative answers

#### Confidence Scores

| Score Range | Interpretation |
|-------------|----------------|
| 0.90–1.00 | High confidence — strong match |
| 0.70–0.89 | Good confidence — likely correct |
| 0.50–0.69 | Moderate — may need validation |
| 0.30–0.49 | Low — uncertain match |
| 0.00–0.29 | Very low — likely wrong answer |

Set a **confidence threshold** in your application to control when the default answer is returned instead of a low-confidence match.

#### Publishing

1. Click "Deploy knowledge base" in Language Studio
2. Select the deployment slot (production)
3. Confirm deployment

After publishing, you receive:
- Endpoint URL
- Project name
- Deployment name
- API key

#### REST Example — Query Custom QA

```http
POST https://<resource>.cognitiveservices.azure.com/language/:query-knowledgebases?projectName=ContosoFAQ&deploymentName=production&api-version=2021-10-01
Content-Type: application/json
Ocp-Apim-Subscription-Key: <key>

{
  "question": "What are your business hours?",
  "top": 3,
  "confidenceScoreThreshold": 0.5,
  "includeUnstructuredSources": true,
  "filters": {
    "metadataFilter": {
      "logicalOperation": "AND",
      "metadata": [
        { "key": "category", "value": "general" }
      ]
    }
  }
}
```

**Response:**

```json
{
  "answers": [
    {
      "questions": ["What are your business hours?"],
      "answer": "We are open Monday through Friday, 9 AM to 5 PM Eastern Time.",
      "confidenceScore": 0.95,
      "id": 1,
      "source": "manual",
      "metadata": { "category": "general" },
      "dialog": {
        "isContextOnly": false,
        "prompts": [
          {
            "displayOrder": 1,
            "displayText": "Holiday hours",
            "qnaId": 15
          }
        ]
      }
    }
  ]
}
```

#### Python SDK — Query Custom QA

```python
from azure.ai.language.questionanswering import QuestionAnsweringClient
from azure.core.credentials import AzureKeyCredential

endpoint = "https://<resource>.cognitiveservices.azure.com/"
key = "<api-key>"
project_name = "ContosoFAQ"
deployment_name = "production"

client = QuestionAnsweringClient(endpoint, AzureKeyCredential(key))

response = client.get_answers(
    question="How do I reset my password?",
    project_name=project_name,
    deployment_name=deployment_name,
    confidence_threshold=0.5,
    top=3
)

for answer in response.answers:
    print(f"Answer: {answer.answer}")
    print(f"Confidence: {answer.confidence:.2f}")
    print(f"Source: {answer.source}")

    # Handle follow-up prompts (multi-turn)
    if answer.dialog and answer.dialog.prompts:
        print("Follow-up options:")
        for prompt in answer.dialog.prompts:
            print(f"  → {prompt.display_text}")
```

> **EXAM TIP:** Use `QuestionAnsweringClient` from `azure.ai.language.questionanswering` to query custom QA. Set `confidence_threshold` to filter low-quality answers. Check `answer.dialog.prompts` for multi-turn follow-up options. The response includes the `source` field showing where the answer came from (URL, file, or manual).

---

### Export

Export QA projects for backup or migration:

| Format | Use Case |
|--------|----------|
| **JSON** | Full export including metadata, settings, synonyms |
| **TSV** | Simple Q&A pair export (question, answer, metadata) |
| **Excel** | Editable format for business users |

#### REST Example — Export

```http
POST https://<resource>.cognitiveservices.azure.com/language/authoring/query-knowledgebases/projects/{projectName}/:export?api-version=2021-10-01&format=json
Ocp-Apim-Subscription-Key: <key>
```

#### Migration Workflow

1. Export from source environment (JSON)
2. Import into target Language resource
3. Retrain and republish
4. Update client applications with new endpoint

---

### Multi-Language Support

#### Single-Language Projects

- All QA pairs in one language
- Questions must be in the same language
- Simpler to manage

#### Multi-Language Projects

- QA pairs can be in different languages
- Questions auto-detected and matched to appropriate language pairs
- Enable "Multi-language" when creating the project

```json
{
  "question": "What are your hours?",
  "answer": "We are open 9 AM to 5 PM.",
  "language": "en"
},
{
  "question": "Quelles sont vos heures?",
  "answer": "Nous sommes ouverts de 9h à 17h.",
  "language": "fr"
}
```

> **EXAM TIP:** Multi-language support must be **enabled at project creation** — you cannot change this later. In a multi-language project, each QA pair is tagged with a language code. The service detects the query language and matches against QA pairs in that language.

---

## Comparison: CLU vs Custom Question Answering

| Feature | CLU | Custom Question Answering |
|---------|-----|---------------------------|
| Purpose | Detect intent and extract entities | Return answers to questions |
| Input | User utterance (command/request) | User question (seeking information) |
| Output | Intent + entities | Answer text + confidence |
| Training data | Intents + utterances + entities | QA pairs |
| Use case | "Book a flight", "Turn on the lights" | "What are your hours?", "How do I reset my password?" |
| Portal | Language Studio | Language Studio |
| SDK | `azure-ai-language-conversations` | `azure-ai-language-questionanswering` |
| Multi-turn | No (handled by orchestration) | Yes (follow-up prompts) |

> **EXAM TIP:** CLU and custom QA solve **different problems**. CLU understands **intent** ("what does the user want to do?"). Custom QA finds **answers** ("what information does the user need?"). The exam may describe a scenario and ask which service to use — look for intent extraction vs information retrieval.

---

## Key Takeaways

1. **CLU** detects user **intent** and extracts **entities** from utterances. It replaces LUIS.
2. The **None intent** is required and catches irrelevant input — include at least 10% of utterances in None.
3. CLU supports four entity types: **learned** (from labeled examples), **list** (predefined values), **prebuilt** (DateTime, Number, etc.), and **regex** (pattern matching).
4. Use at least **5 utterances per intent** (15+ recommended), with varied phrasings and all entities labeled.
5. Evaluate with **precision** (correct predictions), **recall** (found all instances), and **F1 score** (balanced metric). Use the **confusion matrix** to identify problem areas.
6. CLU projects can be **exported as JSON** for backup, CI/CD, and disaster recovery.
7. Use `ConversationAnalysisClient` in Python to consume CLU models.
8. **Custom question answering** returns answers to user questions from a knowledge base of QA pairs.
9. Custom QA requires both a **Language resource** and an **Azure Cognitive Search** resource.
10. **Multi-turn** conversations use follow-up prompts. `isContextOnly: true` hides answers from top-level queries.
11. **Synonyms** are project-level word substitutions; **alternate phrasings** are per-QA-pair question variations.
12. **Chit-chat** personalities (Professional, Friendly, Witty, Caring, Enthusiastic) add pre-built social QA pairs.
13. Use `QuestionAnsweringClient` in Python with a confidence threshold to query custom QA.

---

## Microsoft Documentation

- [CLU overview](https://learn.microsoft.com/azure/ai-services/language-service/conversational-language-understanding/overview)
- [CLU quickstart](https://learn.microsoft.com/azure/ai-services/language-service/conversational-language-understanding/quickstart)
- [CLU entity types](https://learn.microsoft.com/azure/ai-services/language-service/conversational-language-understanding/concepts/entity-components)
- [Custom question answering overview](https://learn.microsoft.com/azure/ai-services/language-service/question-answering/overview)
- [Custom QA quickstart](https://learn.microsoft.com/azure/ai-services/language-service/question-answering/quickstart)
- [Multi-turn conversations](https://learn.microsoft.com/azure/ai-services/language-service/question-answering/how-to/multi-turn)
- [Synonyms in custom QA](https://learn.microsoft.com/azure/ai-services/language-service/question-answering/how-to/add-synonyms)
