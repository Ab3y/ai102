# Module 2: Knowledge Check

Test your understanding of generative AI solutions. 15 scenario-based questions covering all three lessons.

---

## Question 1
**Scenario:** You are building a RAG application. After retrieving relevant documents from Azure AI Search, you need to send them to Azure OpenAI for answer generation. In the chat completions API, where should you place the retrieved document context?

A) In the `user` message content  
B) In the `system` message content  
C) In a separate `context` parameter  
D) In the `data_sources` parameter of the request body  

<details><summary>Answer</summary>

**B)** In a manual RAG implementation, the retrieved context is typically placed in the system message to ground the model's responses. The system message tells the model "use this context to answer questions." Option D (`data_sources`) is for the Azure OpenAI "On Your Data" feature, which is a different approach. Both B and D are valid RAG approaches, but the system message approach is the manual orchestration pattern.
</details>

---

## Question 2
**Scenario:** You are deploying GPT-4o in Azure OpenAI. After creating the resource, you try to call the chat completions API but receive a 404 error. What is the most likely issue?

A) The API version is incorrect  
B) The model has not been deployed to the resource  
C) The region does not support GPT-4o  
D) The API key is invalid  

<details><summary>Answer</summary>

**B)** Creating an Azure OpenAI resource and deploying a model are separate steps. A 404 error when calling a deployment that doesn't exist is the most common result of skipping the model deployment step. An invalid API key would return 401, and a region issue would prevent resource creation.
</details>

---

## Question 3
**Scenario:** Your chatbot needs to generate highly consistent, factual responses for a financial compliance use case. Which parameter settings are most appropriate?

A) `temperature: 1.5, top_p: 0.5`  
B) `temperature: 0.0, top_p: 1.0`  
C) `temperature: 0.8, top_p: 0.8`  
D) `temperature: 0.5, top_p: 0.5`  

<details><summary>Answer</summary>

**B)** For factual, consistent responses, use `temperature: 0.0` (most deterministic) and `top_p: 1.0` (default). Microsoft recommends adjusting one parameter, not both. Options C and D modify both simultaneously. Option A uses very high temperature, producing unreliable output.
</details>

---

## Question 4
**Scenario:** You need to generate images using Azure OpenAI. You want to create 3 variations of a product image using DALL-E 3. What limitation will you encounter?

A) DALL-E 3 cannot generate product images  
B) DALL-E 3 only supports `n=1` — you must make 3 separate API calls  
C) Image generation requires a separate Azure AI Vision resource  
D) DALL-E 3 only supports 256x256 resolution  

<details><summary>Answer</summary>

**B)** DALL-E 3 only supports generating one image per request (`n=1`). To get 3 variations, you must make 3 separate API calls. DALL-E 3 supports 1024x1024, 1792x1024, and 1024x1792 sizes. DALL-E 2 supported higher `n` values but is deprecated.
</details>

---

## Question 5
**Scenario:** In a Microsoft Foundry project, you want to build a workflow that takes a user question, retrieves relevant documents, and generates an answer. Which Foundry feature should you use?

A) Model catalog  
B) Prompt flow  
C) Evaluation flow  
D) Serverless endpoint  

<details><summary>Answer</summary>

**B)** Prompt flow is the Foundry feature for building LLM-powered workflows as directed acyclic graphs (DAGs). It connects steps like retrieval, prompt assembly, and LLM generation. The model catalog is for discovering/deploying models. Evaluation flow assesses quality. Serverless endpoints deploy models for inference.
</details>

---

## Question 6
**Scenario:** Your RAG application sometimes generates answers that are not supported by the source documents. Which evaluation metric specifically measures this problem?

A) Relevance  
B) Coherence  
C) Groundedness  
D) Fluency  

<details><summary>Answer</summary>

**C)** Groundedness measures whether the generated answer is factually supported by the provided context/source documents. Relevance measures if the answer addresses the question. Coherence measures readability. Fluency measures grammatical quality. Groundedness is the specific metric for detecting hallucinations in RAG scenarios.
</details>

---

## Question 7
**Scenario:** You want to extract structured JSON from customer support emails consistently. The model sometimes returns different formats. Which prompt engineering technique is most appropriate?

A) Chain-of-thought prompting  
B) Zero-shot prompting  
C) Few-shot prompting with example outputs  
D) System prompt with `temperature: 2.0`  

<details><summary>Answer</summary>

**C)** Few-shot prompting provides examples of the expected input/output format, which helps the model consistently produce structured JSON in the desired schema. Chain-of-thought is for complex reasoning. Zero-shot gives no formatting guidance. Temperature 2.0 would make output more random and inconsistent.
</details>

---

## Question 8
**Scenario:** You need to build embeddings for 10,000 documents to enable semantic search. Which Azure OpenAI model should you deploy?

A) GPT-4o  
B) DALL-E 3  
C) text-embedding-ada-002  
D) Whisper  

<details><summary>Answer</summary>

**C)** `text-embedding-ada-002` (or the newer `text-embedding-3-small/large`) is specifically designed to generate vector embeddings for semantic search, clustering, and RAG. GPT-4o generates text. DALL-E 3 generates images. Whisper transcribes audio.
</details>

---

## Question 9
**Scenario:** Your model's responses are repetitive, often using the same phrases. Which parameter should you increase?

A) `temperature`  
B) `max_tokens`  
C) `frequency_penalty`  
D) `top_p`  

<details><summary>Answer</summary>

**C)** `frequency_penalty` penalizes tokens proportional to how often they've already appeared in the output, directly reducing repetition. `presence_penalty` encourages topic diversity. `temperature` affects overall randomness. `max_tokens` controls length.
</details>

---

## Question 10
**Scenario:** You are deciding between fine-tuning and RAG for your application. Your AI needs to answer questions about company policies that change quarterly. Which approach is better?

A) Fine-tuning — retrain the model quarterly  
B) RAG — index the latest policies and retrieve them at query time  
C) Increase the model's context window  
D) Use a higher temperature for more creative answers  

<details><summary>Answer</summary>

**B)** RAG is ideal when the AI needs access to current, frequently changing data. Documents are indexed in Azure AI Search and retrieved at query time, so updates take effect immediately without retraining. Fine-tuning is expensive, slow, and the model would be outdated between retraining cycles.
</details>

---

## Question 11
**Scenario:** The Azure OpenAI REST endpoint for chat completions returns `prompt_filter_results` in the response. What does this contain?

A) The revised version of the user's prompt  
B) Content safety filter results for the input prompt  
C) Token count breakdown by prompt section  
D) A list of filtered-out words  

<details><summary>Answer</summary>

**B)** `prompt_filter_results` contains the content safety analysis of the input (prompt) — whether the input triggered any filters for hate, violence, sexual, or self-harm categories. `content_filter_results` on the choices contains the output filter results. Both directions are filtered and reported.
</details>

---

## Question 12
**Scenario:** In a Microsoft Foundry hub, multiple projects share the same Azure OpenAI connection. Where is this connection configured?

A) In each individual project  
B) In the Foundry hub (shared across projects)  
C) In the Azure OpenAI resource directly  
D) In Azure Key Vault  

<details><summary>Answer</summary>

**B)** Connections are configured at the hub level and shared across all projects within that hub. This enables centralized management of credentials and endpoints while allowing multiple projects to use the same underlying services.
</details>

---

## Question 13
**Scenario:** You want your AI to solve a complex multi-step math problem accurately. Which prompting technique is most effective?

A) Zero-shot with `temperature: 0`  
B) Few-shot with example answers  
C) Chain-of-thought prompting  
D) System prompt saying "be accurate"  

<details><summary>Answer</summary>

**C)** Chain-of-thought (CoT) prompting instructs the model to reason step-by-step, which significantly improves accuracy on complex reasoning and math problems. Adding "think step by step" or showing reasoning examples helps the model break down complex problems. Zero-shot with low temperature is deterministic but doesn't improve reasoning. Few-shot helps formatting more than reasoning.
</details>

---

## Question 14
**Scenario:** You are preparing fine-tuning training data for Azure OpenAI. Which file format and structure is required?

A) CSV with columns: input, output  
B) JSONL with each line containing a `messages` array (system, user, assistant roles)  
C) JSON array of prompt-completion pairs  
D) Plain text with prompt and completion separated by `###`  

<details><summary>Answer</summary>

**B)** Azure OpenAI fine-tuning requires JSONL format where each line is a JSON object with a `messages` array containing `role`/`content` pairs using system, user, and assistant roles. This matches the chat completions API format. The old prompt-completion format (options C and D) is for legacy models.
</details>

---

## Question 15
**Scenario:** You want to reduce costs while maintaining quality by routing simple questions to a cheaper model and complex questions to GPT-4o. What is this pattern called?

A) RAG (Retrieval-Augmented Generation)  
B) Chain-of-thought prompting  
C) Multi-model orchestration / model routing  
D) Fine-tuning with curriculum learning  

<details><summary>Answer</summary>

**C)** Multi-model orchestration (or model routing) uses a classifier or simple model to assess query complexity and routes to the appropriate model. Simple queries go to cost-effective models (GPT-4o-mini), complex queries go to powerful models (GPT-4o). This optimizes cost while maintaining quality.
</details>

---

## Scoring

| Score | Assessment |
|-------|-----------|
| 13-15 correct | ✅ Ready to move to Module 3 |
| 10-12 correct | 🔄 Review the lessons for missed topics |
| Below 10 | 📚 Re-study the module before proceeding |
