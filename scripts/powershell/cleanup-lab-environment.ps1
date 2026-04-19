<#
.SYNOPSIS
    Clean up all AI-102 lab resources to avoid charges.
.DESCRIPTION
    Deletes the lab resource group and all resources within it.
.NOTES
    Run this after completing labs to avoid Azure charges!
#>

param(
    [string]$ResourceGroupName = "ai102-labs-rg",
    [switch]$Force
)

Write-Host "========================================" -ForegroundColor Red
Write-Host "  AI-102 Lab Cleanup" -ForegroundColor Red
Write-Host "========================================" -ForegroundColor Red

$rg = Get-AzResourceGroup -Name $ResourceGroupName -ErrorAction SilentlyContinue
if (-not $rg) {
    Write-Host "Resource group '$ResourceGroupName' not found. Nothing to clean up." -ForegroundColor Yellow
    return
}

# List resources
$resources = Get-AzResource -ResourceGroupName $ResourceGroupName
Write-Host "`nResources to be deleted:" -ForegroundColor Yellow
foreach ($r in $resources) {
    Write-Host "  - $($r.Name) ($($r.ResourceType))" -ForegroundColor Gray
}
Write-Host "`nTotal: $($resources.Count) resources" -ForegroundColor Yellow

if (-not $Force) {
    $confirm = Read-Host "`nAre you sure you want to delete ALL these resources? (yes/no)"
    if ($confirm -ne "yes") {
        Write-Host "Cleanup cancelled." -ForegroundColor Yellow
        return
    }
}

Write-Host "`nDeleting resource group (this may take a few minutes)..." -ForegroundColor Cyan
Remove-AzResourceGroup -Name $ResourceGroupName -Force -AsJob | Out-Null

Write-Host "Resource group deletion initiated (running in background)." -ForegroundColor Green
Write-Host "Verify in Azure Portal that all resources are removed." -ForegroundColor Yellow
