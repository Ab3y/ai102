# Lesson 3: Manage, Monitor, and Secure AI Services

## Learning Objectives

- Configure Azure Monitor and Log Analytics for AI services
- Set up diagnostic settings and alerts
- Manage costs and quotas for AI resources
- Implement key rotation using the two-key pattern
- Secure AI services with managed identity, RBAC, Key Vault, and Private Link
- Configure network security for AI endpoints

---

## Monitoring with Azure Monitor

### What Gets Monitored

Azure AI services emit metrics and logs that can be captured by Azure Monitor:

| Data Type | Examples | Destination |
|-----------|----------|-------------|
| **Platform metrics** | Total calls, latency, errors, data in/out | Azure Monitor Metrics (automatic) |
| **Resource logs** | Individual API requests, response codes, durations | Log Analytics (requires diagnostic setting) |
| **Activity logs** | Resource creation, configuration changes, RBAC changes | Azure Monitor (automatic) |

### Key Metrics for AI Services

| Metric | Description | Alert Threshold Example |
|--------|-------------|----------------------|
| `TotalCalls` | Number of API calls | Spike detection |
| `SuccessfulCalls` | Calls returning 2xx | Drop below baseline |
| `TotalErrors` | Calls returning 4xx/5xx | > 5% error rate |
| `Latency` | Response time in ms | P95 > 2000ms |
| `TokenTransaction` | Tokens consumed (OpenAI) | Budget threshold |
| `ProcessedCount` | Items processed | Throughput monitoring |

### Configuring Diagnostic Settings

Diagnostic settings route resource logs to one or more destinations:

```bash
# Enable diagnostic settings via CLI
az monitor diagnostic-settings create \
    --name ai-diagnostics \
    --resource /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.CognitiveServices/accounts/{name} \
    --logs '[{"category": "Audit", "enabled": true}, {"category": "RequestResponse", "enabled": true}]' \
    --metrics '[{"category": "AllMetrics", "enabled": true}]' \
    --workspace /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.OperationalInsights/workspaces/{workspace}
```

### Bicep — Diagnostic Settings

```bicep
resource diagnostics 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = {
  name: 'ai-diagnostics'
  scope: aiServices
  properties: {
    workspaceId: logAnalyticsWorkspace.id
    logs: [
      {
        category: 'Audit'
        enabled: true
      }
      {
        category: 'RequestResponse'
        enabled: true
      }
    ]
    metrics: [
      {
        category: 'AllMetrics'
        enabled: true
      }
    ]
  }
}
```

### Log Analytics — Sample KQL Queries

```kusto
// API call volume by operation over time
AzureDiagnostics
| where ResourceProvider == "MICROSOFT.COGNITIVESERVICES"
| summarize count() by OperationName, bin(TimeGenerated, 1h)
| render timechart

// Error rate by status code
AzureDiagnostics
| where ResourceProvider == "MICROSOFT.COGNITIVESERVICES"
| where ResultType != "Success"
| summarize ErrorCount = count() by ResultType, bin(TimeGenerated, 1h)

// Average latency by operation
AzureDiagnostics
| where ResourceProvider == "MICROSOFT.COGNITIVESERVICES"
| summarize AvgDuration = avg(DurationMs) by OperationName
| order by AvgDuration desc
```

---

## Setting Up Alerts

### Alert Types for AI Services

| Alert Type | Use Case | Example |
|------------|----------|---------|
| **Metric alert** | Threshold-based on metrics | Error rate > 5% |
| **Log alert** | KQL query-based on logs | Specific error pattern detected |
| **Activity log alert** | Resource configuration changes | Key regenerated |
| **Budget alert** | Cost threshold reached | 80% of monthly budget consumed |

### Creating a Metric Alert (CLI)

```bash
az monitor metrics alert create \
    --name "High Error Rate" \
    --resource-group rg-ai-services \
    --scopes /subscriptions/{sub}/resourceGroups/rg-ai-services/providers/Microsoft.CognitiveServices/accounts/my-ai \
    --condition "total TotalErrors > 100" \
    --window-size 5m \
    --evaluation-frequency 1m \
    --action-group /subscriptions/{sub}/resourceGroups/{rg}/providers/Microsoft.Insights/actionGroups/ops-team \
    --description "Alert when AI service errors exceed 100 in 5 minutes"
```

---

## Cost Management

### Understanding AI Services Pricing

| Service | Pricing Model | Example |
|---------|--------------|---------|
| Language Service | Per 1,000 text records | ~$1 per 1,000 records |
| Computer Vision | Per 1,000 transactions | ~$1 per 1,000 transactions |
| Azure OpenAI | Per 1,000 tokens (input/output) | GPT-4o: ~$5/$15 per 1M tokens |
| Speech | Per audio hour (STT) or per 1M characters (TTS) | Varies by voice |
| Document Intelligence | Per page | ~$1.50 per 1,000 pages |
| AI Search | Per index unit/hour + per query | ~$250/month for Basic tier |

### Cost Management Best Practices

1. **Set budgets**: Create Azure budgets with alerts at 50%, 80%, and 100%
2. **Use Free tier** (F0) for development and testing
3. **Monitor token usage** for Azure OpenAI — use `max_tokens` parameter
4. **Implement caching** to reduce redundant API calls
5. **Use batch APIs** where available (Language Service, Document Intelligence)

```bash
# Create a budget with alert
az consumption budget create \
    --budget-name ai-monthly-budget \
    --amount 500 \
    --resource-group rg-ai-services \
    --time-grain Monthly \
    --category Cost
```

---

## Key Management

### Two-Key Rotation Pattern

Every Azure AI service provides **two keys** (key1 and key2) to enable zero-downtime key rotation.

```
Rotation Steps:
1. Application uses Key1
2. Regenerate Key2 (Key2 is not in use — safe to regenerate)
3. Update application to use Key2
4. Verify application works with Key2
5. Regenerate Key1 (Key1 is no longer in use)
6. Key2 is now the active key; Key1 is the backup
```

```bash
# List current keys
az cognitiveservices account keys list \
    --name my-ai-services \
    --resource-group rg-ai-services

# Regenerate key2
az cognitiveservices account keys regenerate \
    --name my-ai-services \
    --resource-group rg-ai-services \
    --key-name key2

# After updating apps to use key2, regenerate key1
az cognitiveservices account keys regenerate \
    --name my-ai-services \
    --resource-group rg-ai-services \
    --key-name key1
```

> ### 📝 Exam Tip
> The two-key rotation pattern is a **frequently tested** topic. Know the exact steps: rotate the unused key first, switch applications to it, then rotate the previously active key.

---

## Managed Identity

Managed identity eliminates the need for API keys by using Azure AD tokens.

### System-Assigned Managed Identity

```bicep
resource aiServices 'Microsoft.CognitiveServices/accounts@2023-10-01-preview' = {
  name: 'my-ai-services'
  location: location
  kind: 'CognitiveServices'
  sku: { name: 'S0' }
  identity: {
    type: 'SystemAssigned'    // Enables managed identity
  }
  properties: {
    customSubDomainName: 'my-ai-services'
  }
}
```

### Using Managed Identity in Code

```python
from azure.identity import DefaultAzureCredential
from azure.ai.textanalytics import TextAnalyticsClient

# DefaultAzureCredential automatically uses managed identity in Azure
credential = DefaultAzureCredential()

client = TextAnalyticsClient(
    endpoint="https://my-ai-services.cognitiveservices.azure.com/",
    credential=credential
)

# No API key needed — authentication is handled by Azure AD
result = client.analyze_sentiment(["Managed identity is more secure!"])
```

> ### 📝 Exam Tip
> `customSubDomainName` is **required** when using Azure AD / managed identity authentication. Without it, only key-based authentication works.

---

## RBAC (Role-Based Access Control)

### Key Roles for AI Services

| Role | Permissions | Use Case |
|------|------------|----------|
| **Cognitive Services Contributor** | Full access to manage and use AI resources | Administrators |
| **Cognitive Services User** | Call APIs (read data plane) but not manage resources | Application service principals |
| **Cognitive Services OpenAI Contributor** | Manage OpenAI resources and deployments | OpenAI administrators |
| **Cognitive Services OpenAI User** | Use OpenAI API (completions, embeddings) | Applications using OpenAI |
| **Reader** | View resource configuration (no API access) | Auditors |

### Assigning RBAC Roles

```bash
# Assign "Cognitive Services User" to a managed identity
az role assignment create \
    --assignee <principal-id> \
    --role "Cognitive Services User" \
    --scope /subscriptions/{sub}/resourceGroups/rg-ai-services/providers/Microsoft.CognitiveServices/accounts/my-ai-services
```

```bicep
resource roleAssignment 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(aiServices.id, appIdentity.id, 'CognitiveServicesUser')
  scope: aiServices
  properties: {
    roleDefinitionId: subscriptionResourceId(
      'Microsoft.Authorization/roleDefinitions',
      'a97b65f3-24c7-4388-baec-2e87135dc908'  // Cognitive Services User
    )
    principalId: appIdentity.properties.principalId
    principalType: 'ServicePrincipal'
  }
}
```

---

## Key Vault Integration

Store AI service keys in Azure Key Vault instead of application configuration.

```python
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Retrieve AI service key from Key Vault
credential = DefaultAzureCredential()
vault_client = SecretClient(
    vault_url="https://my-keyvault.vault.azure.net/",
    credential=credential
)

ai_key = vault_client.get_secret("ai-services-key").value

# Use retrieved key for AI service
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

client = TextAnalyticsClient(
    endpoint="https://my-ai-services.cognitiveservices.azure.com/",
    credential=AzureKeyCredential(ai_key)
)
```

### Best Practice: Use Managed Identity Instead of Key Vault

```
Preference order (most to least secure):
1. Managed Identity (no secrets at all)           ← Best
2. Key Vault + Managed Identity (secrets managed)  ← Good
3. Environment variables with keys                  ← Acceptable for dev
4. Hardcoded keys in code                           ← Never do this
```

---

## Network Security

### Private Link / Private Endpoints

Private endpoints give your AI service a private IP address within your VNet.

```bash
# Disable public access
az cognitiveservices account update \
    --name my-ai-services \
    --resource-group rg-ai-services \
    --public-network-access Disabled

# Create private endpoint
az network private-endpoint create \
    --name ai-private-endpoint \
    --resource-group rg-ai-services \
    --vnet-name my-vnet \
    --subnet ai-subnet \
    --private-connection-resource-id /subscriptions/{sub}/resourceGroups/rg-ai-services/providers/Microsoft.CognitiveServices/accounts/my-ai-services \
    --group-id account \
    --connection-name ai-pe-connection
```

### Network Security Configuration (Bicep)

```bicep
resource aiServices 'Microsoft.CognitiveServices/accounts@2023-10-01-preview' = {
  name: 'my-ai-services'
  location: location
  kind: 'CognitiveServices'
  sku: { name: 'S0' }
  properties: {
    publicNetworkAccess: 'Disabled'
    networkAcls: {
      defaultAction: 'Deny'
      ipRules: [
        {
          value: '203.0.113.0/24'  // Allow specific IP range
        }
      ]
      virtualNetworkRules: [
        {
          id: subnet.id  // Allow specific subnet
        }
      ]
    }
  }
}
```

### Virtual Network Rules

| Configuration | Effect |
|--------------|--------|
| `publicNetworkAccess: Enabled` + no ACLs | Accessible from anywhere (default) |
| `publicNetworkAccess: Enabled` + IP rules | Accessible from listed IPs only |
| `publicNetworkAccess: Disabled` + Private Endpoint | Accessible only from VNet |
| `publicNetworkAccess: Disabled` + no Private Endpoint | Not accessible (locked out!) |

> ### 📝 Exam Tip
> If a question describes a "secure, isolated" deployment, the answer typically involves **Private Link + disabled public access + managed identity + Key Vault**. Know this full security stack.

---

## Key Takeaways

1. **Azure Monitor** provides metrics automatically; **diagnostic settings** must be configured to capture resource logs in Log Analytics.
2. **Two-key rotation**: Regenerate the unused key → switch app to new key → regenerate the old key. Zero downtime.
3. **Managed identity** with `DefaultAzureCredential` is the recommended authentication approach — requires `customSubDomainName` on the resource.
4. **RBAC roles**: `Cognitive Services User` for API access, `Contributor` for management, separate OpenAI-specific roles exist.
5. **Private Link** gives AI services a private IP in your VNet; combine with `publicNetworkAccess: Disabled` for full isolation.
6. **Key Vault** stores keys when managed identity isn't feasible; never hardcode keys.

---

## Further Reading

- [Monitor Azure AI services](https://learn.microsoft.com/en-us/azure/ai-services/diagnostic-logging)
- [Azure AI services security](https://learn.microsoft.com/en-us/azure/ai-services/security-features)
- [Configure virtual networks for AI services](https://learn.microsoft.com/en-us/azure/ai-services/cognitive-services-virtual-networks)
- [Use managed identities with AI services](https://learn.microsoft.com/en-us/azure/ai-services/authentication)
