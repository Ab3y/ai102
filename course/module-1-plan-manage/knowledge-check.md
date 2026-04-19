# Module 1: Knowledge Check

Test your understanding of planning and managing Azure AI solutions. 15 scenario-based questions covering all four lessons.

---

## Question 1
**Scenario:** Your company needs to use both text analytics and computer vision capabilities. You want a single endpoint and key for simplified management. Which resource should you create?

A) A Computer Vision resource and a Text Analytics resource  
B) An Azure AI services multi-service resource  
C) An Azure OpenAI resource  
D) An Azure AI Search resource  

<details><summary>Answer</summary>

**B)** An Azure AI services multi-service resource provides access to multiple AI services (Vision, Language, Speech, etc.) under a single endpoint and key. This simplifies management when you need multiple capabilities. Azure OpenAI and AI Search are not included in multi-service resources.
</details>

---

## Question 2
**Scenario:** You are deploying an Azure AI services container for sentiment analysis in an environment with limited internet connectivity. Which three environment variables are required for the container to function?

A) `Endpoint`, `Key`, `Region`  
B) `ApiKey`, `Billing`, `Eula=accept`  
C) `SubscriptionKey`, `ResourceUrl`, `AcceptTerms`  
D) `ConnectionString`, `ApiVersion`, `License=accept`  

<details><summary>Answer</summary>

**B)** Azure AI services containers require exactly three environment variables: `ApiKey` (subscription key), `Billing` (endpoint URI for billing), and `Eula` (must be set to `accept`). The container still needs periodic internet access for billing even though data is processed locally.
</details>

---

## Question 3
**Scenario:** Your application currently uses Key1 to authenticate with an Azure AI service. Security policy requires you to rotate keys quarterly. What is the correct sequence?

A) Regenerate Key1, update application to use Key1, regenerate Key2  
B) Regenerate Key2, update application to use Key2, regenerate Key1  
C) Regenerate both keys simultaneously, update application  
D) Delete the resource and recreate it with new keys  

<details><summary>Answer</summary>

**B)** The two-key rotation pattern: First regenerate Key2 (which is not in use, so no disruption). Then update the application to use the new Key2. Finally, regenerate Key1 (no longer in use). This ensures zero downtime during rotation.
</details>

---

## Question 4
**Scenario:** You need to analyze text for harmful content. The Content Safety API returns a severity score of 4 for the "Violence" category. What does this indicate?

A) The content is safe with no violent content  
B) The content has low-severity violent references  
C) The content has medium-severity violent content  
D) The content has high-severity violent content  

<details><summary>Answer</summary>

**C)** Content Safety uses severity levels 0, 2, 4, and 6. Level 0 = safe, 2 = low, 4 = medium, 6 = high. A score of 4 indicates medium-severity content that is likely inappropriate but not at the highest severity.
</details>

---

## Question 5
**Scenario:** You want to ensure your Azure AI service is only accessible from within your virtual network. Which two configurations should you apply?

A) Enable public network access and add IP rules  
B) Disable public network access and create a private endpoint  
C) Enable managed identity and disable RBAC  
D) Configure a Web Application Firewall and DNS zone  

<details><summary>Answer</summary>

**B)** To restrict access to VNet-only, disable public network access (`publicNetworkAccess: Disabled`) and create a private endpoint. This gives the AI service a private IP address within your VNet, ensuring all traffic stays on the private network.
</details>

---

## Question 6
**Scenario:** A developer wants to use Azure AD authentication (managed identity) with an Azure AI service instead of API keys. The SDK throws an authentication error. The resource was created without a custom subdomain. What is the likely issue?

A) Managed identity is not supported for AI services  
B) The `customSubDomainName` property must be set on the resource  
C) The developer needs to use Key Vault instead  
D) Azure AD authentication requires the Premium tier  

<details><summary>Answer</summary>

**B)** Azure AD / managed identity authentication requires the AI service resource to have a `customSubDomainName` configured. Without it, the resource only supports key-based authentication. This is a commonly missed configuration step.
</details>

---

## Question 7
**Scenario:** You are building a customer-facing chatbot using Azure OpenAI. Users have found ways to make the bot ignore its system prompt. Which Azure service should you implement to detect these attacks?

A) Azure Content Safety — content filters  
B) Azure Content Safety — prompt shields  
C) Azure Content Safety — blocklists  
D) Azure Monitor — anomaly detection  

<details><summary>Answer</summary>

**B)** Prompt shields specifically detect jailbreak attempts (user prompt attacks) and indirect injection (document attacks). Content filters detect harmful content categories but don't specifically detect prompt manipulation. Blocklists match specific terms. Prompt shields are purpose-built for this scenario.
</details>

---

## Question 8
**Scenario:** You need to provision an Azure OpenAI resource via Bicep. Which `kind` value should you use?

A) `CognitiveServices`  
B) `TextAnalytics`  
C) `OpenAI`  
D) `AzureOpenAI`  

<details><summary>Answer</summary>

**C)** Azure OpenAI resources use `kind: 'OpenAI'` in Bicep/ARM templates. `CognitiveServices` is for multi-service resources (which don't include OpenAI). `TextAnalytics` is for the Language service. `AzureOpenAI` is not a valid kind value.
</details>

---

## Question 9
**Scenario:** Your Azure OpenAI content filter is set to "Medium" severity for the Violence category. Which severity levels will be blocked?

A) Only severity 4  
B) Severity 2, 4, and 6  
C) Severity 4 and 6  
D) Only severity 6  

<details><summary>Answer</summary>

**C)** Medium threshold blocks severity ≥ 4, which means levels 4 and 6. Low blocks ≥ 2 (levels 2, 4, 6). High blocks ≥ 6 (level 6 only). Level 0 is never blocked as it indicates safe content.
</details>

---

## Question 10
**Scenario:** You want to capture detailed API request logs for your AI service and query them with KQL. What must you configure?

A) Enable Azure Monitor metrics (automatic)  
B) Create a diagnostic setting that sends resource logs to a Log Analytics workspace  
C) Install the Azure Monitor agent on the AI service  
D) Enable Application Insights on the AI service  

<details><summary>Answer</summary>

**B)** Platform metrics are collected automatically, but resource logs (detailed API request/response logs) require a diagnostic setting configured to send logs to a destination like Log Analytics. You then query them with KQL. Azure Monitor agent is for VMs, not PaaS services.
</details>

---

## Question 11
**Scenario:** You need to extract data from thousands of invoices in PDF format, pulling out vendor names, amounts, and dates. Which service should you use?

A) Computer Vision OCR  
B) Azure OpenAI GPT-4o with vision  
C) Document Intelligence with the prebuilt invoice model  
D) Language Service with custom NER  

<details><summary>Answer</summary>

**C)** Document Intelligence's prebuilt invoice model is specifically designed to extract structured data from invoices (vendor, amounts, dates, line items). Computer Vision OCR reads text but doesn't understand document structure. GPT-4o could work but is not optimized for high-volume structured extraction. Language Service NER is for entity extraction from unstructured text.
</details>

---

## Question 12
**Scenario:** An application service principal needs to call the Azure OpenAI API to generate chat completions, but should not be able to create or delete resources. Which RBAC role should you assign?

A) Cognitive Services Contributor  
B) Cognitive Services User  
C) Cognitive Services OpenAI User  
D) Reader  

<details><summary>Answer</summary>

**C)** `Cognitive Services OpenAI User` grants permission to use the OpenAI API (completions, embeddings, etc.) without resource management permissions. `Cognitive Services User` works for non-OpenAI services. `Contributor` grants too many permissions. `Reader` doesn't grant API access.
</details>

---

## Question 13
**Scenario:** Your RAG application generates answers from company documents. Sometimes the AI makes claims not supported by the source documents. Which Content Safety feature should you implement?

A) Content filters  
B) Blocklists  
C) Prompt shields  
D) Groundedness detection  

<details><summary>Answer</summary>

**D)** Groundedness detection verifies whether AI-generated content is factually supported by provided source documents. It identifies ungrounded claims (hallucinations). Content filters detect harmful content, not factual accuracy. Blocklists match specific terms. Prompt shields detect manipulation attempts.
</details>

---

## Question 14
**Scenario:** You need to monitor the token consumption of your Azure OpenAI deployment to manage costs. Which metric should you track?

A) `TotalCalls`  
B) `TokenTransaction`  
C) `ProcessedCount`  
D) `DataIn`  

<details><summary>Answer</summary>

**B)** `TokenTransaction` tracks the number of tokens consumed by Azure OpenAI API calls. This directly correlates with cost since OpenAI pricing is per-token. `TotalCalls` counts requests regardless of token usage. `ProcessedCount` and `DataIn` are for other service types.
</details>

---

## Question 15
**Scenario:** Your content moderation system needs to block specific competitor brand names from appearing in AI-generated responses. Which feature should you implement?

A) Content filters with Low severity threshold  
B) Custom blocklists in Content Safety  
C) Prompt shields  
D) A system prompt instructing the AI not to mention competitors  

<details><summary>Answer</summary>

**B)** Custom blocklists allow you to define specific terms (like competitor names) that should be flagged or blocked. Content filters detect harmful content categories, not specific business terms. Prompt shields detect manipulation, not brand mentions. System prompts can be bypassed by jailbreaks and are not reliable for enforcement.
</details>

---

## Scoring

| Score | Assessment |
|-------|-----------|
| 13-15 correct | ✅ Ready to move to Module 2 |
| 10-12 correct | 🔄 Review the lessons for missed topics |
| Below 10 | 📚 Re-study the module before proceeding |
