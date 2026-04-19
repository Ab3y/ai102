"""
AI-102 Lab 2.1: Azure OpenAI Chat Completions
===============================================
Exam Objective: Implement generative AI solutions with Azure OpenAI Service
  - Create chat completion requests
  - Configure model parameters (temperature, top_p, max_tokens)
  - Implement streaming responses
  - Design effective system messages

This script demonstrates:
  1. Non-streaming chat completion
  2. Streaming chat completion
  3. Parameter tuning (temperature, top_p, max_tokens)
  4. Multi-turn conversation with message roles

Prerequisites:
  - pip install openai python-dotenv
  - An Azure OpenAI resource with a GPT model deployed
  - .env file with AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_KEY, AZURE_OPENAI_DEPLOYMENT
"""

import os
from dotenv import load_dotenv
from openai import AzureOpenAI

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
load_dotenv()

ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
API_KEY = os.getenv("AZURE_OPENAI_KEY")
DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o")
API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-06-01")

if not ENDPOINT or not API_KEY:
    raise EnvironmentError(
        "Set AZURE_OPENAI_ENDPOINT and AZURE_OPENAI_KEY in your .env file."
    )

# Create the AzureOpenAI client
client = AzureOpenAI(
    azure_endpoint=ENDPOINT,
    api_key=API_KEY,
    api_version=API_VERSION,
)


# ===========================================================================
# 1. Non-streaming chat completion
# ===========================================================================
def non_streaming_chat():
    """
    Standard (non-streaming) chat completion.
    The full response is returned once generation is complete.

    EXAM TIP: Message roles –
      system:    Sets the assistant's behavior/persona
      user:      The human's input
      assistant: Previous assistant responses (for multi-turn context)
    """
    print("=" * 60)
    print("1. NON-STREAMING CHAT COMPLETION")
    print("=" * 60)

    messages = [
        {
            "role": "system",
            "content": (
                "You are an Azure AI expert helping students prepare for the "
                "AI-102 certification exam. Keep answers concise and accurate."
            ),
        },
        {
            "role": "user",
            "content": "What is the difference between Azure AI Services and Azure OpenAI Service?",
        },
    ]

    try:
        response = client.chat.completions.create(
            model=DEPLOYMENT,
            messages=messages,
            temperature=0.7,    # Controls randomness (0=deterministic, 2=very random)
            max_tokens=300,     # Maximum tokens in the response
            top_p=0.95,         # Nucleus sampling (alternative to temperature)
        )

        # Extract the response
        answer = response.choices[0].message.content
        usage = response.usage

        print(f"\n  Response:\n  {answer}\n")
        print(f"  Token usage:")
        print(f"    Prompt tokens:     {usage.prompt_tokens}")
        print(f"    Completion tokens: {usage.completion_tokens}")
        print(f"    Total tokens:      {usage.total_tokens}")

    except Exception as exc:
        print(f"  Error: {exc}")


# ===========================================================================
# 2. Streaming chat completion
# ===========================================================================
def streaming_chat():
    """
    Streaming returns tokens incrementally as they are generated.
    This is useful for real-time UIs where you want to display partial output.
    """
    print("\n" + "=" * 60)
    print("2. STREAMING CHAT COMPLETION")
    print("=" * 60)

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. Be brief.",
        },
        {
            "role": "user",
            "content": "List three benefits of using managed identity with Azure AI Services.",
        },
    ]

    try:
        print("\n  Streaming response:\n  ", end="")

        stream = client.chat.completions.create(
            model=DEPLOYMENT,
            messages=messages,
            temperature=0.5,
            max_tokens=200,
            stream=True,  # Enable streaming
        )

        # Each chunk contains a delta with partial content
        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="", flush=True)

        print("\n")

    except Exception as exc:
        print(f"\n  Error: {exc}")


# ===========================================================================
# 3. Parameter comparison
# ===========================================================================
def parameter_comparison():
    """
    Demonstrate how temperature affects output randomness.

    EXAM TIP:
      - temperature: 0 → deterministic, 2 → very random (default ~1)
      - top_p: nucleus sampling, 0.1 → only top 10% probability mass
      - max_tokens: hard cap on response length
      - Don't set both temperature AND top_p to extreme values together.
      - frequency_penalty: reduces repetition of tokens already used
      - presence_penalty: encourages the model to talk about new topics
    """
    print("=" * 60)
    print("3. PARAMETER COMPARISON (temperature effect)")
    print("=" * 60)

    prompt = "Give me a one-sentence creative description of cloud computing."
    temperatures = [0.0, 1.0, 1.5]

    for temp in temperatures:
        try:
            response = client.chat.completions.create(
                model=DEPLOYMENT,
                messages=[
                    {"role": "system", "content": "Be creative."},
                    {"role": "user", "content": prompt},
                ],
                temperature=temp,
                max_tokens=60,
            )
            answer = response.choices[0].message.content.strip()
            print(f"\n  temperature={temp}:")
            print(f"    {answer}")

        except Exception as exc:
            print(f"\n  temperature={temp}: Error – {exc}")


# ===========================================================================
# 4. Multi-turn conversation
# ===========================================================================
def multi_turn_conversation():
    """
    Shows how to maintain conversation context by passing the full
    message history with each request.

    EXAM TIP: The model is stateless – you must send the full conversation
    history each time. Token limits apply to input + output combined.
    """
    print("\n" + "=" * 60)
    print("4. MULTI-TURN CONVERSATION")
    print("=" * 60)

    messages = [
        {"role": "system", "content": "You are a quiz master for Azure AI certifications."},
        {"role": "user", "content": "Ask me a question about Azure AI Services."},
    ]

    try:
        # Turn 1: Get the question
        response = client.chat.completions.create(
            model=DEPLOYMENT, messages=messages, max_tokens=150
        )
        assistant_msg = response.choices[0].message.content
        print(f"\n  Assistant: {assistant_msg}")

        # Add assistant response to history for context
        messages.append({"role": "assistant", "content": assistant_msg})

        # Turn 2: User answers
        user_answer = "I think the answer is managed identity."
        messages.append({"role": "user", "content": user_answer})
        print(f"  User: {user_answer}")

        response = client.chat.completions.create(
            model=DEPLOYMENT, messages=messages, max_tokens=150
        )
        assistant_msg = response.choices[0].message.content
        print(f"  Assistant: {assistant_msg}\n")

    except Exception as exc:
        print(f"  Error: {exc}")


# ===========================================================================
# Main
# ===========================================================================
if __name__ == "__main__":
    print("\nAI-102 Lab 2.1 – Azure OpenAI Chat Completions\n")

    non_streaming_chat()
    streaming_chat()
    parameter_comparison()
    multi_turn_conversation()

    # EXAM TIPS SUMMARY:
    # ──────────────────
    # • Use AzureOpenAI client (not plain OpenAI) for Azure deployments.
    # • api_version is required – check docs for the latest stable version.
    # • model parameter = your deployment name, NOT the model name.
    # • System message sets behavior; it's processed but not shown to users.
    # • Token limits vary by model (GPT-4o: 128K context, 4K default output).
    # • Content filters may block requests/responses (see content-safety lab).
    # • Streaming uses SSE (Server-Sent Events) under the hood.

    # CLEANUP NOTE:
    # Azure OpenAI charges per token. Delete deployments when not in use.
