"""
AI-102 Lab 6.1: Query Azure AI Search Index
=============================================
Exam Objective: Implement knowledge mining and document intelligence
  - Execute search queries
  - Apply filters, facets, and sorting
  - Implement vector and hybrid search

This script demonstrates:
  1. Full-text search with highlights
  2. Filters ($filter), select ($select), orderby ($orderby)
  3. Faceted search
  4. Vector search
  5. Hybrid search (keyword + vector)

Prerequisites:
  - pip install azure-search-documents openai python-dotenv
  - An Azure AI Search index with documents (see create-index.py)
  - .env file with AZURE_SEARCH_ENDPOINT, AZURE_SEARCH_KEY, AZURE_SEARCH_INDEX
"""

import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import (
    VectorizedQuery,
    QueryType,
)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
load_dotenv()

SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_ENDPOINT")
SEARCH_KEY = os.getenv("AZURE_SEARCH_KEY")
INDEX_NAME = os.getenv("AZURE_SEARCH_INDEX", "ai102-lab-index")

# For vector search: Azure OpenAI embedding model
OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
EMBEDDING_DEPLOYMENT = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT", "text-embedding-ada-002")

if not SEARCH_ENDPOINT or not SEARCH_KEY:
    raise EnvironmentError(
        "Set AZURE_SEARCH_ENDPOINT and AZURE_SEARCH_KEY in your .env file."
    )

search_client = SearchClient(
    endpoint=SEARCH_ENDPOINT,
    index_name=INDEX_NAME,
    credential=AzureKeyCredential(SEARCH_KEY),
)


# ===========================================================================
# Helper: Generate embedding vector
# ===========================================================================
def get_embedding(text: str) -> list[float]:
    """Generate an embedding vector using Azure OpenAI."""
    if not OPENAI_ENDPOINT or not OPENAI_KEY:
        print("    ⚠️  OpenAI not configured – using zero vector placeholder.")
        return [0.0] * 1536

    from openai import AzureOpenAI

    client = AzureOpenAI(
        azure_endpoint=OPENAI_ENDPOINT,
        api_key=OPENAI_KEY,
        api_version="2024-06-01",
    )

    response = client.embeddings.create(
        model=EMBEDDING_DEPLOYMENT,
        input=text,
    )
    return response.data[0].embedding


# ===========================================================================
# 1. Full-text search
# ===========================================================================
def full_text_search():
    """
    Basic full-text search with result highlights.

    EXAM TIP: Full-text search uses the Lucene query syntax by default.
    query_type="full" enables the full Lucene syntax (wildcards, regex, etc.).
    query_type="simple" is the default (AND, OR, NOT, phrases).
    """
    print("=" * 60)
    print("1. FULL-TEXT SEARCH")
    print("=" * 60)

    try:
        results = search_client.search(
            search_text="Azure AI services managed identity",
            query_type=QueryType.SIMPLE,
            include_total_count=True,
            highlight_fields="content",
            top=5,
            select=["id", "title", "category", "rating"],
        )

        print(f"\n  Total matching documents: {results.get_count()}")

        for result in results:
            print(f"\n    Title:    {result.get('title', 'N/A')}")
            print(f"    Category: {result.get('category', 'N/A')}")
            print(f"    Rating:   {result.get('rating', 'N/A')}")
            print(f"    Score:    {result['@search.score']:.4f}")

            # Show highlighted snippets
            highlights = result.get("@search.highlights", {})
            if "content" in highlights:
                print(f"    Highlight: {highlights['content'][0][:80]}...")

    except Exception as exc:
        print(f"  Error: {exc}")


# ===========================================================================
# 2. Filters, select, and orderby
# ===========================================================================
def filtered_search():
    """
    Apply OData filters, field selection, and sorting.

    EXAM TIP: OData filter syntax –
      Comparison: eq, ne, gt, ge, lt, le
      Logical:    and, or, not
      Functions:  search.in(), search.ismatch()
      Collections: any(), all()
      Geo:        geo.distance(), geo.intersects()

    Examples:
      $filter=rating ge 4.0
      $filter=category eq 'Documentation'
      $filter=tags/any(t: t eq 'python')
      $filter=lastUpdated ge 2024-01-01T00:00:00Z
    """
    print("\n" + "=" * 60)
    print("2. FILTERED SEARCH ($filter, $select, $orderby)")
    print("=" * 60)

    try:
        # Search with filter, select, and orderby
        results = search_client.search(
            search_text="*",                    # Match all documents
            filter="rating ge 4.0",             # Only high-rated docs
            select=["title", "category", "rating", "lastUpdated"],
            order_by=["rating desc", "title asc"],  # Sort by rating descending
            top=10,
            include_total_count=True,
        )

        print(f"\n  Filter: rating ge 4.0")
        print(f"  Total matches: {results.get_count()}")

        for result in results:
            print(
                f"    {result.get('title', 'N/A'):<30} "
                f"category={result.get('category', 'N/A'):<15} "
                f"rating={result.get('rating', 0)}"
            )

    except Exception as exc:
        print(f"  Error: {exc}")

    # Demonstrate collection filter
    try:
        print(f"\n  Filter: tags/any(t: t eq 'python')")
        results = search_client.search(
            search_text="*",
            filter="tags/any(t: t eq 'python')",
            select=["title", "tags"],
            top=5,
        )

        for result in results:
            tags = result.get("tags", [])
            print(f"    {result.get('title', 'N/A'):<30} tags={tags}")

    except Exception as exc:
        print(f"  Error: {exc}")


# ===========================================================================
# 3. Faceted search
# ===========================================================================
def faceted_search():
    """
    Use facets for aggregated counts (like category filters on e-commerce sites).

    EXAM TIP: Facets return distinct values and counts for a field.
    The field must have facetable=True in the index definition.
    """
    print("\n" + "=" * 60)
    print("3. FACETED SEARCH")
    print("=" * 60)

    try:
        results = search_client.search(
            search_text="*",
            facets=["category,count:10", "rating,values:1|2|3|4|5"],
            top=0,  # We only want facets, not results
        )

        facets = results.get_facets()

        if facets:
            for facet_name, facet_values in facets.items():
                print(f"\n  Facet: {facet_name}")
                for fv in facet_values:
                    print(f"    {fv.get('value', 'N/A')}: {fv.get('count', 0)} documents")
        else:
            print("  No facets returned (index may be empty).")

    except Exception as exc:
        print(f"  Error: {exc}")


# ===========================================================================
# 4. Vector search
# ===========================================================================
def vector_search():
    """
    Pure vector search – finds semantically similar documents.

    EXAM TIP: Vector search requires:
      1. A vector field in the index (Collection(Edm.Single))
      2. Documents indexed with embedding vectors
      3. A query vector (same dimensions as indexed vectors)
    """
    print("\n" + "=" * 60)
    print("4. VECTOR SEARCH")
    print("=" * 60)

    query = "How to secure Azure AI services with managed identity"

    try:
        # Generate embedding for the query
        query_vector = get_embedding(query)

        results = search_client.search(
            search_text=None,  # No keyword search – pure vector
            vector_queries=[
                VectorizedQuery(
                    vector=query_vector,
                    k_nearest_neighbors=5,       # Number of results
                    fields="contentVector",       # Vector field name
                ),
            ],
            select=["id", "title", "category"],
        )

        print(f"\n  Query: \"{query}\"")
        for result in results:
            print(
                f"    {result.get('title', 'N/A'):<30} "
                f"score={result['@search.score']:.4f}"
            )

    except Exception as exc:
        print(f"  Error: {exc}")


# ===========================================================================
# 5. Hybrid search (keyword + vector)
# ===========================================================================
def hybrid_search():
    """
    Combine keyword and vector search for best results.

    EXAM TIP: Hybrid search uses Reciprocal Rank Fusion (RRF) to merge
    results from keyword and vector search. This often outperforms either
    approach alone.
    """
    print("\n" + "=" * 60)
    print("5. HYBRID SEARCH (keyword + vector)")
    print("=" * 60)

    query = "managed identity authentication for AI services"

    try:
        query_vector = get_embedding(query)

        results = search_client.search(
            search_text=query,                    # Keyword component
            vector_queries=[
                VectorizedQuery(
                    vector=query_vector,
                    k_nearest_neighbors=5,
                    fields="contentVector",
                ),
            ],
            query_type=QueryType.SEMANTIC,        # Add semantic re-ranking
            semantic_configuration_name="default",
            select=["id", "title", "category", "rating"],
            top=5,
        )

        print(f"\n  Hybrid query: \"{query}\"")
        for result in results:
            reranker_score = result.get("@search.reranker_score", "N/A")
            print(
                f"    {result.get('title', 'N/A'):<30} "
                f"score={result['@search.score']:.4f}  "
                f"reranker={reranker_score}"
            )

    except Exception as exc:
        print(f"  Error: {exc}")


# ===========================================================================
# Main
# ===========================================================================
if __name__ == "__main__":
    print("\nAI-102 Lab 6.1 – Query Azure AI Search\n")

    full_text_search()
    filtered_search()
    faceted_search()
    vector_search()
    hybrid_search()

    # EXAM TIPS:
    # ──────────
    # • query_type: "simple" (default), "full" (Lucene), "semantic".
    # • $filter uses OData syntax, not Lucene syntax.
    # • Facets require facetable=True on the field.
    # • Vector search: k_nearest_neighbors controls result count.
    # • Hybrid = keyword + vector, merged with Reciprocal Rank Fusion (RRF).
    # • Semantic ranking re-ranks the top results using a language model.
    # • Semantic captions and answers extract relevant snippets.
    # • Scoring profiles can boost results based on field values.
    # • search.in() is efficient for multi-value exact matching.

    # CLEANUP NOTE:
    # Search queries are charged per 1,000 queries (depending on tier).
    # Delete the index/resource when no longer needed.
