targetScope = 'resourceGroup'

@description('Azure region for the Azure AI Search resource.')
param location string = resourceGroup().location

@description('Name of the Azure AI Search service. Must be globally unique.')
param searchServiceName string

@description('SKU for the search service.')
@allowed(['free', 'basic', 'standard', 'standard2', 'standard3'])
param sku string = 'basic'

resource search 'Microsoft.Search/searchServices@2024-06-01-preview' = {
  name: searchServiceName
  location: location
  sku: {
    name: sku
  }
  properties: {
    replicaCount: 1
    partitionCount: 1
    hostingMode: 'default'
    publicNetworkAccess: 'enabled'
  }
  tags: {
    purpose: 'ai102-labs'
  }
}

@description('The endpoint URL of the search service.')
output endpoint string = 'https://${searchServiceName}.search.windows.net'

@description('The resource ID of the search service (use to retrieve admin keys).')
output adminKeyResourceId string = search.id
