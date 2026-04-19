targetScope = 'resourceGroup'

@description('Azure region for the Azure OpenAI resource.')
param location string = resourceGroup().location

@description('Name of the Azure OpenAI resource.')
param resourceName string

@description('Chat model name to deploy.')
param chatModelName string = 'gpt-4o'

@description('Embedding model name to deploy.')
param embeddingModelName string = 'text-embedding-ada-002'

@description('Capacity (in thousands of tokens per minute) for chat model deployment.')
param chatModelCapacity int = 10

@description('Capacity (in thousands of tokens per minute) for embedding model deployment.')
param embeddingModelCapacity int = 10

resource openai 'Microsoft.CognitiveServices/accounts@2024-10-01' = {
  name: resourceName
  location: location
  kind: 'OpenAI'
  sku: {
    name: 'S0'
  }
  properties: {
    customSubDomainName: resourceName
    publicNetworkAccess: 'Enabled'
  }
  tags: {
    purpose: 'ai102-labs'
  }
}

resource chatDeployment 'Microsoft.CognitiveServices/accounts/deployments@2024-10-01' = {
  parent: openai
  name: chatModelName
  sku: {
    name: 'Standard'
    capacity: chatModelCapacity
  }
  properties: {
    model: {
      format: 'OpenAI'
      name: chatModelName
      version: '2024-08-06'
    }
  }
}

resource embeddingDeployment 'Microsoft.CognitiveServices/accounts/deployments@2024-10-01' = {
  parent: openai
  name: embeddingModelName
  sku: {
    name: 'Standard'
    capacity: embeddingModelCapacity
  }
  properties: {
    model: {
      format: 'OpenAI'
      name: embeddingModelName
      version: '2'
    }
  }
  dependsOn: [chatDeployment]
}

@description('The endpoint URL of the Azure OpenAI resource.')
output endpoint string = openai.properties.endpoint

@description('The resource ID of the Azure OpenAI resource.')
output resourceId string = openai.id
