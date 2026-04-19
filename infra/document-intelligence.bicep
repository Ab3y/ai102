targetScope = 'resourceGroup'

@description('Azure region for the Document Intelligence resource.')
param location string = resourceGroup().location

@description('Name of the Document Intelligence (Form Recognizer) resource.')
param resourceName string

@description('SKU for the Document Intelligence resource.')
@allowed(['F0', 'S0'])
param sku string = 'S0'

resource documentIntelligence 'Microsoft.CognitiveServices/accounts@2024-10-01' = {
  name: resourceName
  location: location
  kind: 'FormRecognizer'
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

@description('The endpoint URL of the Document Intelligence resource.')
output endpoint string = documentIntelligence.properties.endpoint

@description('The resource ID of the Document Intelligence resource.')
output resourceId string = documentIntelligence.id
