# AI-102 Audio Study Guide — Azure AI Engineer Associate

## A Comprehensive Narrative Guide for Exam Preparation

*Written in conversational style for text-to-speech and read-aloud consumption.*
*Based on the December 23, 2025 skills measured update (Microsoft Foundry branding).*

---

# Introduction

Welcome to your AI-102 Audio Study Guide. Whether you're listening to this on your commute, on a run, or just relaxing at home, this guide is designed to walk you through everything you need to know for the Microsoft AI-102 exam — Designing and Implementing a Microsoft Azure AI Solution — in a natural, conversational way. No bullet points to squint at, no tables to decipher. Just me talking you through the concepts, one topic at a time.

So let's start with the basics. What exactly is the AI-102 exam? This is Microsoft's certification exam for the Azure AI Engineer Associate credential. It's designed for developers and engineers who build, manage, and deploy AI solutions using Azure AI services. If you're someone who works with Azure OpenAI, Azure AI Search, computer vision, natural language processing, document intelligence, or any of the other Azure AI services, this exam is aimed squarely at you.

Here are the key numbers you need to know. The passing score is 700 out of 1000. You'll get approximately 58 questions, and you have 120 minutes to complete the exam. The questions come in various formats — multiple choice, drag and drop, case studies, and sometimes you'll see code snippets where you need to fill in the blanks. Speaking of code, at the very beginning of the exam you'll be asked to choose between Python and C# as your programming language for code-based questions. You cannot change this choice once you've made it, so pick whichever language you're most comfortable reading.

Now, here's something really important. As of December 23, 2025, Microsoft updated the skills measured for this exam with significant branding changes. What was previously called "Azure AI Foundry" is now called "Microsoft Foundry." The underlying technology hasn't fundamentally changed, but the naming convention has shifted, and the exam reflects this new branding. So when you see references to Microsoft Foundry throughout this guide, that's what we're talking about — it's the evolution of Azure AI Studio and Azure AI Foundry into a unified platform.

The exam covers six domains, and the weights break down like this. Domain one, Plan and Manage Azure AI Solutions, is the biggest at 20 to 25 percent. Domain two, Implement Generative AI Solutions, is 15 to 20 percent. Domain three, Implement an Agentic Solution, is the smallest at 5 to 10 percent. Domain four, Implement Computer Vision Solutions, is 10 to 15 percent. Domain five, Implement Natural Language Processing Solutions, is 15 to 20 percent. And domain six, Implement Knowledge Mining and Information Extraction, is also 15 to 20 percent.

If you add up the heavy hitters — domains one, two, five, and six — they collectively represent 65 to 80 percent of the exam. That's where you should focus the bulk of your study time. But don't ignore domains three and four; even a small domain can be the difference between passing and failing.

This guide is structured to walk through each domain in detail, explaining not just what the concepts are, but how they connect to each other and how they're likely to appear on the exam. At the end, we'll cover exam strategy, key takeaways, and the most important things to remember on test day.

Let's get started.

---

# Chapter 1: Plan and Manage Azure AI Solutions (20 to 25 percent)

This is the largest domain on the exam, and for good reason. Before you can build anything with Azure AI, you need to understand the landscape of services available, how to provision them, how to secure them, and how to monitor them. Think of this chapter as the foundation that everything else is built on.

## The Azure AI Service Landscape

Let's start by getting a bird's-eye view of what Azure offers in the AI space. Microsoft has built a broad portfolio of AI services, each designed for specific categories of tasks. Understanding which service to use for which scenario is one of the most heavily tested topics on the exam. They love giving you a scenario and asking you to pick the right service.

First, there's Azure AI Language. This is your go-to service for text analytics. If someone asks you about sentiment analysis, key phrase extraction, named entity recognition, PII detection, or language detection, the answer is Azure AI Language. It also hosts Conversational Language Understanding, which we used to call LUIS, and Custom Question Answering, which replaced QnA Maker.

Next is Azure AI Vision. This covers image analysis, optical character recognition (which we call OCR), and the Read API for extracting printed and handwritten text. It also includes Custom Vision for training your own image classification and object detection models.

Azure AI Speech handles everything related to audio. Speech-to-text, text-to-speech, speech translation, speaker recognition, pronunciation assessment, and keyword recognition. If it involves converting between audio and text, or analyzing spoken language, this is the service.

Azure AI Translator is specifically for translating text between languages. It supports over 100 languages, can auto-detect the source language, and offers both text translation and document translation. Document translation is particularly cool because it preserves the original formatting of your documents.

Azure OpenAI Service gives you access to OpenAI's powerful models — GPT-4o, GPT-4, GPT-3.5-Turbo, DALL-E for image generation, Whisper for speech recognition, and embedding models. This is what you use for generative AI tasks: generating text, summarizing content, writing code, creating images, and building chat experiences.

Azure AI Search, formerly known as Azure Cognitive Search, is your knowledge mining engine. It creates searchable indexes over your data, supports full-text search, vector search, semantic search, and hybrid combinations of all three. It also has an AI enrichment pipeline that can extract insights from your documents as they're indexed.

Document Intelligence, which used to be called Form Recognizer, extracts structured data from documents. It has prebuilt models for common document types like invoices, receipts, ID documents, W-2 tax forms, and health insurance cards. You can also train custom models for your own document formats.

Content Safety is the newer service focused on responsible AI. It analyzes text and images for harmful content across four categories: hate, violence, sexual content, and self-harm. It also includes prompt shields for detecting jailbreak attempts and groundedness detection for checking if AI outputs are factually grounded.

And then there's Microsoft Foundry, which is the overarching platform that ties many of these services together. It provides a unified portal for managing AI projects, deploying models, creating prompt flows, building agents, and evaluating your AI solutions. Think of it as the command center for your AI engineering work.

Finally, Azure AI Video Indexer extracts insights from video content — transcripts, faces, topics, emotions, OCR text within video frames, and brand recognition.

Here's a quick mental model for remembering which service handles what. If it's text analysis, think Language. If it's images, think Vision. If it's audio, think Speech. If it's translating between languages, think Translator. If it's generating new content, think OpenAI. If it's searching through documents, think AI Search. If it's extracting data from forms and documents, think Document Intelligence. If it's about safety and moderation, think Content Safety. If it's video, think Video Indexer. And if you need to orchestrate multiple services together, think Microsoft Foundry.

The exam loves to test your ability to pick the right service. They'll describe a scenario — "A company needs to extract invoice data from PDF documents" — and you need to know that's Document Intelligence. Or "A company wants to build a chatbot that answers questions from their FAQ pages" — that's Custom Question Answering, which lives within Azure AI Language.

Let me give you a bunch more scenario examples, because this is how the exam works. If a company needs to transcribe audio from customer support calls in real time, that's Azure AI Speech with speech-to-text. If they need to translate product documentation into 15 languages while keeping the original formatting intact, that's Azure AI Translator with document translation. If they want to detect whether user-generated content on their platform contains hate speech or violence, that's Azure AI Content Safety. If they need to identify whether a specific person appears in a video, that's Video Indexer's face identification capability. If they want to extract product defects from manufacturing images using categories specific to their products, that's Custom Vision. If they need to build a search experience over thousands of internal documents with AI enrichment, that's Azure AI Search with a skillset.

Here's the pattern you should internalize: the exam gives you a business problem, and you map it to the right Azure AI service. Sometimes the scenario is ambiguous, and two services might seem to apply. In those cases, look for the most specific service. Document Intelligence is more specific than generic OCR for extracting structured fields from invoices. CLU is more specific than generic text analytics for understanding user intents. Custom Vision is more specific than Image Analysis 4.0 when you need domain-specific recognition.

Also, be aware that some services overlap in capabilities. Both Image Analysis 4.0 and Document Intelligence can do OCR. But Image Analysis is better for general photos with text (like a photo of a street sign), while Document Intelligence is better for structured documents (like invoices, receipts, and forms). Both Azure OpenAI and Azure AI Language can generate text, but Azure OpenAI is for open-ended generation while Language services are for specific analytical tasks like sentiment or entity extraction.

One more thing about the service landscape: Microsoft Foundry portal versus Azure Portal. The Azure Portal at portal.azure.com is where you manage Azure resources — create AI service resources, configure networking, set up RBAC, view metrics. The Microsoft Foundry portal at ai.azure.com is the AI-specific experience where you work with models, prompt flows, agents, and evaluations. Both are important, and the exam expects you to know which portal you'd use for different tasks. Creating an Azure AI Search resource? Azure Portal. Deploying a GPT-4o model and testing prompts? Foundry portal. Setting up Private Link for an AI service? Azure Portal. Creating a prompt flow with RAG? Foundry portal.

## Multi-Service versus Single-Service Resources

Now let's talk about an important architectural decision: multi-service resources versus single-service resources. When you create an Azure AI resource, you have two main options.

A multi-service resource, also known as a Cognitive Services resource, is a single Azure resource that gives you access to multiple AI services with one endpoint and one set of API keys. You create a resource with the kind set to "CognitiveServices" and it provides keys that work across Language, Vision, Speech, Translator, and more. The endpoint pattern is your resource name dot cognitiveservices dot azure dot com.

A single-service resource is dedicated to one specific service. For example, you might create a resource of kind "TextAnalytics" just for language analysis, or kind "ComputerVision" just for vision tasks, or kind "OpenAI" specifically for Azure OpenAI.

When should you use which? Multi-service resources are great for simplification. One resource, one bill, one set of keys to manage. They're perfect for development and testing, or when you're using multiple services in the same application. Single-service resources give you more granular control. You can put them in different regions for latency optimization, apply separate RBAC permissions, track costs independently, and scale them separately. In production environments with complex requirements, single-service resources often make more sense.

Here's something important for the exam: Azure OpenAI always requires its own dedicated resource. You cannot access OpenAI models through a multi-service Cognitive Services resource. It has to be a separate resource of kind "OpenAI." Similarly, Azure AI Search has its own resource type that's separate from the Cognitive Services family.

Let me give you a practical scenario to solidify this. Imagine you're building an application that needs to analyze images for object detection, extract sentiment from customer reviews, and convert speech to text. If all three capabilities are in the same region and you want simplicity, a single multi-service resource works perfectly. One endpoint, one key, one bill. Your code just sends different types of requests to the same endpoint with the same credentials.

But now imagine that application grows, and the speech team wants to scale their speech-to-text independently because they're handling millions of calls. They also want to track speech costs separately from vision and language costs. And the security team wants to apply different network restrictions — speech processing needs access from an on-premises data center, while vision processing only runs from Azure Virtual Machines. In this case, separate single-service resources make more sense because each team gets independent scaling, billing, and security boundaries.

Another common exam scenario: the question describes a company that wants to use a single API key across Language, Vision, and Speech services. The answer is a multi-service Cognitive Services resource. If the question describes a company that wants to restrict Vision access to a specific virtual network while keeping Language accessible from the public internet, the answer is separate single-service resources with different network configurations.

The endpoint URL pattern is also worth remembering. Multi-service resources use the generic cognitiveservices.azure.com domain: your-resource-name.cognitiveservices.azure.com. Single-service resources use the same pattern. The key difference isn't the URL format but rather what services the keys work with. A multi-service key works across Language, Vision, Speech, and Translator. A single-service key only works with its specific service.

For pricing tiers, both multi-service and single-service resources offer Free (F0) and Standard (S0) tiers, though the exact pricing differs by service. The free tier has transaction limits that are useful for development but won't support production workloads.

## Provisioning Methods

The exam expects you to know multiple ways to create and deploy Azure AI resources. There are three main methods they'll test you on.

First, the Azure Portal. This is the graphical, point-and-click approach. You go to the Azure portal, click Create a Resource, search for the AI service you want, fill in the form (name, region, resource group, pricing tier), and click Create. The portal is great for learning and exploration, but it's not ideal for repeatable, automated deployments.

Second, the Azure CLI. This is the command-line approach and it's the one you should be most comfortable with for the exam. The key command for creating AI resources is "az cognitiveservices account create." You specify the name, resource group, kind (like CognitiveServices or OpenAI or TextAnalytics), SKU (usually S0 for standard), and location. To get your keys, you use "az cognitiveservices account keys list." To get your endpoint, you use "az cognitiveservices account show" with the query parameter filtering for the endpoint property.

Third, Bicep templates. Bicep is Microsoft's domain-specific language for deploying Azure resources. A Bicep template for an AI resource looks like a resource declaration with the type set to "Microsoft.CognitiveServices/accounts," followed by the name, location, kind, and SKU. Bicep is ideal for infrastructure as code — you define your resources declaratively and deploy them repeatedly across environments.

The exam might show you a Bicep template and ask you to identify what's being created, or they might give you a partially completed template and ask you to fill in the missing parameters. Make sure you're comfortable reading Bicep syntax even if you don't write it daily.

Let me walk you through a specific Bicep example so you can visualize it. A Bicep template for an AI resource starts with the resource keyword, followed by a symbolic name (like "cognitiveServices"), the resource type "Microsoft.CognitiveServices/accounts@2024-10-01" (that's the API version), and then a block with properties. Inside, you'll see the name property (the resource name), the location property (usually set to a parameter), the kind property (like "CognitiveServices" for multi-service or "OpenAI" for Azure OpenAI), and the sku property with a name field (like "S0"). The properties block might also include networkAcls for firewall rules, publicNetworkAccess to control whether the resource is accessible from the internet, and customSubDomainName for the resource's custom endpoint domain.

The important thing for the exam is recognizing the kind values. If kind is "CognitiveServices," it's a multi-service resource. If kind is "OpenAI," it's an Azure OpenAI resource. If kind is "TextAnalytics," it's a dedicated language service resource. If kind is "ComputerVision," it's a vision-only resource. If kind is "SpeechServices," it's speech-only.

You should also know about creating resources via the Azure Portal step by step, because the exam might describe this process. You go to portal.azure.com, click "Create a resource," search for "Azure AI services" (or a specific service name), select the service, click "Create," and fill in the required fields: subscription, resource group, region, name, and pricing tier. After clicking "Review + create" and then "Create," the resource is deployed. You can then find your keys and endpoint in the resource's "Keys and Endpoint" blade.

For CI/CD integration, the exam expects you to know that AI service resources can be deployed through Azure DevOps pipelines or GitHub Actions using Bicep templates or ARM templates. Models, skillsets, and other AI assets can also be deployed programmatically through the SDK or REST API as part of your deployment pipeline. The pattern is: deploy the infrastructure (the Azure resources), then deploy the AI assets (models, indexes, knowledge bases) on top of the infrastructure.

For Azure OpenAI specifically, there's an additional step after creating the resource: deploying a model. You use "az cognitiveservices account deployment create" with parameters for the deployment name, model name (like gpt-4o), model version, model format (OpenAI), SKU name (Standard or Provisioned), and SKU capacity (which represents tokens per minute in thousands). Understanding this two-step process — create the resource, then deploy the model — is essential for the exam.

Let me also mention the three deployment types for Azure OpenAI models, because the exam differentiates between them. Standard deployments are pay-per-token with automatic scaling. They're the simplest to set up and most flexible — you only pay for what you use. Provisioned Throughput Units, or PTU, reserve dedicated compute capacity. You pay a fixed hourly rate regardless of usage, but you get guaranteed throughput with predictable latency. This is ideal for production workloads with consistent demand. Global deployments spread your deployment across multiple Azure regions for the highest availability and can route traffic to the closest region. The exam might describe a scenario and ask which deployment type is most appropriate. High-volume, consistent traffic with latency requirements? PTU. Variable, unpredictable usage? Standard. Global audience with high availability requirements? Global.

## SDK versus REST API Patterns

The exam tests both SDK and REST API approaches, so you need to be comfortable with both. Let me walk through how they differ and when you'd use each.

The SDK approach uses language-specific client libraries. For Python, you'd install packages like azure-ai-textanalytics, openai, azure-search-documents, and azure-ai-formrecognizer. The SDK provides typed objects, handles authentication, manages retries, and gives you a more natural programming experience. For example, with the Text Analytics SDK, you create a TextAnalyticsClient, call the analyze_sentiment method, and get back typed SentimentResult objects.

The REST API approach uses HTTP requests directly. Every Azure AI service exposes a REST API with a consistent pattern: your endpoint, followed by the service path, the API version, and the operation. You authenticate by including your API key in a request header — typically "Ocp-Apim-Subscription-Key" for most services, or "api-key" for Azure Search and Azure OpenAI. The request body is JSON, and the response comes back as JSON.

Here's the general REST endpoint pattern: your endpoint, then the service name, then the API version as a query parameter, then the operation. For example, Azure AI Language endpoints look like your resource dot cognitiveservices dot azure dot com slash language slash colon analyze-text, with the api-version as a query parameter. Azure OpenAI endpoints look like your resource dot openai dot azure dot com slash openai slash deployments slash your-deployment-name slash chat slash completions.

The exam will show you both SDK code and REST API calls. Sometimes they'll give you a code snippet and ask what it does. Other times they'll give you a REST endpoint URL and ask which service it belongs to. Being able to read and understand both patterns is critical.

One important nuance: some operations are asynchronous. Document Intelligence is a great example. When you submit a document for analysis via REST, it returns a 202 Accepted response with an "Operation-Location" header. You then poll that URL with GET requests until the operation completes. The SDK abstracts this away with methods like "begin_analyze_document" that return a poller object you can wait on.

Let me give you concrete examples of both SDK and REST for a common operation, so you can see the patterns side by side.

For sentiment analysis using the REST API, you'd send a POST request to your endpoint at https colon slash slash your-resource dot cognitiveservices dot azure dot com slash language slash colon analyze-text with the api-version query parameter. The request headers include Content-Type set to application/json and Ocp-Apim-Subscription-Key set to your API key. The request body is a JSON object with the "kind" field set to "SentimentAnalysis," a "parameters" object with modelVersion set to "latest," and an "analysisInput" object containing a "documents" array. Each document has an "id" (a string you assign), a "language" field (like "en"), and the "text" field with the actual content to analyze.

The response comes back as JSON with a "results" object containing a "documents" array. Each document result includes the overall sentiment ("positive," "negative," "neutral," or "mixed"), the confidence scores for each sentiment, and a "sentences" array with per-sentence sentiment analysis.

For the same operation using the Python SDK, you'd first install the azure-ai-textanalytics package. Then you'd import TextAnalyticsClient and AzureKeyCredential. You create a client by passing your endpoint and a credential object. Then you call the analyze_sentiment method with a list of strings. The result is a list of AnalyzeSentimentResult objects, each with a sentiment property and confidence_scores property.

The SDK code is clearly more concise and provides type safety. But the REST API gives you language-independence and works from any HTTP client. The exam expects you to recognize both.

For Azure OpenAI, the REST pattern is slightly different. The endpoint is your-resource dot openai dot azure dot com, not cognitiveservices. The authentication header is "api-key" instead of "Ocp-Apim-Subscription-Key." And the request body follows the OpenAI API format with the "messages" array. The endpoint URL includes the deployment name in the path: slash openai slash deployments slash your-deployment-name slash chat slash completions.

For AI Search, it's different yet again. The endpoint is your-service dot search dot windows dot net. The authentication header is "api-key" (same name as OpenAI but a different key type — admin key or query key depending on the operation). Query requests go to slash indexes slash your-index slash docs slash search.

The fact that different services use different header names for the API key is a subtle but testable detail. Most Cognitive Services use "Ocp-Apim-Subscription-Key." Azure OpenAI and Azure AI Search use "api-key." This is worth remembering.

## Container Deployment

Now let's talk about one of the exam's favorite topics: deploying Azure AI services in Docker containers. This is heavily tested, and there are some very specific details you need to memorize.

Azure AI services can be deployed as Docker containers for scenarios where you need data to stay on-premises or you need low-latency inference at the edge. The key concept is that while the AI processing happens locally in the container, billing still goes through Azure. The container needs to phone home to Azure periodically for metering purposes.

There are three environment variables you absolutely must memorize. I call them the three magic environment variables, and the exam loves to test them.

The first is ApiKey. This is your Azure AI resource's API key. The container uses it to authenticate with Azure for billing.

The second is Billing. This is the endpoint URL of your Azure AI resource. For example, https colon slash slash myresource dot cognitiveservices dot azure dot com. Despite the name "Billing," this is really the endpoint URL.

The third is Eula. This must be set to the value "accept" — lowercase, just the word "accept." This indicates you accept the license terms. If you don't set this, the container won't start.

A Docker run command for an AI container looks like this: docker run, then memory and CPU parameters, then the container image from Microsoft Container Registry (MCR), followed by the three environment variables. The container images come from mcr.microsoft.com/azure-cognitive-services, followed by the service path. For example, the sentiment analysis container is at mcr.microsoft.com/azure-cognitive-services/textanalytics/sentiment.

There are two types of containers: connected containers and disconnected containers. Connected containers require internet access for billing — the data stays local, but billing calls go out to Azure. Disconnected containers can run completely air-gapped with no internet at all, but they require a commitment plan purchase and a license file download ahead of time.

The exam might ask you to identify which environment variable is missing from a Docker run command, or they might ask you what happens if the Eula variable isn't set. Know these three variables cold.

Let me give you more detail on the Docker run command because the exam shows you specific commands. A full Docker run command looks like this. You start with "docker run" followed by "--rm" (removes the container when it stops) and "-it" (runs in interactive mode). Then "-p 5000:5000" maps port 5000 on the host to port 5000 in the container (this is the port where the local API is exposed). You might include memory and CPU constraints like "--memory 8g" and "--cpus 4" because AI models need significant compute resources. Then comes the container image path from MCR. And finally the three environment variables as key=value pairs: Eula=accept, Billing=https://your-resource.cognitiveservices.azure.com, and ApiKey=your-api-key.

After the container starts, you can send API requests to localhost:5000, and the container processes them locally. Your data never leaves your network — the only outbound traffic is billing telemetry to Azure.

Let me list the specific container images that are available and exam-relevant. Sentiment Analysis is at mcr.microsoft.com/azure-cognitive-services/textanalytics/sentiment. Language Detection is at mcr.microsoft.com/azure-cognitive-services/textanalytics/language. Key Phrase Extraction is at mcr.microsoft.com/azure-cognitive-services/textanalytics/keyphrase. Named Entity Recognition is at mcr.microsoft.com/azure-cognitive-services/textanalytics/ner. Speech-to-Text is at mcr.microsoft.com/azure-cognitive-services/speechservices/speech-to-text. Text-to-Speech is at mcr.microsoft.com/azure-cognitive-services/speechservices/text-to-speech. Read OCR is at mcr.microsoft.com/azure-cognitive-services/vision/read. And Document Intelligence Layout is at mcr.microsoft.com/azure-cognitive-services/form-recognizer/layout.

Notice the naming pattern: all containers start with mcr.microsoft.com/azure-cognitive-services, then the service area (textanalytics, speechservices, vision, form-recognizer), then the specific capability. This consistent naming pattern can help you identify the correct container image if the exam shows you options.

There are also optional environment variables you might see on the exam. Logging:Console:LogLevel:Default controls the logging verbosity — set to Information, Warning, Error, or Debug. ApplicationInsights:InstrumentationKey enables sending telemetry to Application Insights. Mounts:Input and Mounts:Output specify directories for input and output data in speech and vision containers.

One more container concept: Azure Container Instances (ACI) deployment. Instead of running containers on your own Docker host, you can deploy AI containers to ACI for a managed container hosting experience. ACI handles the infrastructure, and you just specify the container image and the three environment variables. This is often the answer when the exam asks about deploying AI containers in Azure without managing VMs.

## Security: Managed Identity, Key Vault, RBAC, and Private Link

Security is woven throughout the exam, and there are four main security mechanisms you need to understand for Azure AI services.

Let's start with managed identity, because this is probably the single most important security concept on the entire exam. Here's a rule of thumb that will serve you well: whenever the exam asks about the best or recommended way to authenticate an Azure application to an AI service, the answer is almost always managed identity.

Managed identity eliminates the need to store credentials in your code or configuration. Instead, Azure assigns an identity to your compute resource — like an App Service, Function App, VM, or Container App — and that identity can be granted permissions to access AI services. There are two types: system-assigned managed identity, which is tied to the lifecycle of the resource and is deleted when the resource is deleted, and user-assigned managed identity, which exists independently and can be shared across multiple resources.

In code, you use the DefaultAzureCredential class from the Azure Identity SDK. This class automatically detects the available authentication method — managed identity in Azure, or your developer credentials locally — and uses it to obtain an access token. You pass this credential object to your AI service client instead of an API key. It's elegant, it's secure, and it's what Microsoft recommends for production workloads.

Next is Azure Key Vault. Key Vault is a secure store for secrets, certificates, and encryption keys. For AI services, the most common pattern is storing your API keys as Key Vault secrets rather than in application settings or environment variables. Your application then retrieves the key from Key Vault at runtime. You can also use Key Vault references in App Service configuration, which look like @Microsoft.KeyVault(SecretUri=...) and automatically resolve to the secret value.

Key Vault also helps with key rotation. Azure AI services provide two API keys so you can rotate them without downtime — you regenerate key one while your application uses key two, update your application to use the new key one, then regenerate key two. If your keys are stored in Key Vault, you only need to update the secret value in one place.

RBAC — Role-Based Access Control — is how you control who can do what with your AI services. There are several important roles to know. Cognitive Services User allows calling prediction APIs, which is the most common role for applications. Cognitive Services Contributor allows creating and managing resources plus calling APIs. Cognitive Services OpenAI User allows calling OpenAI completion and embedding APIs specifically. Cognitive Services OpenAI Contributor allows managing OpenAI deployments plus calling APIs. For Azure AI Search, there are Search Index Data Reader for querying, Search Index Data Contributor for reading and writing index data, and Search Service Contributor for managing the search service itself.

The exam loves to ask which RBAC role is appropriate for a given scenario. If an application just needs to call the API to get predictions, it's Cognitive Services User. If a developer needs to create and manage the resource, it's Cognitive Services Contributor. For search queries from a client application, it's Search Index Data Reader.

Finally, Private Link and network security. Azure Private Link creates a private endpoint for your AI service within your virtual network. Traffic between your application and the AI service travels over the Microsoft backbone network rather than the public internet. This is important for organizations with strict data residency and security requirements.

You can also configure firewall rules on your AI service to restrict access to specific IP addresses or virtual networks. Service endpoints are another option — they route traffic from your virtual network to the AI service over the Azure backbone while using the service's public endpoint.

The exam might present a scenario where a company requires that no data traverses the public internet, and you need to recommend Private Link. Or they might ask about the difference between service endpoints and private endpoints.

Let me expand on the security topic with some common exam scenarios. 

Scenario one: "An application running on Azure App Service needs to access Azure AI Language for sentiment analysis. The security team requires that no API keys be stored in the application's configuration. What should you do?" The answer is enable system-assigned managed identity on the App Service, grant it the Cognitive Services User role on the AI Language resource, and use DefaultAzureCredential in the application code. No keys needed.

Scenario two: "A company has two AI service keys and needs to rotate them without downtime." The answer is the two-key rotation pattern. Start with your application using Key 1. Regenerate Key 2 (it gets a new value, but the app doesn't use it yet). Update the application to use Key 2. Now regenerate Key 1 (the old key is invalidated, but the app is already using Key 2). Optionally update the application back to Key 1. At no point is the application using a key that has been invalidated.

Scenario three: "A healthcare company requires that AI service traffic never traverses the public internet. What should you configure?" The answer is Azure Private Link with a private endpoint. This creates a network interface in the company's virtual network with a private IP address. DNS resolves the AI service's hostname to this private IP. Traffic flows entirely over the Microsoft backbone network through the private endpoint.

Scenario four: "A developer needs to test AI services from their local machine but the AI service has firewall rules configured." The options are to add the developer's IP to the firewall allow list, use a VPN to connect to the virtual network with the private endpoint, or temporarily disable the firewall (not recommended for production). The exam would typically recommend adding the IP to the firewall allow list for a development scenario.

Here's another important security detail: when using managed identity, the DefaultAzureCredential class tries multiple authentication methods in a specific order. In Azure, it tries managed identity. Locally, it can try the Azure CLI credential, Visual Studio credential, Visual Studio Code credential, or interactive browser credential. This chain of credential providers makes the same code work in both environments without changes.

The scope for obtaining an Entra ID token for Cognitive Services is https colon slash slash cognitiveservices.azure.com/.default. When using the REST API with token authentication instead of API key authentication, you include the token in the Authorization header as "Bearer" followed by the token value. This replaces the Ocp-Apim-Subscription-Key header.

## Monitoring: Diagnostic Settings, Log Analytics, and Alerts

Once your AI services are deployed, you need to monitor them. The exam tests three main monitoring mechanisms.

Diagnostic settings determine where your logs and metrics go. You can route them to a Log Analytics workspace for querying with Kusto Query Language (KQL), to an Azure Storage account for long-term archival, or to an Azure Event Hub for streaming to external systems. You can also send them to multiple destinations simultaneously. Diagnostic settings capture information like API call counts, latency, error rates, and detailed request and response logs.

Log Analytics is where most of your operational analysis happens. It's a powerful query engine that lets you write KQL queries to analyze your AI service logs. For example, you could query for all API calls that returned errors in the last 24 hours, or calculate the average response time for your image analysis calls, or identify which operations are consuming the most tokens in your OpenAI deployment.

Alerts let you define rules that trigger notifications when specific conditions are met. You can create metric alerts that fire when a metric crosses a threshold — like when API error rate exceeds 5 percent or when latency exceeds 2 seconds. You can also create log alerts based on KQL queries that run on a schedule. Alerts can send notifications via email, SMS, webhook, or trigger automated actions through Azure Logic Apps or Azure Functions.

The exam might ask you to set up monitoring for an AI solution. The typical answer involves enabling diagnostic settings to route to Log Analytics, then creating alerts for key metrics like error rates and latency.

Let me elaborate on monitoring because it comes up in subtle ways throughout the exam. When you enable diagnostic settings on an Azure AI resource, you choose which log categories to capture. For Cognitive Services, the main log category is "Audit" logs, which record every API call including the operation name, result code, caller IP, and duration. You might also capture "RequestResponse" logs that include sanitized versions of the request and response bodies. And there are "AllMetrics" for numerical data like total calls, total errors, latency, and data processed.

In Log Analytics, you write KQL (Kusto Query Language) queries to analyze these logs. A simple query might look like this: you reference the AzureDiagnostics table, filter by resource type containing "CognitiveServices," filter by the time range (like the last 24 hours), and summarize the count of requests grouped by operation name. More advanced queries might calculate percentile latencies, identify anomalous error rates, or correlate errors with specific operations.

For Azure OpenAI specifically, monitoring is especially important because of token usage and costs. The metrics include "TokenTransaction" which tells you how many tokens each request consumed, broken down by prompt tokens and completion tokens. You can use Log Analytics to track your daily token consumption, identify which deployments are consuming the most tokens, and set alerts when token usage exceeds expected thresholds.

Alerts work on two models. Metric alerts evaluate a metric condition on a schedule — like "if the error rate exceeds 5% in any 5-minute window, fire the alert." Log alerts run a KQL query on a schedule and fire if the query returns results — like "alert me if any request took longer than 10 seconds in the last 15 minutes."

Action groups define what happens when an alert fires. They can send emails, SMS messages, push notifications, make voice calls, trigger Azure Functions, invoke Logic Apps, send webhooks, or create ITSM incidents. You define the action group once and associate it with multiple alert rules.

The exam might describe a monitoring scenario and ask which combination of diagnostic settings, queries, and alerts would satisfy the requirements. The pattern is always: route logs to Log Analytics, write KQL queries to analyze the data, and create alerts with appropriate action groups.

## Cost Management

Managing costs for AI services is important because these services are billed based on usage, and costs can add up quickly if you're not careful.

Most Azure AI services offer two pricing tiers: a free tier (F0) and a standard tier (S0). The free tier is great for development and testing but comes with transaction limits. The standard tier charges per transaction — per API call, per page analyzed, per minute of audio processed, or per token generated.

Azure OpenAI has additional pricing complexity. There are two main deployment types: Standard, which bills per token processed and is pay-as-you-go, and Provisioned Throughput Units (PTU), which reserve dedicated capacity at a fixed hourly rate. Standard deployments are easier to start with and scale automatically, while PTU deployments are better for predictable, high-volume workloads where you want guaranteed throughput.

For cost management, the exam recommends using Azure Cost Management and Billing to track spending, setting budgets with alerts, and right-sizing your deployments. For OpenAI specifically, monitoring token usage is critical — you can see prompt tokens (input) and completion tokens (output) in your metrics, and you should optimize your prompts to minimize unnecessary tokens.

Let me give you more practical cost management guidance that appears on the exam. Each Azure AI service has its own pricing model, and understanding these is important for choosing cost-effective solutions.

Azure AI Language charges per text record — a text record is 1,000 characters. The free tier includes 5,000 text records per month. Standard tier charges a small amount per 1,000 text records.

Azure AI Vision charges per transaction — each API call is a transaction. OCR, image analysis, and face detection each have their own pricing.

Azure AI Speech charges per hour of audio processed. Speech-to-text and text-to-speech have different rates. Custom Speech has additional charges for model training and hosting.

Azure AI Search has tier-based pricing — Free, Basic, and Standard (S1, S2, S3), plus Storage Optimized (L1, L2). Each tier has limits on the number of indexes, documents, and storage. The free tier supports up to 3 indexes and 50 megabytes of storage. Standard S1 supports up to 50 indexes. Choosing the right tier based on your data volume and query throughput is an important cost optimization.

Document Intelligence charges per page analyzed. The free tier includes 500 pages per month. Custom model training has additional costs for documents used in training.

For the exam, the cost management question often comes down to choosing the right pricing tier and deployment type for a given workload. Using the free tier for development, standard for production. Using Standard deployments instead of PTU when usage is unpredictable. Combining multiple services on a multi-service resource to simplify billing. Implementing caching to reduce redundant API calls.

## Responsible AI: Content Safety, Blocklists, Prompt Shields, and Content Filters

The last major topic in domain one is responsible AI, and this is an area Microsoft cares deeply about. The exam tests specific technical implementations, not just principles.

Azure AI Content Safety is the primary service for content moderation. It analyzes text and images across four categories: Hate, Violence, Sexual content, and Self-Harm. Each category is scored on a severity scale from 0 to 6, where 0 means safe, 2 means low severity, 4 means medium severity, and 6 means high severity. These specific numbers — 0, 2, 4, 6 — are exam favorites. The system uses four severity levels, not seven — the values are 0, 2, 4, and 6.

When you call the Content Safety API, you send text or an image and specify which categories to evaluate. The response includes a severity score for each category. You then implement decision logic: if any category score meets or exceeds your threshold, you reject or flag the content. A strict policy would reject anything with severity 2 or above. A moderate policy would reject severity 4 and above. A lenient policy would only reject severity 6.

Custom blocklists let you define domain-specific terms that should always be blocked, regardless of the AI model's assessment. This is useful for blocking brand names, competitor mentions, internal code names, or any other terms specific to your organization.

Prompt shields detect two types of attacks: jailbreak attempts, where users try to bypass the AI model's safety guidelines through creative prompting, and indirect prompt injection, where malicious instructions are embedded in documents or data that the AI processes. The Content Safety API has a dedicated endpoint for prompt shield analysis.

Content filters on Azure OpenAI deployments are configured at the deployment level. You can set severity thresholds for each content category, choosing to block, warn, or allow content at each severity level. Every Azure OpenAI deployment has default content filters, and you can customize them to be more or less strict depending on your use case.

Groundedness detection is another feature that checks whether an AI model's output is factually grounded in the source material provided to it. This is particularly relevant for RAG (Retrieval-Augmented Generation) scenarios where you want to ensure the model isn't hallucinating information.

Protected material detection identifies known copyrighted text in AI output. This helps organizations avoid inadvertently reproducing protected content.

The exam expects you to know how to configure all of these responsible AI features. They might ask which Content Safety severity level corresponds to "moderate risk" (that's 4), or how to set up a custom blocklist, or what prompt shields protect against. Make sure you're comfortable with both the concepts and the specific implementation details.

---

# Chapter 2: Generative AI Solutions (15 to 20 percent)

Generative AI is the hot topic of our era, and Microsoft has built a comprehensive platform for building generative AI solutions in Azure. This domain covers Microsoft Foundry, Azure OpenAI, prompt engineering, fine-tuning, and the RAG pattern. Let's dive in.

## Microsoft Foundry: Hub versus Project

Microsoft Foundry — formerly known as Azure AI Foundry — is the unified platform for building, deploying, and managing AI solutions. The key organizational concept you need to understand is the distinction between hubs and projects.

A hub is the top-level organizational unit. Think of it as a department or team-level container. A hub provides shared resources: compute, storage, connections to AI services, and security policies. When you create a hub, it automatically provisions supporting resources like an Azure Storage account, a Key Vault, and an Application Insights instance.

A project lives inside a hub. It's where the actual work happens — deploying models, creating prompt flows, building agents, running evaluations, and developing applications. Multiple projects can share a hub's resources, which reduces overhead and ensures consistent security policies.

The relationship is hierarchical: a hub contains one or more projects, and each project inherits the connections and configuration from its parent hub. This is similar to how Azure subscriptions contain resource groups.

When the exam asks about deploying Microsoft Foundry resources, the typical sequence is: create a hub, create a project within that hub, then deploy models and build your solution within the project.

Let me give you a concrete example to make this tangible. Say you're an AI engineering team at a retail company. You'd create a hub called "retail-ai-hub" that has connections to your Azure OpenAI resource, your AI Search service, your storage accounts, and your Key Vault. All security policies and network configurations are set at the hub level.

Within that hub, you might create three projects: "customer-service-bot" for a chatbot that answers customer questions, "product-recommendations" for a recommendation engine, and "content-generation" for marketing content creation. Each project shares the hub's connections and security policies but has its own models, prompt flows, and evaluations.

This architecture gives you governance and consistency at the hub level, with flexibility and independence at the project level. The exam tests this organizational model, so make sure you understand the hub-project hierarchy.

The Foundry portal also provides several important capabilities. The Model Catalog lets you browse and deploy hundreds of AI models — not just OpenAI models, but models from Meta, Mistral, Cohere, and other providers. Prompt Flow is a visual tool for building LLM-based workflows. Evaluations let you test your models and flows against benchmarks. Tracing provides observability into your AI application's behavior. And the Foundry SDK (the azure-ai-projects package in Python) lets you integrate all these capabilities into your application code.

The Foundry portal is accessible at ai.azure.com and provides a visual interface for managing everything. But you can also do everything programmatically using the Foundry SDK, which is the azure-ai-projects package in Python. The SDK is important for integrating Foundry capabilities into your applications.

Prompt templates are another Foundry feature worth understanding. Instead of hardcoding prompts in your application, you can define templates with placeholders that get filled in at runtime. For example, a template might say "You are a helpful assistant for {{company_name}}. Answer questions about {{product_name}} using the following context: {{context}}." At runtime, your application fills in the company name, product name, and retrieved context. This makes prompts easier to manage, version, and A/B test.

## Azure OpenAI: Provisioning and Model Deployment

Azure OpenAI is the centerpiece of most generative AI solutions on Azure. Let's walk through the key concepts you need to know.

First, provisioning. Azure OpenAI resources are created as a Cognitive Services account of kind "OpenAI" in a specific region. Region availability matters — not all models are available in all regions, and some regions have more capacity than others. The exam might ask you to choose a region based on model availability or capacity requirements.

After creating the resource, you deploy models. This is a separate step. A deployment gives a model a name that you use in your API calls, and specifies the deployment type and capacity. There are three main deployment types. Standard is pay-per-token and scales automatically. Provisioned Throughput Units, or PTU, provide reserved capacity at a fixed rate. Global deploys across multiple regions for the highest availability.

The models you should know for the exam include GPT-4o, which is the flagship multimodal model that can handle both text and images. GPT-4 Turbo and GPT-4 are powerful text models. GPT-3.5-Turbo is a faster, cheaper option for simpler tasks. text-embedding-ada-002, text-embedding-3-small, and text-embedding-3-large are embedding models used for semantic search and similarity. DALL-E is the image generation model. And Whisper is the speech recognition model.

Let me elaborate on multimodal models because this is a relatively new and exam-relevant topic. GPT-4o is "multimodal," meaning it can process both text and images as input. You can send an image along with a text question, and the model can analyze, describe, or answer questions about the image. For example, you could send a photo of a chart and ask "What trend does this chart show?" or send a photo of a product and ask "What is this product and what are its features?"

In the API, multimodal input is specified by using a different content format in the user message. Instead of a simple text string, the content field becomes an array of content parts. Each part has a type — either "text" for text content or "image_url" for an image. The image can be provided as a URL or as base64-encoded data.

This is significant for the exam because it represents a different input pattern than standard text-only chat completions. If a question describes analyzing images using GPT-4o, remember that it uses the chat completions endpoint (not the image analysis endpoint from Azure AI Vision) with the multimodal message format.

## The Chat Completions API: Message Roles and Parameters

The Chat Completions API is the primary way you interact with GPT models in Azure OpenAI, and it's heavily tested on the exam. You need to understand the message structure and every parameter.

The API works with a conversation represented as an array of messages, where each message has a role and content. There are three roles.

The system role sets the behavior and persona of the AI. This message comes first and tells the model how to behave. For example: "You are a helpful customer service agent for a software company. Always be polite and concise." The system message is powerful because it shapes all subsequent interactions.

The user role represents the human asking questions or giving instructions. These are the actual user inputs.

The assistant role represents the AI's previous responses. By including assistant messages in the conversation, you provide context — the model can "remember" what it said before. This is how you maintain conversation history.

A typical API call includes the system message first, then alternating user and assistant messages representing the conversation so far, and finally the new user message at the end.

Now let's talk about the parameters, because the exam tests each one. Here's something important to remember: the exam specifically calls out temperature, top_p, max_tokens, frequency_penalty, and presence_penalty as things you need to know.

Temperature controls randomness. It ranges from 0 to 2. A temperature of 0 makes the model almost completely deterministic — it will always choose the most likely next token. A temperature of 1 is the default, providing balanced creativity. A temperature of 2 makes the output very creative and unpredictable. For factual tasks like data extraction or classification, use low temperature. For creative tasks like story writing or brainstorming, use higher temperature.

Top_p is an alternative way to control randomness, called nucleus sampling. It ranges from 0 to 1. A value of 0.1 means the model only considers tokens in the top 10 percent of probability mass. Here's a critical exam tip: Microsoft recommends that you do not change both temperature and top_p at the same time. Adjust one or the other, not both.

Max_tokens controls the maximum number of tokens in the completion — that's the output, not the input. If your prompt uses 500 tokens and you set max_tokens to 100, the model will generate up to 100 output tokens. The total cannot exceed the model's context window. For GPT-4o, the context window is 128,000 tokens and the maximum output is 16,384 tokens.

Frequency_penalty ranges from negative 2 to positive 2, with a default of 0. It penalizes tokens proportional to how often they've appeared in the text so far. Higher values make the model less likely to repeat the same words and phrases. This is useful for reducing repetitive output.

Presence_penalty also ranges from negative 2 to positive 2, with a default of 0. It penalizes tokens based on whether they've appeared at all in the text, regardless of how many times. Higher values encourage the model to talk about new topics rather than staying on the same subject.

Stop sequences let you define up to four strings that cause the model to stop generating when it encounters them. For example, you might set a stop sequence of a newline character if you want the model to generate exactly one line.

The response_format parameter can be set to "text" for normal text output or "json_object" to force JSON output. Important: when you set json_object mode, you must also include an instruction in the prompt telling the model to output JSON. The parameter alone isn't enough.

And the seed parameter enables more deterministic outputs. If you use the same seed with the same parameters and prompt, you should get the same result — though this is best-effort, not guaranteed.

## Token Calculation and Limits

Understanding tokens is essential for working with Azure OpenAI and for the exam. Let me explain how this works.

A token is roughly four characters of English text, or about three-quarters of a word. The word "hamburger" gets broken into three tokens: "ham," "bur," and "ger." Simple words like "the" or "is" are single tokens. Numbers and special characters might be individual tokens.

Every API call consumes tokens in two ways: prompt tokens (your input) and completion tokens (the model's output). The total of prompt tokens plus completion tokens cannot exceed the model's context window.

Here's a practical example. If you have a GPT-4o model with a 128,000 token context window, and your prompt (including system message, conversation history, and the current user message) uses 10,000 tokens, you have up to 16,384 tokens available for the completion (since that's GPT-4o's max output), and the total stays well within the 128,000 context window.

If you set max_tokens to 500, the model will generate at most 500 completion tokens. The response includes usage information telling you exactly how many prompt tokens and completion tokens were consumed. Billing is based on this token usage.

The token limits for the main models are as follows. GPT-4o has a 128,000 token context window with up to 16,384 output tokens. GPT-4o-mini also has 128,000 context with 16,384 output. GPT-4 Turbo has 128,000 context with 4,096 output. GPT-4 with 32K context has 32,768 context with 8,192 output. GPT-3.5-Turbo 16K has 16,384 context with 4,096 output. Embedding models like text-embedding-ada-002 have 8,191 tokens but don't generate output — they produce embedding vectors instead.

The exam might ask you to calculate whether a given prompt will exceed the context window, or what happens when the combined prompt and max_tokens exceed the model's limit. If the prompt alone exceeds the context window, you'll get an error. If the prompt plus max_tokens exceeds it, the model will truncate the output to fit within the window.

## The RAG Pattern: Step by Step

RAG stands for Retrieval-Augmented Generation, and it's one of the most important patterns in modern AI engineering. Let me walk you through it step by step.

The fundamental problem RAG solves is this: large language models are trained on general data up to a knowledge cutoff date. They don't know about your company's specific documents, policies, products, or recent events. RAG gives the model access to your data without retraining it.

Here's how it works, step by step.

Step one: You take your documents — PDFs, Word files, web pages, databases, whatever you have — and break them into manageable chunks. Chunking is important because the model has a context window limit, so you can't just feed it your entire document library.

Step two: You generate embeddings for each chunk. An embedding is a vector — a list of numbers — that represents the semantic meaning of the text. You use an embedding model like text-embedding-ada-002 or text-embedding-3-small to create these vectors. Similar concepts produce vectors that are close together in vector space.

Step three: You store these chunks and their embeddings in a search index. Azure AI Search is the natural choice here. You create an index with both text fields (for keyword search) and vector fields (for semantic search).

Step four: When a user asks a question, you generate an embedding of their question using the same embedding model.

Step five: You search the index to find the chunks most relevant to the user's question. This can be a vector search (finding chunks whose embeddings are closest to the question's embedding), a keyword search, or a hybrid search that combines both approaches.

Step six: You take the retrieved chunks and include them in the prompt to the language model. Typically, you add them to the system message or create a special context section. You tell the model: "Answer the user's question based only on the following context," then include the retrieved chunks.

Step seven: The model generates a response grounded in the retrieved context. Because the relevant information is right there in the prompt, the model can provide accurate, specific answers about your data.

Azure OpenAI has a feature called "On Your Data" that implements this RAG pattern with minimal code. You configure an Azure AI Search index as a data source, and Azure OpenAI automatically handles the retrieval step when you call the Chat Completions API.

Let me dig deeper into the RAG implementation details because the exam tests several nuances.

Chunking strategy matters a lot. If your chunks are too large, you waste context window space and might include irrelevant information. If they're too small, you lose context and the model might not have enough information to answer. Common chunking strategies include fixed-size chunks (like 500 tokens each), paragraph-based chunks (splitting on natural paragraph boundaries), and overlapping chunks (where each chunk overlaps the next by some percentage to preserve context at boundaries). Azure AI Search has a built-in text split skill that can handle chunking for you during indexing.

The embedding model you choose affects search quality. text-embedding-ada-002 produces 1,536-dimensional vectors. text-embedding-3-small produces 1,536 dimensions (configurable). text-embedding-3-large produces 3,072 dimensions (configurable) and is the highest quality option. Higher dimensions generally capture more nuance but require more storage and slightly more processing. You must use the same embedding model for both indexing and querying — if you embed documents with text-embedding-3-small, you must embed queries with text-embedding-3-small.

The retrieval phase can use several search strategies. Pure vector search finds semantically similar chunks regardless of keyword matches. This is great for questions that use different words than the documents. Pure keyword search finds chunks containing the exact words in the query. This is great for specific terms, product names, or jargon. Hybrid search combines both, which generally gives the best results. Semantic ranking can be layered on top to re-rank results using AI understanding.

When constructing the prompt with retrieved chunks, the typical pattern puts them in the system message: "You are a helpful assistant. Answer the user's question based ONLY on the following context. If the answer is not in the context, say 'I don't have that information.' Context: [chunk 1 text] [chunk 2 text] [chunk 3 text]." The instruction to only use the provided context is crucial for reducing hallucination.

The Azure OpenAI "On Your Data" feature automates much of this. When you call the chat completions API with a data_sources parameter pointing to your AI Search index, the service automatically generates a query, searches the index, retrieves relevant documents, includes them in the prompt, and generates a grounded response. The response includes citations showing which documents each part of the answer came from.

For the exam, understand the end-to-end flow, the role of embeddings, the difference between chunking strategies, and how "On Your Data" simplifies the implementation.

## DALL-E Image Generation

DALL-E is Azure OpenAI's image generation model. You provide a text description, and it creates an image. The API is straightforward — you call the images/generations endpoint with a prompt describing the image you want.

You can specify the image size. DALL-E 3 supports 1024 by 1024 (square), 1792 by 1024 (landscape), and 1024 by 1792 (portrait). You can also specify the quality as "standard" or "hd" (which takes longer but produces more detailed images) and the style as "vivid" (hyper-realistic) or "natural" (more subtle).

Content filtering applies to DALL-E just like text models. If the prompt or the generated image triggers content safety filters, the request will be rejected.

The exam doesn't go super deep on DALL-E, but you should know the basic API call structure, the available sizes, and that content filtering applies.

## Prompt Engineering Techniques

Prompt engineering is the art of crafting inputs that get the best outputs from language models. The exam tests several specific techniques.

Zero-shot prompting is when you ask the model to perform a task without giving any examples. "Classify the following email as spam or not spam: [email text]." The model relies on its general training to understand the task.

Few-shot prompting is when you include examples in the prompt. "Classify the following emails as spam or not spam. Example 1: 'You won a prize!' — Spam. Example 2: 'Meeting at 3pm tomorrow.' — Not Spam. Now classify: [email text]." Few-shot examples help the model understand the exact format and criteria you want.

Chain-of-thought prompting encourages the model to show its reasoning step by step before arriving at an answer. "Solve this math problem. Think step by step." This often produces more accurate results for complex reasoning tasks because the model is essentially "thinking out loud."

System prompts are the system messages we discussed earlier. Effective system prompts clearly define the model's persona, behavior boundaries, output format, and any specific rules. A well-crafted system prompt is the single most impactful prompt engineering technique.

Prompt templates use parameterized placeholders that get filled in at runtime. Instead of hardcoding a prompt, you define a template like "Summarize the following document in {num_sentences} sentences: {document_text}" and fill in the parameters dynamically. Microsoft Foundry's prompt flow feature supports prompt templates natively.

The exam might describe a scenario where the model's output isn't meeting expectations and ask which prompt engineering technique would help. If the model doesn't understand the task format, few-shot examples help. If it's making reasoning errors, chain-of-thought helps. If it's not following behavioral guidelines, a better system prompt helps.

## Fine-Tuning: When and How

Fine-tuning is the process of further training a pre-existing model on your own data to customize its behavior. Let me explain when you'd use fine-tuning versus other approaches, and how it works.

When should you fine-tune? Fine-tuning is appropriate when you need the model to consistently produce outputs in a very specific style or format, when few-shot examples aren't enough to guide the behavior, when you want to improve performance on domain-specific tasks, or when you want to reduce prompt size (since the model "learns" the patterns, you don't need as many examples in each prompt).

When should you NOT fine-tune? If you need the model to have access to specific factual data, use RAG instead. Fine-tuning is about style and behavior, not about teaching the model new facts. If few-shot prompting gets good enough results, stick with that — it's much simpler and cheaper than fine-tuning.

The fine-tuning process in Azure OpenAI works as follows. You prepare training data in JSONL format — that's JSON Lines, where each line is a separate JSON object. Each line represents a training example with the same message format used by the Chat Completions API: a system message, a user message, and an assistant message showing the desired response.

Here's what a training example looks like conceptually: a JSON object with a "messages" array containing three objects — one with role "system" and your system prompt, one with role "user" and the input, and one with role "assistant" and the ideal output.

You need at least 10 training examples, but Microsoft recommends 50 to 100 for good results. More examples generally improve quality. You upload your training file, create a fine-tuning job, wait for training to complete, and then deploy the fine-tuned model to an endpoint.

The exam might ask about the training data format (JSONL), the minimum number of examples needed, or when to choose fine-tuning versus RAG.

## Model Evaluation Metrics

Evaluating the quality of generative AI outputs is crucial, and the exam tests several evaluation metrics.

Groundedness measures whether the model's output is factually grounded in the provided context or source material. This is especially important for RAG scenarios. A groundedness score of 1 means everything in the output is supported by the context.

Relevance measures how relevant the output is to the user's question. A response might be factually correct but not actually answer what was asked.

Coherence measures how logically connected and well-structured the output is. Does it flow naturally? Are the ideas organized sensibly?

Fluency measures the linguistic quality — grammar, word choice, readability. Is it well-written?

Similarity measures how close the model's output is to a reference answer, if one is available.

These metrics can be evaluated automatically using evaluation flows in Microsoft Foundry, or manually through human evaluation. The Foundry SDK provides built-in evaluators for each of these metrics.

The exam might describe a scenario where an AI solution is generating outputs that aren't sticking to the provided data, and ask which metric is most relevant. That would be groundedness.

---

# Chapter 3: Agentic Solutions (5 to 10 percent)

This is the smallest domain on the exam, but it represents the cutting edge of AI engineering. Agents are AI systems that can autonomously perform tasks using tools, make decisions, and chain together complex workflows. Let's explore what you need to know.

## What Agents Are and When to Use Them

An AI agent is fundamentally different from a simple chatbot or API call. While a chatbot responds to individual queries in a stateless way, an agent can plan multi-step tasks, use tools to take actions, maintain memory across interactions, and work toward complex goals with minimal human intervention.

Think of it this way: if you ask a chatbot "What's the weather in Seattle?", it gives you an answer and forgets about you. If you ask an agent "Plan a trip to Seattle next week, checking the weather forecast, finding hotels under $200, and booking one that's close to the convention center," the agent would break that into subtasks, call a weather API, search hotel databases, compare options, and potentially make a booking — all autonomously.

You should use agents when the task requires multiple steps and tool interactions, when the workflow benefits from autonomous decision-making, when you need the AI to interact with external systems (databases, APIs, file systems), and when the task involves processing or analyzing documents.

You should NOT use agents for simple question-answering tasks, for straightforward API calls that don't require planning, or when you need fully deterministic behavior with no room for AI decision-making.

## Agent Service versus Agent Framework

Microsoft provides two main approaches for building agents, and understanding the difference is important for the exam.

Microsoft Foundry Agent Service, also called Azure AI Agent Service, is the managed, cloud-hosted approach. You create an agent through the Foundry portal or SDK, configure it with tools (like code interpreter, file search, and custom functions), and deploy it as a managed service. The infrastructure is handled for you — you don't need to worry about hosting, scaling, or orchestration.

The Agent Service provides a straightforward API: you create an agent, create a thread (which represents a conversation), add messages to the thread, and run the agent. The agent autonomously decides which tools to use based on the user's request.

Microsoft Agent Framework, built on top of Semantic Kernel, is for more complex agent implementations. It's a code-first approach where you build agents using the Semantic Kernel SDK. This gives you more control over the agent's behavior, planning strategies, and orchestration patterns.

The Agent Framework is appropriate for complex multi-agent scenarios, custom orchestration logic, or when you need fine-grained control over how the agent makes decisions.

The key difference: Agent Service is managed and simpler (great for straightforward agent tasks), while Agent Framework is more flexible and powerful (better for complex, custom scenarios).

## Tools: Code Interpreter, File Search, and Function Calling

Agents are only as useful as the tools they can access. There are three primary tool types you need to know.

Code Interpreter gives the agent the ability to write and execute Python code in a sandboxed environment. This is powerful for data analysis, mathematical calculations, creating visualizations, and file format conversions. If a user uploads a CSV file and asks "What's the average sales by region?", the agent can write Python code to load the CSV, calculate the averages, and even generate a chart.

File Search allows the agent to search through uploaded documents to find relevant information. When you attach files to an agent or thread, the File Search tool automatically chunks the documents, creates embeddings, and performs retrieval when the agent needs information from those files. This is essentially RAG built into the agent framework.

Function Calling lets you define custom functions that the agent can invoke. You describe the function's purpose and parameters in a JSON schema, and when the agent determines it needs to use that function, it generates the appropriate parameters. Your code then executes the function and returns the result to the agent. This is how agents interact with your external systems — databases, APIs, business logic, and anything else you can wrap in a function.

The exam might present a scenario and ask which tool the agent should use. If it involves calculations or data processing, code interpreter. If it involves finding information in documents, file search. If it involves calling an external API or performing a business action, function calling.

## Multi-Agent Orchestration

For complex workflows, you can use multiple agents working together. This is called multi-agent orchestration.

The most common pattern is the planner-executor model. A planner agent breaks down a complex request into subtasks, then delegates each subtask to specialized executor agents. For example, a research request might involve one agent gathering data, another analyzing it, and a third writing a summary.

In multi-agent systems, agents communicate through shared threads or message passing. Each agent has its own specialization, tools, and instructions, but they coordinate to achieve a common goal.

The exam tests this at a conceptual level rather than diving deep into implementation details. Understand the pattern, when to use it (complex tasks that benefit from specialization), and the basic flow of planning, delegation, and coordination.

## Safety and Testing

Agent safety requires special attention because agents can take autonomous actions. You need to ensure that agents can't perform harmful actions, access unauthorized data, or go off the rails in unexpected ways.

Testing strategies for agents include unit testing individual tools and functions, integration testing the agent's end-to-end behavior, adversarial testing with edge cases and malicious inputs, and monitoring agent behavior in production with human-in-the-loop checkpoints for high-risk actions.

Multi-user scenarios add complexity — you need to ensure that one user's agent interactions don't leak data to another user.

The exam covers agent testing and optimization at a high level. Know that you should test agents thoroughly, monitor their behavior, and include safety guardrails.

---

# Chapter 4: Computer Vision Solutions (10 to 15 percent)

Computer vision is one of the more hands-on domains on the exam. You'll need to understand how to analyze images, build custom vision models, and work with video content. Let's walk through each area.

## Image Analysis 4.0 API and Visual Features

The Image Analysis 4.0 API is the latest version of Azure AI Vision's image analysis capabilities. When you call this API, you specify which visual features you want to analyze, and the service returns results for each requested feature.

The visual features available are as follows.

Tags generate a list of words that describe the image content. Each tag includes a confidence score. For example, an image of a dog in a park might return tags like "dog," "outdoor," "grass," "park," "animal."

Caption generates a human-readable description of the image. For example, "A golden retriever playing in a grassy park."

Dense Captions generate multiple captions for different regions of the image. While regular captioning describes the whole image, dense captions describe specific areas — useful for complex scenes with multiple objects.

Objects detect specific objects in the image and return their bounding boxes — the coordinates that define a rectangle around each detected object. Each object includes its type, confidence score, and bounding box coordinates.

People detect the presence and location of people in the image, returning bounding boxes around each detected person.

Read performs OCR to extract text from the image. This is the same technology available through the Read API endpoint.

Smart Crops suggest optimal crop regions for the image, useful when you need to generate thumbnails or resize images for different aspect ratios.

To call the API, you make a POST request to your resource's computer vision endpoint, specifying the features you want as a query parameter. For example, you'd add "features=caption,tags,objects,read" to the URL. The request body can contain either a URL to the image or the raw image bytes.

The response is a JSON object with results for each requested feature. You'll get arrays of tags with confidence scores, the generated caption with a confidence score, arrays of detected objects with bounding boxes, and extracted text organized into lines and words.

Here's a critical exam detail about file limits for the Image Analysis API. The maximum file size is 4 megabytes. The maximum image dimension is 20 megapixels. The minimum image dimension is 50 by 50 pixels. Supported formats include JPEG, PNG, GIF, BMP, WEBP, ICO, and TIFF. Only one image can be analyzed per request. These numbers are explicitly tested on the exam, so commit them to memory.

## OCR and Handwriting Extraction

The Read API, also accessible as the "read" feature in Image Analysis 4.0, is Azure's OCR technology for extracting text from images and documents. It handles both printed and handwritten text, which is a key differentiator.

The Read API uses deep learning models to extract text from a wide variety of sources — photos of signs, scanned documents, handwritten notes, and complex layouts with mixed content. It supports 164 languages for printed text and a growing number for handwriting.

When you call the Read API, the response organizes the extracted text hierarchically: pages contain lines, and lines contain words. Each word includes the text, a bounding polygon (the outline around the word in the image), and a confidence score. Lines include the combined text and their own bounding polygon.

The confidence scores are important for applications that need to validate extraction quality. A confidence below a certain threshold might trigger manual review.

For the exam, remember that the Read API is the recommended approach for text extraction. It's available both as a standalone API endpoint and as the "read" feature within Image Analysis 4.0. It handles printed text, handwritten text, and mixed content.

## Custom Vision: Classification versus Object Detection

When the prebuilt Image Analysis models don't meet your needs, you turn to Custom Vision to train your own models. There are two main model types, and understanding when to use each is critical for the exam.

Image classification determines what category an image belongs to. There are two subtypes: multiclass classification, where each image belongs to exactly one category (like "cat," "dog," or "bird"), and multilabel classification, where an image can belong to multiple categories simultaneously (like "outdoor," "winter," and "mountain" all applying to the same image).

Object detection locates specific objects within an image and returns their bounding boxes. Unlike classification, which labels the entire image, object detection identifies and locates individual objects. An image of a kitchen might detect "plate," "cup," "fork," "knife" with bounding boxes around each.

When should you use classification? When you need to categorize entire images — quality inspection (defective vs. non-defective), scene recognition, or product categorization. When should you use object detection? When you need to find and locate specific items within images — counting products on a shelf, identifying components in a manufacturing process, or detecting safety equipment on workers.

The training workflow for Custom Vision follows these steps. First, you create a Custom Vision project in the Custom Vision portal or via the SDK, specifying whether it's classification or detection. Second, you upload and label your training images. For classification, you tag each image with its category. For object detection, you draw bounding boxes around objects and label them. Third, you train the model. You need a minimum of 15 images per tag, though Microsoft recommends 50 or more for good results. Fourth, you evaluate the model using the metrics the service provides. Fifth, you publish the model to a prediction endpoint. Sixth, you consume the model from your application using the prediction API.

## Training Workflow and Evaluation Metrics

Let's dig deeper into the evaluation metrics for Custom Vision, because the exam tests these.

Precision measures, of all the predictions the model made for a given class, what percentage were correct. High precision means few false positives. If the model says "this is a cat" 100 times and 95 of those are actually cats, precision is 95 percent.

Recall measures, of all the actual instances of a given class, what percentage did the model correctly identify. High recall means few false negatives. If there are 100 actual cat images and the model correctly identifies 90 of them, recall is 90 percent.

Average Precision, or AP, combines precision and recall into a single score. It's calculated as the area under the precision-recall curve. Higher AP means the model performs well across different confidence thresholds.

Mean Average Precision, or mAP, is the average of AP across all classes. This is the primary metric for object detection models.

The exam might show you evaluation results and ask you to interpret them. If precision is high but recall is low, the model is conservative — when it makes a prediction, it's usually right, but it's missing many actual instances. If recall is high but precision is low, the model is aggressive — it catches most instances but has many false positives.

## The Code-First Approach

The exam specifically tests your ability to build Custom Vision models entirely through code, without using the portal. This is called the code-first approach, and it's a favorite topic.

Using the Custom Vision SDK, you can programmatically create a project, create tags, upload and tag images, train the model, evaluate results, and publish to a prediction endpoint. The training SDK and prediction SDK are separate packages. In Python, you use azure-cognitiveservices-vision-customvision for training and the same package's prediction module for inference.

The key thing the exam tests is whether you know the sequence of SDK calls. Create project, create tag, upload images with tags, train (which returns an iteration), check training status, publish the iteration to a prediction endpoint, then use the prediction client to classify new images.

## Video Indexer Capabilities

Azure AI Video Indexer is a powerful service that extracts a wealth of insights from video content. Here's what it can do.

Transcription extracts the spoken words from the video's audio track, creating a time-stamped transcript.

Face detection identifies and groups faces that appear throughout the video, tracking when each person appears.

Topic identification extracts the key topics discussed in the video.

Emotion detection analyzes the emotions expressed by speakers.

OCR extracts text that appears in the video frames — like slides, signs, or on-screen text.

Brand recognition identifies brands mentioned in the speech or shown in the video.

Scene and shot detection segments the video into logical scenes and camera shots.

Keyword extraction identifies significant keywords from the audio and visual content.

For the exam, know the file limits: maximum file size is 2 gigabytes, maximum video duration is 4 hours, and supported formats include MP4, MOV, AVI, FLV, MKV, WMV, WebM, and others.

Video Indexer can be accessed through its web portal, through its REST API for programmatic access, or embedded into your own applications using widgets.

## Face API and Responsible AI Restrictions

The Face API deserves special mention because of the responsible AI restrictions Microsoft has placed on it.

The Face API can detect faces in images, returning the location (bounding box) and attributes of each face. However, Microsoft has restricted certain facial analysis capabilities. As of June 2023, Microsoft retired facial recognition capabilities that infer emotional states and identity attributes like age, gender, and smile from faces. These features are no longer available in the public API.

The remaining Face API capabilities include face detection (finding faces in an image), face verification (comparing two faces to determine if they belong to the same person), and face identification (matching a face against a group of known faces). However, face verification and identification require an application and approval from Microsoft for use.

The exam tests responsible AI considerations around face analysis. Know that emotion detection and attribute inference from faces is no longer available, and that identity-related features require approval.

## File Size Limits Summary for Vision Services

Let me consolidate the file size limits for all vision-related services, because these are explicitly tested on the exam.

For Image Analysis 4.0: 4 megabyte maximum file size, 20 megapixel maximum dimension, 50 by 50 pixel minimum, supports JPEG, PNG, GIF, BMP, WEBP, ICO, and TIFF.

For Custom Vision: 6 megabyte maximum file size for images, minimum 15 images per tag for training, maximum 500 tags for classification projects or 100 tags for detection projects, maximum 100,000 images per project, supports JPEG, PNG, BMP, and GIF.

For Video Indexer: 2 gigabyte maximum file size, 4 hour maximum duration, supports MP4, MOV, AVI, FLV, MKV, WMV, WebM, and more.

---

# Chapter 5: Natural Language Processing Solutions (15 to 20 percent)

NLP is a rich domain covering text analytics, translation, speech services, and custom language models. This is one of the heavier exam areas, so let's be thorough.

## Text Analytics: Sentiment, Entities, Key Phrases, PII, and Language Detection

Azure AI Language provides a suite of prebuilt text analytics capabilities. Let's walk through each one.

Sentiment analysis determines whether a piece of text expresses positive, negative, neutral, or mixed sentiment. It works at both the document level and the sentence level. For each level, you get confidence scores for positive, negative, and neutral sentiment — three numbers that add up to 1.0. For example, a review saying "The food was amazing but the service was terrible" might get a mixed document sentiment, with the first sentence scored as positive and the second as negative.

The sentiment API also supports opinion mining, which goes even deeper by identifying the specific aspects or targets of opinions and the sentiment toward each. In our restaurant example, opinion mining would identify "food" as a target with positive sentiment and "service" as a target with negative sentiment.

Named Entity Recognition, or NER, identifies and categorizes entities in text. Entities include people, organizations, locations, dates, quantities, URLs, email addresses, and many more categories. Each recognized entity includes the text, the category, a subcategory (when applicable), and a confidence score. For example, in the sentence "Microsoft was founded in 1975 in Albuquerque," NER would identify "Microsoft" as an Organization, "1975" as a DateTime, and "Albuquerque" as a Location.

Key phrase extraction identifies the main talking points in a document. It returns a list of strings representing the key concepts. This is useful for quickly understanding what a document is about without reading the whole thing.

PII detection identifies and optionally redacts personally identifiable information. The categories include names, addresses, email addresses, phone numbers, Social Security numbers, credit card numbers, and many more. The API returns the detected entities with their categories and positions in the text, and also provides a redacted version of the text where PII is replaced with category labels. For example, "Call John at 555-1234" becomes "Call [Person] at [Phone Number]."

Language detection identifies the language of a given text and returns the language name, its ISO code, and a confidence score. It can detect over 120 languages. You can send multiple documents in a single request, and each can be a different language. This is often used as a preprocessing step before sending text to other services that require a language parameter.

All of these text analytics features use the same Azure AI Language endpoint and the same API pattern. You send a POST request with your documents in a specific JSON structure — each document has an ID, optional language, and the text to analyze. You specify the analysis kind (SentimentAnalysis, EntityRecognition, KeyPhraseExtraction, PiiEntityRecognition, or LanguageDetection) in the request body.

Let me share some practical details about each capability that come up on the exam.

For sentiment analysis, the document-level sentiment can be "positive," "negative," "neutral," or "mixed." "Mixed" appears when different sentences within the document express different sentiments. Each sentence gets its own sentiment and confidence scores. The confidence scores for positive, negative, and neutral always add up to 1.0. The exam might show you confidence scores like positive: 0.1, negative: 0.85, neutral: 0.05, and ask what the sentiment is — the answer is negative because it has the highest confidence.

Opinion mining, which is an optional feature of sentiment analysis, goes deeper by identifying specific aspects (or targets) and the opinions about them. In the text "The room was clean but the food was cold," opinion mining would identify two assessments: "clean" is a positive opinion about the target "room," and "cold" is a negative opinion about the target "food." You enable opinion mining by adding the opinionMining parameter to your sentiment analysis request.

For named entity recognition, the categories include Person, Location, Organization, DateTime, Quantity, Percentage, Currency, Email, URL, PhoneNumber, IPAddress, and many more. Each entity has a category, subcategory (like DateTime might have subcategories Date, Time, DateRange, etc.), text, offset, length, and confidence score. The exam might show you NER output and ask you to identify which entity category is returned for a given text span.

For PII detection, the important thing to know is that it returns both the detected entities AND a redacted version of the text. The redacted text replaces each detected PII with its category label in square brackets. So "Call John Smith at 555-0123" becomes "Call [Person] at [PhoneNumber]." You can also specify which PII categories to detect or exclude. The piiCategories parameter lets you limit detection to specific types like SSN, Email, or CreditCardNumber. The domain parameter can be set to "phi" (Protected Health Information) for healthcare scenarios.

For language detection, the response includes the detected language name, the ISO 639-1 code (like "en" for English, "fr" for French, "zh" for Chinese), and a confidence score. If the service can't detect the language, it returns "(Unknown)" with a confidence of 0.0. You can analyze up to 5,120 characters per document.

One batch processing detail: you can send up to 25 documents per request for most text analytics operations. Each document can contain up to 5,120 characters. If you have more documents, you need to split them into multiple requests. The exam might test these batch limits.

## Entity Linking

Entity linking is a distinct capability from named entity recognition, and the exam specifically tests the difference. While NER identifies entities and their categories, entity linking goes further by connecting each entity to a corresponding entry in a well-known knowledge base — specifically, Wikipedia.

For example, if your text mentions "Washington," NER might tag it as a Location. But is it Washington state, Washington D.C., George Washington the person, or Denzel Washington the actor? Entity linking resolves this ambiguity by examining the context and linking to the correct Wikipedia article.

The response includes the entity name, the matched Wikipedia entry, a URL to the Wikipedia article, the data source (Wikipedia), and confidence scores. Each entity also includes the specific matches — the locations in the text where the entity was referenced, along with their offsets and confidence scores.

The exam loves to test the distinction between NER and entity linking. NER categorizes entities by type. Entity linking disambiguates entities and connects them to Wikipedia. If the question asks about identifying the specific real-world entity (not just the category) that a mention refers to, the answer is entity linking.

Let me give you a clear example to cement this distinction. Consider the sentence "Apple released a new product in Cupertino." With NER, you'd get "Apple" categorized as Organization and "Cupertino" categorized as Location. That's useful, but NER doesn't tell you WHICH organization or WHICH location. Entity linking goes further: it would link "Apple" to the Wikipedia article for Apple Inc. (not the fruit) and "Cupertino" to the Wikipedia article for Cupertino, California (not another city with the same name).

The disambiguation is the key differentiator. When text contains ambiguous names — "Paris" (city in France or city in Texas?), "Mercury" (planet, element, or Roman god?), "Jordan" (country, river, or Michael Jordan?) — entity linking resolves the ambiguity by using the surrounding context to identify the correct real-world entity.

Here's another exam scenario: "A company needs to process customer feedback and identify the specific products, companies, and locations mentioned, and provide links to more information about each." This is entity linking, not NER, because the key requirement is "provide links to more information" — entity linking gives you Wikipedia URLs, NER does not.

## Translation: Text, Documents, and Custom Translator

Azure AI Translator provides three main translation capabilities.

Text translation is the most straightforward. You send text in one language, and it comes back translated to one or more target languages. You can specify the source language or let the service auto-detect it. You can translate to multiple target languages in a single request. The API also supports transliteration, which converts text from one script to another — for example, converting Chinese characters to Latin script.

The text translation endpoint is a bit different from other AI services. It uses the global endpoint api.cognitive.microsofttranslator.com rather than a resource-specific endpoint. You authenticate with your resource's subscription key in the "Ocp-Apim-Subscription-Key" header.

Document translation preserves the formatting and structure of your original documents while translating the content. You provide documents in supported formats — PDF, Word, Excel, PowerPoint, HTML, and more — and get back translated documents in the same format. This is an asynchronous, batch operation. You upload source documents to a blob storage container, specify the target language and output container, and the service processes them in the background.

Custom Translator lets you build custom translation models tailored to your specific domain, terminology, and style. You provide parallel training data — sentences in the source language paired with their correct translations in the target language. The service trains a custom model that learns your terminology and style preferences. This is useful for industries with specialized vocabulary like legal, medical, or technical fields.

For the exam, know when to use each approach. Standard text translation for general-purpose, real-time translation. Document translation for preserving formatting in batch scenarios. Custom Translator when you have domain-specific terminology that standard translation doesn't handle well.

Let me share more details on each translation mode because they have distinct API patterns that the exam tests.

For text translation, the REST API endpoint is api.cognitive.microsofttranslator.com/translate. You include the api-version, the "to" parameter with the target language code (like "fr" for French), and optionally the "from" parameter with the source language code (omit this for auto-detection). The request body is a JSON array of objects, each with a "Text" field. You can translate to multiple languages in a single request by including multiple "to" parameters — for example, "to=fr&to=de&to=es" translates to French, German, and Spanish simultaneously.

The response includes the detected language (if you didn't specify "from"), and an array of translations, one for each target language. Each translation includes the translated text, the target language code, and if transliteration was requested, the transliterated text.

Transliteration deserves its own mention because it's sometimes tested. Transliteration is different from translation — it converts text from one script to another without changing the language. For example, converting Japanese Kanji to Latin script (romanization), or converting Hindi Devanagari to Latin script. You use the /transliterate endpoint with the language, "fromScript," and "toScript" parameters.

For document translation, the process is asynchronous and uses Azure Blob Storage. You upload source documents to a source container in blob storage. You specify a target container for the translated documents. You make a POST request to start the translation batch, providing the source URL, target URL, target language, and optionally a glossary URL. The service processes the documents asynchronously and writes translated documents to the target container. You can poll for status or use webhooks for notification.

The glossary feature is important for Custom Translator and worth mentioning. A glossary is a file (CSV or TSV format) that maps specific terms to their translations. This ensures that domain-specific terms are always translated consistently — for example, ensuring that your product name "CloudSync Pro" is never translated and always kept as-is.

Custom Translator takes this further by letting you train a full translation model on your parallel data. You provide sentence-aligned documents in the source and target languages — these are called "parallel corpus" files. The service trains a custom model that learns your terminology, style, and domain patterns. You can then use this custom model for both text translation and document translation.

## Speech-to-Text and Text-to-Speech

Azure AI Speech provides comprehensive speech capabilities. Let's cover both directions.

Speech-to-text, also called speech recognition, converts spoken audio into text. There are several modes.

Real-time recognition transcribes audio as it's being spoken. Using the Speech SDK, you create a speech recognizer, start recognition, and receive results in real-time. There are two main modes: single-shot recognition, which transcribes a single utterance (the recognizer stops at a pause), and continuous recognition, which keeps transcribing until you stop it. Continuous recognition is what you'd use for transcribing a meeting or a long-form conversation.

The REST API for speech-to-text accepts audio files up to 25 megabytes and 60 seconds for a single request. For longer audio, you need to use the SDK's continuous recognition or batch transcription.

Batch transcription is for processing large audio files asynchronously. It supports files up to 1 gigabyte and 24 hours of audio. You upload audio to blob storage, create a batch transcription job, and poll for results. Supported formats include WAV, MP3, OGG, FLAC, WMA, AAC, and others.

Text-to-speech, also called speech synthesis, converts text into spoken audio. Azure offers a wide range of neural voices across many languages, and the output sounds remarkably natural. You can use plain text for simple synthesis or SSML for fine-grained control over the output.

Intent recognition combines speech recognition with language understanding. The Speech SDK can recognize speech and simultaneously extract the intent using a CLU model. This is useful for voice-controlled applications where you need to understand both what was said and what the user wants.

Keyword recognition detects a specific keyword or wake phrase in audio. Think of it like "Hey Siri" or "OK Google" — the system listens for a specific word or phrase and then activates. This is useful for hands-free activation of voice assistants.

Speech translation converts speech in one language to text or speech in another language. It combines speech recognition with translation, and can output either translated text or synthesized translated speech.

Let me expand on the speech services with more practical details that the exam tests.

For real-time speech-to-text using the SDK, the core pattern involves creating a SpeechConfig with your subscription key and region, creating an AudioConfig that specifies the audio source (microphone, audio file, or audio stream), and creating a SpeechRecognizer with both configs. For single-shot recognition, you call recognize_once_async() which returns a SpeechRecognitionResult. The result includes a reason (Recognized, NoMatch, Canceled), and if recognized, the text and timing information. For continuous recognition, you wire up event handlers — recognized events for final results and recognizing events for partial, interim results — then call start_continuous_recognition_async().

For the REST API, speech-to-text uses a different endpoint pattern than other cognitive services. The endpoint is region-based: your-region.stt.speech.microsoft.com for speech-to-text. You send audio data as the request body with a Content-Type of audio/wav (or the appropriate format). The response includes the recognized text, confidence scores, and timing offsets.

For text-to-speech, the SDK pattern is similar: create SpeechConfig, create SpeechSynthesizer, and call speak_text_async() for plain text or speak_ssml_async() for SSML. The output can go to the default speaker, to an audio file, or to an audio stream.

For the REST API, text-to-speech uses the endpoint region.tts.speech.microsoft.com. You specify the desired voice in the request headers (X-Microsoft-OutputFormat for the audio format) and send the text or SSML as the request body. The response is the audio data in the specified format.

Pronunciation assessment is another feature of the Speech service worth knowing. It evaluates how well someone pronounces words and provides scores for accuracy, fluency, completeness, and pronunciation. This is used in language learning applications.

Speaker recognition identifies or verifies speakers based on their voice characteristics. Speaker verification confirms if a speaker is who they claim to be (one-to-one matching). Speaker identification determines which speaker in a group is speaking (one-to-many matching). There are text-dependent and text-independent modes.

Here are the important file limits for speech. Real-time recognition via REST: 25 megabyte max, 60 seconds max. Batch transcription: 1 gigabyte max, 24 hours max. Supported formats for real-time: WAV with PCM encoding, OGG with Opus, FLAC, and MP3. Batch transcription adds WMA, AAC, ALAW, and MULAW. Sample rates of 8 kilohertz or 16 kilohertz for real-time, and 8 to 48 kilohertz for batch.

## SSML Deep Dive

SSML — Speech Synthesis Markup Language — is one of the most heavily tested topics on the entire exam. The exam goes deep on SSML elements, attributes, and values. Let me walk you through every important element.

SSML is an XML-based markup language that gives you fine-grained control over how text-to-speech output sounds. Instead of just sending plain text and getting default speech back, SSML lets you control the voice, speed, pitch, volume, pauses, emphasis, pronunciation, and speaking style.

Every SSML document starts with the speak element. It requires the version attribute (always "1.0"), the XML namespace for the standard synthesis namespace, and the xml:lang attribute specifying the default language. If you're using Microsoft-specific extensions like voice styles, you also include the mstts namespace.

Now let's go through each element in detail.

The voice element selects which neural voice to use. Azure offers dozens of voices across many languages. You specify the voice by name — for example, "en-US-JennyNeural" for an English US female voice, or "en-GB-RyanNeural" for a British English male voice, or "en-US-GuyNeural" for an English US male voice. You can switch voices within the same SSML document by using multiple voice elements, which is useful for dialogues or switching between narrators.

The prosody element controls three aspects of delivery: rate, pitch, and volume. Rate controls how fast or slow the speech is. You can use named values like "x-slow," "slow," "medium," "fast," or "x-fast." You can also use relative values like "plus 20 percent" or "minus 30 percent." Pitch controls how high or low the voice sounds. Named values include "x-low," "low," "medium," "high," and "x-high." You can use relative percentages or absolute values in hertz, like "200Hz." Volume controls loudness, with named values of "silent," "x-soft," "soft," "medium," "loud," and "x-loud," or relative percentages. These prosody attributes are heavily exam-tested.

The break element inserts pauses. You can specify the duration with the time attribute (like "500ms" for half a second or "2s" for two seconds) or use the strength attribute with values like "none," "x-weak," "weak," "medium," "strong," or "x-strong." Each strength value corresponds to a different pause duration. This is incredibly useful for making speech sound natural — real speakers pause between sentences and after important points.

The emphasis element controls how much stress is placed on a word or phrase. The level attribute can be "strong" (heavy emphasis), "moderate" (default emphasis), or "reduced" (less emphasis than surrounding text). For example, wrapping the word "important" in an emphasis element with level "strong" makes the voice stress that word when speaking.

The say-as element controls pronunciation for specific types of content. The interpret-as attribute tells the speech engine how to read the content. The values include "date" (reads numbers as a date — you can specify the format like "mdy" for month-day-year), "time" (reads as a time value), "telephone" (reads as a phone number with appropriate pauses), "cardinal" (reads as a counting number), "ordinal" (reads as an ordinal — "3" becomes "third"), "characters" (spells out each character individually), and "address" (reads as a street address). This is essential for content like phone numbers, dates, and abbreviations that might be read incorrectly with default pronunciation.

The mstts:express-as element is a Microsoft-specific extension that applies speaking styles. Different voices support different styles, but common styles include "cheerful," "sad," "angry," "excited," "friendly," "terrified," "shouting," "whispering," and "hopeful." Not all voices support all styles, so you need to check the documentation. The style attribute specifies which style to use, and you can also include a styledegree attribute from 0.01 to 2 to control the intensity of the style.

The audio element inserts pre-recorded audio into the speech output. You specify the source URL, and the audio file is played at that point in the synthesis. This is useful for jingles, sound effects, or standard announcements.

The sub element provides a pronunciation substitute. The alias attribute specifies what the speech engine should say instead of the element's text content. For example, you might use sub to make "W3C" pronounce as "World Wide Web Consortium."

The phoneme element specifies the exact phonetic pronunciation using the International Phonetic Alphabet (IPA) or SAPI notation. This gives you the most precise control over pronunciation, useful for words the engine might mispronounce.

The lang element switches languages mid-utterance. If your document is primarily in English but includes a French phrase, you can wrap the French text in a lang element with xml:lang="fr-FR" to ensure correct pronunciation.

The bookmark element marks a point in the audio stream and fires an event when the synthesizer reaches that point. This is useful for synchronizing speech with visual content, like highlighting text as it's being read.

The mstts:silence element provides fine-grained silence control, separate from the break element. It can add silence at the beginning (leading) or end (tailing) of the speech, or between sentences (sentenceboundary).

Let me walk you through a comprehensive example to tie it all together. Imagine you're building a news briefing app. Your SSML would start with the speak element and its namespaces. Inside, you'd have a voice element selecting a neural voice. You might apply a friendly style with mstts:express-as. Then you'd use a prosody element to slow down the rate slightly for clarity. You'd use say-as with interpret-as "date" to correctly read the current date. You'd use break elements between sections. You might switch to a different voice for a different segment. And you'd use emphasis on key words.

The exam tests SSML in several ways. They might show you SSML markup and ask what it produces. They might describe a desired speech output and ask you to write the SSML. Or they might give you partially completed SSML and ask you to fill in the missing attributes. Knowing every element and its key attributes is essential.

Let me walk you through more specific SSML scenarios that mirror exam questions.

Scenario one: "You want the speech synthesizer to read a phone number digit by digit, with natural pauses between groups." The SSML uses say-as with interpret-as="telephone." You'd write something like: say-as interpret-as equals telephone, then the phone number plus 1 425 555 0100, then close the say-as tag. The synthesizer will read it naturally as a phone number rather than as the number one billion four hundred twenty-five million.

Scenario two: "You need the synthesizer to pause for two seconds between paragraphs, then speed up for a list of items." You'd use a break element with time="2s" between paragraphs, then wrap the list in a prosody element with rate="fast" or rate="+30%".

Scenario three: "Your application needs to switch between an American English voice for the main narration and a British English voice for quoted text." You'd use nested voice elements — the outer voice with name="en-US-JennyNeural" for the narration, and within the quoted sections, switch to voice name="en-GB-RyanNeural."

Scenario four: "You want the synthesizer to read 'Dr. Smith' as 'Doctor Smith' and 'St.' as 'Street' (not 'Saint')." You'd use the sub element. For "Dr." you'd write sub alias="Doctor," followed by "Dr." as the element content. For "St." in an address context, sub alias="Street."

Scenario five: "The application should express excitement when announcing a prize, then switch to a calm, informative tone for the terms and conditions." You'd use mstts:express-as with style="excited" for the prize announcement, then switch to style="calm" or just remove the style element for the neutral terms section.

Let me also go deeper on the prosody values because the exam gets specific. For rate, the named values map approximately to these speeds: x-slow is about half the normal speed, slow is about 80 percent, medium is normal, fast is about 120 percent, and x-fast is about 150 percent. You can also use relative values like "+20%" to make it 20 percent faster than the default, or absolute multipliers like "1.5" for 1.5 times normal speed.

For pitch, the named values map to different frequency ranges. x-low drops the pitch significantly, low drops it somewhat, medium is the default, high raises it, and x-high raises it significantly. You can specify absolute values in hertz like "200Hz" (which is a fairly high-pitched voice for adult male speakers) or relative values like "+10%" for slightly higher.

For volume, the named values are: silent (no sound), x-soft (barely audible), soft (quiet), medium (normal), loud (louder than normal), and x-loud (maximum volume). These are useful for creating dynamic audio that mirrors natural speech — lowering volume for asides or raising it for emphasis.

The break element's strength attribute values map to these approximate durations: none is zero pause, x-weak is about 250 milliseconds, weak is about 500 milliseconds, medium is about 750 milliseconds, strong is about 1 second, and x-strong is about 1.25 seconds. When you use the time attribute instead, you specify exact durations like "200ms" or "1.5s".

Here's one more important SSML detail: the voice element's name attribute must exactly match a valid Azure neural voice name. These follow the pattern language-region-NameNeural, like "en-US-JennyNeural" or "de-DE-ConradNeural." Using an invalid voice name causes an error. The exam might show you a list of voice names and ask which one is valid for a specific language.

The mstts namespace (Microsoft Text-to-Speech extensions) provides additional capabilities beyond the standard SSML specification. Besides express-as for styles, there's mstts:silence for fine-grained silence control (with types "Leading" for silence before speech, "Tailing" for silence after speech, and "Sentenceboundary" for silence between sentences), and mstts:viseme for generating facial animation data synchronized with speech.

## Custom Speech Models

Custom Speech lets you create speech recognition models tailored to your specific needs. There are two main customization scenarios.

Acoustic model adaptation improves recognition in specific acoustic environments. If your users are in a noisy factory, or speaking through a particular microphone, or your audio has specific acoustic characteristics, you can provide sample audio with transcriptions to improve recognition accuracy in that environment.

Language model adaptation improves recognition of domain-specific vocabulary and phrases. If your application deals with medical terminology, legal jargon, or product names that the default model doesn't handle well, you can provide text data with these terms to improve recognition.

To create a Custom Speech model, you upload training data (audio files with transcriptions for acoustic models, or text files for language models), train the model in the Speech Studio, evaluate it against test data, and deploy it as a custom endpoint.

The exam doesn't go extremely deep on Custom Speech, but you should know that it exists, what it's for, and the basic workflow of training and deploying custom models.

## Conversational Language Understanding: Intents, Entities, and Utterances

Conversational Language Understanding, or CLU, is the replacement for LUIS (Language Understanding Intelligent Service). It's how you build natural language understanding models that can interpret user intent and extract relevant information.

The three core concepts of CLU are intents, entities, and utterances.

An intent represents what the user wants to do. In a home automation system, intents might include "TurnOnLight," "TurnOffLight," "SetTemperature," and "PlayMusic." In a booking system, intents might include "BookFlight," "CancelReservation," and "CheckFlightStatus."

An entity represents a piece of relevant information within the user's statement. In the utterance "Turn on the kitchen light," the intent is "TurnOnLight" and "kitchen" is a location entity. In "Book a flight to Paris on Friday," the intent is "BookFlight," "Paris" is a destination entity, and "Friday" is a date entity.

An utterance is an example of something a user might say. You provide many utterances for each intent, labeled with the correct intent and any entities they contain. The model learns from these examples. For the "TurnOnLight" intent, utterances might include "Turn on the light," "Switch on the lights," "Enable the kitchen light," "Can you turn the lights on please," and so on. Variety in your utterances helps the model generalize.

The workflow for building a CLU model is as follows. You create a project in Language Studio (or via the SDK). You define your intents. You define your entity types — these can be learned entities (extracted from context), list entities (specific lists of values), or prebuilt entities (common types like datetime, number, person). You add utterances for each intent, labeling the entities within them. You need at least 10 utterances per intent, and more is better. You train the model. You evaluate it using precision, recall, and F1 score. You deploy it to a prediction slot. And finally, you consume it from your application.

The training process splits your data into training and testing sets. After training, you review the evaluation metrics for each intent and entity. F1 score is the harmonic mean of precision and recall, and it's the primary metric for CLU model quality. If specific intents have low F1 scores, you add more diverse utterances for those intents.

Deploying a CLU model involves assigning a trained model to a named deployment slot. You can have multiple deployments (like staging and production) and switch between them. Once deployed, you call the prediction API with user text and get back the predicted intent, its confidence score, and any extracted entities.

Let me walk through the CLU API call in detail because the exam shows this in code questions. To call a deployed CLU model, you send a POST request to the Language endpoint at your-resource.cognitiveservices.azure.com/language/:analyze-conversations, with the api-version parameter. The request body includes a "kind" of "Conversation," an "analysisInput" with a "conversationItem" containing the participant ID, an ID, and the "text" (the user's utterance). You also include "parameters" with the "projectName" and "deploymentName."

The response includes the predicted intent (the "topIntent"), its confidence score, and the list of all intents with their confidence scores. It also includes the extracted entities with their category, text, offset, length, and confidence score. If you defined list entities, the response shows which list value matched. If you defined prebuilt entities, the response shows the resolved value (like a parsed DateTime from a natural language date expression).

Using the Python SDK, you create a ConversationAnalysisClient, call the analyze_conversation method with the parameters, and parse the result object. The SDK provides typed access to the intents and entities.

The exam tests CLU in various ways. They might ask about the minimum number of utterances (10 per intent, though more is recommended). They might show you utterances and ask you to identify the correct entity labeling. Or they might describe a scenario and ask how to improve a model with poor performance on specific intents.

Let me give you specific improvement strategies that the exam tests. If an intent has low recall (the model misses many utterances that should match this intent), you need more diverse training utterances. Add examples with different wordings, sentence structures, and vocabulary. If an intent has low precision (the model incorrectly assigns other utterances to this intent), the intent might be too broad or overlap with another intent. Consider splitting it or adding negative examples. If entity extraction has low accuracy, add more examples with the entity in different positions and contexts within utterances.

The "None" intent is automatically included in every CLU project. It represents utterances that don't match any of your defined intents. Having good "None" intent coverage prevents your model from forcing irrelevant utterances into defined intents. The exam might test this — make sure you add diverse examples to the None intent.

## Importing and Exporting Language Projects

The exam specifically tests your knowledge of importing and exporting CLU and Custom Question Answering projects. This is important for several scenarios: backing up your projects, migrating between environments (development to production), version control, and collaboration.

CLU projects can be exported as JSON files that contain the complete project definition — intents, entities, utterances, and configuration. You can then import this JSON file into another Language resource to recreate the project. The export includes the schema version, project metadata, and all assets (intents, entities, and utterances with their labels).

Similarly, Custom Question Answering projects can be exported as files containing all question-answer pairs, their metadata, and conversation flows. You can export from Language Studio or via the REST API.

This is useful for CI/CD pipelines where you want to version-control your language models, test them in a staging environment, and promote them to production programmatically.

## Custom Question Answering: Knowledge Bases, Multi-Turn, and Chit-Chat

Custom Question Answering (which replaced QnA Maker) lets you build question-answering solutions from your existing content. Here's how it works.

You create a project in Language Studio, then add knowledge sources. These can be FAQ web pages (you provide the URL and the system automatically extracts question-answer pairs), documents (PDF, Word, Excel, TSV), or manual entries (you type in question-answer pairs directly).

Each entry in the knowledge base is a question-answer pair. A single answer can have multiple question phrasings — these alternate phrasings help the system match user questions to the right answer even when worded differently. For example, the answer "Our return policy allows returns within 30 days" might have question phrasings like "What's your return policy?", "How long do I have to return something?", "Can I get a refund?", and "What's the return window?"

Multi-turn conversations allow you to create hierarchical, guided conversations where follow-up prompts lead users through a decision tree. For example, asking "Do you need help with billing?" might have follow-up prompts for "View my bill," "Make a payment," or "Dispute a charge." Each follow-up prompt can have its own follow-up prompts, creating a tree structure.

Chit-chat adds personality to your knowledge base with pre-built question-answer pairs for common social interactions. You choose from personality styles — professional, friendly, witty, caring, or enthusiastic — and the system adds appropriate responses for small talk like "How are you?", "Tell me a joke," or "What's your name?"

After building your knowledge base, you train and test it in Language Studio, then publish it to a prediction endpoint. The endpoint returns the best matching answer for a given question, along with a confidence score.

Synonyms are another important feature. You can define synonyms so that different words are treated as equivalent during matching. For example, defining "account" and "subscription" as synonyms means a question about "my subscription" would match answers about "your account."

The exam tests knowledge base creation, multi-turn configuration, alternate phrasings, chit-chat personality selection, and export/import capabilities.

## Multi-Language Solutions

Custom Question Answering supports multi-language projects. When you enable multi-language support, you can add question-answer pairs in multiple languages within the same project. The system detects the language of incoming questions and returns answers in the matching language.

Alternatively, you can create separate projects for each language and route users to the appropriate project based on their language preference.

The exam might present a scenario where a company needs to support customers in multiple languages and ask which approach to use. Multi-language projects are simpler to manage but may have slightly lower accuracy for each language compared to dedicated single-language projects.

---

# Chapter 6: Knowledge Mining and Information Extraction (15 to 20 percent)

Knowledge mining is about making large volumes of unstructured data searchable and usable. This domain covers Azure AI Search, Document Intelligence, and Content Understanding. It's tied with NLP for the second-heaviest exam weight, so give it serious attention.

## Azure AI Search: Indexes, Skillsets, and Indexers

Azure AI Search is a cloud search service that creates rich, searchable indexes over your content. Understanding its architecture is key. There are three main components: indexes, indexers, and skillsets.

An index is the searchable data store. Think of it like a database table, but optimized for search. Each index has a schema that defines its fields. Fields have a name, a data type (like Edm.String for text, Edm.Int32 for integers, Edm.DateTimeOffset for dates, or Collection of Edm.String for arrays), and attributes that control how the field behaves.

The field attributes are critical for the exam. Searchable means the field is included in full-text search queries. Filterable means you can use $filter expressions on it. Sortable means you can use $orderby with it. Facetable means you can use it for faceted navigation (like showing a count of results per category). Retrievable means the field is included in search results. Key means the field uniquely identifies each document. Every index must have exactly one key field.

Here's a practical example. In a product catalog index, you might have a productId field that's the key. A productName field that's searchable, retrievable, and sortable. A description field that's searchable and retrievable. A price field that's filterable, sortable, and facetable. And a category field that's filterable, facetable, and retrievable.

An indexer is the automated data pipeline that pulls data from a source, transforms it, and pushes it into the index. Data sources can include Azure Blob Storage, Azure SQL Database, Azure Cosmos DB, and Azure Table Storage. Indexers can run on a schedule (like every hour) or on demand. They track which documents have changed and only reprocess what's new or modified — this is called incremental indexing.

Indexers also support field mappings, which let you rename or transform fields between the source and the index. For example, if your blob storage has a metadata field called "upload_date" but your index field is called "dateCreated," you use a field mapping to bridge them.

A skillset is a collection of AI enrichment steps that transform your data during indexing. This is where the "AI" in AI Search comes in. As documents flow through the indexer, the skillset applies AI operations to extract additional information.

## Built-In versus Custom Skills

Skillsets contain skills, and there are two categories.

Built-in skills are provided by Microsoft and cover common AI operations. They include entity recognition (extracting named entities from text), key phrase extraction, language detection, sentiment analysis, OCR (extracting text from images), image analysis (generating tags and descriptions for images), text translation, text merge (combining OCR output with original text), text split (chunking text for processing), and PII detection. Each built-in skill maps to an Azure AI service that runs behind the scenes.

Custom skills let you add your own processing logic. The most common approach is a Web API skill that calls an Azure Function you've written. Your function receives the document content, performs whatever processing you need, and returns the enriched data. This is incredibly powerful — you can add domain-specific entity extraction, call external APIs, run machine learning models, or perform any custom transformation.

The interface for custom skills is standardized. Your Azure Function receives a JSON payload with records containing the input data, and returns a JSON payload with records containing the output data. The input and output field names are defined in the skillset configuration.

The exam loves to test custom skills. They might describe a scenario where the built-in skills aren't sufficient and ask how to add custom logic. The answer is almost always a custom Web API skill backed by an Azure Function.

## Knowledge Store Projections

A knowledge store is an optional output of the AI enrichment pipeline that persists enriched data to Azure Storage for downstream analytics. While the index is optimized for search queries, a knowledge store lets you analyze the enriched data using tools like Power BI, Jupyter notebooks, or any other analytics tool.

Knowledge store projections define how enriched data is stored. There are three types.

Table projections store data in Azure Table Storage as rows and columns. This is ideal for structured data that you want to query with tools like Power BI. Each entity type might be stored in a separate table.

Object projections store data as JSON blobs in Azure Blob Storage. This preserves the full hierarchical structure of the enriched documents, which is useful for complex document structures.

File projections store normalized images and other binary data extracted during enrichment as files in Blob Storage.

You can use multiple projection types simultaneously. For example, you might store entity data in tables for Power BI analysis, full enriched documents as JSON blobs for programmatic access, and extracted images as files.

The exam tests knowledge store concepts and the differences between projection types. Know when to use tables (structured analysis), objects (hierarchical data), and files (binary/image data).

## Query Syntax

Querying Azure AI Search is a rich topic with several important concepts. Let me walk through the query capabilities you need to know.

The basic search parameter takes your search text. By default, it uses simple query syntax where terms are matched individually and combined with OR logic. The searchMode parameter controls this: "any" means any term can match (OR), while "all" means all terms must match (AND).

The $filter parameter uses OData filter expressions to narrow results. You can use equality (eq), comparison (gt, ge, lt, le, ne), logical operators (and, or, not), and special functions. For collections, you use any() and all() to test elements. For example, "$filter=tags/any(t: t eq 'azure')" finds documents where the tags collection contains "azure." The search.ismatch function lets you combine full-text search with filtering.

$select specifies which fields to include in the results, reducing the payload size.

$orderby controls the sort order. You can sort by one or more fields, each ascending or descending. For example, "$orderby=rating desc,title asc" sorts by rating descending, then by title ascending for ties.

$top and $skip implement pagination. $top limits the number of results returned, and $skip skips a number of results for getting subsequent pages.

$count returns the total number of matching results, which is useful for pagination UI.

For advanced full-text search, you set queryType to "full" to enable Lucene query syntax. This gives you phrase search (using quotes), wildcards (asterisk for multiple characters, question mark for single character), fuzzy search (tilde followed by edit distance), proximity search (phrase with tilde and word count), term boosting (caret with boost factor), field-scoped search (fieldname colon term), and regular expressions (forward slashes around the pattern).

The exam loves to test query syntax. They might show you a query and ask what it returns, or describe desired search behavior and ask you to write the query. Memorize the OData filter syntax and the Lucene query operators.

## Semantic Search and Vector Search

These are the two advanced search capabilities that take Azure AI Search beyond simple keyword matching.

Semantic search uses AI to understand the meaning of queries and documents, rather than just matching keywords. When you set queryType to "semantic" and specify a semanticConfiguration, the search service re-ranks results using a deep learning model that understands the semantic relationship between the query and the documents. It can also generate extractive captions (highlighting the most relevant passages) and extractive answers (pulling out the specific answer to a question).

To use semantic search, you first create a semantic configuration on your index that identifies which fields to use for title, content, and keywords. Then you include the appropriate parameters in your query.

Vector search uses mathematical similarity between vector embeddings to find relevant results. You generate embeddings for your documents during indexing and embeddings for queries at search time, then find documents whose vectors are closest to the query vector in embedding space.

To use vector search, your index needs vector fields — fields with a vector profile that defines the embedding dimensions and similarity algorithm. You provide the query vector in a vectorQueries array in your search request, specifying the fields to search and k (the number of nearest neighbors to return).

Hybrid search combines keyword search and vector search in a single query. This often produces the best results because it catches both exact keyword matches and semantically similar content. You simply include both a search text and vectorQueries in the same request.

The exam tests your understanding of when to use each approach. Keyword search for exact term matching. Semantic search for understanding query intent. Vector search for finding semantically similar content. Hybrid search for the best of all worlds.

## Document Intelligence: Prebuilt versus Custom Models

Document Intelligence, formerly Form Recognizer, extracts structured data from documents. It offers three main approaches.

Prebuilt models are ready-to-use models trained on specific document types. The available prebuilt models include prebuilt-invoice for extracting data from invoices (vendor name, total amount, line items), prebuilt-receipt for receipts (merchant name, transaction date, total, items), prebuilt-idDocument for identity documents (name, date of birth, document number), prebuilt-tax.us.w2 for W-2 tax forms, prebuilt-healthInsuranceCard for health insurance cards, prebuilt-businessCard for business cards, prebuilt-layout for extracting the general layout structure (tables, paragraphs, selection marks) from any document, and prebuilt-read for extracting raw text with its location.

Custom models are trained on your own labeled documents for domain-specific extraction. There are two types of custom models. Template models work best for fixed-layout documents where fields are always in the same position — like a specific company's invoice template. They need a minimum of 5 labeled training documents. Neural models work with variable-layout documents where the structure can differ between instances. They're more flexible but require more training data.

The analysis workflow follows an asynchronous pattern, especially via REST. You send a POST request with the document to the analyze endpoint. The service returns a 202 response with an Operation-Location header containing a URL. You then poll that URL with GET requests until the status is "succeeded." The results include the extracted fields, their values, confidence scores, and bounding boxes showing where each field was found in the document.

Using the SDK, this is simpler. You call "begin_analyze_document" with the model ID and document, and get back a poller that you wait on. The result contains the same information as the REST response.

The file limits for Document Intelligence are explicitly tested. Free tier (F0): 4 megabyte max file size, 2 pages max per invocation. Standard tier (S0): 500 megabyte max file size, 2,000 pages max per invocation. Minimum image size: 50 by 50 pixels. Supported formats include PDF, JPEG, PNG, BMP, TIFF, HEIF, DOCX, XLSX, and PPTX.

## Composed Models

Composed models are a powerful feature of Document Intelligence that combine multiple custom models into one. Here's how they work and why they matter.

Imagine you have three different invoice formats from three different vendors. You train a separate custom model for each format. Without composed models, your application would need logic to determine which vendor's invoice it's processing and route it to the correct model. With a composed model, you combine all three custom models into one. When you analyze a document, the composed model automatically determines which sub-model to use and applies it.

The composed model evaluates the document against all its sub-models and uses the one that best matches. The response includes which sub-model was selected, so you know which format was detected.

Limits to know: Free tier supports up to 5 sub-models per composed model. Standard tier supports up to 200 sub-models. The exam might ask about composed model limits.

## Content Understanding: OCR Pipelines and Classification

Content Understanding is a newer addition to the Azure AI landscape, introduced as part of Microsoft Foundry. It provides capabilities for processing various content types — documents, images, video, and audio — through unified pipelines.

OCR pipelines in Content Understanding extract text from images and scanned documents, similar to the Read API but integrated into the Foundry platform.

Document classification automatically categorizes documents by type. This is useful when you receive a mix of document types and need to route them to the appropriate processing pipeline.

Attribute detection identifies characteristics of documents, such as whether text is handwritten versus printed, or what language the document is in.

Entity extraction identifies and extracts specific entities from documents, similar to NER but applied to document content.

Table extraction identifies and extracts tabular data from documents, preserving the row-column structure.

Image extraction pulls out embedded images from complex documents.

The key difference between Content Understanding and Document Intelligence is the scope and approach. Document Intelligence focuses on extracting specific fields from known document types. Content Understanding takes a broader approach, providing general-purpose content analysis across multiple modalities (documents, images, video, audio) within the Foundry framework.

The exam tests your ability to distinguish between these services and choose the right one for a given scenario. If the task is extracting specific fields from invoices or receipts, that's Document Intelligence. If the task is general content processing and classification across multiple content types, that's Content Understanding.

---

# Exam Strategy Chapter

Now that we've covered all six domains in detail, let's talk about how to actually take and pass this exam. Exam strategy matters just as much as knowledge.

## Format and Timing

You'll face approximately 58 questions in 120 minutes. That works out to about 2 minutes per question, which sounds generous but can get tight, especially with case studies and long scenario questions.

At the very beginning of the exam, you'll be asked to choose Python or C# as your programming language for code-based questions. This choice is permanent — you cannot switch during the exam. Choose the language you're most comfortable reading. You don't need to be an expert coder, but you need to be able to read code snippets and understand what they do.

The question types include multiple choice (single answer and multiple answer), drag-and-drop ordering, hot area (click on the correct area of a diagram or code snippet), and case studies. Case studies present a scenario with multiple related questions. Here's an important tip: once you complete a case study section, you cannot go back to it. Make sure you've answered all questions in a case study before moving on.

## Using Microsoft Learn During the Exam

Yes, you can access Microsoft Learn during the exam. A split-screen view lets you browse documentation while answering questions. However, use this sparingly. Navigating to find a specific piece of information in Microsoft Learn takes time, and you don't have much to spare. Use it for looking up specific API parameters, service limits, or configuration details that you don't remember — not for learning new concepts.

The best strategy is to know the material well enough that you only need Microsoft Learn for confirming specific details. If you find yourself looking up every other question, you're not prepared enough.

## What the Exam Loves to Test

Based on the exam objectives and common feedback, here are the topics that appear most frequently.

Service limits are explicitly tested. Know the file size limits for every service: 4 megabytes for Image Analysis, 6 megabytes for Custom Vision images, 25 megabytes for real-time speech recognition, 1 gigabyte for batch transcription, 4 megabytes for Document Intelligence free tier, 500 megabytes for standard tier, 2 gigabytes for Video Indexer, and 16 megabytes for AI Search push API documents. These numbers come up again and again.

Managed identity is usually the correct answer for authentication questions. When the exam asks "What is the recommended way to authenticate an Azure App Service to an AI service?", the answer is managed identity with DefaultAzureCredential, not API keys.

The three container environment variables — ApiKey, Billing, and Eula — are tested frequently. Know them cold.

SSML elements and attributes are heavily tested. The exam goes into specific details about prosody rates, say-as interpret-as values, and voice styles. Study the SSML section thoroughly.

Chat completions parameters — temperature, top_p, max_tokens, frequency_penalty, and presence_penalty — are tested individually. Know what each one does and its valid range.

Content Safety severity levels (0, 2, 4, 6) and the four categories (Hate, Violence, Sexual, Self-Harm) come up regularly.

OData filter syntax for AI Search queries is tested. Know the difference between eq, gt, ge, lt, le, ne, and the any/all collection operators.

The difference between NER and entity linking is a classic trap question.

Prebuilt versus custom model decisions across services (Vision, Language, Document Intelligence) are scenario-based favorites.

## Key Tips for Test Day

Start with the questions you're confident about. Don't spend too long on any single question — mark it for review and come back. Many questions can be eliminated down to two choices, and a careful re-read often reveals the answer.

Read the question carefully. Microsoft exams are notorious for nuanced wording. "Most cost-effective" is different from "fastest to implement." "Requires the least administrative effort" is different from "provides the most control." Pay attention to these qualifiers.

For "choose two" or "choose three" questions, make sure you select the right number of answers. Some candidates miss points by selecting too few.

For code questions, trace through the code line by line. Don't assume you know what it does — read it carefully. Look for subtle details like which API version is being called or which parameters are set.

If you've built at least one end-to-end solution using these Azure AI services, many of the questions will feel intuitive. Hands-on experience is the best preparation for scenario-based questions.

## Build at Least One End-to-End Solution

If I could give only one piece of study advice, it would be this: build something real. Create an application that uses multiple Azure AI services together. For example, build a document search application that uses Document Intelligence to extract text from PDFs, Azure AI Search to index the content, Azure OpenAI with RAG to answer questions, and Content Safety to moderate outputs.

The act of building forces you to understand how services connect, how authentication flows work, what the API responses look like, and where things can go wrong. It transforms abstract knowledge into practical understanding, which is exactly what the exam tests.

## Top Resources for Final Preparation

The Microsoft Learn free practice assessment is available at the official exam page. Take it multiple times. The questions change each time, and it gives you a good feel for the exam format and difficulty.

The official Microsoft Learn learning paths for AI-102 cover all domains and include hands-on exercises.

The AI-102 study guide, available at aka.ms/ai102-StudyGuide, lists every objective with links to relevant documentation.

Azure AI Services documentation at learn.microsoft.com is your authoritative reference for API details, limits, and configuration.

And of course, hands-on practice in the Azure portal and with the SDKs is irreplaceable.

---

# Summary and Key Takeaways

Let's wrap up with a one-paragraph summary of each domain and the top things to remember.

## Domain Summaries

Domain one, Plan and Manage, is about knowing the Azure AI service landscape, being able to select the right service for each scenario, provisioning resources through the portal, CLI, and Bicep, and securing and monitoring your deployments. The key themes are service selection, multi-service versus single-service resources, container deployment with the three magic environment variables, authentication with managed identity and Key Vault, monitoring with diagnostic settings and Log Analytics, and responsible AI with Content Safety severity levels and prompt shields. This is the largest domain and the foundation for everything else.

Domain two, Generative AI, centers on Microsoft Foundry and Azure OpenAI. You need to understand the hub-and-project organizational model, how to deploy and configure models, the chat completions API with all its parameters, token management, the RAG pattern for grounding models in your data, DALL-E for image generation, prompt engineering techniques, and fine-tuning workflows. The chat completions parameters and the RAG pattern are the most heavily tested topics in this domain.

Domain three, Agentic Solutions, is the smallest domain but represents the future of AI engineering. Agents are autonomous systems that use tools to accomplish complex tasks. You need to understand the Agent Service versus Agent Framework distinction, the three tool types (code interpreter, file search, function calling), multi-agent orchestration patterns, and agent safety considerations. Focus on conceptual understanding rather than deep implementation details.

Domain four, Computer Vision, covers image analysis, OCR, custom vision models, and video analysis. Key topics include the Image Analysis 4.0 visual features, the Read API for text extraction, the classification versus object detection decision, Custom Vision training workflow and evaluation metrics (precision, recall, AP), the code-first approach to building models, Video Indexer capabilities, and the file size limits for each service. The file limits are explicitly tested.

Domain five, NLP, is the deepest domain covering text analytics, translation, speech, SSML, CLU, and question answering. The most critical topics are the text analytics capabilities (sentiment, NER, key phrases, PII, language detection), entity linking versus NER, the Translator service (text, document, custom), speech-to-text and text-to-speech, and especially the SSML deep dive — know every element, attribute, and value. CLU concepts (intents, entities, utterances) and Custom Question Answering (knowledge bases, multi-turn, chit-chat) round out this domain.

Domain six, Knowledge Mining, covers Azure AI Search, Document Intelligence, and Content Understanding. For AI Search, master the index schema concepts (field types and attributes), the indexer pipeline, built-in and custom skills, knowledge store projections, and query syntax including OData filters and Lucene operators. For Document Intelligence, know the prebuilt models, custom models, composed models, the async analysis pattern, and file size limits. For Content Understanding, understand its role as a general-purpose content processing service versus the more specialized Document Intelligence.

## Top Ten Things to Remember

One: Managed identity with DefaultAzureCredential is the recommended authentication method for production Azure applications accessing AI services. When in doubt, choose managed identity.

Two: The three container environment variables are ApiKey, Billing, and Eula (set to "accept"). Every Azure AI container requires all three to start.

Three: Content Safety severity levels are 0 (safe), 2 (low), 4 (medium), and 6 (high), across four categories: Hate, Violence, Sexual, and Self-Harm.

Four: SSML elements to know cold are voice (select voice), prosody (rate, pitch, volume), break (pause), emphasis (stress), say-as (pronunciation control with interpret-as values), and mstts:express-as (speaking styles).

Five: Chat completions parameters — temperature controls randomness (0 to 2), top_p is nucleus sampling (0 to 1, don't combine with temperature), max_tokens limits output length, frequency_penalty reduces repetition (-2 to 2), and presence_penalty encourages topic diversity (-2 to 2).

Six: File size limits are explicitly tested. The critical ones are 4 megabytes for Image Analysis, 4 megabytes or 500 megabytes for Document Intelligence (free versus standard), 6 megabytes for Custom Vision, 25 megabytes for real-time speech REST, 1 gigabyte for batch transcription, and 2 gigabytes for Video Indexer.

Seven: The RAG pattern involves chunking documents, generating embeddings, storing in a search index, generating a query embedding at search time, retrieving relevant chunks, and including them in the language model prompt. Know this flow end to end.

Eight: Entity linking connects entities to Wikipedia articles for disambiguation. Named entity recognition categorizes entities by type. These are different capabilities and the exam tests the distinction.

Nine: Azure AI Search query syntax includes $filter for OData expressions, $select for field selection, $orderby for sorting, $top and $skip for pagination, queryType "full" for Lucene syntax (wildcards, fuzzy, proximity, boosting), and queryType "semantic" for AI-ranked results.

Ten: Build at least one end-to-end solution before taking the exam. Hands-on experience transforms memorized facts into practical understanding, and the exam is heavily scenario-based.

That's it. You've now heard a comprehensive walkthrough of every major topic on the AI-102 exam. Go build something, take the practice assessment, review the areas where you're weakest, and then go pass that exam. Good luck.

---

*This audio study guide is based on the AI-102 skills measured as of December 23, 2025, with Microsoft Foundry branding. The exam retires June 30, 2026. Always check the official Microsoft exam page for the most current objectives.*
