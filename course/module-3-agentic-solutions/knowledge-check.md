# Module 3: Knowledge Check

Test your understanding of agentic AI solutions. 10 scenario-based questions covering agent concepts and implementation.

---

## Question 1
**Scenario:** You need to build an AI system that can autonomously research a topic, analyze data from uploaded spreadsheets, and produce a summary report. Which type of AI system best fits this requirement?

A) A chatbot with a large context window  
B) A copilot integrated with Office applications  
C) An AI agent with tools for file search and code execution  
D) A fine-tuned language model  

<details><summary>Answer</summary>

**C)** This scenario requires autonomous multi-step execution (research, analyze, report), tool usage (file search for research, code interpreter for data analysis), and planning — all characteristics of an AI agent. A chatbot lacks tool use and autonomy. A copilot assists but doesn't act autonomously. A fine-tuned model has no tool access.
</details>

---

## Question 2
**Scenario:** You are creating an agent using Microsoft Foundry Agent Service. After creating the agent and thread, what must you do to get the agent to process a user message?

A) Call `create_message()` — the agent responds automatically  
B) Call `create_message()` then `create_run()` to start processing  
C) Call `send_message()` which triggers automatic processing  
D) Call `submit_prompt()` with the thread ID  

<details><summary>Answer</summary>

**B)** The Foundry Agent Service lifecycle requires explicit steps: Create Agent → Create Thread → `create_message()` (add user message to thread) → `create_run()` (start the agent processing) → Poll for completion → Read messages. Messages don't trigger agent processing automatically — you must create a run.
</details>

---

## Question 3
**Scenario:** Your agent uses function calling. During a run, the agent decides to call `get_order_status`. The run enters `requires_action` status. What should your code do next?

A) Wait for the agent to execute the function automatically  
B) Execute the function, get the result, and call `submit_tool_outputs()`  
C) Update the agent instructions to include the order data  
D) Create a new run with the function result in the user message  

<details><summary>Answer</summary>

**B)** When a run enters `requires_action` status, the agent has generated the function name and arguments but cannot execute your functions. Your code must: (1) parse the tool call arguments, (2) execute the actual function, (3) call `submit_tool_outputs()` with the results. The agent then continues processing with the function output.
</details>

---

## Question 4
**Scenario:** You want your agent to analyze CSV files, generate charts, and perform statistical calculations. Which agent tool is most appropriate?

A) File Search  
B) Code Interpreter  
C) Function Calling  
D) Azure AI Search  

<details><summary>Answer</summary>

**B)** Code Interpreter provides a sandboxed Python environment that can read uploaded files (including CSVs), execute data analysis code (pandas, numpy), and generate visualizations (matplotlib). File Search is for text-based document retrieval (RAG). Function Calling invokes your custom APIs. Azure AI Search is for indexed document queries.
</details>

---

## Question 5
**Scenario:** You are designing a multi-agent system for research reports. One agent creates a plan, another gathers information, and a third writes the report. What is this pattern called?

A) Chain-of-thought reasoning  
B) Retrieval-Augmented Generation  
C) Planner-Executor orchestration  
D) Model reflection  

<details><summary>Answer</summary>

**C)** Planner-Executor orchestration uses a planner agent to decompose complex tasks into subtasks, then routes each subtask to specialized executor agents. Chain-of-thought is a prompting technique within a single model. RAG retrieves documents. Model reflection verifies outputs.
</details>

---

## Question 6
**Scenario:** Your customer service agent handles multiple users simultaneously. Each user should only see their own conversation history and data. How should you implement this?

A) Use a single thread for all users with user ID tags  
B) Create a separate thread for each user  
C) Create a separate agent instance for each user  
D) Store all messages in a shared database  

<details><summary>Answer</summary>

**B)** Creating separate threads per user ensures conversation isolation. Each thread maintains its own message history, so User A's conversation doesn't leak into User B's. A single shared thread would mix conversations. Creating separate agents per user is unnecessary overhead — threads provide isolation. Shared databases don't provide built-in isolation.
</details>

---

## Question 7
**Scenario:** You need to prevent your agent from executing destructive database operations (DELETE, DROP, UPDATE). What is the best approach?

A) Add instructions telling the agent not to run destructive queries  
B) Implement a function that only accepts SELECT queries and validates input  
C) Use a content filter to block SQL keywords  
D) Set the temperature to 0 to prevent unexpected behavior  

<details><summary>Answer</summary>

**B)** Defense in depth requires enforcing safety at the tool level, not just in instructions. Implement a function that validates queries are read-only (SELECT only) before execution. Instructions can be bypassed through prompt injection. Content filters aren't designed for SQL validation. Temperature doesn't affect tool usage decisions.
</details>

---

## Question 8
**Scenario:** Which of the following is NOT a core component of an AI agent architecture?

A) Tools — external capabilities the agent can invoke  
B) Memory — context maintained across interactions  
C) Fine-tuning — training the model on domain data  
D) Planning — decomposing complex tasks into steps  

<details><summary>Answer</summary>

**C)** The four core components of an AI agent are: Tools (interact with external world), Memory (maintain context), Planning (break down tasks), and Orchestration (coordinate execution). Fine-tuning is a model training technique, not a runtime agent component. An agent can use a fine-tuned model, but fine-tuning itself is not part of the agent architecture.
</details>

---

## Question 9
**Scenario:** Your agent runs in production and you notice it sometimes takes 20+ steps to complete simple tasks that should take 3-4 steps. What operational guardrail should you implement?

A) Increase the temperature for more creative solutions  
B) Set a maximum iteration/step limit per run  
C) Switch to a smaller model  
D) Disable all tools except the most used one  

<details><summary>Answer</summary>

**B)** Setting a maximum iteration limit prevents agents from entering infinite loops or taking unnecessarily long paths. This is a key operational guardrail. If the agent exceeds the limit, it can return a partial result or escalate to a human. Increasing temperature would make behavior more unpredictable. Disabling tools would reduce capabilities.
</details>

---

## Question 10
**Scenario:** You want your agent to search through a collection of product documentation PDFs to answer customer questions. The documents are already uploaded. Which tool configuration should you use?

A) Code Interpreter with the PDF files attached  
B) File Search with a vector store containing the PDFs  
C) Function Calling with a custom PDF parser function  
D) Azure OpenAI "On Your Data" with the PDFs in blob storage  

<details><summary>Answer</summary>

**B)** File Search with a vector store is the purpose-built tool for RAG over uploaded documents in the Agent Service. You create a vector store, add the PDFs, and attach it to the agent. The agent automatically chunks, embeds, and searches the documents. Code Interpreter could read files but isn't optimized for search. Function Calling would require building your own search infrastructure.
</details>

---

## Scoring

| Score | Assessment |
|-------|-----------|
| 9-10 correct | ✅ Excellent — ready for the exam |
| 7-8 correct | 🔄 Review the lesson for missed topics |
| Below 7 | 📚 Re-study the module before proceeding |
