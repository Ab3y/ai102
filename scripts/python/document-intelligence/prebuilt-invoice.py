"""
AI-102 Lab 6.2: Document Intelligence – Prebuilt Invoice Model
================================================================
Exam Objective: Implement knowledge mining and document intelligence
  - Use prebuilt models to extract data from documents
  - Analyze invoices, receipts, ID documents
  - Understand the async polling pattern

This script demonstrates:
  1. Analyzing an invoice with the prebuilt-invoice model
  2. Extracting structured fields (vendor, customer, line items, totals)
  3. The async polling pattern (begin_analyze → poll → result)
  4. Handling different input sources (URL, file, bytes)

Prerequisites:
  - pip install azure-ai-formrecognizer python-dotenv
  - An Azure Document Intelligence (Form Recognizer) resource
  - .env file with DOCUMENT_INTELLIGENCE_ENDPOINT and DOCUMENT_INTELLIGENCE_KEY

EXAM TIP: File size limits –
  - Free (F0) tier: 4 MB per document
  - Standard (S0) tier: 500 MB per document
  - Max pages: 2,000 for standard tier
  - Supported formats: PDF, JPEG, PNG, BMP, TIFF, HEIF, DOCX, XLSX, PPTX, HTML
"""

import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
load_dotenv()

ENDPOINT = os.getenv("DOCUMENT_INTELLIGENCE_ENDPOINT")
API_KEY = os.getenv("DOCUMENT_INTELLIGENCE_KEY")

if not ENDPOINT or not API_KEY:
    raise EnvironmentError(
        "Set DOCUMENT_INTELLIGENCE_ENDPOINT and DOCUMENT_INTELLIGENCE_KEY "
        "in your .env file."
    )

client = DocumentAnalysisClient(
    endpoint=ENDPOINT,
    credential=AzureKeyCredential(API_KEY),
)

# Sample invoice URL (Microsoft sample)
SAMPLE_INVOICE_URL = (
    "https://raw.githubusercontent.com/Azure/azure-sdk-for-python/main/"
    "sdk/formrecognizer/azure-ai-formrecognizer/tests/sample_forms/"
    "forms/Invoice_1.pdf"
)


# ===========================================================================
# 1. Analyze invoice from URL
# ===========================================================================
def analyze_invoice_from_url():
    """
    Analyze an invoice using the prebuilt-invoice model.

    EXAM TIP: Prebuilt models available –
      prebuilt-invoice:    Invoices
      prebuilt-receipt:    Receipts
      prebuilt-idDocument: ID documents (driver's license, passport)
      prebuilt-businessCard: Business cards
      prebuilt-tax.us.w2:  US W-2 tax forms
      prebuilt-read:       OCR (text extraction only)
      prebuilt-layout:     Tables, selection marks, structure
      prebuilt-document:   General key-value pairs
    """
    print("=" * 60)
    print("1. ANALYZE INVOICE FROM URL")
    print("=" * 60)

    try:
        # begin_analyze_document_from_url returns a poller (async pattern)
        print(f"  Analyzing: {SAMPLE_INVOICE_URL[:60]}...")
        poller = client.begin_analyze_document_from_url(
            model_id="prebuilt-invoice",
            document_url=SAMPLE_INVOICE_URL,
        )

        # Poll for completion (the SDK handles this automatically)
        print("  ⏳ Polling for results...")
        result = poller.result()

        print(f"  ✅ Analysis complete. Documents found: {len(result.documents)}")

        for doc_idx, document in enumerate(result.documents):
            print(f"\n  --- Invoice {doc_idx + 1} ---")
            print(f"  Document type: {document.doc_type}")
            print(f"  Confidence: {document.confidence:.2%}")

            fields = document.fields

            # Extract key invoice fields
            extract_field(fields, "VendorName", "Vendor Name")
            extract_field(fields, "VendorAddress", "Vendor Address")
            extract_field(fields, "CustomerName", "Customer Name")
            extract_field(fields, "CustomerAddress", "Customer Address")
            extract_field(fields, "InvoiceId", "Invoice ID")
            extract_field(fields, "InvoiceDate", "Invoice Date")
            extract_field(fields, "DueDate", "Due Date")
            extract_field(fields, "SubTotal", "Subtotal")
            extract_field(fields, "TotalTax", "Total Tax")
            extract_field(fields, "InvoiceTotal", "Invoice Total")
            extract_field(fields, "PurchaseOrder", "Purchase Order")

            # Extract line items (table-like data)
            items_field = fields.get("Items")
            if items_field and items_field.value:
                print(f"\n  Line Items ({len(items_field.value)}):")
                for item_idx, item in enumerate(items_field.value):
                    item_fields = item.value
                    desc = get_field_value(item_fields, "Description")
                    qty = get_field_value(item_fields, "Quantity")
                    unit_price = get_field_value(item_fields, "UnitPrice")
                    amount = get_field_value(item_fields, "Amount")
                    print(
                        f"    [{item_idx + 1}] {desc:<30} "
                        f"qty={qty}  unit=${unit_price}  total=${amount}"
                    )

    except Exception as exc:
        print(f"  Error: {exc}")


def extract_field(fields: dict, field_name: str, display_name: str):
    """Helper to safely extract and print a field value."""
    field = fields.get(field_name)
    if field:
        value = field.content or field.value
        confidence = field.confidence
        print(f"  {display_name:<20}: {value}  (confidence: {confidence:.2%})")


def get_field_value(fields: dict, field_name: str):
    """Helper to get a field value or 'N/A'."""
    if not fields:
        return "N/A"
    field = fields.get(field_name)
    return (field.content or field.value) if field else "N/A"


# ===========================================================================
# 2. Analyze invoice from local file
# ===========================================================================
def analyze_invoice_from_file():
    """
    Analyze a local invoice file.

    EXAM TIP: Use begin_analyze_document() for local files (pass bytes).
    Use begin_analyze_document_from_url() for URLs.
    """
    print("\n" + "=" * 60)
    print("2. ANALYZE INVOICE FROM LOCAL FILE")
    print("=" * 60)

    local_file = os.path.join(os.path.dirname(__file__), "sample-invoice.pdf")

    if not os.path.exists(local_file):
        print(f"  Skipped – File not found: {local_file}")
        print("  Place a PDF invoice at this path to test local file analysis.\n")
        return

    try:
        with open(local_file, "rb") as f:
            poller = client.begin_analyze_document(
                model_id="prebuilt-invoice",
                document=f,
            )

        result = poller.result()
        print(f"  ✅ Analyzed {len(result.documents)} document(s) from file.\n")

        for document in result.documents:
            fields = document.fields
            vendor = get_field_value(fields, "VendorName")
            total = get_field_value(fields, "InvoiceTotal")
            print(f"  Vendor: {vendor}, Total: {total}")

    except Exception as exc:
        print(f"  Error: {exc}")


# ===========================================================================
# 3. Layout analysis (tables and structure)
# ===========================================================================
def analyze_layout():
    """
    Use prebuilt-layout to extract tables, selection marks, and structure.

    EXAM TIP: Layout model extracts:
      - Pages (dimensions, angle/rotation)
      - Tables (rows, columns, cells with spans)
      - Selection marks (checkboxes, radio buttons)
      - Paragraphs and sections
    """
    print("\n" + "=" * 60)
    print("3. LAYOUT ANALYSIS (tables and structure)")
    print("=" * 60)

    try:
        poller = client.begin_analyze_document_from_url(
            model_id="prebuilt-layout",
            document_url=SAMPLE_INVOICE_URL,
        )
        result = poller.result()

        # Page information
        for page in result.pages:
            print(f"\n  Page {page.page_number}:")
            print(f"    Dimensions: {page.width} x {page.height} ({page.unit})")
            print(f"    Lines: {len(page.lines)}")
            print(f"    Words: {len(page.words)}")

            # Print first few lines
            for line in page.lines[:5]:
                print(f"    Line: \"{line.content}\"")

        # Table information
        if result.tables:
            print(f"\n  Tables found: {len(result.tables)}")
            for table_idx, table in enumerate(result.tables):
                print(
                    f"    Table {table_idx + 1}: "
                    f"{table.row_count} rows × {table.column_count} columns"
                )
                # Print first few cells
                for cell in table.cells[:6]:
                    print(
                        f"      [{cell.row_index},{cell.column_index}] "
                        f"\"{cell.content[:30]}\""
                    )
        else:
            print("\n  No tables found.")

    except Exception as exc:
        print(f"  Error: {exc}")


# ===========================================================================
# Main
# ===========================================================================
if __name__ == "__main__":
    print("\nAI-102 Lab 6.2 – Document Intelligence (Prebuilt Invoice)\n")

    analyze_invoice_from_url()
    analyze_invoice_from_file()
    analyze_layout()

    # EXAM TIPS:
    # ──────────
    # • Prebuilt models: invoice, receipt, idDocument, businessCard,
    #   read, layout, document, tax forms.
    # • Custom models: train your own for domain-specific documents.
    # • Composed models: combine multiple custom models.
    # • Async pattern: begin_analyze_document → poller → result().
    # • File size: 4 MB (free), 500 MB (standard).
    # • Supported formats: PDF, JPEG, PNG, BMP, TIFF, HEIF, DOCX, etc.
    # • Layout model: tables, selection marks, paragraphs.
    # • Invoice model extracts: vendor, customer, line items, totals.
    # • Each field has a confidence score (0.0 to 1.0).
    # • Bounding regions (polygons) available for spatial information.
    # • SDK package name: azure-ai-formrecognizer (despite the service
    #   being renamed to "Document Intelligence").

    # CLEANUP NOTE:
    # Document Intelligence charges per page analyzed.
    # Delete the resource when no longer needed.
