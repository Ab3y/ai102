targetScope = 'resourceGroup'

@description('Azure region for the Speech Services resource.')
param location string = resourceGroup().location

@description('Name of the Speech Services resource.')
param resourceName string

@description('SKU for the Speech Services resource.')
@allowed(['F0', 'S0'])
param sku string = 'S0'

resource speech 'Microsoft.CognitiveServices/accounts@2024-10-01' = {
  name: resourceName
  location: location
  kind: 'SpeechServices'
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

@description('The endpoint URL of the Speech Services resource.')
output endpoint string = speech.properties.endpoint

@description('The Azure region where the Speech resource is deployed.')
output region string = location

@description('The resource ID of the Speech Services resource.')
output resourceId string = speech.id
