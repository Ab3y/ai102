"""
AI-102 Lab 2.2: RAG (Retrieval-Augmented Generation) Pattern
=============================================================
Exam Objective: Implement generative AI solutions with Azure OpenAI Service
  - Implement Retrieval-Augmented Generation (RAG)
  - Use your own data with Azure OpenAI
  - Configure Azure AI Search as a data source

This script demonstrates the full RAG flow:
  1. QUERY  – Accept a user question
  2. RETRIEVE – Search Azure AI Search for relevant documents
  3. AUGMENT – Build a grounded prompt with retrieved context
  4. GENERATE – Call Azure OpenAI to produce a grounded answer

Prerequisites:
  - pip install openai azure-search-documents python-dotenv
  - An Azure AI Search index with documents
  - An Azure OpenAI resource with a GPT model deployed
  - .env file with the required variables (see below)
"""

import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizableTextQuery

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
load_dotenv()

# Azure OpenAI settings
OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o")
OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-06-01")

# Azure AI Search settings
SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_ENDPOINT")
SEARCH_KEY = os.getenv("AZURE_SEARCH_KEY")
SEARCH_INDEX = os.getenv("AZURE_SEARCH_INDEX", "ai102-docs-index")

for var_name, var_val in [
    ("AZURE_OPENAI_ENDPOINT", OPENAI_ENDPOINT),
    ("AZURE_OPENAI_KEY", OPENAI_KEY),
    ("AZURE_SEARCH_ENDPOINT", SEARCH_ENDPOINT),
    ("AZURE_SEARCH_KEY", SEARCH_KEY),
]:
    if not var_val:
        raise EnvironmentError(f"Set {var_name} in your .env file.")


# ===========================================================================
# Step 1: RETRIEVE – Search for relevant documents
# ===========================================================================
def retrieve_documents(query: str, top_k: int = 3) -> list[dict]:
    """
    Search the Azure AI Search index for documents relevant to the query.
    Returns a list of dicts with 'content', 'title', and 'score'.
    """
    print(f"  🔍 Searching index '{SEARCH_INDEX}' for: \"{query}\"")

    search_client = SearchClient(
        endpoint=SEARCH_ENDPOINT,
        index_name=SEARCH_INDEX,
        credential=AzureKeyCredential(SEARCH_KEY),
    )

    try:
        results = search_client.search(
            search_text=query,
            top=top_k,
            select=["title", "content", "url"],
            query_type="semantic",              # Use semantic ranking if configured
            semantic_configuration_name="default",
        )

        documents = []
        for result in results:
            documents.append({
                "title": result.get("title", "Untitled"),
                "content": result.get("content", "")[:1000],  # Truncate for prompt
                "url": result.get("url", ""),
                "score": result.get("@search.score", 0),
            })
            print(f"    📄 {result.get('title', 'Untitled')} (score: {result.get('@search.score', 0):.4f})")

        return documents

    except Exception as exc:
        print(f"  Search error: {exc}")
        print("  Hint: Ensure the search index exists and has semantic config.")
        # Return empty list to demonstrate the pattern even without live search
        return []


# ===========================================================================
# Step 2: AUGMENT – Build grounded prompt with context
# ===========================================================================
def build_grounded_prompt(query: str, documents: list[dict]) -> list[dict]:
    """
    Construct the chat messages with retrieved documents as context.

    EXAM TIP: The system message should instruct the model to:
      - Only use provided context
      - Cite sources
      - Say "I don't know" if context is insufficient
    """
    # Format retrieved documents into a context block
    context_parts = []
    for i, doc in enumerate(documents, 1):
        context_parts.append(
            f"[Source {i}: {doc['title']}]\n{doc['content']}\n"
        )
    context = "\n".join(context_parts) if context_parts else "No documents found."

    system_message = (
        "You are an AI assistant that answers questions based ONLY on the "
        "provided context documents. Follow these rules:\n"
        "1. Only use information from the provided context.\n"
        "2. If the context doesn't contain the answer, say 'I don't have "
        "enough information to answer that.'\n"
        "3. Cite your sources using [Source N] notation.\n"
        "4. Be concise and accurate.\n\n"
        f"Context documents:\n{context}"
    )

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": query},
    ]

    print(f"\n  📝 Prompt built with {len(documents)} context documents.")
    return messages


# ===========================================================================
# Step 3: GENERATE – Call Azure OpenAI for grounded response
# ===========================================================================
def generate_response(messages: list[dict]) -> str:
    """Generate a grounded response using Azure OpenAI."""
    print("  🤖 Generating response...")

    client = AzureOpenAI(
        azure_endpoint=OPENAI_ENDPOINT,
        api_key=OPENAI_KEY,
        api_version=OPENAI_API_VERSION,
    )

    try:
        response = client.chat.completions.create(
            model=OPENAI_DEPLOYMENT,
            messages=messages,
            temperature=0.3,    # Low temperature for factual responses
            max_tokens=500,
        )

        answer = response.choices[0].message.content
        usage = response.usage
        print(f"  Token usage: {usage.prompt_tokens} prompt + {usage.completion_tokens} completion")
        return answer

    except Exception as exc:
        return f"Generation error: {exc}"


# ===========================================================================
# Full RAG Flow
# ===========================================================================
def rag_query(user_question: str):
    """Execute the full RAG pipeline: retrieve → augment → generate."""
    print(f"\n{'=' * 60}")
    print(f"RAG QUERY: \"{user_question}\"")
    print("=" * 60)

    # Step 1: Retrieve
    documents = retrieve_documents(user_question)

    # Step 2: Augment
    messages = build_grounded_prompt(user_question, documents)

    # Step 3: Generate
    answer = generate_response(messages)

    print(f"\n  Answer:\n  {answer}\n")
    return answer


# ===========================================================================
# Alternative: Azure OpenAI "On Your Data" (built-in RAG)
# ===========================================================================
def builtin_rag():
    """
    Azure OpenAI's "On Your Data" feature performs RAG internally.
    You point it at an Azure AI Search index and it handles retrieval.

    EXAM TIP: This is the easiest way to implement RAG but offers
    less control over the retrieval step compared to custom RAG.
    """
    print("=" * 60)
    print("ALTERNATIVE: Azure OpenAI 'On Your Data' (built-in RAG)")
    print("=" * 60)

    client = AzureOpenAI(
        azure_endpoint=OPENAI_ENDPOINT,
        api_key=OPENAI_KEY,
        api_version="2024-06-01",
    )

    try:
        response = client.chat.completions.create(
            model=OPENAI_DEPLOYMENT,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "What Azure AI services are available?"},
            ],
            extra_body={
                "data_sources": [
                    {
                        "type": "azure_search",
                        "parameters": {
                            "endpoint": SEARCH_ENDPOINT,
                            "index_name": SEARCH_INDEX,
                            "authentication": {
                                "type": "api_key",
                                "key": SEARCH_KEY,
                            },
                        },
                    }
                ]
            },
            max_tokens=300,
        )

        answer = response.choices[0].message.content
        print(f"\n  Response: {answer}\n")

        # Citations are included in the response context
        if hasattr(response.choices[0].message, "context"):
            print("  Citations available in response.choices[0].message.context")

    except Exception as exc:
        print(f"  Error: {exc}")
        print("  This is expected if the search index is not configured.\n")


# ===========================================================================
# Main
# ===========================================================================
if __name__ == "__main__":
    print("\nAI-102 Lab 2.2 – RAG (Retrieval-Augmented Generation)\n")

    # Custom RAG flow
    rag_query("How do I configure managed identity for Azure AI Services?")

    # Built-in RAG
    builtin_rag()

    # EXAM TIPS:
    # ──────────
    # • RAG = Retrieve + Augment + Generate (three-step pattern).
    # • Grounding reduces hallucination by constraining the model to context.
    # • Azure AI Search supports keyword, vector, and hybrid search.
    # • Semantic ranking re-ranks results using a language model.
    # • "On Your Data" is Azure's built-in RAG – simpler but less flexible.
    # • System message should instruct: use only context, cite sources.
    # • Low temperature (0.1–0.3) is preferred for factual RAG responses.
    # • Chunk size matters: too large wastes tokens, too small loses context.

    # CLEANUP NOTE:
    # Charges apply for both Azure OpenAI (per token) and Azure AI Search
    # (per hour, based on tier). Delete resources when no longer needed.
