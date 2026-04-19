targetScope = 'resourceGroup'

@description('Azure region for the Computer Vision resource.')
param location string = resourceGroup().location

@description('Name of the Computer Vision resource.')
param resourceName string

@description('SKU for the Computer Vision resource.')
@allowed(['F0', 'S0', 'S1'])
param sku string = 'S0'

resource vision 'Microsoft.CognitiveServices/accounts@2024-10-01' = {
  name: resourceName
  location: location
  kind: 'ComputerVision'
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

@description('The endpoint URL of the Computer Vision resource.')
output endpoint string = vision.properties.endpoint

@description('The resource ID of the Computer Vision resource.')
output resourceId string = vision.id
