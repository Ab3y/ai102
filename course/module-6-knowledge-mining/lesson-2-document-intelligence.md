# Lesson 2: Azure AI Document Intelligence

## Learning Objectives

After completing this lesson, you will be able to:

- Provision Azure AI Document Intelligence and understand pricing tiers
- Select the appropriate prebuilt model for common document types
- Implement the asynchronous polling pattern for document analysis (REST and SDK)
- Parse and extract structured data from analysis results
- Train and evaluate custom models (template and neural)
- Create composed models to handle multiple document types through a single endpoint
- Understand file format limitations and size constraints

---

## 1. Provision Document Intelligence

Azure AI Document Intelligence (formerly Azure Form Recognizer) is a cloud-based AI service that extracts text, key-value pairs, tables, and structured data from documents using pre-trained and custom machine learning models.

### Resource Creation

You can create a Document Intelligence resource through:

- **Azure Portal** — Search for "Document Intelligence" in the marketplace
- **Azure CLI:**

```bash
az cognitiveservices account create \
  --name my-doc-intelligence \
  --resource-group my-rg \
  --kind FormRecognizer \
  --sku S0 \
  --location eastus \
  --yes
```

- **Bicep:**

```bicep
resource docIntelligence 'Microsoft.CognitiveServices/accounts@2023-10-01-preview' = {
  name: 'my-doc-intelligence'
  location: 'eastus'
  kind: 'FormRecognizer'
  sku: {
    name: 'S0'
  }
  properties: {
    publicNetworkAccess: 'Enabled'
  }
}
```

> **EXAM TIP:** The Azure resource kind for Document Intelligence is still `FormRecognizer` in the ARM/Bicep API, even though the service has been renamed. Know both the old name (Form Recognizer) and the new name (Document Intelligence) for the exam.

### Pricing Tiers

| Feature | Free (F0) | Standard (S0) |
|---------|-----------|---------------|
| **Price** | Free | Pay-per-page |
| **Max file size** | 4 MB | 500 MB |
| **Max pages per document** | 2 pages | 2,000 pages |
| **Transactions per month** | 500 (prebuilt), 1 model train/month | Unlimited |
| **Custom models** | 1 model | Up to 500 models |
| **Composed models** | Not available | Up to 200 component models |

### Document Intelligence Studio

The [Document Intelligence Studio](https://documentintelligence.ai.azure.com/) is a web-based tool for:

- Testing prebuilt models with your own documents
- Labeling training documents for custom models
- Training and evaluating custom models
- Creating composed models
- Exploring analysis results interactively

---

## 2. Prebuilt Models

Prebuilt models are pre-trained for common document types and require no custom training. They extract specific fields relevant to each document type.

### Invoice Model (`prebuilt-invoice`)

Extracts key fields from invoices:

| Field | Description | Example |
|-------|-------------|---------|
| `VendorName` | Supplier/vendor name | "Contoso Ltd." |
| `VendorAddress` | Supplier address | "123 Main St, Redmond, WA" |
| `CustomerName` | Customer/buyer name | "Fabrikam Inc." |
| `CustomerAddress` | Customer address | "456 Oak Ave, Seattle, WA" |
| `InvoiceId` | Invoice number | "INV-2024-001" |
| `InvoiceDate` | Date of invoice | "2024-03-15" |
| `DueDate` | Payment due date | "2024-04-15" |
| `SubTotal` | Subtotal before tax | 1500.00 |
| `TotalTax` | Tax amount | 127.50 |
| `InvoiceTotal` | Total amount due | 1627.50 |
| `Items` | Line items (description, quantity, unit price, amount) | Array of line items |

### Receipt Model (`prebuilt-receipt`)

Extracts key fields from sales receipts:

| Field | Description | Example |
|-------|-------------|---------|
| `MerchantName` | Store/business name | "Contoso Coffee" |
| `MerchantAddress` | Store address | "789 Pine St, Seattle, WA" |
| `MerchantPhoneNumber` | Store phone number | "(206) 555-0100" |
| `TransactionDate` | Date of purchase | "2024-03-20" |
| `TransactionTime` | Time of purchase | "14:30:00" |
| `Items` | Purchased items (name, quantity, price) | Array of items |
| `Subtotal` | Subtotal before tax/tip | 12.50 |
| `Tax` | Tax amount | 1.06 |
| `Tip` | Tip amount | 2.00 |
| `Total` | Total amount | 15.56 |

### ID Document Model (`prebuilt-idDocument`)

Extracts fields from identity documents (passports, driver's licenses):

| Field | Description | Example |
|-------|-------------|---------|
| `FirstName` | First/given name | "Jane" |
| `LastName` | Last/family name | "Doe" |
| `DateOfBirth` | Date of birth | "1990-05-15" |
| `DocumentNumber` | ID document number | "DL-12345678" |
| `DateOfExpiration` | Expiration date | "2028-05-15" |
| `Address` | Residential address | "123 Elm St, Portland, OR" |
| `Sex` | Gender | "F" |
| `CountryRegion` | Issuing country/region | "USA" |
| `DocumentType` | Type (driverLicense, passport, etc.) | "driverLicense" |

### Business Card Model (`prebuilt-businessCard`)

| Field | Description |
|-------|-------------|
| `ContactNames` | Name(s) on the card |
| `JobTitles` | Job title(s) |
| `CompanyNames` | Company name(s) |
| `Phones` | Phone number(s) |
| `Emails` | Email address(es) |
| `Websites` | Website URL(s) |
| `Addresses` | Physical address(es) |

### W-2 Model (`prebuilt-tax.us.w2`)

| Field | Description |
|-------|-------------|
| `Employee` | Employee name, address, SSN |
| `Employer` | Employer name, address, EIN |
| `WagesTipsAndOtherCompensation` | Box 1 wages |
| `FederalIncomeTaxWithheld` | Box 2 federal tax |
| `SocialSecurityWages` | Box 3 SS wages |
| `SocialSecurityTaxWithheld` | Box 4 SS tax |
| `MedicareWagesAndTips` | Box 5 Medicare wages |
| `MedicareTaxWithheld` | Box 6 Medicare tax |
| `TaxYear` | Tax year |

### Health Insurance Card Model (`prebuilt-healthInsuranceCard.us`)

| Field | Description |
|-------|-------------|
| `Insurer` | Insurance company name |
| `Member` | Member name and ID |
| `Plan` | Plan name and type |
| `GroupNumber` | Group number |
| `CopayBenefits` | Copay amounts |
| `EffectiveDate` | Coverage start date |
| `ExpirationDate` | Coverage end date |

### Prebuilt Model Comparison

| Model | Model ID | Key Use Case | Typical Documents |
|-------|----------|-------------|-------------------|
| **Invoice** | `prebuilt-invoice` | AP/AR automation | Invoices, bills |
| **Receipt** | `prebuilt-receipt` | Expense management | Sales receipts, POS slips |
| **ID Document** | `prebuilt-idDocument` | Identity verification | Passports, driver's licenses |
| **Business Card** | `prebuilt-businessCard` | Contact management | Business cards |
| **W-2** | `prebuilt-tax.us.w2` | Tax processing | US tax forms |
| **Health Insurance** | `prebuilt-healthInsuranceCard.us` | Insurance processing | US health insurance cards |
| **Read** | `prebuilt-read` | General text extraction | Any document (text, handwriting) |
| **Layout** | `prebuilt-layout` | Structure extraction | Any document (tables, sections) |
| **General Document** | `prebuilt-document` | Key-value pair extraction | Semi-structured documents |

> **EXAM TIP:** Know which prebuilt model to use for each document type. The `prebuilt-read` model extracts **text only** (no tables or structure). The `prebuilt-layout` model extracts **text, tables, and structure** but no semantic fields. Use specific models like `prebuilt-invoice` when you need domain-specific field extraction.

---

## 3. Analyze via REST (Async Polling Pattern)

Document Intelligence uses an **asynchronous two-step** pattern for all analysis operations. This is a fundamental pattern tested on the exam.

### Step 1: Submit Analysis Request (POST)

Send the document for analysis. The service returns immediately with a `202 Accepted` status and an `Operation-Location` header containing the URL to poll for results.

```http
POST https://{endpoint}/documentintelligence/documentModels/prebuilt-invoice:analyze?api-version=2024-11-30
Content-Type: application/json
Ocp-Apim-Subscription-Key: {key}

{
  "urlSource": "https://storage.blob.core.windows.net/invoices/sample-invoice.pdf"
}
```

**Alternative — send document bytes directly:**

```http
POST https://{endpoint}/documentintelligence/documentModels/prebuilt-invoice:analyze?api-version=2024-11-30
Content-Type: application/pdf
Ocp-Apim-Subscription-Key: {key}

<binary PDF content>
```

**Response (202 Accepted):**

```http
HTTP/1.1 202 Accepted
Operation-Location: https://{endpoint}/documentintelligence/documentModels/prebuilt-invoice/analyzeResults/{resultId}?api-version=2024-11-30
```

### Step 2: Poll for Results (GET)

Poll the `Operation-Location` URL until `status` equals `succeeded` (or `failed`):

```http
GET https://{endpoint}/documentintelligence/documentModels/prebuilt-invoice/analyzeResults/{resultId}?api-version=2024-11-30
Ocp-Apim-Subscription-Key: {key}
```

**Response (while processing):**

```json
{
  "status": "running",
  "createdDateTime": "2024-03-20T10:30:00Z",
  "lastUpdatedDateTime": "2024-03-20T10:30:02Z"
}
```

**Response (when complete):**

```json
{
  "status": "succeeded",
  "createdDateTime": "2024-03-20T10:30:00Z",
  "lastUpdatedDateTime": "2024-03-20T10:30:05Z",
  "analyzeResult": {
    "apiVersion": "2024-11-30",
    "modelId": "prebuilt-invoice",
    "content": "Full extracted text...",
    "pages": [ ... ],
    "tables": [ ... ],
    "documents": [
      {
        "docType": "invoice",
        "fields": {
          "VendorName": { "type": "string", "valueString": "Contoso Ltd.", "confidence": 0.95 },
          "InvoiceTotal": { "type": "currency", "valueCurrency": { "amount": 1627.50, "currencyCode": "USD" }, "confidence": 0.92 },
          "InvoiceDate": { "type": "date", "valueDate": "2024-03-15", "confidence": 0.97 }
        },
        "confidence": 0.94
      }
    ]
  }
}
```

> **EXAM TIP:** The async polling pattern is critical. Step 1: POST to the analyze endpoint → receive `Operation-Location` header (HTTP 202). Step 2: GET the Operation-Location URL → poll until `status` is `"succeeded"`. The status values are: `notStarted`, `running`, `succeeded`, `failed`. This two-step pattern applies to ALL Document Intelligence operations.

### Response Structure

The `analyzeResult` object contains:

| Property | Description |
|----------|-------------|
| `content` | Full extracted text as a single string |
| `pages` | Array of page objects with dimensions, lines, words, spans |
| `pages[].lines` | Lines of text with bounding polygons |
| `pages[].words` | Individual words with confidence scores |
| `tables` | Extracted tables with rows, columns, and cells |
| `keyValuePairs` | Key-value pairs (for layout/document models) |
| `documents` | Extracted document fields (for prebuilt/custom models) |
| `documents[].fields` | Named fields with values and confidence scores |

---

## 4. Analyze via Python SDK

The Python SDK provides a higher-level interface that abstracts the async polling pattern into a simple method call.

### Setup

```bash
pip install azure-ai-documentintelligence
```

### Analyze an Invoice

```python
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.core.credentials import AzureKeyCredential

endpoint = "https://my-doc-intelligence.cognitiveservices.azure.com/"
key = "<your-key>"

client = DocumentIntelligenceClient(endpoint, AzureKeyCredential(key))

# Analyze from URL
poller = client.begin_analyze_document(
    "prebuilt-invoice",
    AnalyzeDocumentRequest(url_source="https://storage.blob.core.windows.net/invoices/sample.pdf")
)

result = poller.result()  # Blocks until analysis is complete

# Iterate over extracted invoices
for document in result.documents:
    print(f"Document type: {document.doc_type}")
    print(f"Document confidence: {document.confidence:.2f}")

    vendor = document.fields.get("VendorName")
    if vendor:
        print(f"Vendor: {vendor.value_string} (confidence: {vendor.confidence:.2f})")

    total = document.fields.get("InvoiceTotal")
    if total:
        print(f"Total: {total.value_currency.amount} {total.value_currency.currency_code}")

    invoice_date = document.fields.get("InvoiceDate")
    if invoice_date:
        print(f"Date: {invoice_date.value_date}")

    # Extract line items
    items = document.fields.get("Items")
    if items:
        for idx, item in enumerate(items.value_list):
            item_fields = item.value_object
            desc = item_fields.get("Description")
            amount = item_fields.get("Amount")
            print(f"  Item {idx+1}: {desc.value_string if desc else 'N/A'} "
                  f"- ${amount.value_currency.amount if amount else 'N/A'}")
```

### Analyze a Receipt

```python
# Analyze from a local file
with open("receipt.jpg", "rb") as f:
    poller = client.begin_analyze_document(
        "prebuilt-receipt",
        analyze_request=f,
        content_type="application/octet-stream"
    )

result = poller.result()

for document in result.documents:
    merchant = document.fields.get("MerchantName")
    total = document.fields.get("Total")
    date = document.fields.get("TransactionDate")

    print(f"Merchant: {merchant.value_string if merchant else 'N/A'}")
    print(f"Total: {total.value_currency.amount if total else 'N/A'}")
    print(f"Date: {date.value_date if date else 'N/A'}")

    items = document.fields.get("Items")
    if items:
        for item in items.value_list:
            item_fields = item.value_object
            name = item_fields.get("Description")
            price = item_fields.get("TotalPrice")
            print(f"  - {name.value_string if name else 'N/A'}: "
                  f"${price.value_currency.amount if price else 'N/A'}")
```

### Analyze with a Custom Model

```python
custom_model_id = "my-custom-model-id"

poller = client.begin_analyze_document(
    custom_model_id,
    AnalyzeDocumentRequest(url_source="https://storage.blob.core.windows.net/docs/custom-doc.pdf")
)

result = poller.result()

for document in result.documents:
    print(f"Doc type: {document.doc_type}")
    print(f"Confidence: {document.confidence:.2f}")
    for field_name, field_value in document.fields.items():
        print(f"  {field_name}: {field_value.content} "
              f"(confidence: {field_value.confidence:.2f})")
```

### List and Manage Custom Models

```python
# List all models
models = client.list_models()
for model in models:
    print(f"Model ID: {model.model_id}, Created: {model.created_date_time}")

# Get a specific model's details
model_info = client.get_model(model_id="my-custom-model-id")
print(f"Model ID: {model_info.model_id}")
print(f"Description: {model_info.description}")
print(f"Created: {model_info.created_date_time}")
if model_info.doc_types:
    for doc_type, doc_type_info in model_info.doc_types.items():
        print(f"  Doc type: {doc_type}")
        for field_name, field_info in doc_type_info.field_schema.items():
            print(f"    Field: {field_name} ({field_info['type']})")

# Delete a model
client.delete_model(model_id="old-model-id")
```

> **EXAM TIP:** The SDK method `begin_analyze_document()` returns a **long-running operation (LRO)** poller. Calling `.result()` on the poller blocks until the operation completes. This is the SDK equivalent of the REST async polling pattern. You do NOT need to manually poll in the SDK.

---

## 5. Custom Models

When prebuilt models don't cover your specific document types, you can train custom models using your own labeled data.

### Labeling Documents

Use Document Intelligence Studio to label your training documents:

1. Upload documents to an Azure Blob Storage container.
2. Open Document Intelligence Studio and create a new custom model project.
3. Connect to the storage container.
4. Draw bounding regions around fields in each document.
5. Assign a label (field name) to each region.
6. Repeat for all training documents.

### Training Data Requirements

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| **Labeled documents** | 5 | 15+ |
| **File formats** | PDF, JPEG, PNG, BMP, TIFF | PDF preferred |
| **Max file size** | 500 MB (S0) | — |
| **Max total training data** | 50,000 pages | — |
| **Same document type** | Yes | Yes |

### Template vs Neural Custom Models

| Feature | Template Model | Neural Model |
|---------|---------------|-------------|
| **Layout type** | Fixed/structured layouts | Variable/unstructured layouts |
| **Training speed** | Faster (seconds to minutes) | Slower (minutes to hours) |
| **Accuracy on fixed forms** | Very high | High |
| **Accuracy on variable layouts** | Low | High |
| **Min training docs** | 5 | 5 |
| **Language support** | 100+ languages | Expanding (fewer than template) |
| **Use case** | Government forms, tax forms, standardized applications | Contracts, letters, invoices with varying formats |
| **Training compute** | Included | Uses training hours (billing) |

> **EXAM TIP:** Choose **template models** for documents with a consistent, fixed layout (e.g., a specific tax form where fields are always in the same position). Choose **neural models** for documents with variable layouts (e.g., invoices from different vendors). Neural models are more flexible but take longer to train.

### Training a Custom Model (REST)

```http
POST https://{endpoint}/documentintelligence/documentModels:build?api-version=2024-11-30
Content-Type: application/json
Ocp-Apim-Subscription-Key: {key}

{
  "modelId": "my-custom-invoice",
  "description": "Custom invoice model for Contoso suppliers",
  "buildMode": "neural",
  "azureBlobSource": {
    "containerUrl": "https://mystorage.blob.core.windows.net/training-data?sv=...",
    "prefix": "invoices/"
  }
}
```

- `buildMode` values: `"template"` or `"neural"`
- The container must include the labeled documents and their `.ocr.json` and `.labels.json` files generated by Document Intelligence Studio.

### Confidence Scores

Every extracted field includes a confidence score between 0 and 1:

| Score Range | Interpretation | Action |
|-------------|---------------|--------|
| 0.90 – 1.00 | High confidence | Accept automatically |
| 0.70 – 0.89 | Medium confidence | Review if critical |
| Below 0.70 | Low confidence | Manual review recommended |

```python
for field_name, field in document.fields.items():
    confidence = field.confidence
    if confidence >= 0.9:
        # Auto-accept
        process_field(field_name, field.content)
    elif confidence >= 0.7:
        # Flag for review
        flag_for_review(field_name, field.content, confidence)
    else:
        # Manual review required
        require_manual_review(field_name, field.content, confidence)
```

> **EXAM TIP:** Confidence scores are available at both the **field level** and the **document level**. A document-level confidence score indicates how well the model was able to identify the document type. Field-level scores indicate extraction accuracy for individual fields. Design your application to handle low-confidence extractions with human review workflows.

---

## 6. Composed Models

A composed model combines multiple custom models into a single model endpoint. When a document is submitted, the composed model automatically routes it to the most appropriate component model based on document type classification.

### How Composed Models Work

1. You train individual custom models for different document types (e.g., invoice Model A, invoice Model B, purchase order Model C).
2. You compose them into a single model.
3. When a document is submitted, the composed model:
   - Analyzes the document against all component models.
   - Selects the best-matching model based on confidence.
   - Returns results from that model.

### Creating a Composed Model (REST)

```http
POST https://{endpoint}/documentintelligence/documentModels:compose?api-version=2024-11-30
Content-Type: application/json
Ocp-Apim-Subscription-Key: {key}

{
  "modelId": "composed-procurement-model",
  "description": "Handles invoices, POs, and receipts",
  "componentModels": [
    { "modelId": "custom-invoice-model" },
    { "modelId": "custom-purchase-order-model" },
    { "modelId": "custom-receipt-model" }
  ]
}
```

### Creating a Composed Model (Python SDK)

```python
component_models = [
    {"modelId": "custom-invoice-model"},
    {"modelId": "custom-purchase-order-model"},
    {"modelId": "custom-receipt-model"}
]

poller = client.begin_compose_model(
    compose_request={
        "modelId": "composed-procurement-model",
        "description": "Handles invoices, POs, and receipts",
        "componentModels": component_models
    }
)

composed_model = poller.result()
print(f"Composed model ID: {composed_model.model_id}")
print(f"Component models: {len(composed_model.doc_types)} doc types")
```

### Composed Model Limits

| Limit | Value |
|-------|-------|
| **Max component models** | 200 |
| **Nesting** | Composed models cannot contain other composed models |
| **Tier** | Standard (S0) tier only |

> **EXAM TIP:** A composed model can contain up to **200 component models**. When you submit a document to a composed model, it classifies the document first and then applies the most appropriate component model. The response includes a `docType` field indicating which component model was selected. Composed models are **not available on the Free tier**.

### Use Cases for Composed Models

| Scenario | Approach |
|----------|----------|
| Processing invoices from multiple vendors | Train a custom model per vendor layout, compose into one |
| Handling mixed document mailboxes | Train models for each doc type (invoice, PO, receipt), compose |
| Regional variations | Train models for each regional format, compose |
| Multi-language documents | Train models for different languages, compose |

---

## 7. File Limits and Supported Formats

### Size Limits by Tier

| Limit | Free (F0) | Standard (S0) |
|-------|-----------|---------------|
| **Max file size** | 4 MB | 500 MB |
| **Max pages per document** | 2 | 2,000 |
| **Max images per page** | — | 2,000 |

### Supported File Formats

| Format | Extensions | Notes |
|--------|-----------|-------|
| **PDF** | `.pdf` | Most common; text and scanned |
| **JPEG** | `.jpg`, `.jpeg` | Photos and scanned images |
| **PNG** | `.png` | Screenshots and graphics |
| **BMP** | `.bmp` | Bitmap images |
| **TIFF** | `.tif`, `.tiff` | Multi-page scanned documents |
| **HEIF** | `.heif` | High-efficiency image format |
| **DOCX** | `.docx` | Microsoft Word documents |
| **XLSX** | `.xlsx` | Microsoft Excel spreadsheets |
| **PPTX** | `.pptx` | Microsoft PowerPoint presentations |
| **HTML** | `.html` | Web pages |

> **EXAM TIP:** For the Free tier, the limits are **4 MB** file size and **2 pages** per document. For Standard tier, it's **500 MB** and **2,000 pages**. Know these limits for questions about which tier to select or why an analysis might fail.

---

## 8. Service Naming and Synonyms

Azure AI Document Intelligence has undergone naming changes:

| Period | Name | SDK Package |
|--------|------|-------------|
| Before 2023 | Azure Form Recognizer | `azure-ai-formrecognizer` |
| 2023+ | Azure AI Document Intelligence | `azure-ai-documentintelligence` |

> **EXAM TIP:** The exam may reference either "Form Recognizer" or "Document Intelligence" — they are the **same service**. The Azure resource `kind` in ARM templates is still `FormRecognizer`. The Python SDK package was renamed from `azure-ai-formrecognizer` to `azure-ai-documentintelligence`. Be prepared for questions using either name.

### SDK Mapping

| Language | Old Package | New Package |
|----------|------------|-------------|
| Python | `azure-ai-formrecognizer` | `azure-ai-documentintelligence` |
| .NET | `Azure.AI.FormRecognizer` | `Azure.AI.DocumentIntelligence` |
| Java | `azure-ai-formrecognizer` | `azure-ai-documentintelligence` |
| JavaScript | `@azure/ai-form-recognizer` | `@azure-rest/ai-document-intelligence` |

---

## 9. REST Code Examples

### POST: Submit Analysis Request

```http
POST https://{endpoint}/documentintelligence/documentModels/prebuilt-receipt:analyze?api-version=2024-11-30
Content-Type: application/json
Ocp-Apim-Subscription-Key: {key}

{
  "urlSource": "https://storage.blob.core.windows.net/receipts/sample-receipt.jpg"
}
```

**Response Headers:**

```
HTTP/1.1 202 Accepted
Operation-Location: https://{endpoint}/documentintelligence/documentModels/prebuilt-receipt/analyzeResults/abc123?api-version=2024-11-30
```

### GET: Poll for Results

```http
GET https://{endpoint}/documentintelligence/documentModels/prebuilt-receipt/analyzeResults/abc123?api-version=2024-11-30
Ocp-Apim-Subscription-Key: {key}
```

**Response (succeeded):**

```json
{
  "status": "succeeded",
  "analyzeResult": {
    "modelId": "prebuilt-receipt",
    "content": "Contoso Coffee\n789 Pine St...",
    "pages": [
      {
        "pageNumber": 1,
        "width": 8.5,
        "height": 11,
        "unit": "inch",
        "lines": [
          {
            "content": "Contoso Coffee",
            "polygon": [0.5, 0.5, 3.0, 0.5, 3.0, 0.8, 0.5, 0.8]
          }
        ],
        "words": [
          {
            "content": "Contoso",
            "confidence": 0.98,
            "polygon": [0.5, 0.5, 1.5, 0.5, 1.5, 0.8, 0.5, 0.8]
          }
        ]
      }
    ],
    "documents": [
      {
        "docType": "receipt.retailMeal",
        "confidence": 0.95,
        "fields": {
          "MerchantName": {
            "type": "string",
            "valueString": "Contoso Coffee",
            "confidence": 0.97
          },
          "Total": {
            "type": "currency",
            "valueCurrency": {
              "amount": 15.56,
              "currencyCode": "USD"
            },
            "confidence": 0.93
          }
        }
      }
    ]
  }
}
```

---

## 10. Complete Analysis Workflow Example

Here is a complete end-to-end example showing the full workflow from submitting a document to extracting structured data:

```python
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.core.credentials import AzureKeyCredential
import json

endpoint = "https://my-doc-intelligence.cognitiveservices.azure.com/"
key = "<your-key>"

client = DocumentIntelligenceClient(endpoint, AzureKeyCredential(key))

# --- Analyze an invoice ---
invoice_url = "https://storage.blob.core.windows.net/invoices/sample-invoice.pdf"

poller = client.begin_analyze_document(
    "prebuilt-invoice",
    AnalyzeDocumentRequest(url_source=invoice_url)
)
result = poller.result()

# --- Extract page-level information ---
for page in result.pages:
    print(f"Page {page.page_number}: {page.width}x{page.height} {page.unit}")
    print(f"  Lines: {len(page.lines)}")
    print(f"  Words: {len(page.words)}")

# --- Extract tables ---
if result.tables:
    for table_idx, table in enumerate(result.tables):
        print(f"\nTable {table_idx}: {table.row_count} rows x {table.column_count} columns")
        for cell in table.cells:
            print(f"  [{cell.row_index},{cell.column_index}]: {cell.content}")

# --- Extract document fields ---
for doc in result.documents:
    print(f"\nDocument type: {doc.doc_type}")
    print(f"Document confidence: {doc.confidence:.2f}")

    for field_name, field in doc.fields.items():
        value = field.content or field.value_string or str(field.value_currency) if hasattr(field, 'value_currency') else "N/A"
        print(f"  {field_name}: {value} (confidence: {field.confidence:.2f})")
```

---

## Key Takeaways

1. **Service Naming** — Document Intelligence was formerly Form Recognizer. The ARM resource kind is still `FormRecognizer`. Know both names for the exam.

2. **Prebuilt Models** — Use the right model for the document type: `prebuilt-invoice` for invoices, `prebuilt-receipt` for receipts, `prebuilt-idDocument` for IDs, etc. `prebuilt-read` is for text-only extraction; `prebuilt-layout` adds tables and structure.

3. **Async Polling Pattern** — POST to analyze → receive `Operation-Location` header → GET and poll until `status: "succeeded"`. This is the standard pattern for ALL Document Intelligence operations.

4. **SDK Convenience** — `begin_analyze_document()` returns a poller; call `.result()` to get the completed analysis. The SDK handles the polling automatically.

5. **Custom Models** — Minimum 5 labeled documents (15+ recommended). Template models for fixed layouts, neural models for variable layouts.

6. **Composed Models** — Combine up to 200 custom models into one endpoint. Automatic document type routing. S0 tier only.

7. **Confidence Scores** — Available at field and document level. Design human review workflows for low-confidence extractions.

8. **File Limits** — Free: 4 MB / 2 pages. Standard: 500 MB / 2,000 pages.

---

## Further Reading

- [Azure AI Document Intelligence documentation](https://learn.microsoft.com/azure/ai-services/document-intelligence/)
- [Prebuilt models overview](https://learn.microsoft.com/azure/ai-services/document-intelligence/concept-model-overview)
- [Custom models](https://learn.microsoft.com/azure/ai-services/document-intelligence/concept-custom)
- [Composed models](https://learn.microsoft.com/azure/ai-services/document-intelligence/concept-composed-models)
- [Document Intelligence Studio](https://documentintelligence.ai.azure.com/)
- [REST API reference](https://learn.microsoft.com/rest/api/aiservices/document-intelligence)
- [Python SDK reference](https://learn.microsoft.com/python/api/overview/azure/ai-documentintelligence-readme)
