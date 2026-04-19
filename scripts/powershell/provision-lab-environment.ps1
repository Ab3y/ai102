<#
.SYNOPSIS
    Provision all Azure AI resources needed for AI-102 labs.
.DESCRIPTION
    Creates a resource group and deploys all AI service resources
    needed across the 6 exam modules using Bicep templates.
.NOTES
    AI-102 Lab Environment Setup — Run this first!
#>

param(
    [string]$ResourceGroupName = "ai102-labs-rg",
    [string]$Location = "eastus",
    [string]$Prefix = "ai102"
)

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  AI-102 Lab Environment Provisioning" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

# Ensure logged in
$context = Get-AzContext
if (-not $context) {
    Write-Host "Please log in to Azure..." -ForegroundColor Yellow
    Connect-AzAccount
}

Write-Host "`nSubscription: $($context.Subscription.Name)" -ForegroundColor Gray
Write-Host "Location: $Location" -ForegroundColor Gray

# Create resource group
Write-Host "`n[1/7] Creating resource group..." -ForegroundColor Cyan
New-AzResourceGroup -Name $ResourceGroupName -Location $Location -Force | Out-Null
Write-Host "  ✓ Resource group: $ResourceGroupName" -ForegroundColor Green

# Deploy AI Services (multi-service)
Write-Host "`n[2/7] Deploying Azure AI Services (multi-service)..." -ForegroundColor Cyan
New-AzResourceGroupDeployment `
    -ResourceGroupName $ResourceGroupName `
    -TemplateFile "$PSScriptRoot/../../infra/ai-services.bicep" `
    -resourceName "$Prefix-aiservices" `
    -location $Location `
    -ErrorAction Stop | Out-Null
Write-Host "  ✓ AI Services deployed" -ForegroundColor Green

# Deploy Azure OpenAI
Write-Host "`n[3/7] Deploying Azure OpenAI..." -ForegroundColor Cyan
New-AzResourceGroupDeployment `
    -ResourceGroupName $ResourceGroupName `
    -TemplateFile "$PSScriptRoot/../../infra/openai.bicep" `
    -resourceName "$Prefix-openai" `
    -location $Location `
    -ErrorAction Stop | Out-Null
Write-Host "  ✓ Azure OpenAI deployed with GPT-4o + embeddings" -ForegroundColor Green

# Deploy AI Search
Write-Host "`n[4/7] Deploying Azure AI Search..." -ForegroundColor Cyan
New-AzResourceGroupDeployment `
    -ResourceGroupName $ResourceGroupName `
    -TemplateFile "$PSScriptRoot/../../infra/ai-search.bicep" `
    -searchServiceName "$Prefix-search" `
    -location $Location `
    -ErrorAction Stop | Out-Null
Write-Host "  ✓ AI Search deployed" -ForegroundColor Green

# Deploy Document Intelligence
Write-Host "`n[5/7] Deploying Document Intelligence..." -ForegroundColor Cyan
New-AzResourceGroupDeployment `
    -ResourceGroupName $ResourceGroupName `
    -TemplateFile "$PSScriptRoot/../../infra/document-intelligence.bicep" `
    -resourceName "$Prefix-docintell" `
    -location $Location `
    -ErrorAction Stop | Out-Null
Write-Host "  ✓ Document Intelligence deployed" -ForegroundColor Green

# Deploy Speech Services
Write-Host "`n[6/7] Deploying Speech Services..." -ForegroundColor Cyan
New-AzResourceGroupDeployment `
    -ResourceGroupName $ResourceGroupName `
    -TemplateFile "$PSScriptRoot/../../infra/speech.bicep" `
    -resourceName "$Prefix-speech" `
    -location $Location `
    -ErrorAction Stop | Out-Null
Write-Host "  ✓ Speech Services deployed" -ForegroundColor Green

# Deploy Computer Vision
Write-Host "`n[7/7] Deploying Computer Vision..." -ForegroundColor Cyan
New-AzResourceGroupDeployment `
    -ResourceGroupName $ResourceGroupName `
    -TemplateFile "$PSScriptRoot/../../infra/vision.bicep" `
    -resourceName "$Prefix-vision" `
    -location $Location `
    -ErrorAction Stop | Out-Null
Write-Host "  ✓ Computer Vision deployed" -ForegroundColor Green

# Summary
Write-Host "`n========================================" -ForegroundColor Green
Write-Host "  All resources deployed successfully!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host "`nResource Group: $ResourceGroupName" -ForegroundColor Yellow
Write-Host "Location: $Location" -ForegroundColor Yellow
Write-Host "`nTo get keys and endpoints:" -ForegroundColor Cyan
Write-Host "  az cognitiveservices account keys list -g $ResourceGroupName -n $Prefix-aiservices"
Write-Host "`nTo clean up (IMPORTANT — avoid charges!):" -ForegroundColor Red
Write-Host "  az group delete -n $ResourceGroupName --yes --no-wait"
Write-Host "`nEstimated cost: ~`$2-5/day with minimal usage" -ForegroundColor Yellow
