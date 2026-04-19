<#
.SYNOPSIS
    Deploy an Azure AI Services container to Azure Container Instances.
.DESCRIPTION
    Pulls a Cognitive Services container image and deploys it to ACI
    with proper billing endpoint and API key configuration.
.NOTES
    AI-102 Module 1 — Lab 1.4: Deploy AI Services in Containers
    EXAM TIP: Know the required env vars (ApiKey, Billing, Eula)
#>

param(
    [Parameter(Mandatory)]
    [string]$ResourceGroupName,

    [Parameter(Mandatory)]
    [string]$AiServiceName,

    [string]$ContainerName = "ai102-language-container",
    [string]$Location = "eastus",

    [ValidateSet("language", "sentiment", "keyphrase", "language-detection")]
    [string]$ServiceType = "language"
)

# Container image mapping
$imageMap = @{
    "language"           = "mcr.microsoft.com/azure-cognitive-services/textanalytics/language:latest"
    "sentiment"          = "mcr.microsoft.com/azure-cognitive-services/textanalytics/sentiment:latest"
    "keyphrase"          = "mcr.microsoft.com/azure-cognitive-services/textanalytics/keyphrase:latest"
    "language-detection" = "mcr.microsoft.com/azure-cognitive-services/textanalytics/language:latest"
}

# Get AI Services endpoint and key
$aiService = Get-AzCognitiveServicesAccount -ResourceGroupName $ResourceGroupName -Name $AiServiceName
$keys = Get-AzCognitiveServicesAccountKey -ResourceGroupName $ResourceGroupName -Name $AiServiceName

if (-not $aiService -or -not $keys) {
    Write-Error "Cannot find AI Services resource or retrieve keys."
    return
}

$billingEndpoint = $aiService.Endpoint
$apiKey = $keys.Key1

Write-Host "Deploying container: $($imageMap[$ServiceType])" -ForegroundColor Cyan
Write-Host "Billing endpoint: $billingEndpoint" -ForegroundColor Gray

# EXAM KEY POINT: These three environment variables are REQUIRED for all AI Services containers
# - ApiKey: The subscription key
# - Billing: The endpoint URL (for billing purposes)
# - Eula: Must be set to "accept"

$envVars = @{
    "ApiKey"  = $apiKey
    "Billing" = $billingEndpoint
    "Eula"    = "accept"
}

# Deploy to Azure Container Instances
$container = New-AzContainerGroup `
    -ResourceGroupName $ResourceGroupName `
    -Name $ContainerName `
    -Image $imageMap[$ServiceType] `
    -Location $Location `
    -OsType Linux `
    -Cpu 1 `
    -MemoryInGB 4 `
    -Port @(5000) `
    -IpAddressType Public `
    -EnvironmentVariable $envVars

Write-Host "`nContainer deployed!" -ForegroundColor Green
Write-Host "Container FQDN: $($container.Fqdn)" -ForegroundColor Yellow
Write-Host "Test endpoint: http://$($container.Fqdn):5000/status/ready" -ForegroundColor Yellow
Write-Host "`nTest with curl:" -ForegroundColor Cyan
Write-Host @"
curl -X POST "http://$($container.Fqdn):5000/text/analytics/v3.2-preview.2/languages" ``
  -H "Content-Type: application/json" ``
  -d '{"documents": [{"id": "1", "text": "Hello world"}]}'
"@ -ForegroundColor Gray

Write-Host "`n[IMMEDIATE] Test the /status/ready endpoint" -ForegroundColor Magenta
Write-Host "[SHORT-TERM] Send API requests and compare with cloud endpoint" -ForegroundColor Magenta
Write-Host "[LONG-TERM] Evaluate disconnected container scenarios" -ForegroundColor Magenta
