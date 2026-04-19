# AI-102 Azure AI Engineer Associate — 102 Practice Questions

> Comprehensive scenario-based practice questions aligned to the current AI-102 exam objectives. Each question has 4 options with a single best answer, collapsible explanation, and exam-objective mapping.

## How to use

1. Work through a module in order. Cover the answer first.
2. Click **▶ Answer** to reveal the correct option, rationale, and exam objective.
3. Questions marked with 💻 contain code, REST, SSML, KQL, or JSON snippets.
4. Revisit any question you missed; use the linked exam objective to target study.

## Distribution

| Module | Questions | Focus |
|---|---|---|
| 1. Plan & Manage an Azure AI Solution | Q1–Q22 | Resources, security, identity, containers, monitoring, responsible AI |
| 2. Generative AI Solutions (Azure OpenAI) | Q23–Q40 | Deployments, prompts, parameters, RAG, safety, fine-tuning |
| 3. Agentic Solutions | Q41–Q48 | Azure AI Foundry Agents, tools, orchestration |
| 4. Computer Vision Solutions | Q49–Q61 | Image analysis, Custom Vision, Face, Video Indexer |
| 5. Natural Language Processing | Q62–Q79 | Language service, CLU, custom text classification, Speech, Translator |
| 6. Knowledge Mining & Document Intelligence | Q80–Q97 | Azure AI Search, skillsets, Document Intelligence prebuilt & custom |
| 7. Cross-Domain Scenarios | Q98–Q102 | End-to-end architecture |

---

## Module 1 — Plan & Manage an Azure AI Solution (Q1–Q22)

### Question 1
You are creating a new Azure AI multi-service resource that must be used by developers through both **Azure AI Language** and **Azure AI Vision** SDKs. Corporate policy forbids storing account keys in application code or config files. Which authentication mechanism should you configure for the deployed App Service that calls the resource?

A. Shared access signature (SAS) token generated per request
B. Account key stored in Azure Key Vault and retrieved at startup
C. Microsoft Entra ID authentication using the App Service's system-assigned managed identity
D. Azure AD B2C user flow with OAuth 2.0 authorization code grant

<details><summary>▶ Answer</summary>

**Correct: C.** Managed identities eliminate stored credentials entirely; the App Service requests an Entra ID token and calls the Azure AI resource with the `Cognitive Services User` (or more specific) RBAC role. Option B still stores a secret (even if wrapped), violating the intent. SAS is not supported for Cognitive Services data-plane calls. B2C is for end-user auth, not service-to-service.

**Exam Objective:** Plan and manage an Azure AI solution → Manage security for Azure AI services (managed identity & Entra ID auth).
</details>

### Question 2
Your organization requires that an Azure AI Language container run **fully disconnected** from the public internet for 30 days to process sensitive medical text on-premises. Which two requirements must be met? (Choose the single best combined answer.)

A. Standard (S0) tier + billing endpoint reachable every 24 hours
B. A commitment tier plan + a disconnected container configuration downloaded from the Azure portal
C. Free (F0) tier + anonymous endpoint exposure on port 5000
D. Consumption tier + Azure Arc-enabled Kubernetes

<details><summary>▶ Answer</summary>

**Correct: B.** Disconnected containers require a **commitment tier** purchase and a signed configuration file that authorizes offline usage for the committed period. F0 and consumption plans do not support disconnected mode; standard connected containers must reach the billing endpoint periodically.

**Exam Objective:** Plan and manage an Azure AI solution → Deploy Azure AI services in containers (disconnected containers).
</details>

### Question 3 💻
You deploy the **Azure AI Language sentiment** container to an on-prem Docker host. Which **two** environment variables must you pass to `docker run` for the container to start in connected billing mode?

```bash
docker run --rm -it -p 5000:5000 --memory 8g --cpus 2 \
  mcr.microsoft.com/azure-cognitive-services/textanalytics/sentiment:latest \
  Eula=accept \
  ______=<value> \
  ______=<value>
```

A. `ApiKey` and `Endpoint`
B. `Billing` and `ApiKey`
C. `Region` and `SubscriptionId`
D. `TenantId` and `ClientSecret`

<details><summary>▶ Answer</summary>

**Correct: B.** Every connected Cognitive Services container requires `Eula=accept`, `Billing=<endpoint>`, and `ApiKey=<key>` — the endpoint URL and API key of the Azure resource that is billed for usage. `Region`/`SubscriptionId` are not container environment variables.

**Exam Objective:** Plan and manage an Azure AI solution → Deploy Azure AI services in containers.
</details>

### Question 4
A developer calls the Azure AI Language REST endpoint and receives **HTTP 429 Too Many Requests**. Which mitigation should be applied **first** before increasing the pricing tier?

A. Switch the key to the secondary key
B. Implement exponential backoff with jitter in the client
C. Create a second resource in another region and round-robin requests
D. Enable the diagnostic setting `AuditLogs` in Azure Monitor

<details><summary>▶ Answer</summary>

**Correct: B.** Transient 429 responses are expected under burst load; the documented and cheapest mitigation is client-side exponential backoff with jitter. Secondary keys do not increase throughput. Multi-region round-robin adds cost and complexity and should come later. Diagnostic logging is observability, not throttling mitigation.

**Exam Objective:** Plan and manage an Azure AI solution → Monitor Azure AI services.
</details>

### Question 5 💻
You must monitor the **latency p95** and **errors per minute** for an Azure AI Vision resource. Which Kusto query against the `AzureDiagnostics` table gives you both?

```kql
AzureDiagnostics
| where ResourceType == "ACCOUNTS" and Category == "RequestResponse"
| summarize p95_ms = percentile(DurationMs, 95),
            errors = countif(ResultSignature startswith "4" or ResultSignature startswith "5")
            by bin(TimeGenerated, 1m)
```

A. The query is correct as written
B. Replace `DurationMs` with `durationMs_d` and `ResultSignature` with `httpStatusCode_d`
C. Use the `AppRequests` table instead because Cognitive Services logs to Application Insights
D. The query will fail because `AzureDiagnostics` does not support `percentile()`

<details><summary>▶ Answer</summary>

**Correct: B.** In the `AzureDiagnostics` table, numeric columns from resource-specific diagnostics arrive with the `_d` suffix and the HTTP status field is `httpStatusCode_d`. `percentile()` is fully supported. Cognitive Services resource logs land in `AzureDiagnostics` (or a resource-specific table), not `AppRequests`.

**Exam Objective:** Plan and manage an Azure AI solution → Monitor Azure AI services (diagnostic logs & KQL).
</details>

### Question 6
Which RBAC role grants the **least privilege** required for an application to call the **data plane** of Azure AI services (e.g., analyze text) while preventing it from reading or regenerating keys?

A. Cognitive Services Contributor
B. Cognitive Services User
C. Cognitive Services Data Reader (Preview)
D. Reader

<details><summary>▶ Answer</summary>

**Correct: B.** `Cognitive Services User` allows listing keys and calling data-plane APIs but not resource management. `Contributor` is excessive; `Reader` cannot list keys and cannot perform data operations; `Data Reader` is search-indexer specific. For identity-based auth (managed identity + Entra), `Cognitive Services User` is the recommended role.

**Exam Objective:** Plan and manage an Azure AI solution → Manage security (RBAC for Azure AI services).
</details>

### Question 7
You must restrict access to an Azure AI Search resource so that **only** an Azure Function in the same VNet can call it, while the public internet is blocked. Which two features should you combine? (Best combined answer.)

A. IP firewall rule allowing `0.0.0.0/0` + SAS token
B. Private endpoint for Search + disable public network access
C. Service endpoint + allow trusted Microsoft services
D. Azure Front Door with WAF + customer-managed key

<details><summary>▶ Answer</summary>

**Correct: B.** A **private endpoint** places Search on your VNet; disabling public network access blocks everything else. Service endpoints do not work across regions and Search recommends private endpoints. Front Door/WAF does not satisfy the "only VNet" requirement.

**Exam Objective:** Plan and manage an Azure AI solution → Implement network security (private endpoints).
</details>

### Question 8
A Responsible AI assessment for your chatbot requires you to document **limitations and intended uses**. Which artifact should you produce?

A. System prompt
B. Transparency Note
C. Service Level Agreement
D. Data retention schedule

<details><summary>▶ Answer</summary>

**Correct: B.** Microsoft publishes a **Transparency Note** template that describes intended use, capabilities, limitations, and considerations. It is the canonical deliverable of the Responsible AI Impact Assessment.

**Exam Objective:** Plan and manage an Azure AI solution → Apply responsible AI principles.
</details>

### Question 9
Which of the following Azure AI services are offered as a **single multi-service resource** that shares one key and endpoint? (Choose the best answer.)

A. Azure AI Foundry project only
B. Azure AI services (multi-service) including Language, Vision, Speech, Translator, and Content Safety
C. Azure OpenAI + Azure AI Search only
D. Each service must be provisioned individually; no multi-service resource exists

<details><summary>▶ Answer</summary>

**Correct: B.** The **Azure AI services** resource (formerly Cognitive Services multi-service) exposes Language, Vision, Speech, Translator, Document Intelligence, and Content Safety behind one key/endpoint and single bill. Azure OpenAI is a separate resource.

**Exam Objective:** Plan and manage an Azure AI solution → Select and provision Azure AI services.
</details>

### Question 10
You need to estimate **token usage costs** for an Azure OpenAI GPT-4o deployment. Which two metrics in Azure Monitor are most relevant?

A. `Processed Prompt Tokens` and `Generated Completion Tokens`
B. `TotalCalls` and `SuccessfulCalls`
C. `DataIn` and `DataOut`
D. `CPU Percentage` and `Memory Working Set`

<details><summary>▶ Answer</summary>

**Correct: A.** Azure OpenAI emits dedicated metrics for prompt tokens consumed and completion tokens generated. Billing is token-based, so these are the cost-relevant signals.

**Exam Objective:** Plan and manage an Azure AI solution → Monitor Azure AI services (cost & usage).
</details>

### Question 11
Which capability of Azure AI Foundry lets you **centrally manage** projects, hubs, connections, and shared compute for multiple AI workloads?

A. Azure Resource Manager deployment stacks
B. Azure AI Foundry **hub** with **projects** as children
C. Azure Purview accounts
D. Azure Machine Learning classic workspaces only

<details><summary>▶ Answer</summary>

**Correct: B.** An Azure AI Foundry **hub** is the top-level collaboration resource that owns shared resources (storage, Key Vault, connections, compute); **projects** scope individual solutions. This is the recommended organizing model for enterprise AI teams.

**Exam Objective:** Plan and manage an Azure AI solution → Plan, create, and deploy Azure AI services (Foundry hubs & projects).
</details>

### Question 12
You want incoming requests to an Azure AI resource to be encrypted **at rest** with a key you control and can rotate. Which setting should you enable?

A. Transparent data encryption with a service-managed key
B. Customer-managed keys (CMK) stored in Azure Key Vault
C. Always Encrypted with secure enclaves
D. Client-side AES-256 encryption before calling the API

<details><summary>▶ Answer</summary>

**Correct: B.** Azure AI services support **customer-managed keys** stored in Azure Key Vault (or Managed HSM) for encryption at rest. This allows you to rotate and revoke keys. Always Encrypted and TDE are SQL features.

**Exam Objective:** Plan and manage an Azure AI solution → Manage security (encryption with CMK).
</details>

### Question 13
A team wants to expose their Azure AI Language custom classification model through a **load-balanced, regional, private** endpoint across two regions. What should they use?

A. Azure Traffic Manager with performance routing
B. Azure Front Door premium with Private Link origins
C. Azure Application Gateway in each region only
D. A single public endpoint with geo-DNS

<details><summary>▶ Answer</summary>

**Correct: B.** **Azure Front Door Premium** supports Private Link origins and global load balancing while keeping backends private. Traffic Manager is DNS-only (not private), App Gateway is regional.

**Exam Objective:** Plan and manage an Azure AI solution → Implement network security and global availability.
</details>

### Question 14
Which limit should you plan for when ingesting **multiple large PDFs** into Azure AI Document Intelligence prebuilt models?

A. Each file must be ≤ **500 MB** and ≤ 2,000 pages (Standard tier)
B. Each file must be ≤ **4 MB** for all tiers
C. Each file must be ≤ **50 MB** for Free tier only
D. No file size limit applies

<details><summary>▶ Answer</summary>

**Correct: A.** Azure AI Document Intelligence Standard tier accepts up to **500 MB** (4 MB on Free tier) and up to 2,000 pages per document. Knowing the 500 MB / 2,000 page limit is a common exam item.

**Exam Objective:** Plan and manage an Azure AI solution → Understand service limits and quotas.
</details>

### Question 15
Which header is required when calling **Azure OpenAI** REST APIs with **Entra ID** authentication (instead of an API key)?

A. `Ocp-Apim-Subscription-Key: <key>`
B. `api-key: <key>`
C. `Authorization: Bearer <access_token>`
D. `x-ms-client-request-id: <guid>`

<details><summary>▶ Answer</summary>

**Correct: C.** When using Entra ID (e.g., managed identity acquiring a token for `https://cognitiveservices.azure.com/.default`), requests include `Authorization: Bearer <token>`. `api-key` is for key-based auth.

**Exam Objective:** Plan and manage an Azure AI solution → Manage security (Entra ID authentication for Azure OpenAI).
</details>

### Question 16
Which **two** Content Safety severity levels indicate content that you should typically **block by default** for enterprise chatbots?

A. Severity 0 and Severity 2
B. Severity 2 and Severity 4
C. Severity 4 and Severity 6
D. Severity 0 and Severity 6

<details><summary>▶ Answer</summary>

**Correct: C.** Azure AI Content Safety uses severity levels **0, 2, 4, 6** per category. Levels **4 (high)** and **6 (very high)** represent clearly harmful content that most enterprise policies block. Level 2 is often reviewed; level 0 is safe.

**Exam Objective:** Plan and manage an Azure AI solution → Apply responsible AI (Content Safety severity levels).
</details>

### Question 17
You configure **Azure AI Content Safety** with severity threshold of **2** for the `Hate` category. A message scored **Severity 4 / Hate** is submitted. What will the service return?

A. `action: "Accept"` because 4 > 2
B. A blocked/flagged response because 4 ≥ threshold 2
C. HTTP 500 because thresholds above 0 are unsupported
D. It depends on the `Sexual` category score

<details><summary>▶ Answer</summary>

**Correct: B.** If you configure threshold=2, any score **≥2** is flagged. Severity 4 exceeds 2 and is flagged/blocked depending on how your app handles the response.

**Exam Objective:** Plan and manage an Azure AI solution → Apply responsible AI (Content Safety thresholds).
</details>

### Question 18
An Azure OpenAI resource is showing high **latency** only for a specific deployment. Which diagnostic should you check **first**?

A. The deployment's **utilization** (capacity in PTUs or TPM) vs. its quota
B. The storage account's blob throughput
C. Key Vault secret rotation history
D. The VNet's NSG flow logs

<details><summary>▶ Answer</summary>

**Correct: A.** High latency and 429s on Azure OpenAI are usually caused by exceeding the deployment's **tokens-per-minute (TPM)** or PTU capacity. Check the `Azure OpenAI Usage` and `Provisioned Utilization` metrics first.

**Exam Objective:** Plan and manage an Azure AI solution → Monitor Azure AI services (capacity & quotas).
</details>

### Question 19
Which option correctly describes **regional availability** concerns when selecting an Azure AI services region?

A. All models of all Azure AI services are available in every region
B. Feature and model availability (e.g., specific Azure OpenAI models) varies by region and must be verified
C. Region selection affects only latency, never feature availability
D. Azure AI services are global and have no region concept

<details><summary>▶ Answer</summary>

**Correct: B.** Models and features (especially Azure OpenAI model SKUs like GPT-4o, o1, fine-tuning, and container support) vary by region. Always verify the region's availability list before deployment.

**Exam Objective:** Plan and manage an Azure AI solution → Select and provision Azure AI services.
</details>

### Question 20
You need to migrate a workload off a deprecated **Language Understanding (LUIS)** app. Which service is the recommended successor?

A. QnA Maker
B. Conversational Language Understanding (CLU) in Azure AI Language
C. Azure Bot Service Composer intents only
D. Azure OpenAI function calling exclusively

<details><summary>▶ Answer</summary>

**Correct: B.** LUIS is retired; **Conversational Language Understanding (CLU)** in Azure AI Language is the successor with a direct migration path.

**Exam Objective:** Plan and manage an Azure AI solution → Plan migrations from retired services.
</details>

### Question 21
Which statement about **Azure AI services keys** is correct?

A. Keys cannot be rotated once created
B. Each resource has two keys (key1, key2) to enable zero-downtime rotation
C. Keys are valid for 24 hours and must be renewed daily
D. Keys are stored in plain text in resource group tags

<details><summary>▶ Answer</summary>

**Correct: B.** Two keys let you switch clients to the secondary key, then regenerate the primary, then switch back — achieving rotation without downtime.

**Exam Objective:** Plan and manage an Azure AI solution → Manage security (key management).
</details>

### Question 22
Which tool in the Azure portal lets you **test Azure AI service endpoints** interactively with sample payloads and shows the raw request/response?

A. Azure Cloud Shell only
B. Azure AI Foundry playground / portal try-it
C. Azure Monitor Workbooks
D. Azure Resource Graph Explorer

<details><summary>▶ Answer</summary>

**Correct: B.** The **Foundry portal / playground** (and individual service "Try it" panes) provide interactive consoles with auto-generated request URLs, headers, and payloads for rapid testing.

**Exam Objective:** Plan and manage an Azure AI solution → Test and validate Azure AI services.
</details>

---

## Module 2 — Generative AI Solutions (Q23–Q40)

### Question 23
Which Azure OpenAI **parameter** most directly controls the **randomness/creativity** of completions?

A. `temperature`
B. `max_tokens`
C. `presence_penalty`
D. `stop`

<details><summary>▶ Answer</summary>

**Correct: A.** `temperature` (0–2) scales the softmax; lower = more deterministic, higher = more creative. `top_p` is an alternative (nucleus sampling) — use one, not both.

**Exam Objective:** Generative AI → Configure Azure OpenAI parameters.
</details>

### Question 24
Which parameter would you tune to **reduce repetition** of the same tokens in a long response?

A. `temperature`
B. `frequency_penalty`
C. `n`
D. `logit_bias`

<details><summary>▶ Answer</summary>

**Correct: B.** `frequency_penalty` (−2 to 2) penalizes tokens that have already appeared proportional to frequency, reducing verbatim repetition. `presence_penalty` penalizes any token that has appeared at least once (encourages new topics).

**Exam Objective:** Generative AI → Configure Azure OpenAI parameters.
</details>

### Question 25
What is the maximum **total tokens** you can use (prompt + completion) in a single call — called the **context window**?

A. Always 4,096 tokens for every model
B. A property of the model; e.g., GPT-4o has a 128K context window
C. Always 32,768 tokens
D. Determined by the deployment name, not the model

<details><summary>▶ Answer</summary>

**Correct: B.** Context window is per model. GPT-3.5-Turbo supports 4K/16K; GPT-4 Turbo and GPT-4o support **128K**; GPT-4.1 supports 1M. Always check model docs.

**Exam Objective:** Generative AI → Understand tokens and context windows.
</details>

### Question 26 💻
You call the Azure OpenAI Chat Completions API with:

```json
{
  "messages": [
    {"role": "system", "content": "You are a concise assistant."},
    {"role": "user", "content": "Summarize the meeting notes."}
  ],
  "temperature": 0.2,
  "max_tokens": 400
}
```

The response is truncated mid-sentence. What is the most likely cause?

A. `temperature` is too low
B. `max_tokens` is too small for the desired output
C. Missing `top_p` parameter
D. Missing `stop` sequence

<details><summary>▶ Answer</summary>

**Correct: B.** `max_tokens` caps completion tokens. When `finish_reason` is `"length"`, the response was cut off — raise `max_tokens` (while staying within the model's context window minus prompt).

**Exam Objective:** Generative AI → Configure Azure OpenAI parameters (max_tokens, finish_reason).
</details>

### Question 27
Which pattern grounds an LLM with **proprietary, frequently changing** enterprise data without fine-tuning?

A. Few-shot prompting only
B. Retrieval-Augmented Generation (RAG) with a vector index
C. Function calling only
D. Continued pre-training

<details><summary>▶ Answer</summary>

**Correct: B.** **RAG** retrieves relevant chunks from a vector/hybrid index at query time and passes them as context. It scales to changing data, avoids retraining, and reduces hallucinations.

**Exam Objective:** Generative AI → Implement RAG with Azure OpenAI and Azure AI Search.
</details>

### Question 28
In an Azure OpenAI **"On Your Data"** RAG deployment, which Azure service most commonly hosts the **retrieval index**?

A. Azure SQL Database
B. Azure AI Search (with vector and semantic ranking)
C. Azure Cosmos DB for Apache Cassandra
D. Azure Table Storage

<details><summary>▶ Answer</summary>

**Correct: B.** **Azure AI Search** is the first-party retrieval store for Azure OpenAI "On Your Data", supporting vector, keyword, hybrid, and semantic ranking.

**Exam Objective:** Generative AI → Implement RAG (data sources for Azure OpenAI On Your Data).
</details>

### Question 29
You want responses grounded in three specific PDF reports. Which chunking guidance is correct?

A. One chunk per PDF regardless of size
B. Chunks of ~300–1,000 tokens with overlap (e.g., 10–20%) to preserve context
C. Chunks of exactly 1 token
D. Only chunk by page number, ignoring token count

<details><summary>▶ Answer</summary>

**Correct: B.** Typical guidance: 300–1,000 tokens per chunk with small overlap so sentences aren't cut across retrieval boundaries. Whole-document chunks overflow embeddings; per-token is useless.

**Exam Objective:** Generative AI → Implement RAG (chunking strategy).
</details>

### Question 30 💻
Which Python snippet correctly calls an Azure OpenAI chat deployment using the `openai` v1 SDK with Entra ID?

```python
from openai import AzureOpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

token_provider = get_bearer_token_provider(
    DefaultAzureCredential(),
    "https://cognitiveservices.azure.com/.default",
)
client = AzureOpenAI(
    azure_endpoint="https://my-aoai.openai.azure.com/",
    api_version="2024-10-21",
    azure_ad_token_provider=token_provider,
)
resp = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello"}],
)
```

A. Correct
B. Wrong — `model` must be the base model name, not the deployment name
C. Wrong — Entra ID is unsupported for Azure OpenAI
D. Wrong — `api_version` is not a valid parameter

<details><summary>▶ Answer</summary>

**Correct: A.** For Azure OpenAI with the `openai` v1 SDK, `model` is set to the **deployment name**, `api_version` is required, and `azure_ad_token_provider` enables Entra ID auth. This is the recommended passwordless pattern.

**Exam Objective:** Generative AI → Integrate Azure OpenAI (Python SDK with Entra ID).
</details>

### Question 31
Which Azure OpenAI **deployment type** offers **guaranteed, reserved throughput** with predictable latency at a fixed cost?

A. Standard (pay-as-you-go)
B. Provisioned Throughput Units (PTUs)
C. Global Standard only
D. Free (F0)

<details><summary>▶ Answer</summary>

**Correct: B.** **PTUs** (or Provisioned-Managed) reserve capacity; Standard uses shared pools and is TPM-limited per region. Global Standard is still pay-as-you-go.

**Exam Objective:** Generative AI → Deploy Azure OpenAI models (deployment types).
</details>

### Question 32
To **moderate prompts and completions** for a chatbot, which Azure service should you integrate?

A. Azure AI Content Safety (Text moderation, Prompt Shields, Protected Material)
B. Azure Purview only
C. Azure Firewall with TLS inspection
D. Azure Information Protection labels

<details><summary>▶ Answer</summary>

**Correct: A.** **Azure AI Content Safety** provides text/image moderation with severity levels, **Prompt Shields** (for jailbreak/indirect prompt injection), and **Protected Material** detection for generative scenarios.

**Exam Objective:** Generative AI → Implement responsible AI (Content Safety for generative AI).
</details>

### Question 33
Which Content Safety feature specifically detects attempts to **jailbreak** or inject instructions via user/document inputs?

A. Protected Material detection
B. Prompt Shields (direct and indirect attack detection)
C. Groundedness detection
D. Image moderation

<details><summary>▶ Answer</summary>

**Correct: B.** **Prompt Shields** covers direct jailbreak attempts and indirect prompt injection from retrieved documents. Groundedness detects unsupported claims; Protected Material detects copyrighted text/code.

**Exam Objective:** Generative AI → Implement responsible AI (Prompt Shields).
</details>

### Question 34
Which technique **fine-tunes** a base model with your labeled prompt/completion pairs?

A. Retrieval-Augmented Generation
B. Supervised fine-tuning on Azure OpenAI (e.g., `babbage-002`, `gpt-4o-mini` where supported)
C. Function calling
D. Prompt flow

<details><summary>▶ Answer</summary>

**Correct: B.** Fine-tuning in Azure OpenAI accepts JSONL training data and produces a custom model. Availability depends on base model and region.

**Exam Objective:** Generative AI → Fine-tune Azure OpenAI models.
</details>

### Question 35 💻
A developer wants the model to call a custom backend when the user asks about order status. Which Azure OpenAI feature should be used?

```python
tools = [{
  "type": "function",
  "function": {
    "name": "get_order_status",
    "description": "Look up order status by order ID",
    "parameters": {
      "type": "object",
      "properties": {"order_id": {"type": "string"}},
      "required": ["order_id"]
    }
  }
}]
```

A. Function/tool calling
B. Fine-tuning
C. Logprobs
D. Embeddings only

<details><summary>▶ Answer</summary>

**Correct: A.** **Tool (function) calling** lets the model emit structured `tool_calls` that your code executes and feeds back as a tool message. This is the canonical pattern for LLM-to-backend integration.

**Exam Objective:** Generative AI → Implement tool/function calling with Azure OpenAI.
</details>

### Question 36
For semantic search over product descriptions, which Azure OpenAI **model family** should you use to generate the vectors?

A. `gpt-4o` chat models
B. `text-embedding-3-large` or `text-embedding-ada-002`
C. `dall-e-3`
D. `whisper-1`

<details><summary>▶ Answer</summary>

**Correct: B.** Embedding models produce fixed-length vectors (1536 for `ada-002`, up to 3072 for `text-embedding-3-large`) optimized for similarity search. Chat models do not output embeddings directly.

**Exam Objective:** Generative AI → Select Azure OpenAI models (embeddings).
</details>

### Question 37
Which parameter pair should you **avoid setting simultaneously** because they both control sampling diversity?

A. `temperature` and `top_p`
B. `max_tokens` and `stop`
C. `n` and `stream`
D. `frequency_penalty` and `presence_penalty`

<details><summary>▶ Answer</summary>

**Correct: A.** Docs recommend tuning **either** `temperature` **or** `top_p`, not both; combining them leads to unpredictable sampling.

**Exam Objective:** Generative AI → Configure Azure OpenAI parameters.
</details>

### Question 38
What is the **purpose of a system message** in a chat completion request?

A. It authenticates the user
B. It sets the assistant's persona, rules, style, and constraints for the entire conversation
C. It defines the model deployment name
D. It is required for streaming responses

<details><summary>▶ Answer</summary>

**Correct: B.** The `system` role message provides persistent instructions that shape assistant behavior across the conversation.

**Exam Objective:** Generative AI → Design effective prompts (system messages).
</details>

### Question 39
For a RAG chatbot that must cite sources, which design is **best**?

A. Concatenate all documents into the prompt
B. Retrieve top-k chunks, include them in the context with their IDs/URIs, and instruct the model to cite them
C. Fine-tune on documents to avoid citations
D. Use temperature=2 for creativity

<details><summary>▶ Answer</summary>

**Correct: B.** Citations require that retrieval metadata be included in the prompt and the system message instructs the model to attribute claims to those IDs. This mirrors the pattern used by Azure OpenAI On Your Data.

**Exam Objective:** Generative AI → Implement RAG (citations & grounding).
</details>

### Question 40
Which Azure OpenAI safety feature estimates whether the model's answer is **supported by the provided grounding documents**?

A. Prompt Shields
B. Groundedness detection (Content Safety)
C. Protected Material detection
D. Logit bias

<details><summary>▶ Answer</summary>

**Correct: B.** **Groundedness detection** (Azure AI Content Safety for Generative AI) compares the response to source documents and flags unsupported (hallucinated) claims.

**Exam Objective:** Generative AI → Implement responsible AI (groundedness).
</details>

---

## Module 3 — Agentic Solutions (Q41–Q48)

### Question 41
Which Azure service provides a **managed runtime for AI agents** with tools, threads, and orchestration, built on top of Azure OpenAI?

A. Azure Functions Durable Entities
B. Azure AI Foundry **Agent Service**
C. Azure Logic Apps Standard
D. Azure Automation runbooks

<details><summary>▶ Answer</summary>

**Correct: B.** The **Azure AI Foundry Agent Service** (successor to the Assistants API) provides managed threads, messages, tools (code interpreter, file search, functions, OpenAPI), and runs.

**Exam Objective:** Agentic solutions → Build agents with Azure AI Foundry Agent Service.
</details>

### Question 42
Which **built-in tool** would you enable so an agent can execute Python to analyze uploaded CSVs?

A. Code Interpreter
B. Bing Grounding
C. File Search
D. OpenAPI tool

<details><summary>▶ Answer</summary>

**Correct: A.** **Code Interpreter** provides a sandboxed Python runtime for data analysis, chart generation, and file manipulation.

**Exam Objective:** Agentic solutions → Configure agent tools.
</details>

### Question 43
Which built-in tool enables an agent to **retrieve grounded answers** from uploaded documents using vector search?

A. Code Interpreter
B. File Search (built-in vector store)
C. Function calling
D. Image generation

<details><summary>▶ Answer</summary>

**Correct: B.** **File Search** ingests files into a managed vector store and retrieves relevant chunks at run time, providing RAG without bringing your own index.

**Exam Objective:** Agentic solutions → Configure agent tools (file search).
</details>

### Question 44
To let an agent call **your own REST API** defined by a schema, which tool type do you register?

A. OpenAPI-specified tool
B. Bing grounding
C. Code interpreter
D. DALL-E image tool

<details><summary>▶ Answer</summary>

**Correct: A.** Agents support **OpenAPI tool** registration — you upload an OpenAPI spec and the agent can invoke the API's operations as tools with authentication.

**Exam Objective:** Agentic solutions → Integrate external APIs via OpenAPI tools.
</details>

### Question 45
Which resource-level concept in the Agent Service **isolates a conversation** with ordered messages and state?

A. Assistant
B. Thread
C. Run
D. Tool

<details><summary>▶ Answer</summary>

**Correct: B.** A **thread** holds the ordered message history for a user/session. A **run** is an agent execution on a thread.

**Exam Objective:** Agentic solutions → Understand agent primitives (threads, runs, messages).
</details>

### Question 46
Your agent must **authenticate to a backend API** using the calling user's identity. Which capability do you use?

A. Managed identity of the agent only
B. On-behalf-of flow with Entra ID via an OpenAPI tool that accepts a user token
C. Anonymous calls
D. Shared API key embedded in the tool spec

<details><summary>▶ Answer</summary>

**Correct: B.** OpenAPI tools can be configured to use the caller's Entra ID token (OBO) so downstream calls preserve user identity — the recommended pattern for user-context access.

**Exam Objective:** Agentic solutions → Secure agents (authentication flows).
</details>

### Question 47
Which option best describes **multi-agent orchestration** patterns in Azure AI Foundry / Semantic Kernel?

A. A single agent must handle every task; multi-agent is unsupported
B. Agents can be composed (planner/worker, group chat) where one orchestrator delegates to specialized agents
C. Multi-agent requires deploying Azure Service Fabric clusters
D. Only two agents are allowed per project

<details><summary>▶ Answer</summary>

**Correct: B.** Orchestration patterns (planner/worker, supervisor, group-chat) allow a coordinator agent to delegate subtasks to specialists — supported via Foundry connected agents and Semantic Kernel AgentGroupChat.

**Exam Objective:** Agentic solutions → Design multi-agent orchestration.
</details>

### Question 48
To audit an agent's **tool invocations and reasoning steps** for compliance, which feature should you enable?

A. Azure OpenAI logprobs
B. Tracing / run steps persistence and diagnostic logs to Log Analytics
C. VNet flow logs
D. Client-side console logging only

<details><summary>▶ Answer</summary>

**Correct: B.** Agent runs emit **run steps** (message creation, tool calls) that can be persisted; enabling diagnostic settings to Log Analytics (and tracing via OpenTelemetry) provides an auditable record.

**Exam Objective:** Agentic solutions → Monitor and audit agents.
</details>

---

## Module 4 — Computer Vision Solutions (Q49–Q61)

### Question 49
Which Azure AI Vision API returns **dense captions**, **tags**, **objects**, **people**, and **OCR** in a single call?

A. Image Analysis 4.0 `analyze` endpoint
B. Face Detect API
C. Custom Vision prediction endpoint
D. Video Indexer insights

<details><summary>▶ Answer</summary>

**Correct: A.** Image Analysis 4.0 (`/imageanalysis:analyze`) supports `features=caption,denseCaptions,tags,objects,people,read,smartCrops` in one request.

**Exam Objective:** Computer Vision → Analyze images with Image Analysis 4.0.
</details>

### Question 50
You need to extract printed and handwritten text from invoices. Which feature should you enable on Image Analysis?

A. `tags`
B. `read` (OCR)
C. `objects`
D. `smartCrops`

<details><summary>▶ Answer</summary>

**Correct: B.** The **Read** (`read`) feature provides OCR for printed and handwritten text and is the successor to the legacy Read/OCR endpoints.

**Exam Objective:** Computer Vision → Extract text from images (OCR).
</details>

### Question 51
Which service supports **training a custom classification model** with as few as ~50 labeled images per class, with a no-code studio?

A. Azure AI Custom Vision
B. Azure Machine Learning AutoML only
C. Form Recognizer classifier
D. Azure Databricks MLflow

<details><summary>▶ Answer</summary>

**Correct: A.** **Custom Vision** provides image classification and object detection with a portal, SDKs, and REST. It separates **Training** and **Prediction** resources.

**Exam Objective:** Computer Vision → Train Custom Vision models.
</details>

### Question 52
Your Custom Vision project must tag multiple objects per image with bounding boxes. Which project type should you choose?

A. Classification — Multilabel
B. Classification — Multiclass
C. Object Detection
D. Anomaly Detector

<details><summary>▶ Answer</summary>

**Correct: C.** **Object Detection** predicts labels *and* bounding box coordinates; classification outputs are image-level only.

**Exam Objective:** Computer Vision → Select Custom Vision project type.
</details>

### Question 53
To recognize faces of **specific employees** for a building access solution, which API do you use, and what approval is required?

A. Face API **Identify** / **Verify** — requires **Limited Access** approval from Microsoft
B. Image Analysis `people` feature alone
C. Custom Vision face detection
D. Video Indexer celebrity recognition

<details><summary>▶ Answer</summary>

**Correct: A.** **Face Identify/Verify/Find Similar/Group** are Limited Access features; customers must apply and be approved. `people` in Image Analysis only detects people presence without identification.

**Exam Objective:** Computer Vision → Implement Face service (Limited Access).
</details>

### Question 54
Which file size limit applies to Azure AI Vision **Image Analysis 4.0** for synchronous image input?

A. 4 MB
B. 20 MB
C. 50 MB
D. 500 MB

<details><summary>▶ Answer</summary>

**Correct: B.** Image Analysis 4.0 accepts images up to **20 MB** (JPEG/PNG/BMP/GIF/WebP), 50×50 to 16,000×16,000 px.

**Exam Objective:** Computer Vision → Understand service limits (image size).
</details>

### Question 55 💻
A REST call to Image Analysis 4.0:

```
POST https://<endpoint>/computervision/imageanalysis:analyze?api-version=2024-02-01&features=caption,read&language=en
Ocp-Apim-Subscription-Key: <key>
Content-Type: application/octet-stream

<binary image bytes>
```

The call returns `400 InvalidImageSize`. What is the most likely fix?

A. Use `Content-Type: application/json`
B. Resize the image to between 50×50 and 16,000×16,000 px and ≤ 20 MB
C. Switch the API version to `2022-01-01-preview`
D. Remove the `features` parameter

<details><summary>▶ Answer</summary>

**Correct: B.** `InvalidImageSize` is raised when dimensions or bytes exceed supported ranges. Resize to the documented limits.

**Exam Objective:** Computer Vision → Troubleshoot Image Analysis.
</details>

### Question 56
Which Custom Vision export format enables **offline inference on iOS devices**?

A. TensorFlow SavedModel
B. CoreML
C. ONNX
D. Dockerfile

<details><summary>▶ Answer</summary>

**Correct: B.** Custom Vision supports exporting **compact domain** models as **CoreML** (iOS), **TensorFlow/TFLite** (Android), **ONNX** (Windows ML), and Dockerfile (Linux/Windows/ARM) for edge inference.

**Exam Objective:** Computer Vision → Export Custom Vision models for edge.
</details>

### Question 57
Which service analyzes **videos** to extract transcripts, faces, topics, and OCR in a single pipeline?

A. Azure AI Video Indexer
B. Azure Media Services DRM
C. Azure OpenAI Whisper only
D. Azure AI Speech batch transcription alone

<details><summary>▶ Answer</summary>

**Correct: A.** **Video Indexer** (ARM-based) provides multi-modal video insights: transcript, OCR, faces, labels, topics, sentiment, scenes.

**Exam Objective:** Computer Vision → Analyze video with Video Indexer.
</details>

### Question 58
Which **two** types of Custom Vision projects support **compact domain** export?

A. All projects support export regardless of domain
B. Projects built on a **compact** domain (e.g., General (compact), Landmarks (compact))
C. Only object detection projects
D. Only classification projects

<details><summary>▶ Answer</summary>

**Correct: B.** You must choose a **compact** domain to export models for edge.

**Exam Objective:** Computer Vision → Export Custom Vision models.
</details>

### Question 59
To generate **thumbnails focused on salient regions** from a photo, which Image Analysis feature is appropriate?

A. `smartCrops`
B. `objects`
C. `tags`
D. `denseCaptions`

<details><summary>▶ Answer</summary>

**Correct: A.** `smartCrops` returns region-of-interest bounding boxes at specified aspect ratios for intelligent cropping.

**Exam Objective:** Computer Vision → Generate smart crops.
</details>

### Question 60
Which feature set would you use to detect **PPE (hard hats, masks)** on workers at a construction site?

A. Image Analysis `tags` alone
B. **Custom Vision object detection** trained on PPE classes (or Azure AI Vision spatial analysis in some deployments)
C. Face API Identify
D. Anomaly Detector

<details><summary>▶ Answer</summary>

**Correct: B.** Detecting specific PPE classes with locations is a classic object-detection scenario best solved with a **Custom Vision** object detection model.

**Exam Objective:** Computer Vision → Select appropriate vision approach.
</details>

### Question 61
Your image OCR workload contains PDFs with 50+ pages. Which service is **better suited** than Image Analysis Read?

A. Azure AI Document Intelligence (Read/Layout/prebuilt models)
B. Azure Translator document translation
C. Azure Bot Service
D. Azure Cognitive Search OCR skill only

<details><summary>▶ Answer</summary>

**Correct: A.** For multi-page PDFs, tables, and structured extraction, **Document Intelligence** is the right service; Image Analysis Read targets images (single-page) or short scans.

**Exam Objective:** Computer Vision / Document Intelligence → Select OCR service.
</details>

---

## Module 5 — Natural Language Processing (Q62–Q79)

### Question 62
Which Azure AI Language feature classifies **user intent** and extracts **entities** from utterances for a chatbot?

A. Key Phrase Extraction
B. Conversational Language Understanding (CLU)
C. Question Answering
D. Named Entity Recognition (NER) only

<details><summary>▶ Answer</summary>

**Correct: B.** **CLU** trains intent classification plus entity extraction per conversational project — the LUIS successor.

**Exam Objective:** NLP → Implement CLU.
</details>

### Question 63
Which service orchestrates **multiple CLU / Question Answering / custom skills** with a single endpoint and routing?

A. Orchestration workflow (Azure AI Language)
B. Azure Bot Composer only
C. Semantic Kernel planners
D. Logic Apps

<details><summary>▶ Answer</summary>

**Correct: A.** **Orchestration workflow** projects route utterances to the appropriate CLU project, Question Answering knowledge base, or LUIS app (legacy).

**Exam Objective:** NLP → Use orchestration workflow.
</details>

### Question 64 💻
You label CLU training data with entity `{ "category": "City", "offset": 23, "length": 7 }` but inference returns low confidence for common city names. Which action is most likely to improve recognition?

A. Switch training mode to **Advanced** (uses Azure OpenAI-based training) and/or add a **list** component for cities
B. Raise `temperature` of CLU
C. Move to F0 tier
D. Delete all utterances and retrain

<details><summary>▶ Answer</summary>

**Correct: A.** CLU supports **Advanced** training mode (higher quality, more languages) and entity components: **learned**, **list**, **prebuilt**, **regex**. Adding a `list` component with known cities boosts recognition; Advanced training is recommended for multilingual/complex projects.

**Exam Objective:** NLP → Train CLU models (modes, entity components).
</details>

### Question 65
Which Azure AI Language feature determines whether a sentence is **positive, negative, neutral, or mixed** with confidence scores?

A. Sentiment analysis (with opinion mining)
B. Key phrase extraction
C. Language detection
D. PII detection

<details><summary>▶ Answer</summary>

**Correct: A.** **Sentiment analysis** returns document- and sentence-level sentiment with confidence; **opinion mining** adds aspect/target/opinion triples.

**Exam Objective:** NLP → Analyze sentiment.
</details>

### Question 66
Which Azure AI Language feature extracts **Person, Organization, Location, DateTime** and hundreds of other entity types from unstructured text?

A. Named Entity Recognition (NER)
B. Custom Text Classification
C. Text Analytics for Health
D. Question Answering

<details><summary>▶ Answer</summary>

**Correct: A.** Prebuilt **NER** covers a broad taxonomy; for domain-specific entities you can train a **Custom NER** project.

**Exam Objective:** NLP → Extract entities (NER).
</details>

### Question 67
Which service identifies **medical concepts, relations, and UMLS links** in clinical text?

A. Text Analytics for Health
B. Custom Text Classification
C. Document Intelligence prebuilt invoice
D. Azure Health Data Services FHIR only

<details><summary>▶ Answer</summary>

**Correct: A.** **Text Analytics for Health** extracts medical entities (medication, diagnosis, dosage) and links to ontologies like UMLS.

**Exam Objective:** NLP → Use Text Analytics for Health.
</details>

### Question 68
To detect and redact **PII** (emails, phone numbers, SSNs) from support tickets, which feature do you call?

A. PII detection (Azure AI Language)
B. Speaker recognition
C. Translator profanity filter only
D. Anomaly Detector

<details><summary>▶ Answer</summary>

**Correct: A.** Azure AI Language exposes **PII detection** with categories and a `redactedText` field.

**Exam Objective:** NLP → Detect and redact PII.
</details>

### Question 69
Which Speech capability converts spoken audio into text in real time over a WebSocket connection?

A. Real-time Speech-to-Text (SpeechRecognizer)
B. Batch transcription
C. Text-to-Speech
D. Speech translation only

<details><summary>▶ Answer</summary>

**Correct: A.** The **Speech SDK** `SpeechRecognizer` streams audio over WebSocket to a regional endpoint for real-time recognition.

**Exam Objective:** NLP → Implement speech-to-text (real-time).
</details>

### Question 70
Which option describes **batch transcription** in Azure AI Speech?

A. Submits audio stored in Azure Blob Storage for async transcription and polls for results
B. Streams from a microphone with callbacks
C. Requires Speech SDK client apps only
D. Is limited to 10 seconds of audio

<details><summary>▶ Answer</summary>

**Correct: A.** **Batch transcription** is a REST API that processes large volumes of audio from blob URLs/SAS and returns JSON transcripts asynchronously.

**Exam Objective:** NLP → Implement batch transcription.
</details>

### Question 71 💻
Which **SSML** snippet correctly sets a neural voice and slows speaking rate to 90%?

```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
       xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
  <voice name="en-US-JennyNeural">
    <prosody rate="-10%">Welcome to Contoso.</prosody>
  </voice>
</speak>
```

A. Correct
B. Wrong — `rate` must be specified in BPM
C. Wrong — `voice name` must be a standard (non-neural) voice
D. Wrong — SSML is not supported by Azure Speech

<details><summary>▶ Answer</summary>

**Correct: A.** SSML `<prosody rate="-10%">` lowers rate by 10% (≈ 90% of default). Neural voices like `en-US-JennyNeural` are fully supported.

**Exam Objective:** NLP → Customize TTS with SSML (prosody).
</details>

### Question 72 💻
Which SSML element applies a **speaking style** such as `cheerful` to a neural voice that supports styles?

```xml
<voice name="en-US-AriaNeural">
  <mstts:express-as style="cheerful" styledegree="2">
    Congratulations on your promotion!
  </mstts:express-as>
</voice>
```

A. `<prosody>`
B. `<mstts:express-as>`
C. `<say-as>`
D. `<emphasis>`

<details><summary>▶ Answer</summary>

**Correct: B.** The **`mstts:express-as`** element (MS TTS namespace) sets `style` and `styledegree` for expressive neural voices.

**Exam Objective:** NLP → Customize TTS with SSML (styles).
</details>

### Question 73 💻
Which SSML element ensures the text `"1234"` is spoken as **individual digits** ("one two three four")?

A. `<say-as interpret-as="digits">1234</say-as>`
B. `<say-as interpret-as="cardinal">1234</say-as>`
C. `<phoneme alphabet="ipa" ph="...">1234</phoneme>`
D. `<sub alias="one two three four">1234</sub>`

<details><summary>▶ Answer</summary>

**Correct: A.** `interpret-as="digits"` enumerates digits individually; `cardinal` reads "one thousand two hundred thirty-four".

**Exam Objective:** NLP → Customize TTS with SSML (say-as).
</details>

### Question 74 💻
Which SSML element inserts a **500 ms pause** between two sentences?

A. `<break time="500ms"/>`
B. `<pause duration="500ms"/>`
C. `<silence time="500"/>`
D. `<prosody pause="500ms"/>`

<details><summary>▶ Answer</summary>

**Correct: A.** `<break time="500ms"/>` (or `strength`) inserts pauses. Other variants are not valid SSML in Azure.

**Exam Objective:** NLP → Customize TTS with SSML (breaks).
</details>

### Question 75 💻
Which SSML element substitutes **pronunciation** without changing the written word, e.g., reading "Dr." as "Doctor"?

A. `<sub alias="Doctor">Dr.</sub>`
B. `<say-as interpret-as="spell-out">Dr.</say-as>`
C. `<emphasis level="strong">Dr.</emphasis>`
D. `<voice name="Doctor">Dr.</voice>`

<details><summary>▶ Answer</summary>

**Correct: A.** `<sub alias="Doctor">Dr.</sub>` substitutes spoken output without changing visible text.

**Exam Objective:** NLP → Customize TTS with SSML (sub).
</details>

### Question 76
Which Azure Translator feature translates **entire Word/PDF/HTML documents** while preserving formatting?

A. Text Translator `/translate` endpoint only
B. **Document Translation** (async) with source/target blob containers
C. Custom Translator training portal only
D. Speech translation

<details><summary>▶ Answer</summary>

**Correct: B.** **Document Translation** is an asynchronous API that translates entire documents in blob storage preserving formatting; supports glossaries and custom models.

**Exam Objective:** NLP → Implement document translation.
</details>

### Question 77
Which Translator capability lets you train a **domain-specific translation model**?

A. Custom Translator (parallel corpus training)
B. Transliteration endpoint
C. BreakSentence endpoint
D. Dictionary Lookup

<details><summary>▶ Answer</summary>

**Correct: A.** **Custom Translator** trains on aligned parallel documents (TMX/XLIFF/etc.) and exposes a Category ID used in `/translate` calls.

**Exam Objective:** NLP → Implement Custom Translator.
</details>

### Question 78
Which Question Answering source type is **recommended for FAQ pairs** with chit-chat and multi-turn prompts?

A. Custom question answering knowledge base with chit-chat added and follow-up prompts enabled
B. CLU project only
C. Azure AI Search semantic ranking only
D. Azure Bot Composer with hardcoded triggers

<details><summary>▶ Answer</summary>

**Correct: A.** **Custom question answering** in Azure AI Language supports FAQ ingestion, chit-chat persona import, multi-turn follow-up prompts, and synonyms.

**Exam Objective:** NLP → Implement question answering.
</details>

### Question 79
Which statement about **language detection** is true?

A. It requires at least 1,000 characters of input
B. It returns an ISO 639 language code and confidence; "unknown" when it cannot determine
C. It only supports English and Spanish
D. It is part of Translator and not Language service

<details><summary>▶ Answer</summary>

**Correct: B.** Language Detection returns ISO 639-1 code (e.g., `en`, `es`) with a confidence score; returns `(Unknown)` when it cannot confidently determine.

**Exam Objective:** NLP → Detect language.
</details>

---

## Module 6 — Knowledge Mining & Document Intelligence (Q80–Q97)

### Question 80
Which Azure AI Search feature **re-ranks top results** using a transformer-based semantic model and extracts captions/answers?

A. Scoring profiles
B. Semantic ranker (semantic configuration)
C. Synonym maps
D. Suggesters

<details><summary>▶ Answer</summary>

**Correct: B.** **Semantic ranker** (requires semantic configuration and a qualifying tier) re-ranks the top 50 results, generates captions, and can extract short answers.

**Exam Objective:** Knowledge mining → Implement semantic ranking.
</details>

### Question 81 💻
Which query is the correct **Lucene syntax** for "all documents whose `category` equals Hotel **and** rating ≥ 4"?

```
search=*&$filter=category eq 'Hotel' and rating ge 4
```

vs.

```
search=category:Hotel AND rating:[4 TO *]&queryType=full
```

A. Only the `$filter` form is valid
B. Both express the intent; `$filter` uses OData filter syntax and Lucene uses range query with `queryType=full`
C. Only the Lucene form is valid
D. Neither — use semantic query only

<details><summary>▶ Answer</summary>

**Correct: B.** Azure AI Search supports **OData `$filter`** for structured filtering and **Lucene full query** (`queryType=full`) for advanced text, both valid. Choose based on needs; `$filter` for structured predicates, Lucene for text-level features.

**Exam Objective:** Knowledge mining → Query Azure AI Search (filter & Lucene).
</details>

### Question 82 💻
Which query enables **vector search** in Azure AI Search using REST (api-version ≥ 2024-07-01)?

```json
{
  "vectorQueries": [
    {
      "kind": "vector",
      "vector": [0.12, -0.04, ... ],
      "fields": "contentVector",
      "k": 10
    }
  ],
  "select": "id,title"
}
```

A. Correct
B. Wrong — vector search is unsupported by Azure AI Search
C. Wrong — must use `search=` with text only
D. Wrong — `fields` must be `*`

<details><summary>▶ Answer</summary>

**Correct: A.** Vector queries are specified in the `vectorQueries` array; `fields` names the vector field(s) to search, and `k` limits neighbors. Hybrid search combines `search=...` text with `vectorQueries`.

**Exam Objective:** Knowledge mining → Implement vector search.
</details>

### Question 83 💻
Which REST call creates a **synonym map** that maps "usa" and "u.s.a" to "united states"?

```http
PUT https://<svc>.search.windows.net/synonymmaps/countries?api-version=2023-11-01
api-key: <admin-key>
Content-Type: application/json

{
  "name": "countries",
  "format": "solr",
  "synonyms": "usa, u.s.a, united states\n"
}
```

A. Correct
B. Wrong — `format` must be `openapi`
C. Wrong — synonyms must be JSON array only
D. Wrong — synonym maps are deprecated

<details><summary>▶ Answer</summary>

**Correct: A.** Synonym maps use **Solr** format; multiple groups separated by newlines. Then assign the map to an analyzed field via `synonymMaps` on the field definition.

**Exam Objective:** Knowledge mining → Customize Azure AI Search (synonyms).
</details>

### Question 84
Which component of an Azure AI Search **indexer pipeline** extracts enrichments like OCR text, key phrases, and entities?

A. Skillset
B. Data source
C. Index schema
D. Suggester

<details><summary>▶ Answer</summary>

**Correct: A.** A **skillset** is the ordered list of cognitive skills (OCR, key phrases, entity recognition, custom skills, splitting, embedding) applied during indexing.

**Exam Objective:** Knowledge mining → Build enrichment pipelines (skillsets).
</details>

### Question 85
Which skill would you include to **generate vector embeddings** during indexing?

A. Azure OpenAI Embedding skill
B. Sentiment skill
C. Entity linking skill
D. Shaper skill

<details><summary>▶ Answer</summary>

**Correct: A.** The built-in **Azure OpenAI Embedding skill** calls an embedding deployment and writes vectors to a target field during indexing (integrated vectorization).

**Exam Objective:** Knowledge mining → Implement integrated vectorization.
</details>

### Question 86
Which feature lets you add **your own HTTP-callable enrichment logic** into an Azure AI Search skillset?

A. Built-in language skill only
B. Web API custom skill (and Azure Machine Learning skill)
C. Suggesters
D. Scoring profiles

<details><summary>▶ Answer</summary>

**Correct: B.** A **Web API custom skill** calls an external HTTP endpoint with a defined input/output contract. **Azure Machine Learning skill** integrates AML-hosted models.

**Exam Objective:** Knowledge mining → Extend skillsets with custom skills.
</details>

### Question 87
Which tier of Azure AI Search is required to use the **semantic ranker** feature?

A. Free
B. Basic and above (with semantic ranker enabled; billed separately beyond the free allotment)
C. Only Storage Optimized L1/L2
D. Only Standard S3 High Density

<details><summary>▶ Answer</summary>

**Correct: B.** Semantic ranker requires **Basic or higher** with the semantic ranker turned on for the service; a free monthly quota exists before additional charges.

**Exam Objective:** Knowledge mining → Plan Azure AI Search (tiers & semantic).
</details>

### Question 88
Which component defines **fields, analyzers, vector configurations, and semantic configurations** in Azure AI Search?

A. Index
B. Indexer
C. Data source
D. Skillset

<details><summary>▶ Answer</summary>

**Correct: A.** The **index** schema declares fields, analyzers, vector search profiles, and semantic configurations.

**Exam Objective:** Knowledge mining → Design Azure AI Search indexes.
</details>

### Question 89
Which Azure AI Document Intelligence **prebuilt model** extracts **key-value pairs, tables, paragraphs, and selection marks** from arbitrary documents?

A. `prebuilt-layout`
B. `prebuilt-invoice`
C. `prebuilt-receipt`
D. `prebuilt-idDocument`

<details><summary>▶ Answer</summary>

**Correct: A.** **Layout** extracts structural elements (tables, selection marks, paragraphs, K/V) without targeting a specific document type. Invoice/Receipt/ID are domain prebuilt models.

**Exam Objective:** Document Intelligence → Use prebuilt layout model.
</details>

### Question 90
Which prebuilt model extracts **fields like InvoiceId, VendorName, InvoiceDate, Items, SubTotal, Total**?

A. `prebuilt-invoice`
B. `prebuilt-receipt`
C. `prebuilt-businessCard`
D. `prebuilt-read`

<details><summary>▶ Answer</summary>

**Correct: A.** The **Invoice** prebuilt model targets these specific fields and returns them as typed fields with confidence.

**Exam Objective:** Document Intelligence → Use prebuilt invoice model.
</details>

### Question 91
Which **custom model** type in Document Intelligence trains on **structured forms with consistent layout**?

A. Custom template model (requires as few as 5 labeled documents)
B. Custom neural model (handles varying layouts)
C. Custom composed model
D. Custom classifier

<details><summary>▶ Answer</summary>

**Correct: A.** **Template** models learn positional field locations from ~5 labeled samples for consistent forms. **Neural** models handle variable layouts but typically need more labeled data.

**Exam Objective:** Document Intelligence → Train custom models (template vs. neural).
</details>

### Question 92
You must extract fields from **three** different form layouts using one endpoint. Which feature do you use?

A. Custom composed model (combines multiple custom models; Document Intelligence routes to the right one)
B. Multi-tenant model
C. One index per layout
D. Prebuilt read only

<details><summary>▶ Answer</summary>

**Correct: A.** A **composed** model aggregates multiple custom models and a classifier routes each input to the correct model automatically.

**Exam Objective:** Document Intelligence → Compose custom models.
</details>

### Question 93
Which Document Intelligence capability returns the **exact text, bounding polygons, and reading order** for pages, lines, and words?

A. `prebuilt-read`
B. `prebuilt-invoice` fields only
C. `prebuilt-businessCard`
D. `prebuilt-idDocument`

<details><summary>▶ Answer</summary>

**Correct: A.** **Read (OCR)** returns pages/lines/words with polygons and language info. Layout adds tables/selection marks.

**Exam Objective:** Document Intelligence → Use prebuilt read model.
</details>

### Question 94
Which file size limit applies per document for Azure AI Document Intelligence **Standard (S0)** tier?

A. 4 MB
B. 20 MB
C. 100 MB
D. 500 MB

<details><summary>▶ Answer</summary>

**Correct: D.** Standard tier: up to **500 MB** per file and up to **2,000 pages**. Free tier is limited to **4 MB** and **2 pages**.

**Exam Objective:** Document Intelligence → Understand service limits.
</details>

### Question 95 💻
Which REST call submits a document to the layout model and which call retrieves the result?

```
POST {endpoint}/documentintelligence/documentModels/prebuilt-layout:analyze?api-version=2024-11-30
  → returns Operation-Location: {endpoint}/documentintelligence/documentModels/prebuilt-layout/analyzeResults/{id}?api-version=2024-11-30

GET  {that Operation-Location URL}
  → returns status running|succeeded|failed and the analyzeResult JSON when succeeded
```

A. Correct
B. Wrong — the API is synchronous; a single POST returns all results
C. Wrong — must use the `/formrecognizer/` base path in current GA
D. Wrong — api-version must be `2023-07-31` in current GA

<details><summary>▶ Answer</summary>

**Correct: A.** Document Intelligence uses an **async** pattern: POST returns `Operation-Location` for polling with GET until `status=succeeded`. The current GA uses the `/documentintelligence/` base path and `2024-11-30` api-version.

**Exam Objective:** Document Intelligence → Use REST API (async pattern).
</details>

### Question 96
Which feature lets you **classify a document type** before extracting fields, so you can route it to the correct custom model?

A. Custom classification model (Document Intelligence document classifier)
B. Image Analysis `tags`
C. CLU intent routing
D. Index scoring profile

<details><summary>▶ Answer</summary>

**Correct: A.** **Document classification** models identify the document type (e.g., Invoice vs. W-2 vs. Contract); you can pair this with composed models for automated routing.

**Exam Objective:** Document Intelligence → Use document classifiers.
</details>

### Question 97
Which statement about **Document Intelligence Studio** is true?

A. It is a no-code portal to label data, train custom models, and test prebuilt/custom models
B. It only runs on-premises in Docker
C. It is deprecated in favor of Power Automate only
D. It cannot connect to Azure Blob Storage

<details><summary>▶ Answer</summary>

**Correct: A.** **Document Intelligence Studio** provides labeling, training, testing, and composed-model management in a browser, connecting to Blob Storage for training sets.

**Exam Objective:** Document Intelligence → Use Document Intelligence Studio.
</details>

---

## Module 7 — Cross-Domain Scenarios (Q98–Q102)

### Question 98
A contact-center solution must (1) transcribe calls, (2) detect PII in transcripts, (3) summarize calls, and (4) search historical calls semantically. Which composition is most appropriate?

A. Azure AI Speech (batch transcription) → Azure AI Language (PII + summarization) → Azure OpenAI for abstractive summary → Azure AI Search with vector index for semantic retrieval
B. Azure OpenAI alone handles all four tasks end-to-end
C. Azure Bot Service only
D. Azure Machine Learning custom models for every step

<details><summary>▶ Answer</summary>

**Correct: A.** The idiomatic pattern chains **Speech** (STT), **Language** (PII redaction, extractive/conversation summarization), **Azure OpenAI** (abstractive summarization/insights), and **AI Search** (vector/hybrid indexing for retrieval) — each service for its specialty.

**Exam Objective:** Cross-domain → Architect end-to-end call-center solutions.
</details>

### Question 99
An enterprise knowledge assistant must (a) ingest PDFs/Office docs, (b) keep data in the tenant, (c) ground answers with citations, (d) enforce content safety, and (e) support Entra ID user access with per-user document permissions. Which architecture best satisfies all requirements?

A. Azure AI Search with integrated vectorization (doc ingestion + embeddings) + Azure OpenAI chat (RAG) + Azure AI Content Safety (Prompt Shields, groundedness) + App Service/Functions front end with Entra ID auth + security trimming using the document ACLs field
B. Client-side JavaScript only hitting OpenAI public API
C. One big fine-tuned model with all documents baked in
D. Bing Search alone

<details><summary>▶ Answer</summary>

**Correct: A.** Use **integrated vectorization** to ingest docs into Azure AI Search, perform RAG via Azure OpenAI with citations, gate inputs/outputs with **Content Safety (Prompt Shields + groundedness)**, and enforce per-user access with **security trimming** on a principal-IDs field and Entra ID tokens propagated to the search query.

**Exam Objective:** Cross-domain → Architect secure enterprise RAG.
</details>

### Question 100
A retail app must (i) detect product defects in images from an assembly line in near real-time, (ii) run at the edge due to bandwidth limits, and (iii) periodically retrain on new defect images. Which composition works?

A. Custom Vision object detection (compact domain) exported to ONNX/Docker for edge inference; scheduled retraining in the cloud on new labeled defects
B. Image Analysis `tags` in the cloud only
C. Face API on the edge
D. Azure OpenAI GPT-4o Vision on the edge

<details><summary>▶ Answer</summary>

**Correct: A.** **Custom Vision compact** models can be exported as **ONNX/TensorFlow/CoreML/Docker** and run at the edge; retraining in Custom Vision in the cloud with new labeled images supports continuous improvement.

**Exam Objective:** Cross-domain → Architect edge computer vision solutions.
</details>

### Question 101 💻
A multilingual field service app needs: speech input in any supported language → translated English transcript → intent classification → response TTS in the user's language. Which pipeline is correct?

```
[Speech SDK: SpeechTranslation to English]
  → [CLU in English]
    → [App business logic]
      → [Translator back to user language]
        → [Azure AI Speech TTS with localized neural voice]
```

A. Correct
B. Wrong — CLU supports translation internally, so Translator and speech translation are unnecessary
C. Wrong — you cannot combine Speech and Translator services
D. Wrong — TTS does not support non-English voices

<details><summary>▶ Answer</summary>

**Correct: A.** Azure Speech `TranslationRecognizer` produces translated text; CLU classifies intent in a trained language (English often used as hub); Translator converts responses back; TTS renders them using a neural voice matching the user's locale (e.g., `es-ES-ElviraNeural`). All four services are designed to compose.

**Exam Objective:** Cross-domain → Architect multilingual conversational solutions.
</details>

### Question 102
Which architectural checklist **best** reflects responsible-AI, security, and operational readiness for a production Azure AI solution? (Select the best combined answer.)

A. Entra ID + managed identities (no keys in code), Private Endpoints + disabled public access, Customer-Managed Keys, Content Safety (incl. Prompt Shields & groundedness), diagnostic logs to Log Analytics, quota/capacity alerts, Responsible AI Transparency Note, and documented data retention
B. Public endpoints with account keys rotated yearly and no monitoring
C. Fine-tuning the base model with production traffic data automatically
D. Skipping Content Safety because models are already aligned

<details><summary>▶ Answer</summary>

**Correct: A.** Production readiness combines **identity (Entra/managed identities)**, **network isolation (Private Endpoints)**, **data protection (CMK)**, **responsible AI controls (Content Safety, Transparency Note)**, **observability (diagnostics)**, and **capacity planning (quota alerts)**. The other options violate baseline security and RAI guidance.

**Exam Objective:** Cross-domain → Apply Responsible AI, security, and operations best practices.
</details>

---

## Answer key (quick index)

| Module | Correct count validations |
|---|---|
| 1 (Q1–Q22) | 22 questions covering identity, containers, monitoring, responsible AI, limits |
| 2 (Q23–Q40) | 18 questions covering Azure OpenAI parameters, RAG, safety, fine-tuning, tool calling |
| 3 (Q41–Q48) | 8 questions covering Foundry Agent Service, tools, orchestration |
| 4 (Q49–Q61) | 13 questions covering Image Analysis, Custom Vision, Face, Video Indexer |
| 5 (Q62–Q79) | 18 questions covering Language, CLU, Speech, SSML, Translator |
| 6 (Q80–Q97) | 18 questions covering Azure AI Search, skillsets, Document Intelligence |
| 7 (Q98–Q102) | 5 cross-domain architecture scenarios |

**Total: 102 questions.** Good luck on AI-102!
