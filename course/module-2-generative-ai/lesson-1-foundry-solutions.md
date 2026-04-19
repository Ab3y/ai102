# Lesson 1: Build Solutions with Microsoft Foundry

## Learning Objectives

- Understand the Microsoft Foundry hub and project architecture
- Navigate the model catalog and deploy models
- Create, test, and evaluate prompt flows
- Implement the RAG (Retrieval-Augmented Generation) pattern
- Use evaluation metrics to assess model quality
- Integrate Foundry with the SDK

---

## Microsoft Foundry Architecture

### Hub vs. Project

Microsoft Foundry uses a two-level hierarchy:

| Component | Purpose | Scope |
|-----------|---------|-------|
| **Hub** | Shared infrastructure — compute, connections, security policies | Organization or team level |
| **Project** | Individual workspace — models, flows, evaluations, deployments | Application or workload level |

```
Foundry Hub (Organization)
├── Shared Connections (Azure OpenAI, AI Search, Storage)
├── Shared Compute Resources
├── Security Policies & RBAC
│
├── Project A (Customer Chatbot)
│   ├── Model Deployments
│   ├── Prompt Flows
│   ├── Evaluations
│   └── Endpoints
│
├── Project B (Document Summarizer)
│   ├── Model Deployments
│   ├── Prompt Flows
│   ├── Evaluations
│   └── Endpoints
│
└── Project C (Code Assistant)
    └── ...
```

### Creating a Hub and Project

```bash
# Install the AI CLI extension
az extension add --name ml

# Create a hub
az ml workspace create \
    --kind hub \
    --name my-ai-hub \
    --resource-group rg-ai \
    --location eastus

# Create a project under the hub
az ml workspace create \
    --kind project \
    --name chatbot-project \
    --resource-group rg-ai \
    --hub-id /subscriptions/{sub}/resourceGroups/rg-ai/providers/Microsoft.MachineLearningServices/workspaces/my-ai-hub
```

> ### 📝 Exam Tip
> Know the difference between **Hub** (shared infrastructure, connections, policies) and **Project** (application-specific workspace). Hubs are managed by admins; projects by developers. Multiple projects share one hub's resources.

---

## Model Catalog

The model catalog provides access to models from multiple providers:

| Provider | Example Models | Deployment Type |
|----------|---------------|-----------------|
| **OpenAI** | GPT-4o, GPT-4o-mini, DALL-E 3 | Managed compute or Azure OpenAI |
| **Microsoft** | Phi-3, Phi-3.5 | Managed compute (serverless) |
| **Meta** | Llama 3, Llama 3.1 | Managed compute (serverless) |
| **Mistral** | Mistral Large, Mistral Small | Managed compute (serverless) |
| **Cohere** | Command R, Command R+ | Managed compute (serverless) |

### Deploying a Model from the Catalog

```python
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

# Connect to the project
ml_client = MLClient(
    credential=DefaultAzureCredential(),
    subscription_id="<sub-id>",
    resource_group_name="rg-ai",
    workspace_name="chatbot-project"
)

# Deploy a serverless model
from azure.ai.ml.entities import ServerlessEndpoint, ServerlessEndpointProperties

endpoint = ServerlessEndpoint(
    name="gpt4o-endpoint",
    model_id="azureml://registries/azure-openai/models/gpt-4o/versions/1"
)

ml_client.serverless_endpoints.begin_create_or_update(endpoint)
```

---

## Prompt Flow

Prompt flow is a visual tool for building, testing, and deploying LLM-powered workflows.

### Core Concepts

| Concept | Description |
|---------|-------------|
| **Flow** | A DAG (directed acyclic graph) of connected nodes |
| **Node** | A single step (LLM call, Python code, prompt, tool) |
| **Connection** | External service reference (OpenAI, AI Search, etc.) |
| **Variant** | Alternative versions of a node for A/B testing |
| **Run** | An execution of a flow with specific inputs |

### Flow Types

| Type | Use Case |
|------|----------|
| **Standard flow** | General-purpose LLM pipelines |
| **Chat flow** | Conversational scenarios with history |
| **Evaluation flow** | Assess quality of other flows' outputs |

### Building a Prompt Flow (YAML)

```yaml
# flow.dag.yaml
inputs:
  question:
    type: string
    default: "What is Azure AI?"

outputs:
  answer:
    type: string
    reference: ${generate_answer.output}

nodes:
  - name: retrieve_context
    type: python
    source:
      type: code
      path: retrieve.py
    inputs:
      question: ${inputs.question}

  - name: generate_answer
    type: llm
    source:
      type: code
      path: answer_prompt.jinja2
    inputs:
      deployment_name: gpt-4o
      context: ${retrieve_context.output}
      question: ${inputs.question}
    connection: my-openai-connection
    api: chat
```

### Prompt Template (Jinja2)

```jinja2
{# answer_prompt.jinja2 #}
system:
You are a helpful assistant. Answer the question using only the provided context.
If the answer is not in the context, say "I don't have that information."

user:
Context:
{{context}}

Question: {{question}}
```

### Running a Prompt Flow (SDK)

```python
from promptflow.client import PFClient

pf = PFClient()

# Test a flow locally
result = pf.test(
    flow="./my-flow",
    inputs={"question": "What services does Azure AI offer?"}
)
print(result["answer"])

# Run a batch evaluation
run = pf.run(
    flow="./my-flow",
    data="./test-data.jsonl",
    column_mapping={
        "question": "${data.question}"
    }
)
```

> ### 📝 Exam Tip
> Understand the three flow types: **Standard** (general pipelines), **Chat** (conversational with history), **Evaluation** (quality assessment). The exam may ask which type to use for a specific scenario.

---

## RAG Pattern (Retrieval-Augmented Generation)

RAG is the **most important pattern** for enterprise generative AI. It grounds model responses in your organization's data.

### RAG Pipeline Steps

```
1. SEARCH     → User query hits Azure AI Search index
2. RETRIEVE   → Top-k relevant documents/chunks returned
3. AUGMENT    → Retrieved context injected into prompt
4. GENERATE   → LLM generates response grounded in context
```

### Detailed RAG Architecture

```
User Question
     │
     ▼
┌─────────────┐    ┌──────────────────┐
│  Embedding  │───▶│  Azure AI Search │
│  Model      │    │  (Vector Index)  │
└─────────────┘    └────────┬─────────┘
                            │ Top-k results
                            ▼
                   ┌──────────────────┐
                   │  Prompt Assembly  │
                   │  System + Context │
                   │  + User Question  │
                   └────────┬─────────┘
                            │
                            ▼
                   ┌──────────────────┐
                   │   Azure OpenAI   │
                   │   (GPT-4o)       │
                   └────────┬─────────┘
                            │
                            ▼
                     Grounded Answer
```

### RAG Implementation

```python
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from openai import AzureOpenAI

# Step 1 & 2: Search and Retrieve
search_client = SearchClient(
    endpoint="https://my-search.search.windows.net",
    index_name="knowledge-base",
    credential=AzureKeyCredential("<search-key>")
)

# Hybrid search (keyword + vector)
results = search_client.search(
    search_text=user_question,
    vector_queries=[{
        "kind": "text",
        "text": user_question,
        "fields": "content_vector",
        "k_nearest_neighbors": 5
    }],
    top=5,
    select=["content", "title", "source"]
)

# Step 3: Augment — Build context from search results
context = "\n\n".join([
    f"[Source: {doc['title']}]\n{doc['content']}"
    for doc in results
])

# Step 4: Generate — Send to LLM with context
openai_client = AzureOpenAI(
    azure_endpoint="https://my-openai.openai.azure.com/",
    api_key="<key>",
    api_version="2024-02-01"
)

response = openai_client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "system",
            "content": f"""Answer questions using only the provided context.
            If the answer is not in the context, say so.

            Context:
            {context}"""
        },
        {"role": "user", "content": user_question}
    ],
    temperature=0.3  # Lower temperature for factual responses
)

print(response.choices[0].message.content)
```

### Azure OpenAI "On Your Data" (Simplified RAG)

Azure OpenAI provides a built-in RAG feature that eliminates manual orchestration:

```python
response = openai_client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "What is our refund policy?"}],
    extra_body={
        "data_sources": [{
            "type": "azure_search",
            "parameters": {
                "endpoint": "https://my-search.search.windows.net",
                "index_name": "company-docs",
                "authentication": {
                    "type": "api_key",
                    "key": "<search-key>"
                }
            }
        }]
    }
)
```

> ### 📝 Exam Tip
> Know both RAG approaches: **manual orchestration** (you write the search + prompt assembly code) and **Azure OpenAI "On Your Data"** (built-in, requires `data_sources` in the API call). The exam tests both.

---

## Model Evaluation Metrics

### Key Metrics

| Metric | What It Measures | Scale | Good Score |
|--------|-----------------|-------|------------|
| **Groundedness** | Is the answer supported by the provided context? | 1–5 | ≥ 4 |
| **Relevance** | Does the answer address the question asked? | 1–5 | ≥ 4 |
| **Coherence** | Is the answer well-structured and readable? | 1–5 | ≥ 4 |
| **Fluency** | Is the language natural and grammatically correct? | 1–5 | ≥ 4 |
| **Similarity** | How close is the answer to a ground-truth reference? | 1–5 | ≥ 3 |

### Running Evaluations

```python
from promptflow.evals.evaluators import (
    GroundednessEvaluator,
    RelevanceEvaluator,
    CoherenceEvaluator
)

# Initialize evaluators with a model deployment
groundedness_eval = GroundednessEvaluator(model_config={
    "azure_endpoint": "https://my-openai.openai.azure.com/",
    "api_key": "<key>",
    "azure_deployment": "gpt-4o"
})

# Evaluate a single response
result = groundedness_eval(
    question="What is our return policy?",
    answer="You can return items within 30 days.",
    context="Our return policy allows returns within 30 days of purchase."
)
print(f"Groundedness score: {result['groundedness']}")
# Output: Groundedness score: 5
```

### Batch Evaluation in Foundry

```python
from promptflow.evals import evaluate

eval_result = evaluate(
    data="./test-dataset.jsonl",
    evaluators={
        "groundedness": groundedness_eval,
        "relevance": relevance_eval,
        "coherence": coherence_eval
    },
    evaluator_config={
        "groundedness": {
            "question": "${data.question}",
            "answer": "${target.answer}",
            "context": "${target.context}"
        }
    }
)

# View aggregate results
print(eval_result.metrics)
# {'groundedness.groundedness': 4.2, 'relevance.relevance': 4.5, ...}
```

---

## Foundry SDK Integration

### Prompt Templates

```python
from promptflow.core import Prompty

# Load and render a prompt template
prompty = Prompty.load("chat.prompty")
result = prompty(
    question="What is Azure?",
    context="Azure is Microsoft's cloud computing platform."
)
```

### `.prompty` File Format

```yaml
---
name: Chat Assistant
description: A helpful chat assistant with RAG
model:
  api: chat
  configuration:
    azure_deployment: gpt-4o
  parameters:
    temperature: 0.3
    max_tokens: 800
inputs:
  question:
    type: string
  context:
    type: string
---
system:
You are a helpful assistant. Use the context to answer questions.

Context: {{context}}

user:
{{question}}
```

---

## Key Takeaways

1. **Foundry Hub** = shared infrastructure (connections, compute, policies); **Project** = application workspace (models, flows, endpoints).
2. **Model catalog** provides models from OpenAI, Microsoft, Meta, Mistral, and Cohere — deployed as serverless endpoints.
3. **Prompt flow** builds LLM pipelines as DAGs with three types: Standard, Chat, and Evaluation.
4. **RAG pattern**: Search → Retrieve → Augment → Generate. Can be implemented manually or via Azure OpenAI "On Your Data."
5. **Evaluation metrics**: Groundedness (factual accuracy), Relevance (addresses the question), Coherence (readability), scored 1–5.
6. `.prompty` files define reusable prompt templates with model configuration.

---

## Further Reading

- [Microsoft Foundry documentation](https://learn.microsoft.com/en-us/azure/ai-studio/)
- [Prompt flow documentation](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/prompt-flow)
- [RAG with Azure AI](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview)
- [Evaluation metrics](https://learn.microsoft.com/en-us/azure/ai-studio/concepts/evaluation-metrics-built-in)
