# Lesson 1: Azure AI Search

## Learning Objectives

After completing this lesson, you will be able to:

- Provision Azure AI Search and select the appropriate service tier
- Create search indexes with properly configured field attributes
- Configure data sources and indexers for pull-based data ingestion
- Build skillsets using built-in and custom skills for AI enrichment
- Create knowledge store projections for downstream analytics
- Write effective search queries using simple and full Lucene syntax
- Implement semantic ranking for improved relevance
- Configure vector search and hybrid search for AI-powered retrieval

---

## 1. Provision Azure AI Search

Azure AI Search (formerly Azure Cognitive Search) is a fully managed cloud search service that provides AI-powered indexing and querying over heterogeneous content. It supports full-text search, vector search, semantic ranking, and AI enrichment pipelines.

### Service Tiers

Azure AI Search offers several pricing tiers. Choosing the right tier depends on your workload requirements, data volume, and availability needs.

| Feature | Free | Basic | S1 (Standard) | S2 (Standard) | S3 (Standard) | S3 HD | L1 (Storage Optimized) | L2 (Storage Optimized) |
|---------|------|-------|----------------|----------------|----------------|-------|------------------------|------------------------|
| **Max Indexes** | 3 | 15 | 50 | 200 | 200 | 1000 | 10 | 10 |
| **Max Indexers** | 3 | 15 | 50 | 200 | 200 | — | 10 | 10 |
| **Max Skillsets** | 3 | 15 | 50 | 200 | 200 | — | 10 | 10 |
| **Storage per Partition** | 50 MB | 2 GB | 25 GB | 100 GB | 200 GB | 200 GB | 1 TB | 2 TB |
| **Max Partitions** | — | 1 | 12 | 12 | 12 | 3 | 12 | 12 |
| **Max Replicas** | — | 3 | 12 | 12 | 12 | 12 | 12 | 12 |
| **SLA** | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes |

### SLA and Replica Requirements

Understanding replica requirements for SLA is critical for the exam:

| Scenario | Minimum Replicas | SLA |
|----------|-----------------|-----|
| Query (read) workloads | **2 replicas** | 99.9% |
| Query and indexing (read/write) workloads | **3 replicas** | 99.9% |
| Single replica | 1 | No SLA |

> **EXAM TIP:** You need **2 replicas** for a read SLA (queries only) and **3 replicas** for a read/write SLA (queries + indexing). The Free tier has no SLA regardless. This is a very commonly tested concept.

### When to Choose Each Tier

- **Free** — Learning, prototyping, very small datasets. No SLA, limited resources.
- **Basic** — Small-scale production workloads with modest search requirements.
- **S1/S2/S3** — Production workloads requiring more indexes, documents, and higher throughput.
- **S3 HD** — Multi-tenant scenarios with very many small indexes (up to 1000).
- **L1/L2 (Storage Optimized)** — Large data volumes where storage is the primary constraint (e.g., log analytics, archiving).

---

## 2. Create an Index

A search index is the primary data structure in Azure AI Search. It defines the schema for your searchable content—similar to a table in a database.

### Index Fields

Every index requires a set of fields, each with:

- **name** — Field identifier (alphanumeric, must start with a letter)
- **type** — Data type (see below)
- **key** — One field must be marked as the document key (unique identifier)

### Field Types

| Type | Description | Example Use |
|------|-------------|-------------|
| `Edm.String` | Text/string data | Titles, descriptions, content |
| `Edm.Int32` | 32-bit integer | Counts, ratings |
| `Edm.Int64` | 64-bit integer | Large numeric IDs |
| `Edm.Double` | Double-precision floating point | Prices, coordinates |
| `Edm.Boolean` | True/false | Flags, toggles |
| `Edm.DateTimeOffset` | Date and time with timezone | Created dates, timestamps |
| `Edm.GeographyPoint` | Latitude/longitude pair | Location data |
| `Collection(Edm.String)` | Array of strings | Tags, categories |
| `Collection(Edm.Single)` | Array of single-precision floats | **Vector embeddings** |

> **EXAM TIP:** `Collection(Edm.Single)` is the field type used for **vector search** embeddings. Know this for questions about vector search index configuration.

### Field Attributes

Field attributes control how each field behaves in search operations:

| Attribute | Description | Applicable Types |
|-----------|-------------|-----------------|
| **searchable** | Included in full-text search; text is tokenized and analyzed | `Edm.String`, `Collection(Edm.String)` only |
| **filterable** | Can be used in `$filter` expressions | All types |
| **sortable** | Can be used in `$orderby` expressions | All types except `Collection(*)` |
| **facetable** | Can be used for faceted navigation (category counts) | All types except `Edm.GeographyPoint` |
| **retrievable** | Returned in search results | All types |
| **key** | Unique document identifier (exactly one per index) | `Edm.String` only |

> **EXAM TIP:** Only **string fields** can be `searchable`. Numeric, Boolean, and date fields can be `filterable`, `sortable`, and `facetable`, but NOT `searchable`. The `key` field must be `Edm.String`.

### Analyzers

Analyzers process text during indexing and querying. Azure AI Search provides three categories:

1. **Standard Lucene Analyzer** — Default analyzer; handles tokenization, lowercasing, and common transformations.
2. **Language Analyzers** — Language-specific analyzers (e.g., `en.microsoft`, `fr.lucene`) that handle stemming, stop words, and grammar rules for 50+ languages.
3. **Custom Analyzers** — User-defined analyzers with custom tokenizers, token filters, and character filters.

```json
{
  "name": "my-index",
  "fields": [
    { "name": "id", "type": "Edm.String", "key": true, "filterable": true },
    { "name": "title", "type": "Edm.String", "searchable": true, "retrievable": true, "analyzer": "en.microsoft" },
    { "name": "content", "type": "Edm.String", "searchable": true, "retrievable": true },
    { "name": "category", "type": "Edm.String", "filterable": true, "facetable": true, "retrievable": true },
    { "name": "rating", "type": "Edm.Int32", "filterable": true, "sortable": true, "facetable": true, "retrievable": true },
    { "name": "lastUpdated", "type": "Edm.DateTimeOffset", "filterable": true, "sortable": true, "retrievable": true }
  ]
}
```

### Suggesters

Suggesters enable autocomplete and suggestions (search-as-you-type) on specified fields:

```json
{
  "suggesters": [
    {
      "name": "sg",
      "searchMode": "analyzingInfixMatching",
      "sourceFields": ["title", "category"]
    }
  ]
}
```

- Only **one suggester** per index (but it can reference multiple fields).
- Suggesters work on `Edm.String` fields only.
- Must be defined at index creation time (cannot add to existing fields later without rebuilding).

---

## 3. Data Sources

Azure AI Search indexers pull data from supported Azure data sources:

| Data Source | Description | Notes |
|-------------|-------------|-------|
| **Azure Blob Storage** | Most common; indexes documents (PDF, DOCX, JSON, CSV, etc.) | Supports `parsingMode` for JSON arrays, delimited text |
| **Azure SQL Database** | Relational data from tables/views | Requires change tracking column |
| **Azure Cosmos DB** | NoSQL documents via SQL API or MongoDB API | Must enable change feed |
| **Azure Table Storage** | Key-value table data | Simple structured data |
| **Azure Data Lake Storage Gen2** | Hierarchical file storage | Similar capabilities to Blob Storage |
| **Azure MySQL** | MySQL database tables | Preview support |

> **EXAM TIP:** Azure Blob Storage is the most commonly tested data source. Know that different `parsingMode` values (`default`, `json`, `jsonArray`, `jsonLines`, `delimitedText`) control how blob content is parsed into search documents.

### Creating a Data Source (REST)

```http
POST https://[service-name].search.windows.net/datasources?api-version=2024-07-01
Content-Type: application/json
api-key: [admin-key]

{
  "name": "my-blob-datasource",
  "type": "azureblob",
  "credentials": {
    "connectionString": "DefaultEndpointsProtocol=https;AccountName=..."
  },
  "container": {
    "name": "documents",
    "query": "subfolder/"
  }
}
```

---

## 4. Indexers

Indexers automate data ingestion by crawling a data source and populating a search index. They implement a **pull model** — the indexer reaches out to the data source on a schedule.

### Indexer Configuration

| Setting | Description |
|---------|-------------|
| **Schedule** | `once`, every 5 minutes, hourly, daily, or custom interval (ISO 8601 duration) |
| **Field mappings** | Maps source fields to index fields (name transformation) |
| **Output field mappings** | Maps skillset outputs to index fields |
| **Parameters** | Configuration like `maxFailedItems`, `maxFailedItemsPerBatch`, `parsingMode` |

### Field Mappings

Field mappings translate source field names to index field names:

```json
{
  "fieldMappings": [
    { "sourceFieldName": "metadata_storage_name", "targetFieldName": "documentName" },
    { "sourceFieldName": "metadata_storage_path", "targetFieldName": "documentUrl" },
    { "sourceFieldName": "metadata_storage_last_modified", "targetFieldName": "lastModified" }
  ]
}
```

### Output Field Mappings

Output field mappings route enriched content from the skillset to index fields:

```json
{
  "outputFieldMappings": [
    { "sourceFieldName": "/document/merged_content/keyphrases", "targetFieldName": "keyphrases" },
    { "sourceFieldName": "/document/normalized_images/*/text", "targetFieldName": "imageText" },
    { "sourceFieldName": "/document/merged_content/language", "targetFieldName": "language" }
  ]
}
```

### Change Detection and Deletion Detection

- **Change detection** — Uses a high water mark column (e.g., `LastModified` timestamp) to index only new or modified documents. For Blob Storage, built-in change detection uses the `LastModified` property automatically.
- **Deletion detection** — Uses a soft-delete column/value to remove documents from the index when the source marks them as deleted. Configure with `softDeleteColumnName` and `softDeleteMarkerValue`.

### Reset and Re-run

- **Reset** — Clears the indexer's change tracking state, forcing a full re-crawl on the next run.
- **Reset Documents** — Re-process specific documents by their key.
- **Reset Skills** — Re-run specific skills in a skillset for all documents.

> **EXAM TIP:** If you change a skillset and want to re-process all documents through the updated pipeline, you need to **reset the indexer** before re-running it. Simply re-running without reset will only process new/changed documents.

---

## 5. Built-in Skillsets

A skillset defines a pipeline of AI enrichment steps that transform raw content during indexing. Built-in skills use pre-trained models from Azure AI Services.

### Cognitive Skills Categories

#### Natural Language Processing (NLP) Skills

| Skill | Description | Output |
|-------|-------------|--------|
| **Entity Recognition** | Extracts named entities (person, location, organization, etc.) | List of entities with types |
| **Key Phrase Extraction** | Identifies key phrases in text | List of key phrases |
| **Language Detection** | Detects the language of input text | Language code and name |
| **Sentiment Analysis** | Determines positive/negative/neutral sentiment | Sentiment scores |
| **PII Detection** | Detects personally identifiable information | PII entities and masked text |
| **Entity Linking** | Links entities to Wikipedia entries | Entity links with URLs |
| **Text Translation** | Translates text to target language | Translated text |

#### Image Analysis Skills

| Skill | Description | Output |
|-------|-------------|--------|
| **OCR** | Extracts text from images | Extracted text and layout info |
| **Image Analysis** | Generates tags, captions, categories from images | Image metadata |
| **Custom Vision** | Uses a trained Custom Vision model | Classification or detection results |

#### Utility Skills

| Skill | Description | Output |
|-------|-------------|--------|
| **Text Merge** | Combines text from multiple fields/images into one field | Merged text |
| **Text Split** | Splits large text into pages or sentences | Array of text chunks |
| **Shaper** | Creates a complex type from multiple inputs (for knowledge store) | Structured object |
| **Conditional** | Routes processing based on conditions | Conditional output |
| **Document Extraction** | Extracts content from embedded documents | Extracted content |

### Skill Inputs and Outputs

Every skill has defined inputs and outputs. Inputs reference the enrichment tree using a path notation:

```json
{
  "@odata.type": "#Microsoft.Skills.Text.V3.EntityRecognitionSkill",
  "name": "entity-recognition",
  "context": "/document/merged_content",
  "categories": ["Person", "Location", "Organization"],
  "inputs": [
    { "name": "text", "source": "/document/merged_content" },
    { "name": "languageCode", "source": "/document/language" }
  ],
  "outputs": [
    { "name": "persons", "targetName": "people" },
    { "name": "locations", "targetName": "places" },
    { "name": "organizations", "targetName": "orgs" }
  ]
}
```

### Skill Context

The `context` property determines the granularity at which the skill executes:

| Context | Description | When to Use |
|---------|-------------|-------------|
| `/document` | Runs once per document | Language detection, document-level metadata |
| `/document/pages/*` | Runs once per page (after Text Split) | Per-page entity extraction |
| `/document/normalized_images/*` | Runs once per image | OCR, image analysis |

### Attaching Azure AI Services

For production workloads (more than 20 documents/day in the free enrichment limit), you must attach an Azure AI Services multi-service resource to the skillset:

```json
{
  "name": "my-skillset",
  "skills": [ ... ],
  "cognitiveServices": {
    "@odata.type": "#Microsoft.Azure.Search.CognitiveServicesByKey",
    "key": "<your-ai-services-key>",
    "description": "AI Services for enrichment"
  }
}
```

> **EXAM TIP:** The free enrichment limit allows processing **20 documents per day** without attaching an AI Services resource. For anything beyond that, you must attach a **multi-service** Azure AI Services resource (not a single-service resource). The AI Services resource must be in the **same region** as the search service.

---

## 6. Custom Skills

When built-in skills don't meet your requirements, you can create custom skills using Azure Functions or any Web API endpoint.

### Web API Custom Skill

Custom skills use the `#Microsoft.Skills.Custom.WebApiSkill` type and call an external HTTP endpoint:

```json
{
  "@odata.type": "#Microsoft.Skills.Custom.WebApiSkill",
  "name": "my-custom-skill",
  "description": "Custom entity extraction",
  "uri": "https://my-function-app.azurewebsites.net/api/custom-entity?code=...",
  "httpMethod": "POST",
  "timeout": "PT30S",
  "batchSize": 10,
  "context": "/document",
  "inputs": [
    { "name": "text", "source": "/document/merged_content" },
    { "name": "language", "source": "/document/language" }
  ],
  "outputs": [
    { "name": "customEntities", "targetName": "customEntities" }
  ]
}
```

### Custom Skill Contract

The Azure Function must accept and return a specific JSON contract:

**Request Format:**

```json
{
  "values": [
    {
      "recordId": "record1",
      "data": {
        "text": "The document content goes here...",
        "language": "en"
      }
    },
    {
      "recordId": "record2",
      "data": {
        "text": "Another document's content...",
        "language": "en"
      }
    }
  ]
}
```

**Response Format:**

```json
{
  "values": [
    {
      "recordId": "record1",
      "data": {
        "customEntities": ["Entity1", "Entity2"]
      },
      "errors": [],
      "warnings": []
    },
    {
      "recordId": "record2",
      "data": {
        "customEntities": ["Entity3"]
      },
      "errors": [],
      "warnings": []
    }
  ]
}
```

> **EXAM TIP:** Custom skills MUST return the same `recordId` values that were sent in the request. Each record in the response must include `recordId`, `data`, `errors`, and `warnings` fields. This contract is frequently tested.

### Custom Entity Lookup Skill

A specialized built-in skill that matches text against a custom list of entities (from an inline list or external file):

```json
{
  "@odata.type": "#Microsoft.Skills.Text.CustomEntityLookupSkill",
  "name": "custom-entity-lookup",
  "context": "/document/merged_content",
  "inputs": [
    { "name": "text", "source": "/document/merged_content" }
  ],
  "outputs": [
    { "name": "entities", "targetName": "customEntities" }
  ],
  "entitiesDefinitionUri": "https://storage.blob.core.windows.net/entities/entities.json",
  "defaultLanguageCode": "en"
}
```

### When to Use Custom vs Built-in Skills

| Scenario | Recommendation |
|----------|---------------|
| Standard NLP (entities, key phrases, sentiment) | Built-in skills |
| Domain-specific entity extraction | Custom skill (Azure Function) |
| Custom ML model inference | Custom skill |
| External API integration | Custom skill |
| Text matching against known entity lists | Custom Entity Lookup (built-in) |
| Image analysis with custom categories | Custom Vision skill (built-in) |

---

## 7. Knowledge Store

A knowledge store is a secondary output of an enrichment pipeline that persists enriched content to Azure Storage for downstream analytics, independent of the search index.

### Three Projection Types

| Projection Type | Target | Format | Use Case |
|----------------|--------|--------|----------|
| **Table projections** | Azure Table Storage | Tabular rows | Power BI, structured analytics |
| **Object projections** | Azure Blob Storage | JSON documents | Data science, ML pipelines |
| **File projections** | Azure Blob Storage | Binary files (images) | Image galleries, downstream processing |

### Knowledge Store Configuration

```json
{
  "name": "my-skillset",
  "skills": [ ... ],
  "knowledgeStore": {
    "storageConnectionString": "DefaultEndpointsProtocol=https;AccountName=...",
    "projections": [
      {
        "tables": [
          {
            "tableName": "documentsTable",
            "generatedKeyName": "docId",
            "source": "/document/shapedData"
          },
          {
            "tableName": "keyPhrasesTable",
            "generatedKeyName": "kpId",
            "source": "/document/shapedData/keyPhrases/*"
          }
        ],
        "objects": [
          {
            "storageContainer": "enriched-documents",
            "generatedKeyName": "objId",
            "source": "/document/shapedData"
          }
        ],
        "files": [
          {
            "storageContainer": "document-images",
            "generatedKeyName": "fileId",
            "source": "/document/normalized_images/*"
          }
        ]
      }
    ]
  }
}
```

### Using the Shaper Skill for Projections

The Shaper skill creates a structured complex type that defines the shape of your projections:

```json
{
  "@odata.type": "#Microsoft.Skills.Util.ShaperSkill",
  "name": "shaper",
  "context": "/document",
  "inputs": [
    { "name": "title", "source": "/document/metadata_storage_name" },
    { "name": "content", "source": "/document/merged_content" },
    { "name": "keyPhrases", "source": "/document/merged_content/keyphrases" },
    { "name": "entities", "source": "/document/merged_content/people" },
    { "name": "language", "source": "/document/language" }
  ],
  "outputs": [
    { "name": "output", "targetName": "shapedData" }
  ]
}
```

### Knowledge Store vs Search Index

| Aspect | Search Index | Knowledge Store |
|--------|-------------|-----------------|
| **Purpose** | Real-time search and querying | Downstream analytics and processing |
| **Query** | Azure AI Search query APIs | Direct access via Azure Storage APIs, Power BI |
| **Format** | Inverted index (optimized for search) | Tables, JSON objects, files |
| **Update** | Incremental via indexer | Re-projected on indexer run |
| **Use cases** | Search apps, chatbots, RAG | Power BI dashboards, ML training, data exploration |

> **EXAM TIP:** Table projections go to **Azure Table Storage**, object and file projections go to **Azure Blob Storage**. Projections within the same projection group share a common generated key, enabling cross-referencing between tables, objects, and files.

---

## 8. Query Syntax

Azure AI Search supports two query syntaxes:

### Simple Query Syntax (Default)

| Feature | Syntax | Example |
|---------|--------|---------|
| Term search | `word` | `hotel` |
| Phrase search | `"phrase"` | `"luxury hotel"` |
| AND | `+` | `+luxury +hotel` |
| OR | `\|` | `luxury \| budget` |
| NOT | `-` | `luxury -budget` |
| Suffix wildcard | `*` | `hot*` |
| Precedence | `()` | `(luxury \| premium) +hotel` |

### Full Lucene Query Syntax

Enable with `queryType=full` in the request. Adds:

| Feature | Syntax | Example | Description |
|---------|--------|---------|-------------|
| Field-scoped query | `field:term` | `title:hotel` | Search within a specific field |
| Fuzzy search | `term~N` | `hotel~1` | Matches with up to N edit distance (default 2) |
| Proximity search | `"term1 term2"~N` | `"luxury hotel"~3` | Terms within N words of each other |
| Term boosting | `term^N` | `luxury^2 hotel` | Boost relevance of a term |
| Regex | `/pattern/` | `/[mh]otel/` | Regular expression matching |
| Wildcard | `?` and `*` | `ho?el`, `ho*` | Single char and multi-char wildcards |

> **EXAM TIP:** Fuzzy search (`~`) allows matching terms with spelling variations. `hotel~1` matches "hotel", "hosel", "motel" (1 edit away). The default edit distance is **2** if you omit the number. Proximity search requires **full Lucene syntax** (`queryType=full`).

### OData Filter Expressions (`$filter`)

Filters narrow results based on structured field values:

```
$filter=rating ge 4 and category eq 'Luxury'
$filter=location/lat gt 47.0 and location/lon lt -122.0
$filter=tags/any(t: t eq 'wifi')
$filter=lastRenovated gt 2020-01-01T00:00:00Z
```

| Operator | Description | Example |
|----------|-------------|---------|
| `eq` | Equal | `category eq 'Hotel'` |
| `ne` | Not equal | `category ne 'Motel'` |
| `gt` | Greater than | `rating gt 3` |
| `lt` | Less than | `price lt 200` |
| `ge` | Greater than or equal | `rating ge 4` |
| `le` | Less than or equal | `price le 500` |
| `and` | Logical AND | `rating ge 4 and price lt 200` |
| `or` | Logical OR | `category eq 'Hotel' or category eq 'Resort'` |
| `not` | Logical NOT | `not category eq 'Motel'` |

### Other Query Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `$select` | Fields to return | `$select=title,description,rating` |
| `$orderby` | Sort order | `$orderby=rating desc, price asc` |
| `$top` | Number of results to return | `$top=10` |
| `$skip` | Number of results to skip (pagination) | `$skip=20` |
| `$count` | Include total count of matches | `$count=true` |
| `search` | Search text | `search=luxury hotel spa` |
| `searchFields` | Fields to search in | `searchFields=title,description` |
| `searchMode` | `any` (OR) or `all` (AND) between terms | `searchMode=all` |
| `queryType` | `simple` (default) or `full` (Lucene) | `queryType=full` |
| `scoringProfile` | Apply a custom scoring profile | `scoringProfile=boosted` |

### search.ismatch and search.ismatchscoring

These functions allow combining full-text search with filters in the `$filter` expression:

```
$filter=search.ismatch('luxury', 'title') and rating ge 4
$filter=search.ismatchscoring('spa pool', 'amenities', 'full', 'any')
```

- `search.ismatch` — Returns true/false without affecting relevance scores.
- `search.ismatchscoring` — Returns true/false AND affects relevance scoring.

---

## 9. Semantic Search

Semantic search uses Microsoft's deep learning models to re-rank search results for improved relevance. It adds a secondary ranking pass on top of the initial BM25 keyword ranking.

### Key Concepts

| Concept | Description |
|---------|-------------|
| **Semantic ranker** | Re-ranks the top 50 BM25 results using a transformer model |
| **Semantic captions** | Extracts the most relevant passages from documents |
| **Semantic answers** | Extracts a direct answer to a question (if available) |
| **SemanticConfiguration** | Defines which fields to use for semantic ranking |

### Enabling Semantic Search

1. Enable semantic ranking on the search service (must be Basic tier or higher).
2. Create a `semanticConfiguration` in the index definition.
3. Use the `semantic` query parameter in search requests.

```json
{
  "name": "my-index",
  "fields": [ ... ],
  "semantic": {
    "configurations": [
      {
        "name": "my-semantic-config",
        "prioritizedFields": {
          "titleField": { "fieldName": "title" },
          "contentFields": [
            { "fieldName": "content" }
          ],
          "keywordsFields": [
            { "fieldName": "tags" }
          ]
        }
      }
    ]
  }
}
```

### Semantic Query

```http
POST https://[service].search.windows.net/indexes/my-index/docs/search?api-version=2024-07-01
{
  "search": "What hotels have a spa?",
  "queryType": "semantic",
  "semanticConfiguration": "my-semantic-config",
  "captions": "extractive",
  "answers": "extractive|count-3",
  "queryLanguage": "en-us"
}
```

> **EXAM TIP:** Semantic search requires a `semanticConfiguration` in the index. The semantic ranker re-ranks the top results from the initial BM25 ranking — it does NOT search the entire index semantically. It is available on **Basic tier and above** (not Free).

---

## 10. Vector Search

Vector search enables similarity-based retrieval using numerical embeddings. Documents and queries are converted to vectors, and results are found by measuring vector proximity.

### Vector Field Configuration

Vector fields use the `Collection(Edm.Single)` type and require additional configuration:

```json
{
  "name": "contentVector",
  "type": "Collection(Edm.Single)",
  "searchable": true,
  "retrievable": false,
  "dimensions": 1536,
  "vectorSearchProfile": "my-vector-profile"
}
```

### Vector Search Profiles and Algorithms

```json
{
  "vectorSearch": {
    "algorithms": [
      {
        "name": "my-hnsw",
        "kind": "hnsw",
        "hnswParameters": {
          "m": 4,
          "efConstruction": 400,
          "efSearch": 500,
          "metric": "cosine"
        }
      },
      {
        "name": "my-eknn",
        "kind": "exhaustiveKnn",
        "exhaustiveKnnParameters": {
          "metric": "cosine"
        }
      }
    ],
    "profiles": [
      {
        "name": "my-vector-profile",
        "algorithm": "my-hnsw"
      }
    ]
  }
}
```

| Algorithm | Description | Trade-off |
|-----------|-------------|-----------|
| **HNSW** (Hierarchical Navigable Small World) | Approximate nearest neighbor search | Faster but approximate results |
| **Exhaustive KNN** | Brute-force exact nearest neighbor | Slower but exact results |

### Generating Embeddings

Use Azure OpenAI's embedding models (e.g., `text-embedding-ada-002`, `text-embedding-3-small`) to generate vectors:

```python
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="https://my-openai.openai.azure.com/",
    api_key="<key>",
    api_version="2024-02-01"
)

response = client.embeddings.create(
    input="What is Azure AI Search?",
    model="text-embedding-ada-002"
)

embedding = response.data[0].embedding  # List of 1536 floats
```

### Vector Query

```http
POST https://[service].search.windows.net/indexes/my-index/docs/search?api-version=2024-07-01
{
  "vectorQueries": [
    {
      "kind": "vector",
      "vector": [0.01, -0.03, 0.12, ...],
      "k": 10,
      "fields": "contentVector"
    }
  ],
  "select": "title, content, category"
}
```

### Hybrid Search (Keyword + Vector)

Hybrid search combines traditional keyword search with vector search for the best of both approaches:

```http
POST https://[service].search.windows.net/indexes/my-index/docs/search?api-version=2024-07-01
{
  "search": "luxury hotel with spa",
  "vectorQueries": [
    {
      "kind": "vector",
      "vector": [0.01, -0.03, 0.12, ...],
      "k": 10,
      "fields": "contentVector"
    }
  ],
  "select": "title, content, category"
}
```

> **EXAM TIP:** Hybrid search is performed by specifying BOTH a `search` text query AND a `vectorQueries` array. The results are combined using Reciprocal Rank Fusion (RRF). Know that HNSW is the default and recommended algorithm for vector search due to its performance characteristics.

---

## 11. Code Examples

### Python: Create an Index

```python
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SearchField,
    SearchFieldDataType,
    SimpleField,
    SearchableField,
)
from azure.core.credentials import AzureKeyCredential

endpoint = "https://my-search-service.search.windows.net"
api_key = "<admin-key>"

client = SearchIndexClient(endpoint, AzureKeyCredential(api_key))

fields = [
    SimpleField(name="id", type=SearchFieldDataType.String, key=True, filterable=True),
    SearchableField(name="title", type=SearchFieldDataType.String, analyzer_name="en.microsoft"),
    SearchableField(name="content", type=SearchFieldDataType.String),
    SimpleField(name="category", type=SearchFieldDataType.String, filterable=True, facetable=True),
    SimpleField(name="rating", type=SearchFieldDataType.Int32, filterable=True, sortable=True, facetable=True),
    SimpleField(name="lastUpdated", type=SearchFieldDataType.DateTimeOffset, filterable=True, sortable=True),
]

index = SearchIndex(name="hotels-index", fields=fields)
result = client.create_or_update_index(index)
print(f"Index '{result.name}' created successfully.")
```

### Python: Upload Documents

```python
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

search_client = SearchClient(
    endpoint="https://my-search-service.search.windows.net",
    index_name="hotels-index",
    credential=AzureKeyCredential("<admin-key>")
)

documents = [
    {
        "id": "1",
        "title": "Grand Luxury Hotel",
        "content": "A premium five-star hotel with spa, pool, and fine dining.",
        "category": "Luxury",
        "rating": 5,
        "lastUpdated": "2024-01-15T00:00:00Z"
    },
    {
        "id": "2",
        "title": "Budget Inn Express",
        "content": "Affordable accommodation with free breakfast and parking.",
        "category": "Budget",
        "rating": 3,
        "lastUpdated": "2024-02-20T00:00:00Z"
    }
]

result = search_client.upload_documents(documents=documents)
print(f"Uploaded {len(result)} documents.")
```

### Python: Simple Search Query

```python
results = search_client.search(
    search_text="luxury spa",
    select=["title", "category", "rating"],
    filter="rating ge 4",
    order_by=["rating desc"],
    top=10,
    include_total_count=True
)

print(f"Total results: {results.get_count()}")
for result in results:
    print(f"  {result['title']} (Rating: {result['rating']}, Category: {result['category']})")
```

### Python: Filtered Search with Facets

```python
results = search_client.search(
    search_text="*",
    facets=["category,count:10", "rating,values:1|2|3|4|5"],
    filter="rating ge 3",
    top=20
)

# Display facets
for facet_name, facet_values in results.get_facets().items():
    print(f"\n{facet_name}:")
    for fv in facet_values:
        print(f"  {fv['value']}: {fv['count']}")
```

### Python: Vector Search

```python
from azure.search.documents.models import VectorizedQuery

vector_query = VectorizedQuery(
    vector=embedding,  # List of floats from embedding model
    k_nearest_neighbors=10,
    fields="contentVector"
)

results = search_client.search(
    search_text="luxury hotel with spa",     # Keyword part (hybrid)
    vector_queries=[vector_query],            # Vector part
    select=["title", "content", "category"],
    top=10
)

for result in results:
    print(f"  Score: {result['@search.score']:.4f} | {result['title']}")
```

### REST: Create an Indexer with Skillset

```http
POST https://[service-name].search.windows.net/indexers?api-version=2024-07-01
Content-Type: application/json
api-key: [admin-key]

{
  "name": "my-indexer",
  "dataSourceName": "my-blob-datasource",
  "targetIndexName": "my-index",
  "skillsetName": "my-skillset",
  "schedule": {
    "interval": "PT2H"
  },
  "parameters": {
    "maxFailedItems": 10,
    "maxFailedItemsPerBatch": 5,
    "configuration": {
      "dataToExtract": "contentAndMetadata",
      "imageAction": "generateNormalizedImages"
    }
  },
  "fieldMappings": [
    { "sourceFieldName": "metadata_storage_path", "targetFieldName": "id", "mappingFunction": { "name": "base64Encode" } },
    { "sourceFieldName": "metadata_storage_name", "targetFieldName": "documentName" }
  ],
  "outputFieldMappings": [
    { "sourceFieldName": "/document/merged_content/keyphrases", "targetFieldName": "keyphrases" },
    { "sourceFieldName": "/document/language", "targetFieldName": "language" }
  ]
}
```

### REST: Query with $filter and $select

```http
POST https://[service-name].search.windows.net/indexes/my-index/docs/search?api-version=2024-07-01
Content-Type: application/json
api-key: [query-key]

{
  "search": "luxury spa pool",
  "searchMode": "all",
  "queryType": "full",
  "$filter": "rating ge 4 and category eq 'Luxury'",
  "$select": "title, description, rating, category",
  "$orderby": "rating desc",
  "$top": 10,
  "$skip": 0,
  "$count": true,
  "highlight": "description",
  "highlightPreTag": "<b>",
  "highlightPostTag": "</b>"
}
```

---

## Key Takeaways

1. **Service Tiers** — Choose based on storage, index count, and SLA needs. Remember: 2 replicas for read SLA, 3 for read/write SLA.

2. **Index Design** — Only string fields can be `searchable`. The key field must be `Edm.String`. Use `Collection(Edm.Single)` for vector fields.

3. **Indexers** — Pull-based ingestion with scheduling, field mappings, and change detection. Reset the indexer to force full re-processing.

4. **Skillsets** — AI enrichment pipeline using built-in and custom skills. Attach an Azure AI Services multi-service resource for production workloads (>20 docs/day free limit).

5. **Custom Skills** — Azure Function or Web API that follows the recordId-based request/response contract.

6. **Knowledge Store** — Three projection types: tables (Table Storage), objects (Blob Storage), files (Blob Storage). Use the Shaper skill to structure projections.

7. **Query Syntax** — Simple syntax is the default. Full Lucene adds fuzzy search, proximity, boosting, and regex. OData `$filter` for structured filtering.

8. **Semantic Search** — Re-ranks top BM25 results using transformer models. Requires a `semanticConfiguration` and Basic tier or above.

9. **Vector Search** — Uses `Collection(Edm.Single)` fields with HNSW or exhaustive KNN algorithms. Hybrid search combines keyword + vector for best results.

---

## Further Reading

- [Azure AI Search documentation](https://learn.microsoft.com/azure/search/)
- [Search index overview](https://learn.microsoft.com/azure/search/search-what-is-an-index)
- [Indexer overview](https://learn.microsoft.com/azure/search/search-indexer-overview)
- [Skillset concepts](https://learn.microsoft.com/azure/search/cognitive-search-working-with-skillsets)
- [Knowledge store overview](https://learn.microsoft.com/azure/search/knowledge-store-concept-intro)
- [Query types and composition](https://learn.microsoft.com/azure/search/search-query-overview)
- [Semantic ranking](https://learn.microsoft.com/azure/search/semantic-search-overview)
- [Vector search overview](https://learn.microsoft.com/azure/search/vector-search-overview)
