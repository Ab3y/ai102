<#
.SYNOPSIS
    Configure diagnostic settings for Azure AI Services resources.
.DESCRIPTION
    Sets up diagnostic logging to a Log Analytics workspace for monitoring
    Azure AI Services usage, errors, and performance.
.NOTES
    AI-102 Module 1 — Lab 1.3: Monitor Azure AI Services
#>

param(
    [Parameter(Mandatory)]
    [string]$ResourceGroupName,

    [Parameter(Mandatory)]
    [string]$AiServiceName,

    [string]$WorkspaceName = "law-ai102-labs",
    [string]$Location = "eastus"
)

# Create Log Analytics workspace if it doesn't exist
$workspace = Get-AzOperationalInsightsWorkspace -ResourceGroupName $ResourceGroupName -Name $WorkspaceName -ErrorAction SilentlyContinue
if (-not $workspace) {
    Write-Host "Creating Log Analytics workspace: $WorkspaceName" -ForegroundColor Cyan
    $workspace = New-AzOperationalInsightsWorkspace `
        -ResourceGroupName $ResourceGroupName `
        -Name $WorkspaceName `
        -Location $Location `
        -Sku PerGB2018
}

# Get AI Services resource
$aiService = Get-AzCognitiveServicesAccount -ResourceGroupName $ResourceGroupName -Name $AiServiceName
if (-not $aiService) {
    Write-Error "AI Services resource '$AiServiceName' not found in resource group '$ResourceGroupName'"
    return
}

# Configure diagnostic settings
Write-Host "Configuring diagnostic settings..." -ForegroundColor Cyan
$logCategories = @(
    New-AzDiagnosticSettingLogSettingsObject -Enabled $true -CategoryGroup "allLogs"
)
$metricCategories = @(
    New-AzDiagnosticSettingMetricSettingsObject -Enabled $true -Category "AllMetrics"
)

New-AzDiagnosticSetting `
    -ResourceId $aiService.Id `
    -Name "ai102-diagnostics" `
    -WorkspaceId $workspace.ResourceId `
    -Log $logCategories `
    -Metric $metricCategories

Write-Host "Diagnostic settings configured successfully!" -ForegroundColor Green
Write-Host "View logs at: https://portal.azure.com/#@/resource$($workspace.ResourceId)/logs" -ForegroundColor Yellow

# Create alert rule for errors
Write-Host "Creating alert rule for API errors..." -ForegroundColor Cyan
$condition = New-AzMetricAlertRuleV2Criteria `
    -MetricName "ClientErrors" `
    -TimeAggregation Total `
    -Operator GreaterThan `
    -Threshold 10

Add-AzMetricAlertRuleV2 `
    -ResourceGroupName $ResourceGroupName `
    -Name "ai102-client-errors" `
    -TargetResourceId $aiService.Id `
    -Condition $condition `
    -WindowSize (New-TimeSpan -Minutes 5) `
    -Frequency (New-TimeSpan -Minutes 1) `
    -Severity 2 `
    -Description "Alert when AI Services client errors exceed 10 in 5 minutes"

Write-Host "Alert rule created." -ForegroundColor Green
Write-Host "`n[IMMEDIATE] Check Azure Monitor metrics in the portal" -ForegroundColor Magenta
Write-Host "[SHORT-TERM] Run sample API calls to generate diagnostic data" -ForegroundColor Magenta
Write-Host "[LONG-TERM] Set up cost alerts and budget notifications" -ForegroundColor Magenta
