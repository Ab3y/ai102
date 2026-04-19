"""
AI-102 Lab 1.2: Secure Access to Azure AI Services
====================================================
Exam Objective: Plan and manage an Azure AI solution
  - Manage account keys
  - Implement Azure Key Vault for AI service credentials
  - Manage authentication for an Azure AI Services resource
  - Configure managed identities for Azure AI Services

This script shows:
  1. INSECURE pattern – hardcoded/plain-text key (anti-pattern)
  2. SECURE pattern  – DefaultAzureCredential (managed identity / RBAC)
  3. SECURE pattern  – Key Vault secret retrieval for API keys

Prerequisites:
  - pip install azure-identity azure-keyvault-secrets azure-ai-textanalytics python-dotenv
  - A Key Vault with the AI Services key stored as a secret
  - App registration or managed identity with RBAC access
  - .env file with the required variables (see below)
"""

import os
from dotenv import load_dotenv

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
load_dotenv()

AI_SERVICES_ENDPOINT = os.getenv("AI_SERVICES_ENDPOINT")
AI_SERVICES_KEY = os.getenv("AI_SERVICES_KEY")           # only for demo
KEY_VAULT_NAME = os.getenv("KEY_VAULT_NAME")              # e.g., "mykeyvault"
KEY_VAULT_SECRET_NAME = os.getenv("KEY_VAULT_SECRET_NAME", "ai-services-key")


# ===========================================================================
# PATTERN 1 – INSECURE: Hardcoded / environment-variable key (anti-pattern)
# ===========================================================================
def insecure_pattern():
    """
    ⚠️  Anti-pattern shown for exam awareness only.
    Never commit API keys to source control or hardcode them.
    """
    print("=" * 60)
    print("PATTERN 1: INSECURE – Plain-text API key (anti-pattern)")
    print("=" * 60)

    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics import TextAnalyticsClient

    if not AI_SERVICES_ENDPOINT or not AI_SERVICES_KEY:
        print("  Skipped – AI_SERVICES_ENDPOINT / AI_SERVICES_KEY not set.\n")
        return

    try:
        # This works but is NOT recommended for production
        client = TextAnalyticsClient(
            endpoint=AI_SERVICES_ENDPOINT,
            credential=AzureKeyCredential(AI_SERVICES_KEY),
        )
        result = client.detect_language(documents=["Hello world"])
        lang = result[0].primary_language
        print(f"  Detected: {lang.name} ({lang.confidence_score:.0%})")
        print("  ⚠️  Key is exposed in code / env vars – rotate regularly!\n")

    except Exception as exc:
        print(f"  Error: {exc}\n")


# ===========================================================================
# PATTERN 2 – SECURE: DefaultAzureCredential (managed identity / RBAC)
# ===========================================================================
def secure_default_credential():
    """
    Best practice: use DefaultAzureCredential which tries, in order:
      1. EnvironmentCredential (AZURE_CLIENT_ID, etc.)
      2. ManagedIdentityCredential (system- or user-assigned MI)
      3. AzureCLICredential (az login)
      4. … and others

    EXAM TIP: To use token-based auth the resource must support Microsoft
    Entra ID (AAD) authentication AND the identity must have the correct
    RBAC role, e.g., "Cognitive Services User".
    """
    print("=" * 60)
    print("PATTERN 2: SECURE – DefaultAzureCredential (RBAC)")
    print("=" * 60)

    from azure.identity import DefaultAzureCredential
    from azure.ai.textanalytics import TextAnalyticsClient

    if not AI_SERVICES_ENDPOINT:
        print("  Skipped – AI_SERVICES_ENDPOINT not set.\n")
        return

    try:
        # No API key needed – identity-based authentication
        credential = DefaultAzureCredential()
        client = TextAnalyticsClient(
            endpoint=AI_SERVICES_ENDPOINT,
            credential=credential,
        )

        result = client.detect_language(documents=["Bonjour le monde"])
        lang = result[0].primary_language
        print(f"  Detected: {lang.name} ({lang.confidence_score:.0%})")
        print("  ✅ No key in code – identity authenticated via RBAC.\n")

    except Exception as exc:
        # Common error: identity lacks "Cognitive Services User" role
        print(f"  Error: {exc}")
        print("  Hint: Assign 'Cognitive Services User' role to the identity.\n")


# ===========================================================================
# PATTERN 3 – SECURE: Retrieve key from Azure Key Vault
# ===========================================================================
def secure_key_vault():
    """
    Store the API key as a Key Vault secret and retrieve it at runtime.
    The application identity needs the "Key Vault Secrets User" role or
    a Key Vault access policy with GET permission.

    EXAM TIP: Key Vault supports two permission models:
      - Vault access policy (legacy)
      - Azure RBAC (recommended)
    """
    print("=" * 60)
    print("PATTERN 3: SECURE – Key Vault secret retrieval")
    print("=" * 60)

    from azure.identity import DefaultAzureCredential
    from azure.keyvault.secrets import SecretClient
    from azure.core.credentials import AzureKeyCredential
    from azure.ai.textanalytics import TextAnalyticsClient

    if not KEY_VAULT_NAME or not AI_SERVICES_ENDPOINT:
        print("  Skipped – KEY_VAULT_NAME / AI_SERVICES_ENDPOINT not set.\n")
        return

    try:
        # Step 1: Authenticate to Key Vault with DefaultAzureCredential
        credential = DefaultAzureCredential()
        vault_url = f"https://{KEY_VAULT_NAME}.vault.azure.net"
        secret_client = SecretClient(vault_url=vault_url, credential=credential)

        # Step 2: Retrieve the API key stored as a secret
        secret = secret_client.get_secret(KEY_VAULT_SECRET_NAME)
        api_key = secret.value
        print(f"  Retrieved secret '{KEY_VAULT_SECRET_NAME}' from Key Vault.")

        # Step 3: Use the retrieved key to call AI Services
        text_client = TextAnalyticsClient(
            endpoint=AI_SERVICES_ENDPOINT,
            credential=AzureKeyCredential(api_key),
        )

        result = text_client.detect_language(documents=["Hallo Welt"])
        lang = result[0].primary_language
        print(f"  Detected: {lang.name} ({lang.confidence_score:.0%})")
        print("  ✅ Key retrieved from Key Vault – never in source code.\n")

    except Exception as exc:
        print(f"  Error: {exc}")
        print("  Hint: Ensure 'Key Vault Secrets User' role is assigned.\n")


# ===========================================================================
# Main
# ===========================================================================
if __name__ == "__main__":
    print("\nAI-102 Lab 1.2 – Secure Access to Azure AI Services\n")

    insecure_pattern()
    secure_default_credential()
    secure_key_vault()

    # EXAM TIPS SUMMARY:
    # ──────────────────
    # • Prefer managed identity + RBAC over API keys.
    # • DefaultAzureCredential chains multiple credential types automatically.
    # • RBAC role "Cognitive Services User" grants invoke access (no mgmt).
    # • RBAC role "Cognitive Services Contributor" grants management access.
    # • Key Vault RBAC role "Key Vault Secrets User" allows reading secrets.
    # • Rotate keys regularly (two keys allow zero-downtime rotation).
    # • Network restrictions (VNet, private endpoints) add another layer.

    # CLEANUP NOTE:
    # Delete test Key Vault secrets and revoke test RBAC assignments when done.
