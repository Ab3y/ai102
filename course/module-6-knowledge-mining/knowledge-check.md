# Module 6: Knowledge Mining & Document Intelligence — Knowledge Check

## Instructions

Answer all 15 questions. Each question has one correct answer unless stated otherwise. Target score: **80% or higher** (12/15).

---

### Question 1

**You are building a search solution for a hotel review website. The index contains a `rating` field (Edm.Int32), a `city` field (Edm.String), and a `description` field (Edm.String). Users need to search reviews by keywords in the description, filter by minimum rating, and see how many hotels are in each city. Which set of field attributes should you configure for each field?**

- A) `description`: searchable, filterable; `rating`: searchable, sortable; `city`: searchable, facetable
- B) `description`: searchable, retrievable; `rating`: filterable, sortable; `city`: filterable, facetable
- C) `description`: filterable, retrievable; `rating`: filterable, sortable; `city`: filterable, facetable
- D) `description`: searchable, retrievable; `rating`: searchable, filterable; `city`: searchable, sortable

---

### Question 2

**Your organization wants a 99.9% SLA for an Azure AI Search service that handles both search queries and continuous indexing from an Azure Blob Storage data source. What is the minimum number of replicas you must configure?**

- A) 1 replica
- B) 2 replicas
- C) 3 replicas
- D) 4 replicas

---

### Question 3

**You have created a skillset that includes Entity Recognition, Key Phrase Extraction, and OCR skills. The skillset processes documents from Azure Blob Storage. After deploying to production, you discover that enrichment stops working after processing 20 documents per day. What should you do to resolve this?**

- A) Upgrade the Azure AI Search service to the Standard (S1) tier
- B) Attach an Azure AI Services multi-service resource to the skillset
- C) Increase the number of replicas on the search service
- D) Create a separate skillset for each cognitive skill

---

### Question 4

**You are configuring a knowledge store to support a Power BI dashboard that displays key phrases extracted per document, and a data science team that needs the full enriched JSON for each document. Which projection types should you configure?**

- A) Table projections for Power BI, Object projections for data science
- B) File projections for Power BI, Table projections for data science
- C) Object projections for Power BI, File projections for data science
- D) Table projections for both Power BI and data science

---

### Question 5

**You need to search an Azure AI Search index for hotels that contain the word "luxurious" OR any similar spelling within 1 edit distance. The search should also boost results that contain "spa" by a factor of 3. Which query should you use?**

- A) `search=luxurious~1 spa^3&queryType=simple`
- B) `search=luxurious~1 spa^3&queryType=full`
- C) `search=luxurious* spa&queryType=full&$orderby=spa`
- D) `search="luxurious spa"~1&queryType=full`

---

### Question 6

**You are implementing a custom skill for your Azure AI Search skillset using an Azure Function. Your function receives a batch of records and processes them. Which of the following response formats is correct for returning results back to the indexer?**

- A)
```json
{
  "results": [
    { "id": "record1", "output": { "entities": ["Entity1"] } }
  ]
}
```

- B)
```json
{
  "values": [
    { "recordId": "record1", "data": { "entities": ["Entity1"] }, "errors": [], "warnings": [] }
  ]
}
```

- C)
```json
{
  "documents": [
    { "recordId": "record1", "entities": ["Entity1"], "status": "success" }
  ]
}
```

- D)
```json
{
  "values": [
    { "id": "record1", "result": { "entities": ["Entity1"] } }
  ]
}
```

---

### Question 7

**A developer needs to extract vendor name, invoice total, and line items from invoices received from multiple vendors. The invoices have varying layouts. Which approach should the developer use?**

- A) Use the `prebuilt-read` model to extract all text, then parse the text manually
- B) Use the `prebuilt-invoice` model to analyze the invoices
- C) Train a custom template model with 5 sample invoices
- D) Use the `prebuilt-layout` model to extract tables and key-value pairs

---

### Question 8

**You are implementing document analysis using the Document Intelligence REST API. You submit a POST request to analyze an invoice and receive an HTTP 202 response. What should you do next?**

- A) Parse the response body for the `analyzeResult` object containing the extracted fields
- B) Send a GET request to the URL in the `Operation-Location` response header and poll until the status is `succeeded`
- C) Send another POST request with the same document to retrieve the results
- D) Wait 30 seconds and send a GET request to the original POST endpoint with the same parameters

---

### Question 9

**Your application processes insurance claim forms that have a fixed layout with fields always in the same positions. You have 20 labeled training documents. You need the model to train as quickly as possible. Which custom model type should you choose?**

- A) Neural custom model
- B) Template custom model
- C) Composed model
- D) Prebuilt layout model

---

### Question 10

**A company receives documents from three different departments: HR forms, expense reports, and purchase orders. Each department's documents have a unique layout. The company wants to process all documents through a single API endpoint. What should they do?**

- A) Train one custom model using documents from all three departments
- B) Train three separate custom models and create a composed model
- C) Use the prebuilt-document model for all three types
- D) Create three separate Document Intelligence resources, one per department

---

### Question 11

**A developer is testing their Document Intelligence solution using the Free (F0) tier. They submit a 10-page PDF (3 MB) for analysis but receive an error. What is the most likely cause?**

- A) The file size exceeds the Free tier limit of 2 MB
- B) The page count exceeds the Free tier limit of 2 pages per document
- C) The Free tier does not support PDF format
- D) The Free tier requires documents to be uploaded to Azure Blob Storage first

---

### Question 12

**You need to process a collection of scanned legal contracts to extract key dates, party names, and generate a 2-sentence summary of each contract. None of the contracts follow a standard form layout. Which Azure AI service should you use?**

- A) Azure AI Document Intelligence with prebuilt-document model
- B) Azure AI Vision Read API
- C) Azure AI Content Understanding
- D) Azure AI Language (text summarization)

---

### Question 13

**Your organization has a library of training video recordings. You need to build a solution that generates searchable transcripts, identifies the main topics discussed, and creates a summary for each video. Which Azure AI service is best suited for this requirement?**

- A) Azure AI Speech combined with Azure AI Language
- B) Azure AI Video Indexer
- C) Azure AI Content Understanding
- D) Azure AI Vision with spatial analysis

---

### Question 14

**A developer needs to extract text from photographs of street signs in multiple languages. The solution requires fast, simple OCR without any additional document structure analysis. Which service should they use?**

- A) Azure AI Content Understanding
- B) Azure AI Document Intelligence (prebuilt-read model)
- C) Azure AI Vision Read API
- D) Azure AI Document Intelligence (prebuilt-layout model)

---

### Question 15

**You are designing an Azure AI Search solution that uses both keyword and vector search. Users type natural language questions, and the system should search using both the question text and its embedding vector. The index has a `content` field (Edm.String, searchable) and a `contentVector` field (Collection(Edm.Single)). Which search approach should you implement?**

- A) Submit two separate queries — one keyword search and one vector search — and merge the results in your application
- B) Submit a single hybrid search request with both a `search` text value and a `vectorQueries` array
- C) Convert the user's question to a vector and use only vector search, as it is more accurate than keyword search
- D) Use semantic search with a `semanticConfiguration` — it automatically performs both keyword and vector search

---

## Answers

### Question 1

**Correct Answer: B**

**Explanation:** Only `Edm.String` fields can be `searchable`, so `rating` (Edm.Int32) cannot be searchable — this eliminates options A and D. The `description` field needs to be `searchable` for full-text search (eliminates C). The `city` field needs to be `facetable` for counting hotels per city, and the `rating` field needs to be `filterable` for minimum rating filters and `sortable` for ordering by rating.

---

### Question 2

**Correct Answer: C**

**Explanation:** Azure AI Search requires **2 replicas** for a read-only (query) SLA and **3 replicas** for a read/write (query + indexing) SLA. Since the service handles both search queries and continuous indexing, you need 3 replicas for the 99.9% SLA.

---

### Question 3

**Correct Answer: B**

**Explanation:** The free enrichment limit in Azure AI Search allows processing only **20 documents per day** without an attached AI Services resource. To process more, you must attach an **Azure AI Services multi-service resource** to the skillset. The resource must be in the same region as the search service. Upgrading the search tier or adding replicas does not affect the enrichment limit.

---

### Question 4

**Correct Answer: A**

**Explanation:** **Table projections** store structured, tabular data in Azure Table Storage, which Power BI can connect to directly for dashboards. **Object projections** store full JSON objects in Azure Blob Storage, which is ideal for data science teams that need the complete enriched document structure. File projections are for binary files like images, not structured data.

---

### Question 5

**Correct Answer: B**

**Explanation:** Fuzzy search (`~1`) and term boosting (`^3`) require **full Lucene query syntax** (`queryType=full`). Option A uses simple syntax, which doesn't support these features. Option D uses proximity search syntax (`"phrase"~N`), not fuzzy search. The correct query `luxurious~1 spa^3` with `queryType=full` finds "luxurious" or similar spellings within 1 edit distance and boosts "spa" results by 3x.

---

### Question 6

**Correct Answer: B**

**Explanation:** The custom skill contract requires a response with a `values` array where each item has `recordId` (matching the request), `data` (the skill outputs), `errors` (array), and `warnings` (array). The `recordId` must match the IDs sent in the request. Options A, C, and D use incorrect property names or structures.

---

### Question 7

**Correct Answer: B**

**Explanation:** The `prebuilt-invoice` model is specifically designed to extract invoice fields (vendor name, totals, line items, dates) from invoices of varying layouts. It requires no training. The `prebuilt-read` model only extracts text (no semantic fields). A template custom model would struggle with varying layouts. The `prebuilt-layout` model extracts tables and key-value pairs but doesn't understand invoice-specific semantics.

---

### Question 8

**Correct Answer: B**

**Explanation:** Document Intelligence uses an **asynchronous polling pattern**. After the initial POST returns HTTP 202, the response includes an `Operation-Location` header with a URL. You must send GET requests to this URL and poll until the `status` field equals `"succeeded"`. The analysis results are NOT included in the initial POST response (they haven't been computed yet).

---

### Question 9

**Correct Answer: B**

**Explanation:** **Template custom models** are designed for documents with fixed, consistent layouts — fields are always in the same position. They train much faster than neural models (seconds to minutes vs. minutes to hours). Since the insurance forms have a fixed layout and fast training is a priority, template is the correct choice. Neural models are better for variable layouts.

---

### Question 10

**Correct Answer: B**

**Explanation:** **Composed models** combine multiple custom models into a single endpoint. Train a separate custom model for each document type (HR forms, expense reports, purchase orders), then compose them. When a document is submitted, the composed model automatically classifies it and routes it to the correct component model. Training one model on all three types would produce poor results due to different layouts.

---

### Question 11

**Correct Answer: B**

**Explanation:** The Free (F0) tier limits documents to **2 pages** per document. A 10-page PDF exceeds this limit. The Free tier file size limit is 4 MB (not 2 MB), and the file is only 3 MB, so size is not the issue. PDF is a supported format on all tiers.

---

### Question 12

**Correct Answer: C**

**Explanation:** Azure AI Content Understanding can extract entities (dates, names), perform text extraction, and **generate summaries** — all in one service. Document Intelligence's prebuilt-document model can extract key-value pairs but cannot generate summaries. AI Vision Read API only does OCR. AI Language can summarize text but cannot process scanned documents directly (it requires text input, not images/PDFs).

---

### Question 13

**Correct Answer: C**

**Explanation:** Azure AI Content Understanding provides unified **video processing** capabilities including transcription, topic extraction, and summarization through a single analyzer. While Azure AI Speech + Language could achieve parts of this, Content Understanding provides a more integrated solution for video content analysis. The question asks about generating transcripts, topics, AND summaries from video — Content Understanding handles all three.

---

### Question 14

**Correct Answer: C**

**Explanation:** The **Azure AI Vision Read API** is optimized for simple, fast OCR on images. It supports multiple languages and is the best choice when you only need text extraction from photographs without document structure analysis. Document Intelligence is designed for documents (forms, invoices), not general photographs. Content Understanding would work but is overkill for simple OCR on photographs.

---

### Question 15

**Correct Answer: B**

**Explanation:** **Hybrid search** in Azure AI Search is performed by including both a `search` text query (for keyword/BM25 ranking) and a `vectorQueries` array (for vector similarity) in a single search request. The results are automatically combined using Reciprocal Rank Fusion (RRF). Submitting separate queries and merging manually (A) is inefficient. Vector-only search (C) misses exact keyword matches. Semantic search (D) re-ranks keyword results but does not perform vector search.
