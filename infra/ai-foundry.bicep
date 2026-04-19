targetScope = 'resourceGroup'

@description('Azure region for all resources.')
param location string = resourceGroup().location

@description('Name of the AI Foundry hub resource.')
param hubName string

@description('Name of the AI Foundry project.')
param projectName string

@description('Unique suffix for globally unique resource names.')
param uniqueSuffix string = uniqueString(resourceGroup().id)

var storageAccountName = 'st${replace(hubName, '-', '')}${take(uniqueSuffix, 6)}'
var keyVaultName = 'kv-${hubName}-${take(uniqueSuffix, 6)}'
var appInsightsName = '${hubName}-insights'
var logAnalyticsName = '${hubName}-logs'

resource storageAccount 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: take(storageAccountName, 24)
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    accessTier: 'Hot'
    supportsHttpsTrafficOnly: true
    minimumTlsVersion: 'TLS1_2'
  }
  tags: {
    purpose: 'ai102-labs'
  }
}

resource keyVault 'Microsoft.KeyVault/vaults@2023-07-01' = {
  name: take(keyVaultName, 24)
  location: location
  properties: {
    sku: {
      family: 'A'
      name: 'standard'
    }
    tenantId: subscription().tenantId
    enableRbacAuthorization: true
    enableSoftDelete: true
    softDeleteRetentionInDays: 7
  }
  tags: {
    purpose: 'ai102-labs'
  }
}

resource logAnalytics 'Microsoft.OperationalInsights/workspaces@2023-09-01' = {
  name: logAnalyticsName
  location: location
  properties: {
    sku: {
      name: 'PerGB2018'
    }
    retentionInDays: 30
  }
  tags: {
    purpose: 'ai102-labs'
  }
}

resource appInsights 'Microsoft.Insights/components@2020-02-02' = {
  name: appInsightsName
  location: location
  kind: 'web'
  properties: {
    Application_Type: 'web'
    WorkspaceResourceId: logAnalytics.id
  }
  tags: {
    purpose: 'ai102-labs'
  }
}

resource hub 'Microsoft.MachineLearningServices/workspaces@2024-04-01' = {
  name: hubName
  location: location
  kind: 'Hub'
  sku: {
    name: 'Basic'
    tier: 'Basic'
  }
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    friendlyName: hubName
    storageAccount: storageAccount.id
    keyVault: keyVault.id
    applicationInsights: appInsights.id
  }
  tags: {
    purpose: 'ai102-labs'
  }
}

resource project 'Microsoft.MachineLearningServices/workspaces@2024-04-01' = {
  name: projectName
  location: location
  kind: 'Project'
  sku: {
    name: 'Basic'
    tier: 'Basic'
  }
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    friendlyName: projectName
    hubResourceId: hub.id
  }
  tags: {
    purpose: 'ai102-labs'
  }
}

@description('The resource ID of the AI Foundry hub.')
output hubResourceId string = hub.id

@description('The resource ID of the AI Foundry project.')
output projectResourceId string = project.id

@description('The name of the storage account created for the hub.')
output storageAccountName string = storageAccount.name

@description('The name of the Key Vault created for the hub.')
output keyVaultName string = keyVault.name
