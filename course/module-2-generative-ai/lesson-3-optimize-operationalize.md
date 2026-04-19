# Lesson 3: Optimize and Operationalize Generative AI

## Learning Objectives

- Apply prompt engineering techniques (few-shot, chain-of-thought, system prompts)
- Tune parameters for different use cases
- Understand fine-tuning vs. RAG vs. prompt engineering trade-offs
- Monitor models and implement tracing/feedback
- Deploy models in containers for edge scenarios
- Orchestrate multi-model pipelines

---

## Prompt Engineering Techniques

### System Prompts

The system message defines the AI's behavior, personality, constraints, and output format:

```python
messages = [
    {
        "role": "system",
        "content": """You are a customer service assistant for Contoso Electronics.

Rules:
- Only answer questions about Contoso products
- If asked about competitors, politely redirect to Contoso alternatives
- Always include a product SKU when recommending items
- Respond in the same language as the customer
- Keep responses under 200 words

Output format: Use bullet points for product features."""
    },
    {"role": "user", "content": "What laptop do you recommend for developers?"}
]
```

### Zero-Shot Prompting

No examples provided — rely on the model's training:

```python
messages = [
    {"role": "system", "content": "Classify the sentiment as Positive, Negative, or Neutral."},
    {"role": "user", "content": "The product quality is terrible and shipping was late."}
]
# Expected: "Negative"
```

### Few-Shot Prompting

Provide examples to guide the model's behavior:

```python
messages = [
    {"role": "system", "content": "Extract the product name and issue from support tickets."},
    # Example 1
    {"role": "user", "content": "My Surface Pro keeps crashing when I open Excel."},
    {"role": "assistant", "content": '{"product": "Surface Pro", "issue": "crashes with Excel"}'},
    # Example 2
    {"role": "user", "content": "Xbox controller not connecting via Bluetooth."},
    {"role": "assistant", "content": '{"product": "Xbox Controller", "issue": "Bluetooth connection failure"}'},
    # Actual input
    {"role": "user", "content": "Outlook on my Surface Laptop freezes during meetings."}
]
# Expected: {"product": "Surface Laptop", "issue": "Outlook freezes in meetings"}
```

### Chain-of-Thought (CoT) Prompting

Instruct the model to reason step-by-step:

```python
messages = [
    {
        "role": "system",
        "content": """You are a technical support assistant.
When diagnosing issues, think step by step:
1. Identify the symptoms
2. List possible causes
3. Recommend diagnostic steps
4. Suggest a solution
Show your reasoning before giving the final answer."""
    },
    {
        "role": "user",
        "content": "My Azure Function is timing out after 5 minutes."
    }
]
```

### Prompt Engineering Comparison

| Technique | When to Use | Pros | Cons |
|-----------|-------------|------|------|
| **Zero-shot** | Simple, well-defined tasks | No examples needed, fast | Less reliable for complex tasks |
| **Few-shot** | Format-specific output, classification | Consistent output format | Uses token budget for examples |
| **Chain-of-thought** | Complex reasoning, math, multi-step | Better accuracy on hard problems | More tokens, slower |
| **System prompt** | Behavior control, persona setting | Consistent behavior across turns | Can be overridden by jailbreaks |

> ### 📝 Exam Tip
> The exam tests when to use each technique. **Few-shot** is for consistent output formatting. **Chain-of-thought** is for complex reasoning. **System prompts** set behavioral boundaries. Know practical examples of each.

---

## Parameter Tuning Effects

### Temperature Experiments

```python
# Same prompt, different temperatures
prompt = "Suggest a name for a cloud computing startup."

# temperature=0.0 — Deterministic, always same answer
# "CloudPeak Technologies"

# temperature=0.5 — Moderate variety
# "NimbusScale Solutions" or "CloudPeak Technologies"

# temperature=1.0 — Creative variety
# "CirrusByte Innovations" or "VaporForge Labs"

# temperature=1.5+ — Often incoherent
# "Cl0udZephyr∆Works" (unreliable output)
```

### Frequency Penalty vs. Presence Penalty

```python
# frequency_penalty — Reduces repetition proportional to frequency
#   Higher values → model avoids repeating the same words
#   Useful for: reducing verbosity, avoiding loops

# presence_penalty — Encourages topic diversity
#   Higher values → model introduces new topics
#   Useful for: brainstorming, creative writing, exploring ideas
```

| Setting | frequency_penalty | presence_penalty | Best For |
|---------|------------------|-----------------|----------|
| Factual Q&A | 0 | 0 | Precise, focused answers |
| Summarization | 0.3 | 0 | Avoid repetitive phrasing |
| Brainstorming | 0 | 0.6 | Diverse ideas |
| Creative writing | 0.5 | 0.5 | Varied, engaging text |

---

## Fine-Tuning

### When to Fine-Tune vs. RAG vs. Prompt Engineering

```
Decision flow:
1. Can prompt engineering solve it?
   └── YES → Use prompt engineering (cheapest, fastest)
   └── NO → Continue to 2

2. Does the model need access to current/proprietary data?
   └── YES → Use RAG (search + retrieval)
   └── NO → Continue to 3

3. Does the model need a fundamentally different style/behavior?
   └── YES → Fine-tune the model
   └── NO → Revisit prompt engineering with more examples
```

### Comparison Table

| Approach | Cost | Effort | Data Needed | Best For |
|----------|------|--------|-------------|----------|
| **Prompt engineering** | Low (tokens only) | Hours | None | Output formatting, behavior control |
| **Few-shot prompting** | Low–Medium | Hours | 3–10 examples | Classification, extraction |
| **RAG** | Medium | Days | Document corpus | Grounded Q&A, current data access |
| **Fine-tuning** | High | Weeks | 50–1000+ examples | Consistent style, domain adaptation |

### Fine-Tuning Data Format (JSONL)

```jsonl
{"messages": [{"role": "system", "content": "You are a medical coding assistant."}, {"role": "user", "content": "Patient presents with acute bronchitis"}, {"role": "assistant", "content": "ICD-10: J20.9 - Acute bronchitis, unspecified"}]}
{"messages": [{"role": "system", "content": "You are a medical coding assistant."}, {"role": "user", "content": "Diagnosis: Type 2 diabetes mellitus with diabetic nephropathy"}, {"role": "assistant", "content": "ICD-10: E11.21 - Type 2 diabetes mellitus with diabetic nephropathy"}]}
{"messages": [{"role": "system", "content": "You are a medical coding assistant."}, {"role": "user", "content": "Patient treated for essential hypertension"}, {"role": "assistant", "content": "ICD-10: I10 - Essential (primary) hypertension"}]}
```

### Fine-Tuning Process

```python
# Step 1: Upload training data
file = client.files.create(
    file=open("training_data.jsonl", "rb"),
    purpose="fine-tune"
)

# Step 2: Create fine-tuning job
job = client.fine_tuning.jobs.create(
    training_file=file.id,
    model="gpt-4o-mini",
    hyperparameters={
        "n_epochs": 3,
        "batch_size": 1,
        "learning_rate_multiplier": 0.3
    }
)

# Step 3: Monitor training
status = client.fine_tuning.jobs.retrieve(job.id)
print(f"Status: {status.status}")

# Step 4: Use the fine-tuned model (after training completes)
response = client.chat.completions.create(
    model=status.fine_tuned_model,  # e.g., "ft:gpt-4o-mini:org:custom-name:abc123"
    messages=[...]
)
```

> ### 📝 Exam Tip
> Know the **JSONL format** for fine-tuning: each line is a JSON object with a `messages` array containing system, user, and assistant roles. The exam may show different formats and ask which is correct. Also remember: try prompt engineering first, then RAG, then fine-tuning.

---

## Model Monitoring and Tracing

### What to Monitor

| Metric | Why It Matters |
|--------|---------------|
| **Latency (P50, P95)** | User experience; detect model slowdowns |
| **Token throughput** | Capacity planning and cost management |
| **Error rate** | Content filter triggers, rate limits, timeouts |
| **Groundedness score** | RAG quality — are answers factually accurate? |
| **User feedback** | Direct signal of answer quality |

### Implementing Tracing

```python
import logging
import json
from datetime import datetime

def traced_completion(client, messages, **kwargs):
    """Wrapper that logs all OpenAI interactions for tracing."""
    start_time = datetime.utcnow()

    try:
        response = client.chat.completions.create(
            messages=messages,
            **kwargs
        )

        trace = {
            "timestamp": start_time.isoformat(),
            "model": kwargs.get("model", "unknown"),
            "prompt_tokens": response.usage.prompt_tokens,
            "completion_tokens": response.usage.completion_tokens,
            "latency_ms": (datetime.utcnow() - start_time).total_seconds() * 1000,
            "finish_reason": response.choices[0].finish_reason,
            "input": messages[-1]["content"][:200],
            "output": response.choices[0].message.content[:200]
        }
        logging.info(f"OpenAI trace: {json.dumps(trace)}")

        return response

    except Exception as e:
        logging.error(f"OpenAI error: {str(e)}")
        raise
```

### Feedback Collection

```python
def collect_feedback(trace_id: str, rating: int, comment: str = None):
    """Record user feedback for model improvement."""
    feedback = {
        "trace_id": trace_id,
        "rating": rating,          # 1-5 scale
        "comment": comment,
        "timestamp": datetime.utcnow().isoformat()
    }
    # Store in database or analytics service
    log_feedback(feedback)

    # Use negative feedback to improve system prompt or add to fine-tuning data
    if rating <= 2:
        flag_for_review(feedback)
```

---

## Container Deployment for Edge

For scenarios requiring low latency, data sovereignty, or offline capability:

```python
# Deploy a fine-tuned or small model to a container
# Use Azure ML managed endpoints

from azure.ai.ml.entities import (
    ManagedOnlineEndpoint,
    ManagedOnlineDeployment
)

# Create endpoint
endpoint = ManagedOnlineEndpoint(
    name="edge-model-endpoint",
    auth_mode="key"
)
ml_client.online_endpoints.begin_create_or_update(endpoint)

# Create deployment
deployment = ManagedOnlineDeployment(
    name="phi3-deployment",
    endpoint_name="edge-model-endpoint",
    model="azureml://registries/azureml/models/Phi-3-mini-4k-instruct/versions/1",
    instance_type="Standard_DS3_v2",
    instance_count=1
)
ml_client.online_deployments.begin_create_or_update(deployment)
```

### Edge Deployment Considerations

| Factor | Consideration |
|--------|--------------|
| **Model size** | Use smaller models (Phi-3) for edge; GPT-4o requires cloud |
| **Latency** | Local inference eliminates network round-trip |
| **Data privacy** | Data never leaves the device/location |
| **Connectivity** | Works offline (unlike AI service containers that need billing) |
| **Compute** | Requires sufficient GPU/CPU on edge device |

---

## Multi-Model Orchestration

### Pattern: Router Model

```python
def route_request(user_input: str) -> str:
    """Route to the appropriate model based on complexity."""

    # Use a cheap model to classify the request
    classification = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Classify as 'simple' or 'complex'."},
            {"role": "user", "content": user_input}
        ],
        max_tokens=10,
        temperature=0
    )

    complexity = classification.choices[0].message.content.strip().lower()

    if complexity == "simple":
        # Use cheaper model for simple queries
        model = "gpt-4o-mini"
    else:
        # Use powerful model for complex queries
        model = "gpt-4o"

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": user_input}],
        temperature=0.7
    )
    return response.choices[0].message.content
```

### Pattern: Reflection (Self-Verification)

```python
def reflect_and_improve(question: str, context: str) -> str:
    """Generate answer, then verify and improve it."""

    # Step 1: Generate initial answer
    initial = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": f"Answer using this context:\n{context}"},
            {"role": "user", "content": question}
        ]
    )
    initial_answer = initial.choices[0].message.content

    # Step 2: Reflect — check for errors
    reflection = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": """Review this answer for:
1. Factual errors compared to the context
2. Missing important information
3. Unclear explanations
Provide a corrected version if needed."""},
            {"role": "user", "content": f"Question: {question}\n\nContext: {context}\n\nAnswer: {initial_answer}"}
        ]
    )
    return reflection.choices[0].message.content
```

---

## Optimization Best Practices Summary

| Goal | Strategy |
|------|----------|
| **Reduce cost** | Use `gpt-4o-mini` for simple tasks, cache frequent queries, limit `max_tokens` |
| **Improve accuracy** | Lower temperature, use RAG for grounding, add few-shot examples |
| **Reduce latency** | Use streaming, reduce prompt length, use smaller models |
| **Handle scale** | Implement retry with exponential backoff, use provisioned throughput |
| **Ensure safety** | Content filters + prompt shields + system prompt guardrails |

---

## Key Takeaways

1. **Prompt engineering** is the first optimization lever: system prompts for behavior, few-shot for format, chain-of-thought for reasoning.
2. **Optimization hierarchy**: Prompt engineering → RAG → Fine-tuning (try in this order, increasing cost and effort).
3. **Fine-tuning** uses JSONL format with `messages` arrays; best for consistent style/behavior changes, not for accessing new data.
4. **Monitor** latency, token usage, error rates, and user feedback to maintain quality.
5. **Multi-model orchestration** routes simple queries to cheaper models and complex ones to powerful models.
6. **Model reflection** uses a second LLM call to verify and improve the initial response.

---

## Further Reading

- [Prompt engineering techniques](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering)
- [Fine-tuning Azure OpenAI models](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/fine-tuning)
- [Azure OpenAI best practices](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/advanced-prompt-engineering)
- [Monitoring Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/monitoring)
