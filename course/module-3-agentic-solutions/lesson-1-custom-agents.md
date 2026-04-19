# Lesson 1: Build Custom Agents

## Learning Objectives

- Define what AI agents are and how they differ from standard LLM applications
- Understand the core components: tools, memory, orchestration, and planning
- Create agents using Microsoft Foundry Agent Service
- Configure agent tools: code interpreter, file search, and function calling
- Implement multi-agent orchestration patterns
- Apply safety guardrails and test/optimize/deploy agents

---

## What Is an AI Agent?

An AI agent is an AI system that can **autonomously** take actions to accomplish goals. Unlike a simple chatbot that responds to a single prompt, agents can:

- **Plan**: Break complex tasks into steps
- **Use tools**: Execute code, search files, call APIs
- **Remember**: Maintain context across interactions
- **Iterate**: Evaluate results and adjust their approach
- **Orchestrate**: Coordinate with other agents or services

### Agent vs. Chatbot vs. Copilot

| Feature | Chatbot | Copilot | Agent |
|---------|---------|---------|-------|
| **Interaction** | Reactive (respond to prompts) | Reactive (assist human tasks) | Proactive (autonomous actions) |
| **Tool use** | None or limited | Integrated with workspace | Multiple tools, dynamic selection |
| **Memory** | Session only | Session + workspace context | Long-term + working memory |
| **Autonomy** | None — human drives | Low — augments human | High — plans and executes independently |
| **Planning** | None | None | Multi-step planning and replanning |
| **Example** | FAQ bot | GitHub Copilot | Research agent that gathers, analyzes, and reports |

> ### 📝 Exam Tip
> Know the distinction between a chatbot (reactive, no tools), a copilot (assists human, integrated tools), and an agent (autonomous, plans, uses multiple tools). The exam tests conceptual understanding of agent capabilities.

---

## Core Agent Components

### 1. Tools

Tools give agents the ability to interact with the external world:

| Tool Type | Description | Example |
|-----------|-------------|---------|
| **Code Interpreter** | Execute Python code in a sandbox | Data analysis, chart generation, calculations |
| **File Search** | Search through uploaded documents | RAG over user-provided files |
| **Function Calling** | Call developer-defined functions | API calls, database queries, send emails |
| **Azure AI Search** | Query a search index | Enterprise knowledge base retrieval |
| **Microsoft 365** | Access Office apps | Read emails, calendar, SharePoint |

### 2. Memory

| Memory Type | Scope | Implementation |
|-------------|-------|----------------|
| **Working memory** | Current conversation | Message history in the thread |
| **Short-term memory** | Current session | Thread context window |
| **Long-term memory** | Across sessions | External storage (database, vector store) |
| **Shared memory** | Across agents | Common data store for multi-agent scenarios |

### 3. Orchestration

The orchestration layer controls how an agent processes requests:

```
User Request
    │
    ▼
┌──────────────┐
│   Planning    │ ← Break request into steps
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Tool Select  │ ← Choose appropriate tool for each step
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   Execute     │ ← Run tool and get results
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   Evaluate    │ ← Assess results, decide if more steps needed
└──────┬───────┘
       │
   ┌───┴───┐
   │ Done?  │
   └───┬───┘
    Yes│  No└──→ Back to Planning
       ▼
   Final Answer
```

### 4. Planning

| Strategy | Description | Use Case |
|----------|-------------|----------|
| **ReAct** | Reason → Act → Observe → Repeat | General-purpose task solving |
| **Plan-and-Execute** | Create full plan, then execute steps | Complex multi-step tasks |
| **Reflexion** | Execute, reflect on errors, retry | Self-improving tasks |

---

## Microsoft Foundry Agent Service

Foundry Agent Service provides a managed platform for building, deploying, and running AI agents.

### Creating an Agent

```python
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import Agent, AgentThread

# Connect to Foundry project
client = AIProjectClient(
    credential=DefaultAzureCredential(),
    endpoint="https://my-project.services.ai.azure.com"
)

# Create an agent
agent = client.agents.create_agent(
    model="gpt-4o",
    name="data-analyst",
    instructions="""You are a data analysis assistant.
When asked to analyze data:
1. Read the uploaded file
2. Understand the data structure
3. Perform the requested analysis
4. Create visualizations when helpful
5. Provide clear insights and recommendations""",
    tools=[
        {"type": "code_interpreter"},   # Can execute Python code
        {"type": "file_search"}          # Can search uploaded files
    ]
)
print(f"Agent created: {agent.id}")
```

### Agent Threads and Messages

Threads maintain conversation state:

```python
# Create a conversation thread
thread = client.agents.create_thread()

# Add a message to the thread
message = client.agents.create_message(
    thread_id=thread.id,
    role="user",
    content="Analyze the sales data and identify top-performing regions",
    attachments=[{
        "file_id": uploaded_file.id,
        "tools": [{"type": "code_interpreter"}]
    }]
)

# Run the agent on the thread
run = client.agents.create_run(
    thread_id=thread.id,
    agent_id=agent.id
)

# Poll for completion
import time
while run.status in ["queued", "in_progress"]:
    time.sleep(2)
    run = client.agents.get_run(thread_id=thread.id, run_id=run.id)

# Get the agent's response
messages = client.agents.list_messages(thread_id=thread.id)
for msg in messages.data:
    if msg.role == "assistant":
        for content in msg.content:
            if content.type == "text":
                print(content.text.value)
```

> ### 📝 Exam Tip
> Understand the Foundry Agent Service lifecycle: **Create Agent** → **Create Thread** → **Add Messages** → **Create Run** → **Poll for Completion** → **Read Messages**. The exam tests this sequence.

---

## Agent Tools Deep Dive

### Code Interpreter

Code Interpreter provides a sandboxed Python environment:

```python
agent = client.agents.create_agent(
    model="gpt-4o",
    name="code-agent",
    instructions="You are a Python data analyst.",
    tools=[{"type": "code_interpreter"}]
)

# The agent can now:
# - Write and execute Python code
# - Install common packages (pandas, matplotlib, numpy)
# - Read uploaded files (CSV, Excel, JSON)
# - Generate charts and visualizations
# - Output files (images, CSVs)
```

**Capabilities:**
- Execute arbitrary Python code safely
- Access uploaded files
- Generate output files (images, CSVs, etc.)
- Install and use common data science packages

**Limitations:**
- Sandboxed environment (no internet access from code)
- Session-based (code state resets between runs)
- Limited execution time

### File Search

File Search enables RAG over uploaded documents:

```python
# Create a vector store for the agent's knowledge base
vector_store = client.agents.create_vector_store(
    name="product-docs",
    file_ids=[file1.id, file2.id, file3.id]
)

# Create agent with file search
agent = client.agents.create_agent(
    model="gpt-4o",
    name="support-agent",
    instructions="Answer customer questions using the product documentation.",
    tools=[{"type": "file_search"}],
    tool_resources={
        "file_search": {
            "vector_store_ids": [vector_store.id]
        }
    }
)
```

**Supported file types:** PDF, DOCX, TXT, MD, HTML, JSON, CSV, and more.

### Function Calling

Function calling lets agents invoke developer-defined functions:

```python
# Define functions the agent can call
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_order_status",
            "description": "Look up the status of a customer order by order ID",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "The order ID (e.g., ORD-12345)"
                    }
                },
                "required": ["order_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_support_ticket",
            "description": "Create a support ticket for an issue that cannot be resolved immediately",
            "parameters": {
                "type": "object",
                "properties": {
                    "customer_email": {"type": "string"},
                    "issue_summary": {"type": "string"},
                    "priority": {
                        "type": "string",
                        "enum": ["low", "medium", "high", "critical"]
                    }
                },
                "required": ["customer_email", "issue_summary", "priority"]
            }
        }
    }
]

agent = client.agents.create_agent(
    model="gpt-4o",
    name="customer-service",
    instructions="You are a customer service agent. Use tools to look up orders and create tickets.",
    tools=tools
)
```

### Handling Function Calls

```python
# After creating a run, check if the agent wants to call a function
run = client.agents.create_run(thread_id=thread.id, agent_id=agent.id)

while run.status in ["queued", "in_progress", "requires_action"]:
    time.sleep(2)
    run = client.agents.get_run(thread_id=thread.id, run_id=run.id)

    if run.status == "requires_action":
        tool_calls = run.required_action.submit_tool_outputs.tool_calls
        tool_outputs = []

        for tool_call in tool_calls:
            if tool_call.function.name == "get_order_status":
                args = json.loads(tool_call.function.arguments)
                result = lookup_order(args["order_id"])  # Your function
                tool_outputs.append({
                    "tool_call_id": tool_call.id,
                    "output": json.dumps(result)
                })

            elif tool_call.function.name == "create_support_ticket":
                args = json.loads(tool_call.function.arguments)
                result = create_ticket(**args)  # Your function
                tool_outputs.append({
                    "tool_call_id": tool_call.id,
                    "output": json.dumps(result)
                })

        # Submit results back to the agent
        run = client.agents.submit_tool_outputs(
            thread_id=thread.id,
            run_id=run.id,
            tool_outputs=tool_outputs
        )
```

> ### 📝 Exam Tip
> Function calling follows a specific flow: **Agent decides to call a function** → **Run enters `requires_action` status** → **Your code executes the function** → **Submit results back** → **Agent continues**. The agent never executes your functions directly — it only generates the arguments.

---

## Multi-Agent Orchestration

### Pattern: Planner + Executor

```python
# Planner agent — breaks tasks into subtasks
planner = client.agents.create_agent(
    model="gpt-4o",
    name="planner",
    instructions="""You are a task planner. Given a complex request:
1. Break it into numbered subtasks
2. Specify which specialist should handle each subtask
3. Define the order and dependencies
Output as JSON: {"tasks": [{"id": 1, "description": "...", "specialist": "researcher|analyst|writer"}]}"""
)

# Specialist agents
researcher = client.agents.create_agent(
    model="gpt-4o",
    name="researcher",
    instructions="You research topics and gather facts.",
    tools=[{"type": "file_search"}]
)

analyst = client.agents.create_agent(
    model="gpt-4o",
    name="analyst",
    instructions="You analyze data and produce insights.",
    tools=[{"type": "code_interpreter"}]
)

writer = client.agents.create_agent(
    model="gpt-4o",
    name="writer",
    instructions="You write clear, professional reports based on provided facts and analysis."
)
```

### Orchestration Flow

```python
def orchestrate(user_request: str):
    # Step 1: Plan
    plan = run_agent(planner, user_request)
    tasks = json.loads(plan)["tasks"]

    results = {}
    for task in tasks:
        # Step 2: Route to specialist
        specialist = {
            "researcher": researcher,
            "analyst": analyst,
            "writer": writer
        }[task["specialist"]]

        # Include prior results as context
        context = f"Previous results: {json.dumps(results)}\n\nTask: {task['description']}"
        results[task["id"]] = run_agent(specialist, context)

    return results
```

### Microsoft Agent Framework

For more complex agent systems, Microsoft provides frameworks:

| Framework | Best For | Key Features |
|-----------|----------|-------------|
| **Foundry Agent Service** | Single agents, managed deployment | Built-in tools, managed infrastructure |
| **Semantic Kernel** | .NET/Python agent orchestration | Plugin system, planners, memory connectors |
| **AutoGen** | Multi-agent conversations | Agent-to-agent communication, code execution |

```python
# Semantic Kernel example
import semantic_kernel as sk
from semantic_kernel.agents import ChatCompletionAgent

agent = ChatCompletionAgent(
    service_id="gpt4o",
    kernel=kernel,
    name="support-agent",
    instructions="Help customers with their orders."
)

# Add plugins (tools)
kernel.add_plugin(OrderPlugin(), "orders")
kernel.add_plugin(TicketPlugin(), "tickets")
```

---

## Multi-User Scenarios

When agents serve multiple users simultaneously:

| Concern | Solution |
|---------|----------|
| **Data isolation** | Separate threads per user; user-scoped vector stores |
| **Authentication** | User identity passed via function calling context |
| **Rate limiting** | Per-user quotas; queue management |
| **Conversation history** | Thread-per-user; session management |
| **Personalization** | User profiles stored externally; loaded into system prompt |

```python
def get_or_create_user_thread(user_id: str) -> str:
    """Ensure each user has their own conversation thread."""
    thread_id = db.get_thread_for_user(user_id)
    if not thread_id:
        thread = client.agents.create_thread()
        db.save_thread_for_user(user_id, thread.id)
        thread_id = thread.id
    return thread_id
```

---

## Safety Guardrails

### Implementing Agent Safety

```python
agent = client.agents.create_agent(
    model="gpt-4o",
    name="safe-agent",
    instructions="""You are a helpful assistant with these safety rules:

BOUNDARIES:
- Never execute destructive operations (DELETE, DROP, etc.)
- Always confirm before making changes that affect production data
- If unsure, ask the user for clarification rather than guessing
- Never reveal internal system details, API keys, or credentials

ESCALATION:
- If the user requests something outside your capabilities, explain why and suggest alternatives
- If you detect potential security issues, flag them immediately

OUTPUT LIMITS:
- Maximum 1000 words per response
- Always cite sources when making factual claims
- Label generated content as AI-generated""",
    tools=[
        {
            "type": "function",
            "function": {
                "name": "execute_query",
                "description": "Execute a READ-ONLY database query. Only SELECT statements allowed.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "SQL SELECT query (no INSERT/UPDATE/DELETE)"
                        }
                    },
                    "required": ["query"]
                }
            }
        }
    ]
)
```

### Safety Checklist

```
Agent Safety Checklist:
├── Input Validation
│   ├── Content Safety filters on all user inputs
│   ├── Prompt shields for jailbreak detection
│   └── Input length limits
├── Tool Safety
│   ├── Read-only permissions where possible
│   ├── Rate limits on tool execution
│   ├── Sandboxed code execution (code interpreter)
│   └── Function allow-lists (not deny-lists)
├── Output Validation
│   ├── Content filters on generated responses
│   ├── PII detection before returning responses
│   └── Output length limits
└── Operational Safety
    ├── Maximum iterations per run
    ├── Timeout limits
    ├── Cost caps per user/session
    └── Human-in-the-loop for high-impact actions
```

> ### 📝 Exam Tip
> Agent safety is about **defense in depth**: validate inputs (prompt shields), restrict tools (least privilege), validate outputs (content filters), and limit autonomy (iteration caps, human approval for high-impact actions).

---

## Testing and Optimizing Agents

### Testing Strategies

| Test Type | What It Validates | Example |
|-----------|-------------------|---------|
| **Unit tests** | Individual tool functions work correctly | Order lookup returns expected data |
| **Integration tests** | Agent selects the right tool for a request | "Check my order" → calls `get_order_status` |
| **Scenario tests** | End-to-end agent workflows | Full customer service conversation |
| **Red team tests** | Agent resists manipulation | Jailbreak attempts, prompt injection |
| **Load tests** | Agent handles concurrent users | 100 simultaneous conversations |

### Evaluation Metrics for Agents

| Metric | Description |
|--------|-------------|
| **Task completion rate** | % of requests successfully resolved |
| **Tool selection accuracy** | % of times the agent chose the correct tool |
| **Steps to completion** | Average number of steps to resolve a request |
| **Latency** | Total time from request to final response |
| **Safety violations** | Number of guardrail triggers |
| **User satisfaction** | Feedback ratings on agent responses |

### Optimization Techniques

```python
# 1. Improve instructions for better tool selection
instructions = """
When to use each tool:
- get_order_status: When user asks about order status, tracking, delivery
- create_support_ticket: When an issue cannot be resolved immediately
- search_knowledge_base: For product questions, policies, FAQs

ALWAYS search the knowledge base before creating a ticket — the answer might be there.
"""

# 2. Add few-shot examples to instructions
instructions += """
Example interactions:
User: "Where's my order ORD-12345?"
→ Call get_order_status("ORD-12345")

User: "How do I return an item?"
→ Call search_knowledge_base("return policy")
"""
```

---

## Deploying Agents

### Deployment Options

| Option | Hosting | Best For |
|--------|---------|----------|
| **Foundry Agent Service** | Fully managed (Azure) | Production agents, enterprise workloads |
| **Azure Container Apps** | Container-based | Custom agent frameworks, microservices |
| **Azure Functions** | Serverless | Event-driven agent triggers |
| **Azure App Service** | Web app hosting | Agent APIs behind a web frontend |

### Production Deployment Checklist

```
Pre-deployment:
☐ All scenario tests pass
☐ Red team testing completed
☐ Content safety filters configured
☐ Rate limiting implemented
☐ Cost caps set per user/session
☐ Monitoring and alerting configured
☐ Logging for all agent interactions
☐ PII handling policy implemented
☐ Rollback plan documented

Post-deployment:
☐ Monitor task completion rate
☐ Track safety violation rate
☐ Review user feedback weekly
☐ Update instructions based on failure patterns
☐ Scale based on usage patterns
```

---

## Key Takeaways

1. **Agents** differ from chatbots and copilots by their ability to **plan, use tools, remember context, and act autonomously**.
2. **Foundry Agent Service** lifecycle: Create Agent → Create Thread → Add Messages → Create Run → Poll → Read Messages.
3. **Three built-in tools**: Code Interpreter (execute Python), File Search (RAG over documents), Function Calling (invoke your APIs).
4. **Function calling** flow: Agent generates arguments → Run enters `requires_action` → Your code executes → Submit results back.
5. **Multi-agent orchestration** uses patterns like Planner + Executor with specialized agents for different subtasks.
6. **Safety guardrails** require defense in depth: input validation, tool restrictions, output filtering, and operational limits.
7. **Testing agents** requires unit, integration, scenario, and red team testing — agent behavior is non-deterministic.

---

## Further Reading

- [Azure AI Agent Service](https://learn.microsoft.com/en-us/azure/ai-services/agents/)
- [Function calling](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/function-calling)
- [Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/)
- [AutoGen framework](https://microsoft.github.io/autogen/)
- [Responsible AI for agents](https://learn.microsoft.com/en-us/azure/ai-services/agents/concepts/safety)
