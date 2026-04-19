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
