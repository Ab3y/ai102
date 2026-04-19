targetScope = 'resourceGroup'

@description('Azure region for the AI Services resource.')
param location string = resourceGroup().location

@description('Name of the Azure AI Services multi-service resource.')
param resourceName string

@description('SKU for the AI Services resource.')
@allowed(['F0', 'S0'])
param sku string = 'S0'

resource aiServices 'Microsoft.CognitiveServices/accounts@2024-10-01' = {
  name: resourceName
  location: location
  kind: 'CognitiveServices'
  sku: {
    name: sku
  }
  properties: {
    customSubDomainName: resourceName
    publicNetworkAccess: 'Enabled'
  }
  tags: {
    purpose: 'ai102-labs'
  }
}

@description('The endpoint URL of the AI Services resource.')
output endpoint string = aiServices.properties.endpoint

@description('The resource ID of the AI Services resource.')
output resourceId string = aiServices.id
