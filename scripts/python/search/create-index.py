"""
AI-102 Lab 6.1: Create an Azure AI Search Index
=================================================
Exam Objective: Implement knowledge mining and document intelligence
  - Create an Azure AI Search index
  - Define fields with proper attributes
  - Configure a data source and indexer
  - Add vector search configuration

This script demonstrates:
  1. Creating a search index with typed fields
  2. Field attributes (searchable, filterable, sortable, facetable)
  3. Vector field configuration for vector/hybrid search
  4. Creating a data source connection
  5. Creating an indexer with optional skillset

Prerequisites:
  - pip install azure-search-documents python-dotenv
  - An Azure AI Search resource
  - .env file with AZURE_SEARCH_ENDPOINT and AZURE_SEARCH_KEY
"""

import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient, SearchIndexerClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SearchField,
    SearchFieldDataType,
    SimpleField,
    SearchableField,
    ComplexField,
    SearchIndex,
    VectorSearch,
    HnswAlgorithmConfiguration,
    VectorSearchProfile,
    SearchIndexerDataContainer,
    SearchIndexerDataSourceConnection,
    SearchIndexer,
    FieldMapping,
    SemanticConfiguration,
    SemanticSearch,
    SemanticPrioritizedFields,
    SemanticField,
)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
load_dotenv()

SEARCH_ENDPOINT = os.getenv("AZURE_SEARCH_ENDPOINT")
SEARCH_KEY = os.getenv("AZURE_SEARCH_KEY")
INDEX_NAME = os.getenv("AZURE_SEARCH_INDEX", "ai102-lab-index")

if not SEARCH_ENDPOINT or not SEARCH_KEY:
    raise EnvironmentError(
        "Set AZURE_SEARCH_ENDPOINT and AZURE_SEARCH_KEY in your .env file."
    )

credential = AzureKeyCredential(SEARCH_KEY)


# ===========================================================================
# 1. Create a search index with fields
# ===========================================================================
def create_search_index():
    """
    Create a search index with various field types and attributes.

    EXAM TIP: Field attributes –
      searchable: included in full-text search (strings only)
      filterable: used in $filter expressions
      sortable:   used in $orderby expressions
      facetable:  used for faceted navigation / aggregation
      retrievable: returned in search results (default: True)
      key:        unique document identifier (exactly one per index)

    Data types: Edm.String, Edm.Int32, Edm.Int64, Edm.Double,
    Edm.Boolean, Edm.DateTimeOffset, Edm.GeographyPoint,
    Collection(Edm.String), Collection(Edm.Single) for vectors
    """
    print("=" * 60)
    print("1. CREATE SEARCH INDEX")
    print("=" * 60)

    # Define fields
    fields = [
        # Key field – every index must have exactly one
        SimpleField(
            name="id",
            type=SearchFieldDataType.String,
            key=True,
            filterable=True,
        ),
        # Searchable text fields
        SearchableField(
            name="title",
            type=SearchFieldDataType.String,
            filterable=True,
            sortable=True,
        ),
        SearchableField(
            name="content",
            type=SearchFieldDataType.String,
            analyzer_name="en.microsoft",  # Language-specific analyzer
        ),
        SearchableField(
            name="category",
            type=SearchFieldDataType.String,
            filterable=True,
            facetable=True,
        ),
        # Numeric and date fields
        SimpleField(
            name="rating",
            type=SearchFieldDataType.Double,
            filterable=True,
            sortable=True,
            facetable=True,
        ),
        SimpleField(
            name="lastUpdated",
            type=SearchFieldDataType.DateTimeOffset,
            filterable=True,
            sortable=True,
        ),
        # Collection field (multi-value)
        SearchableField(
            name="tags",
            type=SearchFieldDataType.Collection(SearchFieldDataType.String),
            filterable=True,
            facetable=True,
        ),
        # Vector field for vector/hybrid search
        SearchField(
            name="contentVector",
            type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
            searchable=True,
            vector_search_dimensions=1536,  # Must match embedding model output
            vector_search_profile_name="vector-profile",
        ),
        # URL field (retrievable but not searchable)
        SimpleField(
            name="url",
            type=SearchFieldDataType.String,
            filterable=False,
        ),
    ]

    # Configure vector search
    vector_search = VectorSearch(
        algorithms=[
            HnswAlgorithmConfiguration(
                name="hnsw-config",
                # HNSW parameters (defaults are usually fine)
            ),
        ],
        profiles=[
            VectorSearchProfile(
                name="vector-profile",
                algorithm_configuration_name="hnsw-config",
            ),
        ],
    )

    # Configure semantic search
    semantic_config = SemanticConfiguration(
        name="default",
        prioritized_fields=SemanticPrioritizedFields(
            title_field=SemanticField(field_name="title"),
            content_fields=[SemanticField(field_name="content")],
            keywords_fields=[SemanticField(field_name="tags")],
        ),
    )

    semantic_search = SemanticSearch(configurations=[semantic_config])

    # Create the index
    index = SearchIndex(
        name=INDEX_NAME,
        fields=fields,
        vector_search=vector_search,
        semantic_search=semantic_search,
    )

    index_client = SearchIndexClient(SEARCH_ENDPOINT, credential)

    try:
        result = index_client.create_or_update_index(index)
        print(f"  ✅ Index created/updated: {result.name}")
        print(f"  Fields: {len(result.fields)}")
        for field in result.fields:
            attrs = []
            if field.key:
                attrs.append("key")
            if field.searchable:
                attrs.append("searchable")
            if field.filterable:
                attrs.append("filterable")
            if field.sortable:
                attrs.append("sortable")
            if field.facetable:
                attrs.append("facetable")
            print(f"    {field.name:<20} {field.type:<35} [{', '.join(attrs)}]")

    except Exception as exc:
        print(f"  Error: {exc}")


# ===========================================================================
# 2. Create a data source connection
# ===========================================================================
def create_data_source():
    """
    Create a data source connection for the indexer.

    EXAM TIP: Supported data sources –
      - Azure Blob Storage (most common)
      - Azure SQL Database
      - Azure Cosmos DB
      - Azure Table Storage
      - SharePoint Online (preview)
    """
    print("\n" + "=" * 60)
    print("2. CREATE DATA SOURCE CONNECTION")
    print("=" * 60)

    # Connection string for Azure Blob Storage (from .env)
    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    container_name = os.getenv("AZURE_STORAGE_CONTAINER", "documents")

    if not connection_string:
        print("  Skipped – AZURE_STORAGE_CONNECTION_STRING not set.")
        print("  Set this variable to connect to your Blob Storage container.\n")
        return

    indexer_client = SearchIndexerClient(SEARCH_ENDPOINT, credential)

    data_source = SearchIndexerDataSourceConnection(
        name=f"{INDEX_NAME}-datasource",
        type="azureblob",
        connection_string=connection_string,
        container=SearchIndexerDataContainer(
            name=container_name,
            query=None,  # Optional: subfolder path
        ),
    )

    try:
        result = indexer_client.create_or_update_data_source_connection(data_source)
        print(f"  ✅ Data source created: {result.name}")
        print(f"  Type: {result.type}")
        print(f"  Container: {container_name}")

    except Exception as exc:
        print(f"  Error: {exc}")


# ===========================================================================
# 3. Create an indexer
# ===========================================================================
def create_indexer():
    """
    Create an indexer that pulls data from the data source into the index.

    EXAM TIP: Indexers can run on a schedule or be triggered manually.
    Field mappings map source fields to index fields.
    Output field mappings map enriched fields from skillsets.
    """
    print("\n" + "=" * 60)
    print("3. CREATE INDEXER")
    print("=" * 60)

    connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    if not connection_string:
        print("  Skipped – data source not configured.\n")
        return

    indexer_client = SearchIndexerClient(SEARCH_ENDPOINT, credential)

    indexer = SearchIndexer(
        name=f"{INDEX_NAME}-indexer",
        data_source_name=f"{INDEX_NAME}-datasource",
        target_index_name=INDEX_NAME,
        field_mappings=[
            # Map source fields to index fields if names differ
            FieldMapping(source_field_name="metadata_storage_path", target_field_name="id"),
            FieldMapping(source_field_name="metadata_storage_name", target_field_name="title"),
        ],
        # schedule: run every hour (ISO 8601 duration)
        # schedule={"interval": "PT1H"},
    )

    try:
        result = indexer_client.create_or_update_indexer(indexer)
        print(f"  ✅ Indexer created: {result.name}")
        print(f"  Data source: {result.data_source_name}")
        print(f"  Target index: {result.target_index_name}")

        # Run the indexer immediately
        indexer_client.run_indexer(result.name)
        print("  🔄 Indexer run triggered.")

    except Exception as exc:
        print(f"  Error: {exc}")


# ===========================================================================
# Main
# ===========================================================================
if __name__ == "__main__":
    print("\nAI-102 Lab 6.1 – Create Azure AI Search Index\n")

    create_search_index()
    create_data_source()
    create_indexer()

    # EXAM TIPS:
    # ──────────
    # • Every index needs exactly one key field (Edm.String).
    # • searchable applies only to Edm.String fields.
    # • Analyzers: standard.lucene (default), language-specific (en.microsoft).
    # • Vector fields: Collection(Edm.Single), dimensions must match embeddings.
    # • HNSW is the default vector search algorithm.
    # • Semantic search re-ranks results using a language understanding model.
    # • Indexers support scheduling (ISO 8601 interval, e.g., "PT1H").
    # • Skillsets add AI enrichment (OCR, entity extraction, translation, etc.).
    # • Field mappings: source → index; output field mappings: skillset → index.
    # • Blob indexer: extracts content and metadata automatically.

    # CLEANUP NOTE:
    # Delete the index, data source, and indexer when done:
    #   index_client.delete_index(INDEX_NAME)
    #   indexer_client.delete_data_source_connection(f"{INDEX_NAME}-datasource")
    #   indexer_client.delete_indexer(f"{INDEX_NAME}-indexer")
