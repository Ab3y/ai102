# Lesson 2: Implement Azure OpenAI Service

## Learning Objectives

- Provision Azure OpenAI and deploy models (GPT-4o, embeddings, DALL-E)
- Use the chat completions API with message roles
- Tune parameters (temperature, top_p, max_tokens, penalties)
- Calculate and manage token usage
- Generate images with DALL-E
- Work with multimodal models
- Understand REST endpoint structure and authentication

---

## Provisioning Azure OpenAI

### Region Availability

Azure OpenAI is **not available in all regions**. Key regions:

| Region | GPT-4o | DALL-E 3 | Embeddings | Whisper |
|--------|--------|----------|------------|---------|
| East US | ✅ | ✅ | ✅ | ✅ |
| East US 2 | ✅ | ✅ | ✅ | ✅ |
| West US | ✅ | ❌ | ✅ | ✅ |
| Sweden Central | ✅ | ✅ | ✅ | ✅ |
| UK South | ✅ | ❌ | ✅ | ✅ |
| Japan East | ✅ | ❌ | ✅ | ✅ |

> ### 📝 Exam Tip
> The exam may present a scenario where a specific model is needed and ask which region supports it. Always check **model availability by region** — not all models are available everywhere. DALL-E 3 has the most limited availability.

### Creating the Resource

```bash
# Create Azure OpenAI resource
az cognitiveservices account create \
    --name my-openai \
    --resource-group rg-ai \
    --kind OpenAI \
    --sku S0 \
    --location eastus2 \
    --yes
```

### Deploying Models

Each model must be **deployed** before use. A deployment maps a model to an endpoint.

```bash
# Deploy GPT-4o
az cognitiveservices account deployment create \
    --name my-openai \
    --resource-group rg-ai \
    --deployment-name gpt-4o \
    --model-name gpt-4o \
    --model-version "2024-05-13" \
    --model-format OpenAI \
    --sku-capacity 10 \
    --sku-name Standard

# Deploy text-embedding-ada-002
az cognitiveservices account deployment create \
    --name my-openai \
    --resource-group rg-ai \
    --deployment-name text-embedding \
    --model-name text-embedding-ada-002 \
    --model-version "2" \
    --model-format OpenAI \
    --sku-capacity 10 \
    --sku-name Standard

# Deploy DALL-E 3
az cognitiveservices account deployment create \
    --name my-openai \
    --resource-group rg-ai \
    --deployment-name dall-e-3 \
    --model-name dall-e-3 \
    --model-version "3.0" \
    --model-format OpenAI \
    --sku-capacity 1 \
    --sku-name Standard
```

---

## Chat Completions API

### Message Roles

The chat completions API uses a conversation format with three roles:

| Role | Purpose | Example |
|------|---------|---------|
| **system** | Sets the AI's behavior, personality, and constraints | "You are a helpful assistant that speaks formally." |
| **user** | The human's input message | "What is Azure?" |
| **assistant** | Previous AI responses (for context/history) | "Azure is Microsoft's cloud platform..." |

### Python SDK

```python
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="https://my-openai.openai.azure.com/",
    api_key="<api-key>",
    api_version="2024-02-01"
)

response = client.chat.completions.create(
    model="gpt-4o",         # This is the deployment name
    messages=[
        {
            "role": "system",
            "content": "You are a helpful AI assistant specialized in Azure services."
        },
        {
            "role": "user",
            "content": "What is Azure AI Search?"
        }
    ],
    temperature=0.7,
    max_tokens=800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0
)

print(response.choices[0].message.content)
print(f"Tokens used: {response.usage.total_tokens}")
```

### REST API

```http
POST https://my-openai.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-02-01
Content-Type: application/json
api-key: <your-api-key>

{
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "What is Azure AI Search?"
    }
  ],
  "temperature": 0.7,
  "max_tokens": 800,
  "top_p": 0.95,
  "frequency_penalty": 0,
  "presence_penalty": 0
}
```

**Response structure:**

```json
{
  "id": "chatcmpl-abc123",
  "object": "chat.completion",
  "created": 1699000000,
  "model": "gpt-4o",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Azure AI Search is a cloud search service..."
      },
      "finish_reason": "stop",
      "content_filter_results": {
        "hate": { "filtered": false, "severity": "safe" },
        "violence": { "filtered": false, "severity": "safe" },
        "sexual": { "filtered": false, "severity": "safe" },
        "self_harm": { "filtered": false, "severity": "safe" }
      }
    }
  ],
  "usage": {
    "prompt_tokens": 25,
    "completion_tokens": 150,
    "total_tokens": 175
  }
}
```

> ### 📝 Exam Tip
> Know the REST endpoint structure: `https://{resource}.openai.azure.com/openai/deployments/{deployment}/chat/completions?api-version={version}`. The deployment name goes in the URL path, and `api-key` is the authentication header (not `Ocp-Apim-Subscription-Key`).

---

## Multi-Turn Conversations

For chat applications, include conversation history in the messages array:

```python
conversation = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is Azure?"},
    {"role": "assistant", "content": "Azure is Microsoft's cloud computing platform."},
    {"role": "user", "content": "What AI services does it offer?"}  # Follow-up
]

response = client.chat.completions.create(
    model="gpt-4o",
    messages=conversation,
    temperature=0.7,
    max_tokens=500
)

# Add response to history for next turn
conversation.append({
    "role": "assistant",
    "content": response.choices[0].message.content
})
```

---

## Parameters Deep Dive

### Parameter Reference

| Parameter | Range | Default | Effect |
|-----------|-------|---------|--------|
| `temperature` | 0.0–2.0 | 1.0 | Randomness — higher = more creative, lower = more focused |
| `top_p` | 0.0–1.0 | 1.0 | Nucleus sampling — limits token pool by cumulative probability |
| `max_tokens` | 1–model max | Model dependent | Maximum tokens in the completion |
| `frequency_penalty` | -2.0–2.0 | 0 | Penalizes tokens based on their frequency in the text so far |
| `presence_penalty` | -2.0–2.0 | 0 | Penalizes tokens based on whether they appear at all in the text |
| `stop` | String/array | null | Stop sequences — generation stops when encountered |
| `n` | 1–128 | 1 | Number of completions to generate |

### When to Use Which Parameter

| Scenario | Recommended Settings |
|----------|---------------------|
| **Factual Q&A / RAG** | `temperature: 0.0–0.3`, `top_p: 1.0` |
| **Creative writing** | `temperature: 0.8–1.2`, `top_p: 0.9` |
| **Code generation** | `temperature: 0.0–0.2`, `top_p: 1.0` |
| **Diverse brainstorming** | `temperature: 1.0`, `presence_penalty: 0.6` |
| **Concise responses** | `max_tokens: 100–300`, `temperature: 0.5` |

### Temperature vs. Top_p

```
temperature = 0.0  →  Always picks the most likely token (deterministic)
temperature = 1.0  →  Standard sampling from full distribution
temperature = 2.0  →  Very random, often incoherent

top_p = 0.1  →  Only considers top 10% probability mass
top_p = 0.5  →  Considers top 50% probability mass
top_p = 1.0  →  Considers all tokens (default)
```

> ### 📝 Exam Tip
> **Do not modify both `temperature` and `top_p` simultaneously** — Microsoft recommends adjusting one or the other. The exam may test this. Also know that `temperature: 0` gives the most deterministic (but not perfectly identical) results.

---

## Token Calculation

### What Is a Token?

- A token ≈ 4 characters in English text
- A token ≈ ¾ of a word
- 1,000 tokens ≈ 750 words

### Token Limits

| Model | Context Window | Max Output |
|-------|---------------|------------|
| GPT-4o | 128,000 tokens | 16,384 tokens |
| GPT-4o-mini | 128,000 tokens | 16,384 tokens |
| GPT-4 (8K) | 8,192 tokens | 8,192 tokens |
| GPT-4 (32K) | 32,768 tokens | 32,768 tokens |
| text-embedding-ada-002 | 8,191 tokens | N/A (returns vector) |

### Cost Calculation

```
Total cost = (prompt_tokens × input_price) + (completion_tokens × output_price)

Example for GPT-4o:
  Input:  1,000 tokens × $0.005/1K = $0.005
  Output:   500 tokens × $0.015/1K = $0.0075
  Total: $0.0125 per request
```

### Counting Tokens (Python)

```python
import tiktoken

# Get the tokenizer for GPT-4o
encoding = tiktoken.encoding_for_model("gpt-4o")

text = "Azure AI services provide cloud-based AI capabilities."
tokens = encoding.encode(text)
print(f"Token count: {len(tokens)}")  # Token count: 9
print(f"Tokens: {tokens}")            # [35694, 15592, 3600, ...]
```

---

## Embeddings

Embeddings convert text into numerical vectors for semantic search, clustering, and RAG.

### Generating Embeddings

```python
response = client.embeddings.create(
    model="text-embedding",   # deployment name
    input="Azure AI Search enables intelligent search"
)

embedding = response.data[0].embedding
print(f"Dimensions: {len(embedding)}")   # 1536 for ada-002
print(f"First 5 values: {embedding[:5]}")
```

### REST API

```http
POST https://my-openai.openai.azure.com/openai/deployments/text-embedding/embeddings?api-version=2024-02-01
Content-Type: application/json
api-key: <key>

{
  "input": "Azure AI Search enables intelligent search"
}
```

### Batch Embeddings

```python
texts = [
    "First document about Azure",
    "Second document about AI",
    "Third document about search"
]

response = client.embeddings.create(
    model="text-embedding",
    input=texts
)

for i, item in enumerate(response.data):
    print(f"Document {i}: {len(item.embedding)} dimensions")
```

---

## DALL-E Image Generation

### Generating Images

```python
response = client.images.generate(
    model="dall-e-3",       # deployment name
    prompt="A futuristic data center in the clouds, digital art style",
    size="1024x1024",       # 1024x1024, 1792x1024, or 1024x1792
    quality="standard",     # "standard" or "hd"
    n=1                     # DALL-E 3 only supports n=1
)

image_url = response.data[0].url
revised_prompt = response.data[0].revised_prompt
print(f"Image URL: {image_url}")
print(f"Revised prompt: {revised_prompt}")
```

### REST API

```http
POST https://my-openai.openai.azure.com/openai/deployments/dall-e-3/images/generations?api-version=2024-02-01
Content-Type: application/json
api-key: <key>

{
  "prompt": "A futuristic data center in the clouds",
  "size": "1024x1024",
  "quality": "standard",
  "n": 1
}
```

### DALL-E 3 Specifications

| Parameter | Options |
|-----------|---------|
| Size | `1024x1024`, `1792x1024`, `1024x1792` |
| Quality | `standard`, `hd` |
| Count (n) | `1` only (DALL-E 3 limitation) |
| Style | `natural`, `vivid` |

> ### 📝 Exam Tip
> DALL-E 3 only supports `n=1` (one image per request). It automatically **revises your prompt** for better results — the `revised_prompt` field shows what was actually used. DALL-E 3 sizes differ from DALL-E 2.

---

## Multimodal Models (Vision)

GPT-4o can process both text and images:

```python
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe what you see in this image."},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://example.com/photo.jpg",
                        "detail": "high"   # "low", "high", or "auto"
                    }
                }
            ]
        }
    ],
    max_tokens=300
)
```

### Image Input Options

| Method | Format |
|--------|--------|
| URL | `"url": "https://..."` |
| Base64 | `"url": "data:image/png;base64,{base64_data}"` |

### Detail Levels

| Level | Token Cost | Use Case |
|-------|-----------|----------|
| `low` | 85 tokens fixed | Quick classification, simple questions |
| `high` | Variable (based on image size) | Detailed analysis, OCR, fine-grained tasks |
| `auto` | Model decides | Default — let the model choose |

---

## REST Endpoint Structure Summary

```
Base: https://{resource-name}.openai.azure.com/openai/deployments/{deployment-name}

Chat:       /chat/completions?api-version=2024-02-01
Embeddings: /embeddings?api-version=2024-02-01
Images:     /images/generations?api-version=2024-02-01
Audio:      /audio/transcriptions?api-version=2024-02-01

Authentication: api-key header
```

---

## Key Takeaways

1. **Azure OpenAI** has limited regional availability — always verify model availability before choosing a region.
2. **Model deployment** is separate from resource creation — you deploy specific model versions to named deployments.
3. **Chat completions** use three roles: `system` (behavior), `user` (input), `assistant` (history).
4. **Temperature** controls randomness (0 = deterministic, 2 = very random); don't adjust both `temperature` and `top_p` together.
5. **Token costs** differ for input vs. output; use `tiktoken` to estimate token counts before sending.
6. **DALL-E 3** only generates one image at a time (`n=1`), automatically revises prompts, and has specific size options.
7. **GPT-4o** supports multimodal input (text + images) with configurable detail levels.

---

## Further Reading

- [Azure OpenAI Service documentation](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Chat completions API reference](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference)
- [DALL-E quickstart](https://learn.microsoft.com/en-us/azure/ai-services/openai/dall-e-quickstart)
- [Model availability by region](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models#model-summary-table-and-region-availability)
- [Tokens and pricing](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/openai-service/)
