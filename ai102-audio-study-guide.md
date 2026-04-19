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

Before we dive into the domains, let me share some important context about how this exam relates to the broader Microsoft certification ecosystem. The AI-102 is one of several role-based certifications for AI on Azure. The AI-900 is the foundational certification — it covers the basics at a conceptual level and doesn't require coding skills. The AI-102 is the associate-level certification we're preparing for — it's technical, hands-on, and requires understanding both concepts and implementation. There's also the AI-050 which focuses specifically on developing generative AI solutions with Azure OpenAI.

The AI-102 assumes you have some foundational knowledge. You should be comfortable with Python or C# at a basic level — you'll need to read code, not write it from scratch. You should understand basic Azure concepts like resource groups, subscriptions, and the Azure portal. You should know what APIs are, how HTTP requests work, and what JSON looks like. If you have the AZ-900 (Azure Fundamentals) certification, you have the right foundation.

One more thing before we start with the domains. The exam uses scenario-based questions extensively. Rather than asking "What is managed identity?", it will present a scenario like "A company is deploying an Azure Web App that needs to access Azure OpenAI. The security team requires that no secrets be stored in the application. Which authentication method should you recommend?" Understanding why managed identity is the right answer for this scenario is more important than memorizing a definition.

The exam also tests what I call "decision architecture" — your ability to choose between similar options. It's not enough to know what each service does; you need to know which one is the BEST choice for a specific situation. Throughout this guide, I'll highlight these decision points and give you the thinking framework to navigate them.

Alright, let's start with domain one.

---

# Chapter 1: Plan and Manage Azure AI Solutions (20 to 25 percent)

This is the largest domain on the exam, and for good reason. Before you can build anything with Azure AI, you need to understand the landscape of services available, how to provision them, how to secure them, and how to monitor them. Think of this chapter as the foundation that everything else is built on.

Everything in domains two through six relies on the concepts you'll learn here. How to create AI resources, how to authenticate to them, how to monitor them, how to secure them, and how to implement responsible AI practices. If you master domain one, the other domains become much easier because you understand the underlying patterns.

The exam tests this domain heavily because it's where Azure AI engineers spend a significant portion of their time. Building AI solutions isn't just about calling APIs — it's about designing architectures, managing resources, implementing security, controlling costs, and ensuring responsible use. Let's start with the landscape.

## The Azure AI Service Landscape

Let's start by getting a bird's-eye view of what Azure offers in the AI space. Microsoft has built a broad portfolio of AI services, each designed for specific categories of tasks. Understanding which service to use for which scenario is one of the most heavily tested topics on the exam. They love giving you a scenario and asking you to pick the right service.

In fact, service selection questions might appear 5 to 10 times across the exam in various forms. Sometimes the question is direct: "Which Azure AI service should you use to..." Other times it's embedded in a larger scenario: "A company needs to build a solution that..." and one of the answer choices is about which service or API endpoint to use. Either way, you need an instinctive mapping between business requirements and Azure AI services.

Let me walk you through each major service family.

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

Let me reinforce this mental model with a memorization technique. Think of a complete AI application lifecycle from start to finish. A customer speaks (Speech) in a foreign language (Translator), asking about a product they saw in an image (Vision). Their text is analyzed for sentiment (Language), and the system searches the product catalog (AI Search) and extracts the product details from a PDF spec sheet (Document Intelligence). It generates a personalized response (OpenAI), checks the response for harmful content (Content Safety), and speaks the response back to the customer (Speech again). If the request was captured on video, it's analyzed for additional context (Video Indexer). And all of this is orchestrated through Microsoft Foundry.

Each step in this lifecycle maps to a specific Azure AI service. When the exam gives you a scenario, think about where in this lifecycle the requirement falls, and you'll quickly narrow down the right service.

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

Let me also talk about region considerations, because this comes up on the exam. Not every Azure region supports every model. GPT-4o might be available in East US, West US, and West Europe, but not in every region. When you're planning your deployment, you need to check regional availability for your chosen models. The exam might describe a scenario where a specific model is needed, and ask which region to deploy in — the answer requires knowing or checking regional availability.

Another provisioning concept: quota management. Each Azure subscription has quota limits for Azure OpenAI deployments, measured in tokens per minute (TPM). If you try to deploy more capacity than your quota allows, the deployment fails. You can request quota increases through the Azure portal. The exam might present a scenario where a deployment fails due to insufficient quota and ask what to do.

For CI/CD integration with AI resources, the exam expects you to understand the pattern of deploying both infrastructure and AI assets programmatically. Infrastructure includes the Azure resources themselves (OpenAI resources, Search services, Language resources). AI assets include model deployments, search indexes and indexers, CLU projects, and knowledge bases. A complete CI/CD pipeline deploys infrastructure first (using Bicep or Terraform), then deploys AI assets on top (using SDK/REST calls or specialized tools). The exam might ask about the order of operations or which tools to use for each step.

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

You can also configure firewall rules on your AI service to restrict access to specific IP addresses or virtual networks. When you enable the firewall, by default all traffic is blocked except from the allowed list. You can add IP ranges, virtual network rules, and exceptions for trusted Microsoft services.

The difference between private endpoints and service endpoints is important and sometimes tested. Service endpoints extend your virtual network identity to the Azure service over the Azure backbone network. The traffic goes through the public endpoint of the service, but the service can verify that the traffic is coming from your virtual network. Private endpoints, on the other hand, give the service a private IP address within your virtual network — traffic never hits the public endpoint at all. When should you use which? Service endpoints are simpler and cheaper, suitable when you just need to restrict access to your virtual network. Private endpoints are more secure, required when policies prohibit any use of public endpoints.

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

Here's a practical monitoring scenario that the exam might test. A company deploys an Azure OpenAI chatbot and wants to monitor three things: response quality (are users satisfied?), operational health (are requests succeeding?), and cost (how many tokens are being consumed?). The solution combines several monitoring components.

For response quality, you implement feedback collection using Application Insights custom events. When users rate responses with thumbs up or thumbs down, you log this as a custom event with properties for the conversation ID, the feedback score, and the model deployment used. You can then query Application Insights to calculate satisfaction rates per deployment, identify conversations with negative feedback for review, and track satisfaction trends over time.

For operational health, you enable diagnostic settings on the Azure OpenAI resource to route to Log Analytics. You monitor metrics like total API calls, error rates (4xx and 5xx responses), and average latency. You create alerts for error rate spikes (above 5%) and latency increases (above 3 seconds). You might also monitor rate limiting events — when requests are throttled because they exceed the tokens-per-minute quota.

For cost monitoring, you track token consumption through the diagnostic logs. Each request logs the prompt tokens and completion tokens consumed. You build KQL queries to calculate daily and weekly token costs, identify which deployment or which user is consuming the most tokens, and project future costs based on current trends. You set budget alerts to notify you when spending approaches your allocated budget.

This end-to-end monitoring scenario touches on diagnostic settings, Log Analytics, Application Insights, KQL queries, alerts, and cost management — all topics that could appear on the exam.

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

The responsible AI governance framework is the overarching structure that ties all these capabilities together. It includes defining acceptable use policies for your AI solutions, implementing technical controls (content filters, prompt shields, blocklists), establishing human oversight processes (content review workflows, escalation procedures), conducting regular audits of AI system behavior, documenting your AI systems and their intended uses, and providing transparency to users about when they're interacting with AI.

The exam expects you to understand responsible AI not just as a set of API features, but as a comprehensive approach to building AI responsibly. Questions might ask about the appropriate governance measures for a specific scenario — like deploying a customer-facing chatbot — and the answer should address both technical controls (content filters, prompt shields) and organizational processes (human review, monitoring, policies).

Microsoft's Responsible AI principles that underpin all of these capabilities are: fairness (AI systems should treat all people fairly), reliability and safety (AI systems should perform reliably and safely), privacy and security (AI systems should be secure and respect privacy), inclusiveness (AI systems should empower everyone and engage people), transparency (AI systems should be understandable), and accountability (people should be accountable for AI systems).

The exam doesn't test these principles as abstract concepts — it tests them through concrete scenarios. "A company's AI chatbot has been generating responses that stereotype certain demographic groups. Which Content Safety feature should they configure?" The answer involves both content filters (to catch harmful content) and potentially custom blocklists (to block specific stereotyping language). This connects the abstract principle of fairness to concrete technical implementation.

---

# Chapter 2: Generative AI Solutions (15 to 20 percent)

Generative AI is the hot topic of our era, and Microsoft has built a comprehensive platform for building generative AI solutions in Azure. This domain covers Microsoft Foundry, Azure OpenAI, prompt engineering, fine-tuning, and the RAG pattern. Let's dive in.

Generative AI has transformed the AI landscape in just the past two years, and Microsoft has invested heavily in making these capabilities accessible through Azure. This domain represents 15 to 20 percent of the exam, which reflects how central generative AI has become to the Azure AI platform.

The key shift to understand is this: traditional AI services (like sentiment analysis, image classification, and entity extraction) perform specific, predefined tasks. Generative AI models create new content — they generate text, write code, create images, summarize documents, and engage in open-ended conversations. The architecture and design patterns for generative AI solutions are fundamentally different from traditional AI solutions, and the exam tests these new patterns extensively.

Let's start with the organizational framework for building generative AI solutions on Azure.

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

Let me share a few more DALL-E details that might appear on the exam. The API endpoint for DALL-E image generation is different from the chat completions endpoint. Instead of the /chat/completions path, you use /images/generations. The request body includes the prompt, size, quality, style, and the number of images to generate (n parameter, which is 1 by default and can be at most 1 for DALL-E 3).

The response includes a revised_prompt field — this is because DALL-E 3 automatically enhances your prompt for better results. The actual prompt sent to the model might be different from what you submitted. The response also includes the generated image, either as a URL (valid for a limited time) or as base64-encoded data, depending on the response_format parameter.

Content filtering for DALL-E works both on the input (the prompt is checked for harmful content) and the output (the generated image is checked for harmful content). If either check fails, the request is rejected with a content filter error.

One important distinction: DALL-E generates images from text descriptions. It does NOT edit existing images or create variations (unlike the standalone OpenAI API). In Azure OpenAI, DALL-E is text-to-image only. If the exam asks about modifying an existing image, DALL-E is not the correct answer.

The image sizes available for DALL-E 3 are: 1024 by 1024 pixels (square), 1792 by 1024 pixels (landscape, about 16:9 aspect ratio), and 1024 by 1792 pixels (portrait). The exam might ask about supported sizes — know that these are the only three options for DALL-E 3.

## Prompt Engineering Techniques

Prompt engineering is the art of crafting inputs that get the best outputs from language models. The exam tests several specific techniques.

Zero-shot prompting is when you ask the model to perform a task without giving any examples. "Classify the following email as spam or not spam: [email text]." The model relies on its general training to understand the task.

Few-shot prompting is when you include examples in the prompt. "Classify the following emails as spam or not spam. Example 1: 'You won a prize!' — Spam. Example 2: 'Meeting at 3pm tomorrow.' — Not Spam. Now classify: [email text]." Few-shot examples help the model understand the exact format and criteria you want.

Chain-of-thought prompting encourages the model to show its reasoning step by step before arriving at an answer. "Solve this math problem. Think step by step." This often produces more accurate results for complex reasoning tasks because the model is essentially "thinking out loud."

System prompts are the system messages we discussed earlier. Effective system prompts clearly define the model's persona, behavior boundaries, output format, and any specific rules. A well-crafted system prompt is the single most impactful prompt engineering technique.

Prompt templates use parameterized placeholders that get filled in at runtime. Instead of hardcoding a prompt, you define a template like "Summarize the following document in {num_sentences} sentences: {document_text}" and fill in the parameters dynamically. Microsoft Foundry's prompt flow feature supports prompt templates natively.

The exam might describe a scenario where the model's output isn't meeting expectations and ask which prompt engineering technique would help. If the model doesn't understand the task format, few-shot examples help. If it's making reasoning errors, chain-of-thought helps. If it's not following behavioral guidelines, a better system prompt helps.

Let me share more detailed prompt engineering strategies because they're tested beyond just naming the techniques.

For system prompts, there are several best practices. Be specific about the persona: "You are a senior tax accountant with expertise in corporate tax law" is better than "You are helpful." Define output format: "Always respond in JSON with the fields 'answer', 'confidence', and 'sources'" gives the model clear structure to follow. Set boundaries: "Only answer questions about our products. If asked about competitors, say 'I can only help with our products.'" Include examples within the system prompt for common interactions.

For few-shot prompting, the quality and diversity of your examples matter more than the quantity. Use 3 to 5 well-chosen examples that cover different edge cases. Include both positive examples (correct classifications) and negative examples (things that should NOT be classified a certain way). Format your examples consistently so the model learns the pattern.

For chain-of-thought, the magic phrase "Let's think step by step" has been shown to improve reasoning. But you can be more specific: "Before answering, reason through these steps: 1. Identify the relevant information. 2. Consider what could go wrong. 3. Form your conclusion." This structured chain-of-thought gives even better results.

For output format control, beyond the response_format parameter for JSON, you can use prompt engineering to get structured output. "Respond in EXACTLY this format: CATEGORY: [category name] CONFIDENCE: [high/medium/low] EXPLANATION: [one sentence]" gives you consistent, parseable output.

Temperature and parameter tuning is also part of prompt engineering. For a customer service bot, you might use temperature 0.3 (consistent, reliable answers), max_tokens 500 (concise responses), and presence_penalty 0 (don't diverge from the topic). For a creative writing assistant, temperature 1.2 (creative variety), max_tokens 2000 (longer responses), and presence_penalty 0.6 (explore new topics).

## Fine-Tuning: When and How

Fine-tuning is the process of further training a pre-existing model on your own data to customize its behavior. Let me explain when you'd use fine-tuning versus other approaches, and how it works.

When should you fine-tune? Fine-tuning is appropriate when you need the model to consistently produce outputs in a very specific style or format, when few-shot examples aren't enough to guide the behavior, when you want to improve performance on domain-specific tasks, or when you want to reduce prompt size (since the model "learns" the patterns, you don't need as many examples in each prompt).

When should you NOT fine-tune? If you need the model to have access to specific factual data, use RAG instead. Fine-tuning is about style and behavior, not about teaching the model new facts. If few-shot prompting gets good enough results, stick with that — it's much simpler and cheaper than fine-tuning.

The fine-tuning process in Azure OpenAI works as follows. You prepare training data in JSONL format — that's JSON Lines, where each line is a separate JSON object. Each line represents a training example with the same message format used by the Chat Completions API: a system message, a user message, and an assistant message showing the desired response.

Here's what a training example looks like conceptually: a JSON object with a "messages" array containing three objects — one with role "system" and your system prompt, one with role "user" and the input, and one with role "assistant" and the ideal output.

You need at least 10 training examples, but Microsoft recommends 50 to 100 for good results. More examples generally improve quality. You upload your training file, create a fine-tuning job, wait for training to complete, and then deploy the fine-tuned model to an endpoint.

The exam might ask about the training data format (JSONL), the minimum number of examples needed, or when to choose fine-tuning versus RAG.

Let me give you a clear decision framework for fine-tuning versus RAG versus prompt engineering, since the exam tests this decision.

Start with prompt engineering. Can you get acceptable results by crafting better prompts, using few-shot examples, or adjusting parameters? If yes, you're done. This is the simplest and cheapest approach.

If prompt engineering isn't enough, consider the problem type. Does the model need access to specific, current data that it wasn't trained on? Use RAG. The data might change frequently, and you don't want to retrain the model every time. RAG is also better when you need citations and source attribution.

Does the model need to consistently behave in a specific way, use a particular tone, follow a specific format, or demonstrate domain expertise in how it communicates? Use fine-tuning. Fine-tuning is about teaching the model patterns of behavior, not facts.

Sometimes you need both. You might fine-tune a model to have a specific communication style for your company, AND use RAG to ground its responses in your current product documentation. These approaches are complementary, not mutually exclusive.

The cost comparison is also relevant. Prompt engineering costs nothing beyond normal API usage. RAG adds the cost of embedding generation, search infrastructure, and slightly longer prompts (because retrieved context is included). Fine-tuning has upfront training costs and you pay for a dedicated model deployment.

One more fine-tuning detail: the validation data. In addition to your training data, you can provide a separate validation dataset. The training process uses this to evaluate the model's performance at each training step, helping you detect overfitting. Overfitting is when the model memorizes the training data too closely and doesn't generalize well to new inputs. The validation loss metric should decrease during training — if it starts increasing while training loss continues decreasing, the model is overfitting.

The fine-tuning process creates a new model deployment that's separate from the base model. You reference your fine-tuned model by its deployment name in API calls, just like any other deployment. The fine-tuned model has the same API interface as the base model — the only difference is that it's been customized with your training data.

## Model Evaluation Metrics

Evaluating the quality of generative AI outputs is crucial, and the exam tests several evaluation metrics.

Groundedness measures whether the model's output is factually grounded in the provided context or source material. This is especially important for RAG scenarios. A groundedness score of 1 means everything in the output is supported by the context.

Relevance measures how relevant the output is to the user's question. A response might be factually correct but not actually answer what was asked.

Coherence measures how logically connected and well-structured the output is. Does it flow naturally? Are the ideas organized sensibly?

Fluency measures the linguistic quality — grammar, word choice, readability. Is it well-written?

Similarity measures how close the model's output is to a reference answer, if one is available.

These metrics can be evaluated automatically using evaluation flows in Microsoft Foundry, or manually through human evaluation. The Foundry SDK provides built-in evaluators for each of these metrics.

The exam might describe a scenario where an AI solution is generating outputs that aren't sticking to the provided data, and ask which metric is most relevant. That would be groundedness.

Let me connect these evaluation metrics to practical scenarios you'll see on the exam.

Scenario: "A company's RAG-based chatbot sometimes includes information in its responses that doesn't appear in the retrieved documents." Which metric is failing? Groundedness — the model is hallucinating information not present in the context.

Scenario: "A customer service bot gives accurate answers about products but often includes irrelevant details about company history when asked about pricing." Which metric is failing? Relevance — the responses are factually correct but not relevant to the specific question asked.

Scenario: "An AI summarization tool produces summaries that are accurate and relevant, but the sentences are disjointed and hard to follow." Which metric is failing? Coherence — the output lacks logical flow and organization.

Scenario: "A translation assistant produces translations that are accurate in meaning but read awkwardly with grammatical errors." Which metric is failing? Fluency — the linguistic quality needs improvement.

Understanding these distinctions helps you both answer exam questions about evaluation and design evaluation strategies for real-world AI solutions.

Let me also discuss model reflection, which is mentioned in the exam objectives and is a newer concept. Model reflection involves having the AI evaluate its own output before presenting it to the user. The pattern typically involves generating a response, then sending that response back to the model (or a separate evaluation model) with instructions to check for accuracy, completeness, and adherence to guidelines. If the reflection step identifies issues, the model regenerates the response.

In Microsoft Foundry, you can implement model reflection using prompt flow. You create a flow where the first step generates a response, the second step evaluates it using an evaluation prompt, and if the evaluation fails, the flow loops back to regenerate. This is particularly useful for high-stakes applications where accuracy is critical.

Tracing is another operational concept the exam covers. Tracing in Microsoft Foundry provides visibility into each step of your AI application's processing — from the initial request through any tool calls, RAG retrievals, and model invocations, to the final response. It's like application performance monitoring but specifically designed for AI workflows.

You enable tracing using the Foundry SDK and Application Insights. Each trace shows the sequence of operations, their inputs and outputs, latency at each step, token counts, and any errors. This is invaluable for debugging, optimization, and understanding your AI application's behavior in production.

Feedback collection is the complement to tracing — while tracing captures technical metrics, feedback captures user satisfaction. You can implement thumbs up/thumbs down buttons, rating scales, or free-text feedback in your application. This feedback is sent to Application Insights and can be analyzed alongside traces to correlate technical behavior with user experience. For example, if responses grounded in fewer than 3 retrieved documents consistently get negative feedback, you might increase the retrieval count.

---

# Chapter 3: Agentic Solutions (5 to 10 percent)

This is the smallest domain on the exam, but it represents the cutting edge of AI engineering. Agents are AI systems that can autonomously perform tasks using tools, make decisions, and chain together complex workflows. Let's explore what you need to know.

Although this domain only represents 5 to 10 percent of the exam, don't skip it. Even a small domain can make the difference between passing and failing, and agents are likely to become a larger part of future certification updates as the technology matures.

The concept of AI agents represents a fundamental shift in how we think about AI applications. Traditional AI applications are reactive — you send a request, the AI processes it, and you get a response. Agents are proactive — they can plan sequences of actions, use tools to interact with the world, maintain context over extended conversations, and work toward goals with autonomy.

Microsoft has invested heavily in agent capabilities through both the Foundry Agent Service (managed, cloud-hosted agents) and the Agent Framework built on Semantic Kernel (code-first, flexible agents). Understanding when to use each and how they work is what the exam tests.

## What Agents Are and When to Use Them

An AI agent is fundamentally different from a simple chatbot or API call. While a chatbot responds to individual queries in a stateless way, an agent can plan multi-step tasks, use tools to take actions, maintain memory across interactions, and work toward complex goals with minimal human intervention.

Think of it this way: if you ask a chatbot "What's the weather in Seattle?", it gives you an answer and forgets about you. If you ask an agent "Plan a trip to Seattle next week, checking the weather forecast, finding hotels under $200, and booking one that's close to the convention center," the agent would break that into subtasks, call a weather API, search hotel databases, compare options, and potentially make a booking — all autonomously.

You should use agents when the task requires multiple steps and tool interactions, when the workflow benefits from autonomous decision-making, when you need the AI to interact with external systems (databases, APIs, file systems), and when the task involves processing or analyzing documents.

You should NOT use agents for simple question-answering tasks, for straightforward API calls that don't require planning, or when you need fully deterministic behavior with no room for AI decision-making.

## Agent Service versus Agent Framework

Microsoft provides two main approaches for building agents, and understanding the difference is important for the exam.

Microsoft Foundry Agent Service, also called Azure AI Agent Service, is the managed, cloud-hosted approach. You create an agent through the Foundry portal or SDK, configure it with tools (like code interpreter, file search, and custom functions), and deploy it as a managed service. The infrastructure is handled for you — you don't need to worry about hosting, scaling, or orchestration.

The Agent Service provides a straightforward API: you create an agent, create a thread (which represents a conversation), add messages to the thread, and run the agent. The agent autonomously decides which tools to use based on the user's request.

Let me walk through this API flow in more detail because the exam tests the concepts.

Step one: Create an agent. You define the agent's instructions (similar to a system message), the model to use (like GPT-4o), and the tools it has access to. The instructions tell the agent its purpose and behavior — "You are a helpful data analyst. Use the code interpreter to analyze data and create visualizations."

Step two: Create a thread. A thread is the conversation container. It persists the conversation history and any files associated with the conversation.

Step three: Add a message. You add the user's request as a message in the thread. For example, "Analyze this sales data and tell me which region performed best."

Step four: Create a run. This triggers the agent to process the conversation. The agent reads the messages, decides which tools to use, executes them, and generates a response. The run is asynchronous — you create it and then poll for completion.

Step five: Retrieve the result. Once the run completes, you retrieve the agent's response messages from the thread.

During a run, the agent might make multiple tool calls. For example, it might first use file search to find relevant data, then use code interpreter to analyze the data and create a chart, then compose a text response summarizing the findings. The agent orchestrates these steps autonomously.

Microsoft Agent Framework, built on top of Semantic Kernel, is for more complex agent implementations. It's a code-first approach where you build agents using the Semantic Kernel SDK. This gives you more control over the agent's behavior, planning strategies, and orchestration patterns.

Semantic Kernel is an open-source SDK that lets you orchestrate AI capabilities (called "plugins") with conventional code. In the context of agents, Semantic Kernel provides planning capabilities (where the AI decides which steps to take), plugin management (defining available tools and functions), and memory management (maintaining context across interactions).

The Agent Framework is appropriate for complex multi-agent scenarios, custom orchestration logic, or when you need fine-grained control over how the agent makes decisions.

The key difference: Agent Service is managed and simpler (great for straightforward agent tasks), while Agent Framework is more flexible and powerful (better for complex, custom scenarios). The exam might describe a scenario and ask which approach is more appropriate. If the scenario describes a simple agent with standard tools (code interpreter, file search), Agent Service is the answer. If it describes complex multi-agent workflows with custom planning logic, Agent Framework is the answer.

## Tools: Code Interpreter, File Search, and Function Calling

Agents are only as useful as the tools they can access. There are three primary tool types you need to know.

Code Interpreter gives the agent the ability to write and execute Python code in a sandboxed environment. This is powerful for data analysis, mathematical calculations, creating visualizations, and file format conversions. If a user uploads a CSV file and asks "What's the average sales by region?", the agent can write Python code to load the CSV, calculate the averages, and even generate a chart.

File Search allows the agent to search through uploaded documents to find relevant information. When you attach files to an agent or thread, the File Search tool automatically chunks the documents, creates embeddings, and performs retrieval when the agent needs information from those files. This is essentially RAG built into the agent framework.

Function Calling lets you define custom functions that the agent can invoke. You describe the function's purpose and parameters in a JSON schema, and when the agent determines it needs to use that function, it generates the appropriate parameters. Your code then executes the function and returns the result to the agent. This is how agents interact with your external systems — databases, APIs, business logic, and anything else you can wrap in a function.

The exam might present a scenario and ask which tool the agent should use. If it involves calculations or data processing, code interpreter. If it involves finding information in documents, file search. If it involves calling an external API or performing a business action, function calling.

Let me give you more details on function calling because it's the most complex and exam-relevant tool type. When you define a function for an agent, you provide a JSON schema that describes the function's name, description, and parameters. The description is crucial because the agent uses it to decide when to call the function. Each parameter has a type, description, and whether it's required.

For example, you might define a function called "get_weather" with the description "Get the current weather for a location." It has two parameters: "location" (a required string) and "unit" (an optional string that defaults to "celsius"). When a user asks "What's the weather in Paris?", the agent recognizes this requires the get_weather function, generates the parameters (location: "Paris"), and asks your code to execute the function.

The flow for function calling involves a back-and-forth. The agent generates a "tool_calls" response indicating which functions to call and with what parameters. Your code executes those functions and sends the results back to the agent. The agent then uses those results to generate its final response.

This is particularly powerful for connecting agents to enterprise systems. You might define functions for querying a CRM database, creating support tickets, checking inventory levels, or making reservations. The agent decides which functions to call based on the user's request, and your code handles the actual execution.

## Multi-Agent Orchestration

For complex workflows, you can use multiple agents working together. This is called multi-agent orchestration.

The most common pattern is the planner-executor model. A planner agent breaks down a complex request into subtasks, then delegates each subtask to specialized executor agents. For example, a research request might involve one agent gathering data, another analyzing it, and a third writing a summary.

In multi-agent systems, agents communicate through shared threads or message passing. Each agent has its own specialization, tools, and instructions, but they coordinate to achieve a common goal.

Let me give you a concrete multi-agent example. Consider a customer support system with three specialized agents. The Router Agent receives the initial customer query and determines which specialist to route it to. The Billing Agent handles billing-related queries — it has access to the billing database through function calling and can look up account details, explain charges, and process refund requests. The Technical Agent handles technical support — it has access to a knowledge base through file search and can troubleshoot issues, provide step-by-step guides, and escalate to human support if needed.

When a customer says "I was charged twice for my subscription and now the app won't open," the Router Agent recognizes this involves both billing and technical issues. It routes the billing part to the Billing Agent (which checks the account and processes a refund for the duplicate charge) and the technical part to the Technical Agent (which troubleshoots the app issue). Both agents' responses are combined into a single reply to the customer.

The orchestration pattern determines how agents coordinate. In a sequential pattern, one agent finishes before the next starts. In a parallel pattern, multiple agents work simultaneously. In a hierarchical pattern (like our example), a supervisor agent manages worker agents.

The exam tests this at a conceptual level rather than diving deep into implementation details. Understand the pattern, when to use it (complex tasks that benefit from specialization), and the basic flow of planning, delegation, and coordination.

## Safety and Testing

Agent safety requires special attention because agents can take autonomous actions. You need to ensure that agents can't perform harmful actions, access unauthorized data, or go off the rails in unexpected ways.

Testing strategies for agents include unit testing individual tools and functions, integration testing the agent's end-to-end behavior, adversarial testing with edge cases and malicious inputs, and monitoring agent behavior in production with human-in-the-loop checkpoints for high-risk actions.

Multi-user scenarios add complexity — you need to ensure that one user's agent interactions don't leak data to another user.

The exam covers agent testing and optimization at a high level. Know that you should test agents thoroughly, monitor their behavior, and include safety guardrails.

Let me share a few more details about agent safety that are relevant for the exam.

Guardrails are constraints you place on agent behavior. These include input validation (checking user messages for harmful content before sending to the agent), output validation (checking agent responses before showing to the user), action limits (restricting what actions the agent can perform — for example, an agent might be allowed to query a database but not delete records), and escalation policies (when certain conditions are met, the agent should hand off to a human operator).

Human-in-the-loop is a design pattern where certain high-risk actions require human approval before the agent executes them. For example, an agent that can place orders might require manager approval for orders over a certain value. The agent generates the action, pauses execution, and waits for human approval via a notification or approval workflow.

Testing agents requires a different approach than testing traditional applications because agent behavior is non-deterministic. Best practices include defining test scenarios with expected outcomes (not exact responses), testing edge cases and adversarial inputs, monitoring for drift in agent behavior over time, and A/B testing different agent configurations to compare quality.

Multi-user scenarios add a security dimension. Each user's conversation thread must be isolated — agent A serving user 1 must not have access to the conversation history of user 2. When using file search, each user's files must be scoped appropriately. Function calls must respect the calling user's permissions. The exam might describe a multi-user agent scenario and ask about data isolation requirements.

---

# Chapter 4: Computer Vision Solutions (10 to 15 percent)

Computer vision is one of the more hands-on domains on the exam. You'll need to understand how to analyze images, build custom vision models, and work with video content. Let's walk through each area.

Computer vision is fundamentally about teaching machines to understand visual information. Azure provides a range of vision services from fully prebuilt models that work out of the box to custom models you train on your own data. The exam tests your ability to choose the right approach for each scenario and implement it correctly.

The decision between prebuilt and custom models is a recurring theme in this domain, just as it is in NLP and Document Intelligence. Here's the general rule: if the prebuilt Image Analysis 4.0 model recognizes what you need (common objects, general scenes, standard text), use it. It's faster to implement, requires no training data, and is continuously improved by Microsoft. If you need to recognize domain-specific objects (specific product defects, particular medical conditions, proprietary equipment), train a Custom Vision model.

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

Let me walk through the response structure in more detail because the exam shows you JSON responses and asks you to interpret them.

For tags, each tag has a "name" (the tag text) and a "confidence" score between 0 and 1. Tags are sorted by confidence, highest first. You might see tags like: name "outdoor" with confidence 0.99, name "sky" with confidence 0.98, name "building" with confidence 0.95, name "architecture" with confidence 0.87. The exam might ask which tag the service is most confident about — you look for the highest confidence score.

For captions, the result includes a "text" field (the generated description) and a "confidence" score. Dense captions return an array of captions, each with text, confidence, and a "boundingBox" that defines the region of the image the caption describes. The bounding box is an object with x, y, width, and height values, where x and y are the top-left corner.

For objects, each detected object has a "tags" array (with the object type and confidence), and a "boundingBox" with x, y, width, and height. For example, detecting a car might return tags containing name "car" with confidence 0.92, and a bounding box that defines where the car is in the image. The bounding box coordinates are in pixels relative to the original image dimensions.

For people detection, each person has a "boundingBox" and a "confidence" score. No facial attributes or identity information is provided — just the presence and location of people.

For the read feature (OCR), the result contains a "readResult" with "blocks," which contain "lines," which contain "words." Each word has the "text," a "confidence" score, and a "boundingPolygon" (an array of four points defining the corners of the word's bounding box). Lines also have text, a bounding polygon, and the array of contained words.

The exam might show you a JSON response and ask questions like "What is the most confident object detection?" or "What text was extracted from the image?" or "What are the coordinates of the detected person?" Being able to navigate the response JSON structure is essential.

Here's a critical exam detail about file limits for the Image Analysis API. The maximum file size is 4 megabytes. The maximum image dimension is 20 megapixels. The minimum image dimension is 50 by 50 pixels. Supported formats include JPEG, PNG, GIF, BMP, WEBP, ICO, and TIFF. Only one image can be analyzed per request. These numbers are explicitly tested on the exam, so commit them to memory.

## OCR and Handwriting Extraction

The Read API, also accessible as the "read" feature in Image Analysis 4.0, is Azure's OCR technology for extracting text from images and documents. It handles both printed and handwritten text, which is a key differentiator.

The Read API uses deep learning models to extract text from a wide variety of sources — photos of signs, scanned documents, handwritten notes, and complex layouts with mixed content. It supports 164 languages for printed text and a growing number for handwriting.

When you call the Read API, the response organizes the extracted text hierarchically: pages contain lines, and lines contain words. Each word includes the text, a bounding polygon (the outline around the word in the image), and a confidence score. Lines include the combined text and their own bounding polygon.

The confidence scores are important for applications that need to validate extraction quality. A confidence below a certain threshold might trigger manual review.

For the exam, remember that the Read API is the recommended approach for text extraction. It's available both as a standalone API endpoint and as the "read" feature within Image Analysis 4.0. It handles printed text, handwritten text, and mixed content.

Let me share more details about the Read API that are relevant for the exam. The Read API supports 164 languages for printed text recognition. Handwriting recognition is more limited in language support but includes the major languages like English, Chinese, Japanese, Korean, French, German, Italian, Portuguese, and Spanish.

The API can handle complex document layouts with multi-column text, headers and footers, watermarks, annotations, and mixed printed and handwritten content. It uses deep learning models to handle varying fonts, font sizes, orientations, and image quality.

When using the REST API, the Read operation is asynchronous. You send a POST request with the image, receive a 202 response with an Operation-Location header, then poll the status URL until it completes. This is the same pattern used by Document Intelligence.

One important distinction for the exam: the Read API is for extracting raw text from images and documents. Document Intelligence's prebuilt-read model provides similar raw text extraction but with additional capabilities for document-specific scenarios. Image Analysis 4.0's read feature is the same Read API technology but called through the Image Analysis endpoint. These are three ways to access essentially the same OCR technology, but through different service endpoints.

The exam might present a scenario where you need to extract handwritten notes from a photo. The answer is the Read API (or the read feature of Image Analysis 4.0), not Document Intelligence (which is better for structured forms with labeled fields).

Spatial analysis in Azure AI Vision is also worth mentioning, though it's less heavily tested. Spatial analysis uses computer vision to understand how people interact with physical spaces — detecting their presence, movement patterns, and proximity. It runs on edge devices using the spatial analysis container and can detect events like people entering or exiting a zone, dwelling in an area, or maintaining social distance. This is used in retail analytics, workspace optimization, and safety compliance.

## Custom Vision: Classification versus Object Detection

When the prebuilt Image Analysis models don't meet your needs, you turn to Custom Vision to train your own models. There are two main model types, and understanding when to use each is critical for the exam.

Image classification determines what category an image belongs to. There are two subtypes: multiclass classification, where each image belongs to exactly one category (like "cat," "dog," or "bird"), and multilabel classification, where an image can belong to multiple categories simultaneously (like "outdoor," "winter," and "mountain" all applying to the same image).

Object detection locates specific objects within an image and returns their bounding boxes. Unlike classification, which labels the entire image, object detection identifies and locates individual objects. An image of a kitchen might detect "plate," "cup," "fork," "knife" with bounding boxes around each.

When should you use classification? When you need to categorize entire images — quality inspection (defective vs. non-defective), scene recognition, or product categorization. When should you use object detection? When you need to find and locate specific items within images — counting products on a shelf, identifying components in a manufacturing process, or detecting safety equipment on workers.

Let me give you a decision framework that helps with exam scenarios. Ask yourself: "Do I need to know WHAT an image is about, or WHERE specific things are in the image?" If you just need to know what the image shows (is it a cat or a dog?), that's classification. If you need to know where things are (where is the defect on this circuit board?), that's object detection.

Here's another nuance: multiclass versus multilabel classification. In multiclass, each image gets exactly one label — it's either a cat OR a dog OR a bird, never more than one. In multilabel, each image can have multiple labels — a beach photo might be labeled both "ocean" and "sunset" and "tropical." The exam might describe a scenario and ask which type is appropriate. If items are mutually exclusive categories (product types, quality grades), use multiclass. If items can belong to multiple categories simultaneously (image attributes, scene characteristics), use multilabel.

For object detection, the training requires you to not only label images but also draw bounding boxes around each instance of each object type. A single training image might contain multiple objects of different types — a photo of a table setting might have bounding boxes around a plate, a glass, a fork, and a knife, each labeled with its type. You need at least 15 instances of each object type across your training set.

The training workflow for Custom Vision follows these steps. First, you create a Custom Vision project in the Custom Vision portal or via the SDK, specifying whether it's classification or detection. Second, you upload and label your training images. For classification, you tag each image with its category. For object detection, you draw bounding boxes around objects and label them. Third, you train the model. You need a minimum of 15 images per tag, though Microsoft recommends 50 or more for good results. Fourth, you evaluate the model using the metrics the service provides. Fifth, you publish the model to a prediction endpoint. Sixth, you consume the model from your application using the prediction API.

## Training Workflow and Evaluation Metrics

Let's dig deeper into the evaluation metrics for Custom Vision, because the exam tests these.

Precision measures, of all the predictions the model made for a given class, what percentage were correct. High precision means few false positives. If the model says "this is a cat" 100 times and 95 of those are actually cats, precision is 95 percent.

Recall measures, of all the actual instances of a given class, what percentage did the model correctly identify. High recall means few false negatives. If there are 100 actual cat images and the model correctly identifies 90 of them, recall is 90 percent.

Average Precision, or AP, combines precision and recall into a single score. It's calculated as the area under the precision-recall curve. Higher AP means the model performs well across different confidence thresholds.

Mean Average Precision, or mAP, is the average of AP across all classes. This is the primary metric for object detection models.

The exam might show you evaluation results and ask you to interpret them. If precision is high but recall is low, the model is conservative — when it makes a prediction, it's usually right, but it's missing many actual instances. If recall is high but precision is low, the model is aggressive — it catches most instances but has many false positives.

F1 score is the harmonic mean of precision and recall, providing a single metric that balances both. It's calculated as 2 times precision times recall, divided by precision plus recall. An F1 score of 1.0 means perfect precision and recall. An F1 score of 0.5 is mediocre. The exam might show you F1 scores for different iterations of a model and ask which iteration is best — the one with the highest F1 score.

Mean Average Precision, or mAP, is particularly important for object detection. It averages the AP across all classes, giving you a single number that represents overall detection quality. A mAP of 0.8 or higher is generally considered good for most applications.

Let me give you a practical example to make these metrics concrete. Say you're building a model to detect defective products on a manufacturing line. There are 100 products, 10 of which are actually defective.

If your model identifies 8 products as defective, and 7 of those are truly defective (plus 1 false positive), your precision is 7/8 = 87.5% (of the ones it called defective, 87.5% actually were) and your recall is 7/10 = 70% (of the 10 actual defectives, it found 7). The 3 defective products it missed could end up in customers' hands.

If your model identifies 20 products as defective, and all 10 truly defective products are in that group (plus 10 false positives), your precision is 10/20 = 50% (half the flagged products are actually fine) but your recall is 10/10 = 100% (it caught every single defective product). No defective product escapes, but you're wasting time inspecting 10 perfectly good products.

Which is better depends on the business context. In manufacturing where defective products could be dangerous, high recall is critical — you'd rather waste time on false positives than miss a real defect. In content recommendation where you're classifying products into categories, high precision matters more — you'd rather miss a product than misclassify it.

The exam uses these trade-offs in scenario questions. Understanding the real-world implications of precision versus recall helps you answer them correctly.

For Custom Vision training specifically, there are two training types: Quick Training (faster, good for prototyping) and Advanced Training (takes longer but often produces better results). Advanced training also lets you set a training budget — you specify how many hours to train for. The exam might ask about these options.

## The Code-First Approach

The exam specifically tests your ability to build Custom Vision models entirely through code, without using the portal. This is called the code-first approach, and it's a favorite topic.

Using the Custom Vision SDK, you can programmatically create a project, create tags, upload and tag images, train the model, evaluate results, and publish to a prediction endpoint. The training SDK and prediction SDK are separate packages. In Python, you use azure-cognitiveservices-vision-customvision for training and the same package's prediction module for inference.

The key thing the exam tests is whether you know the sequence of SDK calls. Create project, create tag, upload images with tags, train (which returns an iteration), check training status, publish the iteration to a prediction endpoint, then use the prediction client to classify new images.

Let me walk through the SDK code pattern in more detail. In Python, you'd import the CustomVisionTrainingClient and CustomVisionPredictionClient from the azure.cognitiveservices.vision.customvision packages.

For training, you first create a training client with your training endpoint and training key. Then you call client.create_project with a name and optionally a domain ID (domains include "General," "Food," "Landmarks," "Retail," and more — each domain is optimized for specific content types). Next, you create tags: client.create_tag(project_id, "tag_name") for each category. Then you upload images: client.create_images_from_files with a list of ImageFileCreateEntry objects, each containing the filename, file data, and associated tag IDs. After uploading enough images, you call client.train_project(project_id) which returns an iteration. You poll the iteration status with client.get_iteration until it completes. Finally, you publish the iteration: client.publish_iteration(project_id, iteration_id, publish_name, prediction_resource_id).

For prediction, you create a prediction client with your prediction endpoint and prediction key. Then you call client.classify_image (for classification) or client.detect_image (for object detection), passing the project ID, published name, and the image data. The result contains the predictions with their tag names and probabilities.

The exam might show you this code with a blank and ask you to fill in the missing call, or show you the complete code and ask what it accomplishes. Being comfortable reading this pattern is essential.

For object detection specifically, the training process is similar but you draw bounding boxes around objects in addition to labeling them. Each image can contain multiple objects with different tags. The normalized bounding box coordinates are specified as left, top, width, and height, all as values between 0 and 1 (representing the percentage of the image's dimensions).

The domain selection is worth knowing for the exam. There are "general" domains for broad use cases, and "compact" domains for models you want to export and run on edge devices. Compact models can be exported to ONNX, TensorFlow, CoreML, or Docker container formats. The exam might ask how to deploy a Custom Vision model to an edge device — the answer is to use a compact domain and export the model.

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

Let me share additional Video Indexer details that appear on the exam. Video Indexer needs to be connected to an Azure AI Services account to use its full capabilities. When you create a Video Indexer account, you associate it with an Azure AI Services resource. This connection enables the AI-powered features like face detection, object detection, and OCR within videos.

The API workflow follows a specific pattern. First, you get an access token by calling the authorization API. Then you upload a video using the upload endpoint, which starts the indexing process. You poll for indexing completion using the get index endpoint. Once complete, you can retrieve specific insights — the transcript, faces, topics, keywords, and more — through dedicated API endpoints.

Each insight type has its own structure in the API response. The transcript is a time-stamped array of spoken text. Faces include face IDs, time ranges when each face appears, and optionally matched identities (if you've enrolled known faces). Topics are extracted themes with confidence scores. Emotions are detected at the sentence level in the transcript, with scores for joy, sadness, anger, fear, and surprise.

Video Indexer also supports custom language models and custom person models. A custom language model improves transcription accuracy for domain-specific vocabulary. A custom person model lets you enroll known faces so the system can identify them by name in future videos.

One more thing about Video Indexer: it supports both video-on-demand (uploading pre-recorded files) and live stream analysis (connecting to a live video feed). The exam typically focuses on video-on-demand scenarios.

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

Natural language processing is about enabling computers to understand, interpret, and generate human language. Azure provides a comprehensive suite of NLP services that cover the entire spectrum from simple text analysis to complex conversational AI.

This domain has the widest breadth of any on the exam. You'll need to know about text analytics (six different capabilities), translation (three different modes), speech services (speech-to-text, text-to-speech, SSML, custom speech, intent recognition, keyword recognition, speech translation), and custom language models (CLU and Custom Question Answering). That's a lot of ground to cover, but the good news is that many of these services follow similar patterns — once you understand one, the others become easier.

The key decision patterns in this domain are: prebuilt versus custom (when are the built-in text analytics sufficient versus when you need CLU?), text versus speech (which modality is appropriate for the scenario?), and standard versus custom translation (when does domain-specific translation justify the overhead of training a custom model?).

Let's start with the foundational text analytics capabilities.

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

The Translator service has some unique characteristics compared to other Azure AI services that are worth highlighting. First, it can be used with either a multi-service Cognitive Services resource or a dedicated Translator resource. However, for document translation, you need a dedicated single-service Translator resource — a multi-service resource won't work for batch document translation. This is an important gotcha the exam tests.

Second, the Translator service supports a dictionary lookup feature that provides alternative translations for a word or phrase. You call the /dictionary/lookup endpoint with a word, and it returns a list of translations with part-of-speech information, usage examples, and confidence scores. There's also a /dictionary/examples endpoint that provides example sentences showing how a word is used in both the source and target languages.

Third, the Translator service has a /detect endpoint that identifies the language of a text input. While Azure AI Language also has language detection, the Translator's detect endpoint is specifically useful when you're about to translate and want to know the source language first. It returns the language code, confidence score, and whether the detected language is supported for both text and transliteration.

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

Let me explain why Custom Speech matters and when you'd use it, because the exam tests this decision.

The standard speech-to-text models work well for clear, standard speech in common scenarios. But they can struggle in several situations. Noisy environments — a factory floor, a busy restaurant, a moving vehicle — have acoustic characteristics that degrade recognition. Domain-specific vocabulary — medical terms like "acetaminophen" or "myocardial infarction," legal terms like "voir dire" or "habeas corpus," or industry jargon — might not be in the standard model's vocabulary. Accented speech or speech patterns specific to a region or community might have lower recognition accuracy. And product names, brand names, or internal terminology specific to your organization won't be recognized correctly.

Custom Speech addresses these challenges through two types of adaptation.

Acoustic model adaptation improves recognition in specific acoustic environments. If your users are in a noisy factory, or speaking through a particular microphone, or your audio has specific acoustic characteristics, you can provide sample audio with transcriptions to improve recognition accuracy in that environment.

Language model adaptation improves recognition of domain-specific vocabulary and phrases. If your application deals with medical terminology, legal jargon, or product names that the default model doesn't handle well, you can provide text data with these terms to improve recognition.

To create a Custom Speech model, you upload training data (audio files with transcriptions for acoustic models, or text files for language models), train the model in the Speech Studio, evaluate it against test data, and deploy it as a custom endpoint.

The exam doesn't go extremely deep on Custom Speech, but you should know that it exists, what it's for, and the basic workflow of training and deploying custom models.

You should also know about speech translation in a bit more detail. Speech translation combines speech recognition with text translation in a single pipeline. You speak in one language, the service recognizes your speech, translates it, and outputs either translated text or synthesized speech in the target language. This is different from doing speech-to-text followed by separate text translation — the integrated pipeline is more efficient and can handle the nuances of spoken language better.

The speech translation API supports real-time translation, making it suitable for scenarios like live meetings with multilingual participants, real-time captioning in multiple languages, and travel assistance applications. You specify the source language (or enable auto-detection) and one or more target languages. The response includes both the recognized text in the source language and the translated text in each target language.

Intent recognition deserves more attention because it bridges the speech and language domains. The Speech SDK can perform intent recognition by combining speech-to-text with a CLU model. You configure the speech recognizer with a CLU model endpoint and deployment name. When the user speaks, the SDK transcribes the speech and immediately sends the text to the CLU model for intent extraction. The result includes both the recognized text and the predicted intent with entities.

This is useful for voice-controlled applications where you need to understand not just what was said, but what the user wants to do. A smart home system might recognize the speech "Turn on the living room lights," extract the intent "TurnOn" with the entity "living room lights," and trigger the appropriate action — all in a single, integrated step.

Keyword recognition, also called keyword spotting, is the wake word detection capability. You define a keyword model (a specific word or short phrase like "Hey Computer" or "Start Listening"), and the speech service continuously listens for that keyword. When detected, it activates the full speech recognition pipeline. This is how voice assistants know when they're being addressed. You create a keyword model in Speech Studio, download it, and configure the SDK to use it.

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

The exam might ask about the minimum number of utterances (10 per intent, though more is recommended). They might show you utterances and ask you to identify the correct entity labeling. Or they might describe a scenario and ask how to improve a model with poor performance on specific intents.

Here's something the exam loves to test: the CLU evaluation workflow. After training a CLU model, Language Studio shows you evaluation results for each intent and each entity. The key metrics are precision, recall, and F1 score — the same metrics used in Custom Vision, just applied to language understanding.

For intents, the evaluation tells you how well the model classifies utterances into the correct intent. If the "BookFlight" intent has an F1 of 0.95, the model does great at recognizing flight booking requests. If the "CancelReservation" intent has an F1 of 0.6, the model struggles — maybe because the cancellation utterances are too similar to booking utterances, or because you don't have enough diverse examples.

For entities, the evaluation tells you how well the model extracts entities from utterances. Entity evaluation measures both whether the entity is detected at all (recall) and whether the detected text span is correct (precision). If the "destination" entity has high recall but lower precision, the model often extracts the destination but sometimes includes extra words or misses part of the name.

The improvement cycle for CLU follows a consistent pattern. Train the model, evaluate the results, identify weak intents and entities by their F1 scores, add more diverse utterances for weak intents, add more entity label examples for weak entities, retrain, and re-evaluate. Repeat until the F1 scores meet your quality threshold.

Let me give you specific improvement strategies that the exam tests. If an intent has low recall (the model misses many utterances that should match this intent), you need more diverse training utterances. Add examples with different wordings, sentence structures, and vocabulary. If an intent has low precision (the model incorrectly assigns other utterances to this intent), the intent might be too broad or overlap with another intent. Consider splitting it or adding negative examples. If entity extraction has low accuracy, add more examples with the entity in different positions and contexts within utterances.

The "None" intent is automatically included in every CLU project. It represents utterances that don't match any of your defined intents. Having good "None" intent coverage prevents your model from forcing irrelevant utterances into defined intents. The exam might test this — make sure you add diverse examples to the None intent.

## Importing and Exporting Language Projects

The exam specifically tests your knowledge of importing and exporting CLU and Custom Question Answering projects. This is important for several scenarios: backing up your projects, migrating between environments (development to production), version control, and collaboration.

CLU projects can be exported as JSON files that contain the complete project definition — intents, entities, utterances, and configuration. You can then import this JSON file into another Language resource to recreate the project. The export includes the schema version, project metadata, and all assets (intents, entities, and utterances with their labels).

Similarly, Custom Question Answering projects can be exported as files containing all question-answer pairs, their metadata, and conversation flows. You can export from Language Studio or via the REST API.

This is useful for CI/CD pipelines where you want to version-control your language models, test them in a staging environment, and promote them to production programmatically.

The export/import workflow is straightforward but important to understand. For CLU, you call the export REST API on your Language resource, which returns a JSON file representing the complete project. This file contains the project metadata (name, language, description), all intents with their definitions, all entities with their definitions and components, and all utterances with their intent assignments and entity labels. You can save this file in version control, modify it programmatically, or import it into another Language resource using the import API.

For Custom Question Answering, the export produces a file containing all question-answer pairs, their sources (which URL or document they came from), metadata tags, and follow-up prompts for multi-turn conversations. The format is JSON or TSV (tab-separated values), and you can import it back into the same or a different project.

The exam might present a scenario like "A team has a CLU model in development and needs to deploy it to a production Language resource in a different region." The answer involves exporting the project from the development resource and importing it into the production resource. This is the standard approach for environment promotion.

Another common scenario: "A company needs to maintain version history of their language model." The answer is to export the project after each significant change and store the exported files in source control (like Git). This gives you a complete history of the model's evolution and the ability to roll back to any previous version.

Let me also discuss CLU entity types in more detail because the exam tests the differences. There are several entity component types you can use.

Learned entities are the most flexible — the model learns to extract them from context based on your labeled examples. If you label "Seattle" as a destination entity in multiple utterances, the model learns to extract other city names as destination entities even if it hasn't seen them in training. Learned entities are great for entities that appear in varied contexts.

List entities are explicit lists of values. You define a list of canonical values and their synonyms. For example, a "size" entity might have the list: Small (with synonyms "sm," "little," "compact"), Medium (with synonyms "med," "regular"), and Large (with synonyms "lg," "big," "jumbo"). When the model sees any of these values, it maps them to the canonical form. List entities are best for closed sets of values where you know all possible options.

Prebuilt entities are pre-trained entity types provided by the service. These include DateTime (dates, times, durations, time ranges), Number (integers, decimals), Ordinal (first, second, third), Age, Currency, Dimension, Email, Phone Number, URL, and Temperature. You don't need to train these — they work out of the box. The exam might ask which entity type to use for extracting dates or numbers — the answer is prebuilt entities.

Regex entities use regular expressions to match patterns. For example, a product code like "ABC-1234" could be captured with the regex pattern "[A-Z]{3}-\d{4}". Regex entities are perfect for codes, IDs, and other structured patterns.

You can combine multiple entity components on a single entity. For example, a "product" entity might use a learned component (to extract product names from context), a list component (for known product names and their abbreviations), and a regex component (for product codes). The model uses all components together to maximize extraction accuracy.

This compositional entity design is a key differentiator of CLU compared to the older LUIS service, and the exam tests your understanding of how to combine entity components for optimal extraction.

## Custom Question Answering: Knowledge Bases, Multi-Turn, and Chit-Chat

Custom Question Answering (which replaced QnA Maker) lets you build question-answering solutions from your existing content. Here's how it works.

You create a project in Language Studio, then add knowledge sources. These can be FAQ web pages (you provide the URL and the system automatically extracts question-answer pairs), documents (PDF, Word, Excel, TSV), or manual entries (you type in question-answer pairs directly).

Each entry in the knowledge base is a question-answer pair. A single answer can have multiple question phrasings — these alternate phrasings help the system match user questions to the right answer even when worded differently. For example, the answer "Our return policy allows returns within 30 days" might have question phrasings like "What's your return policy?", "How long do I have to return something?", "Can I get a refund?", and "What's the return window?"

Multi-turn conversations allow you to create hierarchical, guided conversations where follow-up prompts lead users through a decision tree. For example, asking "Do you need help with billing?" might have follow-up prompts for "View my bill," "Make a payment," or "Dispute a charge." Each follow-up prompt can have its own follow-up prompts, creating a tree structure.

Chit-chat adds personality to your knowledge base with pre-built question-answer pairs for common social interactions. You choose from personality styles — professional, friendly, witty, caring, or enthusiastic — and the system adds appropriate responses for small talk like "How are you?", "Tell me a joke," or "What's your name?"

After building your knowledge base, you train and test it in Language Studio, then publish it to a prediction endpoint. The endpoint returns the best matching answer for a given question, along with a confidence score.

Synonyms are another important feature. You can define synonyms so that different words are treated as equivalent during matching. For example, defining "account" and "subscription" as synonyms means a question about "my subscription" would match answers about "your account."

The exam tests knowledge base creation, multi-turn configuration, alternate phrasings, chit-chat personality selection, and export/import capabilities.

Let me go deeper on each of these areas with exam-relevant detail.

Knowledge base creation can draw from multiple sources simultaneously. You might add your FAQ web page, a product manual PDF, and some manually created QA pairs. The system merges all these into a unified knowledge base. When you add a URL, the system crawls the page, identifies question-answer structures (typically from HTML headers and their associated paragraphs, or from definition lists), and creates QA pairs automatically. You can review and edit the extracted pairs.

For multi-turn conversations, the key concept is "follow-up prompts." When a user asks a broad question, the system can return an answer along with suggested follow-up prompts that guide the user to more specific information. For example, if someone asks "Tell me about your plans," the response might be "We offer three plans" with follow-up prompts for "Basic Plan," "Professional Plan," and "Enterprise Plan." Each follow-up prompt links to a different QA pair in the knowledge base.

Multi-turn conversations can be defined manually in Language Studio by adding follow-up prompts to specific answers, or they can be extracted automatically from structured documents. Word documents with headings and subheadings, for example, can be automatically converted into multi-turn conversation flows where each heading level represents a layer of the conversation.

Alternate phrasings are crucial for good matching performance. Users express the same question in many different ways, and the more phrasings you provide, the more likely the system is to match correctly. The system uses these phrasings during matching to calculate similarity scores. Best practice is to include at least five to ten alternate phrasings per answer, covering different vocabulary, sentence structures, and levels of formality.

Chit-chat adds personality to your bot without you having to manually create social QA pairs. When you enable chit-chat, you choose a personality (professional, friendly, witty, caring, or enthusiastic), and the system adds hundreds of pre-built QA pairs covering common small talk. For example, "Hi" gets a personality-appropriate greeting, "Tell me a joke" gets a humorous response matching the personality style, and "Thank you" gets an acknowledgment. This makes your bot feel more natural and engaging.

Metadata tags can be added to QA pairs for filtering. Each tag is a key-value pair. When querying the knowledge base, you can include metadata filters to narrow the results. For example, if you have QA pairs tagged with product="basic" and product="premium," you can filter by the user's product tier to show only relevant answers.

The confidence score threshold determines when the system returns an answer versus saying it doesn't know. A higher threshold means the system only returns high-confidence matches, while a lower threshold returns more matches but with lower quality. You can configure this threshold in the project settings. The default is typically 0.3, meaning any match with 30% or higher confidence is returned. For production systems, you might raise this to 0.5 or 0.7 to reduce false positive answers.

Testing in Language Studio provides an interactive interface where you can type questions and see the matched answers, confidence scores, and source information. This is essential for iterating on your knowledge base quality.

## Multi-Language Solutions

Custom Question Answering supports multi-language projects. When you enable multi-language support, you can add question-answer pairs in multiple languages within the same project. The system detects the language of incoming questions and returns answers in the matching language.

Alternatively, you can create separate projects for each language and route users to the appropriate project based on their language preference.

The exam might present a scenario where a company needs to support customers in multiple languages and ask which approach to use. Multi-language projects are simpler to manage but may have slightly lower accuracy for each language compared to dedicated single-language projects.

Let me also discuss custom translation in more detail since it's included in the NLP domain.

Custom Translator lets you build domain-specific translation models. The workflow starts with preparing parallel training data — documents in the source language paired with their translations in the target language. These can be sentence-aligned files (where each line in the source file corresponds to a line in the target file) or translation memory files in formats like TMX or XLIFF.

You upload this parallel data to the Custom Translator portal, create a project specifying the source and target languages, assign the data to training, testing, and tuning sets, and train the model. The training process uses your data to learn domain-specific terminology, phrase patterns, and translation preferences that the base translation model doesn't handle well.

After training, you can test the custom model in the portal to compare its translations against the standard model. You can then deploy the model and use it through the regular Translator API by specifying the category parameter with your custom model's category ID. This is a seamless integration — your application uses the same Translator API endpoint, just with an additional parameter to route to your custom model.

The exam might describe a scenario where a legal firm's standard translations consistently mistranslate legal terminology. The solution is Custom Translator trained on the firm's existing translated legal documents. This ensures terms like "injunction," "deposition," and "affidavit" are translated correctly in the legal context.

Custom Translator also supports a dictionary feature. A dictionary is a set of phrase pairs (source and target) that should always be translated in a specific way, regardless of context. Unlike glossaries that influence the translation, dictionary entries override the model's translation for those specific phrases. This is useful for brand names, product names, and technical terms that must always remain untranslated or have a fixed translation.

The quality of your custom translation model depends heavily on the quality and quantity of your parallel training data. Microsoft recommends at least 10,000 parallel sentences for good quality, though models can be trained with as few as 500 sentences. The more data you provide, and the closer it matches your actual translation needs, the better the results.

---

# Chapter 6: Knowledge Mining and Information Extraction (15 to 20 percent)

Knowledge mining is about making large volumes of unstructured data searchable and usable. This domain covers Azure AI Search, Document Intelligence, and Content Understanding. It's tied with NLP for the second-heaviest exam weight, so give it serious attention.

Knowledge mining represents one of the most practical and impactful applications of AI in enterprise settings. Most organizations have vast repositories of unstructured data — documents, images, emails, reports, contracts — that contain valuable information but are impossible to search or analyze at scale. Azure AI Search with its AI enrichment pipeline transforms this unstructured content into searchable, structured knowledge.

This domain is divided into three main service areas. Azure AI Search is the search engine and enrichment pipeline — it creates indexes, runs enrichment skillsets, and serves queries. Document Intelligence extracts structured data from specific document types — invoices, receipts, forms. Content Understanding provides general-purpose content processing across multiple modalities.

The common thread across all three is the transformation of unstructured content into structured, actionable information. The exam tests your ability to choose the right service for each extraction scenario, configure the processing pipelines correctly, and query the results effectively.

Let me also note that this domain has significant overlap with domain two (Generative AI) when it comes to the RAG pattern. Azure AI Search is the retrieval component in RAG, and understanding how to build and query search indexes is essential for building effective RAG solutions. The exam might present a question that bridges both domains — building a search index with enrichment, then using it as the knowledge base for an Azure OpenAI chat application.

## Azure AI Search: Indexes, Skillsets, and Indexers

Azure AI Search is a cloud search service that creates rich, searchable indexes over your content. Understanding its architecture is key. There are three main components: indexes, indexers, and skillsets.

An index is the searchable data store. Think of it like a database table, but optimized for search. Each index has a schema that defines its fields. Fields have a name, a data type (like Edm.String for text, Edm.Int32 for integers, Edm.DateTimeOffset for dates, or Collection of Edm.String for arrays), and attributes that control how the field behaves.

The field attributes are critical for the exam. Searchable means the field is included in full-text search queries. Filterable means you can use $filter expressions on it. Sortable means you can use $orderby with it. Facetable means you can use it for faceted navigation (like showing a count of results per category). Retrievable means the field is included in search results. Key means the field uniquely identifies each document. Every index must have exactly one key field.

Let me explain faceting in more detail because it's a concept the exam tests and it's not always intuitive from the name. Faceted navigation is what you see on e-commerce sites — when you search for "laptop" and the sidebar shows filters like "Brand: Dell (15), HP (12), Lenovo (8)" and "Price Range: Under $500 (5), $500-$1000 (18), Over $1000 (12)." Those filters are facets. When you mark a field as facetable, Azure AI Search can calculate the distinct values and counts for that field, enabling this kind of interactive filtering.

To get facets in your query results, you include the "facets" parameter in your search request with the field name. The response includes a facets section showing each value and its count. You can customize facets with intervals for numeric and date fields — for example, "price,interval:100" groups prices into $100 ranges.

Here's a practical example. In a product catalog index, you might have a productId field that's the key. A productName field that's searchable, retrievable, and sortable. A description field that's searchable and retrievable. A price field that's filterable, sortable, and facetable. And a category field that's filterable, facetable, and retrievable.

Let me also talk about field data types in more detail. Edm.String is for text fields. Edm.Int32 and Edm.Int64 are for integers. Edm.Double is for floating-point numbers. Edm.Boolean is for true/false. Edm.DateTimeOffset is for dates with time zones. Edm.GeographyPoint is for latitude/longitude pairs (useful for geo-spatial queries). Collection(Edm.String) is for arrays of strings — useful for tags or categories where a single document can have multiple values. Collection(Edm.Single) is for vector fields used in vector search.

The exam might show you an index schema and ask you which queries are possible based on the field attributes. If a field isn't filterable, you can't use $filter on it. If it isn't sortable, you can't use $orderby. If it isn't searchable, it won't be included in full-text queries. Understanding these attribute-to-capability mappings is essential.

An indexer is the automated data pipeline that pulls data from a source, transforms it, and pushes it into the index. Data sources can include Azure Blob Storage, Azure SQL Database, Azure Cosmos DB, and Azure Table Storage. Indexers can run on a schedule (like every hour) or on demand. They track which documents have changed and only reprocess what's new or modified — this is called incremental indexing.

Indexers also support field mappings, which let you rename or transform fields between the source and the index. For example, if your blob storage has a metadata field called "upload_date" but your index field is called "dateCreated," you use a field mapping to bridge them.

There are two types of field mappings: field mappings (for mapping source fields to index fields before enrichment) and output field mappings (for mapping enriched fields from a skillset to index fields). Output field mappings are specifically used when your skillset produces enriched data — like extracted entities or key phrases — that you want to store in the index.

Let me walk through the complete indexer pipeline because understanding this end-to-end flow is critical for the exam. Step one: you define a data source that points to your data — a blob storage container, a SQL database table, or a Cosmos DB collection. Step two: you create an index with the schema defining all the fields you want to make searchable. Step three: you optionally create a skillset with AI enrichment skills. Step four: you create an indexer that connects the data source to the index, optionally through the skillset, with field mappings.

When the indexer runs, it reads documents from the data source, runs them through the skillset (if defined) to extract enriched data, maps the original and enriched fields to the index schema, and pushes the documents into the index. On subsequent runs, it detects changes and only processes new or modified documents.

The indexer schedule is defined with an interval (minimum 5 minutes) and an optional start time. For example, "interval: PT1H" runs every hour. The exam might ask about indexer scheduling — know that you can set schedules and that incremental indexing is the default behavior.

Blob indexer file limits are also tested: Standard tiers can index blobs up to 256 megabytes, while the Free tier is limited to 16 megabytes. The skillset execution timeout is 230 seconds per document — if enrichment for a single document takes longer than that, it times out.

A skillset is a collection of AI enrichment steps that transform your data during indexing. This is where the "AI" in AI Search comes in. As documents flow through the indexer, the skillset applies AI operations to extract additional information.

## Built-In versus Custom Skills

Skillsets contain skills, and there are two categories.

Built-in skills are provided by Microsoft and cover common AI operations. They include entity recognition (extracting named entities from text), key phrase extraction, language detection, sentiment analysis, OCR (extracting text from images), image analysis (generating tags and descriptions for images), text translation, text merge (combining OCR output with original text), text split (chunking text for processing), and PII detection. Each built-in skill maps to an Azure AI service that runs behind the scenes.

Custom skills let you add your own processing logic. The most common approach is a Web API skill that calls an Azure Function you've written. Your function receives the document content, performs whatever processing you need, and returns the enriched data. This is incredibly powerful — you can add domain-specific entity extraction, call external APIs, run machine learning models, or perform any custom transformation.

The interface for custom skills is standardized. Your Azure Function receives a JSON payload with records containing the input data, and returns a JSON payload with records containing the output data. The input and output field names are defined in the skillset configuration.

Let me walk through the custom skill interface in detail because the exam tests this structure. The request body sent to your Azure Function has a "values" array. Each value has a "recordId" (a unique identifier for the document), a "data" object with the input fields, and optional "errors" and "warnings" arrays. Your function processes each record and returns a response with the same structure: a "values" array where each value has the same "recordId" and a "data" object with the output fields.

In the skillset definition, you specify the custom skill using the WebApiSkill type. The key properties include the "uri" (the URL of your Azure Function), the "httpHeaders" (for authentication), and the "inputs" and "outputs" arrays that define how data flows in and out. The inputs specify which enriched data to send to your function (using the skillset's internal reference syntax like "/document/content" or "/document/merged_content"), and the outputs specify the names of the fields your function returns.

Here's a concrete example. Say you want to extract product codes from documents using a regular expression pattern that your built-in skills can't handle. You'd create an Azure Function that receives document text, applies your regex pattern, and returns an array of matched product codes. In the skillset, you'd define a WebApiSkill pointing to your function's URL, with an input of "/document/content" and an output of "productCodes." Then you'd use an output field mapping to store "productCodes" in your index's productCodes field.

Skills within a skillset can be chained — the output of one skill becomes the input of another. For example, an OCR skill might extract text from an image, a text merge skill might combine that OCR text with the document's existing text, and then a key phrase skill might extract key phrases from the merged text. The exam tests your understanding of these skill chains and the data flow between them.

The exam loves to test custom skills. They might describe a scenario where the built-in skills aren't sufficient and ask how to add custom logic. The answer is almost always a custom Web API skill backed by an Azure Function.

## Knowledge Store Projections

A knowledge store is an optional output of the AI enrichment pipeline that persists enriched data to Azure Storage for downstream analytics. While the index is optimized for search queries, a knowledge store lets you analyze the enriched data using tools like Power BI, Jupyter notebooks, or any other analytics tool.

Knowledge store projections define how enriched data is stored. There are three types.

Table projections store data in Azure Table Storage as rows and columns. This is ideal for structured data that you want to query with tools like Power BI. Each entity type might be stored in a separate table.

Object projections store data as JSON blobs in Azure Blob Storage. This preserves the full hierarchical structure of the enriched documents, which is useful for complex document structures.

File projections store normalized images and other binary data extracted during enrichment as files in Blob Storage.

You can use multiple projection types simultaneously. For example, you might store entity data in tables for Power BI analysis, full enriched documents as JSON blobs for programmatic access, and extracted images as files.

Let me walk through a concrete knowledge store example because the exam tests the configuration. Imagine you have a pipeline that processes PDF documents. The indexer extracts the text, the OCR skill extracts text from embedded images, the entity recognition skill extracts person and organization entities, and the key phrase skill extracts key phrases.

Without a knowledge store, all this enriched data goes into the search index — great for searching, but what if you want to build a Power BI dashboard showing the most frequently mentioned organizations, or create a data lake of extracted entities for further analysis? That's where the knowledge store comes in.

You'd configure table projections to create an "entities" table with columns for entity name, entity type, document ID, and count. You'd also create a "keyphrases" table with key phrase, document ID, and frequency. These tables are stored in Azure Table Storage and can be queried by Power BI, Azure Data Explorer, or any other analytics tool.

You might also configure object projections to store the complete enriched document (with all entities, key phrases, sentiment scores, and OCR text) as a JSON blob in Azure Blob Storage. This preserves the full context for any application that needs the complete enrichment output.

And file projections would store any images extracted from the PDFs as individual image files in Blob Storage, organized by document.

The knowledge store is defined in the skillset JSON. It has three arrays: tables, objects, and files. Each projection has a name, a generatedKeyName (a unique identifier for each projected row/object), and a source path (which enriched data to project). The source path uses the same reference syntax as skill inputs — "/document/entities" for the entities extracted from the entire document, or "/document/pages/*/entities" for entities from each page.

The exam tests knowledge store concepts and the differences between projection types. Know when to use tables (structured analysis, Power BI), objects (hierarchical data, programmatic access), and files (binary/image data, downstream processing).

## Query Syntax

Querying Azure AI Search is a rich topic with several important concepts. Let me walk through the query capabilities you need to know.

The basic search parameter takes your search text. By default, it uses simple query syntax where terms are matched individually and combined with OR logic. The searchMode parameter controls this: "any" means any term can match (OR), while "all" means all terms must match (AND).

The $filter parameter uses OData filter expressions to narrow results. You can use equality (eq), comparison (gt, ge, lt, le, ne), logical operators (and, or, not), and special functions. For collections, you use any() and all() to test elements. For example, "$filter=tags/any(t: t eq 'azure')" finds documents where the tags collection contains "azure." The search.ismatch function lets you combine full-text search with filtering.

$select specifies which fields to include in the results, reducing the payload size.

$orderby controls the sort order. You can sort by one or more fields, each ascending or descending. For example, "$orderby=rating desc,title asc" sorts by rating descending, then by title ascending for ties.

$top and $skip implement pagination. $top limits the number of results returned, and $skip skips a number of results for getting subsequent pages.

$count returns the total number of matching results, which is useful for pagination UI.

Let me walk through several detailed query examples because the exam shows specific query syntax and asks what results would be returned.

Example one: A simple keyword search with filtering. You search for "cloud computing" with a filter of "category eq 'Technology'" and select "title, content, category." This returns documents that contain the words "cloud" or "computing" (OR by default with searchMode any), where the category field exactly equals "Technology," and only includes the title, content, and category fields in the response.

Example two: Collection filtering with any(). Suppose each document has a "tags" field that's a Collection of Edm.String. The filter "tags/any(t: t eq 'azure')" returns documents where at least one tag equals "azure." The variable "t" is a range variable that iterates over the collection elements. The filter "tags/all(t: t ne 'deprecated')" returns documents where ALL tags are not equal to "deprecated" — meaning none of the tags is "deprecated."

Example three: Combining search with filter using search.ismatch. The filter "search.ismatch('wifi', 'amenities')" performs a full-text search for "wifi" within the "amenities" field specifically. This is different from the main search parameter, which searches across all searchable fields.

Example four: Geo-spatial filtering. If your index has a GeographyPoint field called "location," you can filter by distance: the filter uses geo.distance with your coordinates and a less-than-or-equal comparison to find documents within a certain kilometer radius.

For advanced full-text search, you set queryType to "full" to enable Lucene query syntax. This gives you phrase search (using quotes), wildcards (asterisk for multiple characters, question mark for single character), fuzzy search (tilde followed by edit distance), proximity search (phrase with tilde and word count), term boosting (caret with boost factor), field-scoped search (fieldname colon term), and regular expressions (forward slashes around the pattern).

Let me elaborate on each Lucene operator with examples. Phrase search — putting terms in quotes like "cloud computing" — requires the exact phrase, not just both words appearing anywhere. Wildcard search — "comp*" matches "computer," "computing," "company," and so on. The question mark matches exactly one character: "comput?r" matches "computer" but not "computing." Fuzzy search — "computer~1" matches words within one edit distance of "computer," like "compter" or "computr." This is great for handling typos. Proximity search — the phrase "cloud computing" with tilde 5 finds documents where "cloud" and "computing" appear within 5 words of each other. Boosting — "cloud^4 computing" makes "cloud" four times more important in relevance scoring. Field-scoped search — "title:azure AND content:machine learning" searches specific fields.

The exam loves to test query syntax. They might show you a query and ask what it returns, or describe desired search behavior and ask you to write the query. Memorize the OData filter syntax and the Lucene query operators.

## Semantic Search and Vector Search

These are the two advanced search capabilities that take Azure AI Search beyond simple keyword matching.

Semantic search uses AI to understand the meaning of queries and documents, rather than just matching keywords. When you set queryType to "semantic" and specify a semanticConfiguration, the search service re-ranks results using a deep learning model that understands the semantic relationship between the query and the documents. It can also generate extractive captions (highlighting the most relevant passages) and extractive answers (pulling out the specific answer to a question).

To use semantic search, you first create a semantic configuration on your index that identifies which fields to use for title, content, and keywords. Then you include the appropriate parameters in your query.

Vector search uses mathematical similarity between vector embeddings to find relevant results. You generate embeddings for your documents during indexing and embeddings for queries at search time, then find documents whose vectors are closest to the query vector in embedding space.

To use vector search, your index needs vector fields — fields with a vector profile that defines the embedding dimensions and similarity algorithm. You provide the query vector in a vectorQueries array in your search request, specifying the fields to search and k (the number of nearest neighbors to return).

Hybrid search combines keyword search and vector search in a single query. This often produces the best results because it catches both exact keyword matches and semantically similar content. You simply include both a search text and vectorQueries in the same request.

Let me expand on vector search implementation because it has several components the exam tests. First, you need an embedding model to generate vectors. This is typically an Azure OpenAI embedding model like text-embedding-ada-002 or text-embedding-3-small. During indexing, you generate an embedding for each document's content and store it in a vector field in the index. At query time, you generate an embedding for the user's search query and include it in the vectorQueries parameter.

The vector field in your index schema has a type of Collection(Edm.Single), which is an array of floating-point numbers. You configure a vector profile on the field that specifies the number of dimensions (matching your embedding model — 1536 for ada-002, 1536 or less for embedding-3-small, 3072 or less for embedding-3-large) and the similarity algorithm (cosine similarity is most common, but dot product and Euclidean distance are also available).

The k parameter in your vector query specifies how many nearest neighbors to retrieve. A k of 5 means you get the 5 most similar documents. The exhaustive parameter controls whether the search does an exact nearest-neighbor search (exhaustive: true) or an approximate nearest-neighbor search (exhaustive: false, which is faster but slightly less accurate). For most applications, approximate search is fine and much faster for large indexes.

The semantic configuration for semantic search is defined at the index level. You specify which field to use as the title (the most semantically important short field), which fields to use as content (the main body text), and which fields to use as keywords (additional context). The AI model uses these fields to understand each document and re-rank results.

When you use semantic search, the response includes additional properties. Semantic captions are highlighted excerpts showing the most relevant passages. Semantic answers are extracted answers to the query — the service tries to find a direct answer within the documents. The queryLanguage parameter tells the semantic ranker which language the query is in, enabling proper language understanding.

The exam tests your understanding of when to use each approach. Keyword search for exact term matching and known terminology. Semantic search for natural language questions where the user might not use the exact terms in the documents — like asking "how does solar power work?" when the documents use the phrase "photovoltaic energy conversion." Vector search for finding semantically similar content using mathematical similarity of embeddings — especially powerful when the vocabulary doesn't overlap at all between the query and the relevant documents. Hybrid search for the best of all worlds — combining keyword matching, vector similarity, and optionally semantic re-ranking for the most comprehensive results.

Let me also describe how you'd set up vector search step by step, since this is a common exam scenario. First, you choose an embedding model — say text-embedding-ada-002, which produces 1536-dimensional vectors. Second, during indexing, you generate embeddings for each document's content using the embedding model and store both the text and the embedding vector in the index. The vector field in your schema is defined as Collection(Edm.Single) with a vector search profile specifying the dimensions (1536) and the similarity algorithm (typically cosine). Third, at query time, you generate an embedding for the user's search query using the same model. Fourth, you include this query vector in the vectorQueries parameter of your search request, specifying the vector field to search and k (the number of nearest neighbors).

The k parameter deserves special attention. If k is too small (like 1 or 2), you might miss relevant results. If k is too large (like 50 or 100), you include too much irrelevant content, which can dilute the quality of RAG responses. A k of 3 to 10 is typical for most applications. The exam might ask about tuning the k parameter for optimal retrieval quality.

Here's an important AI Search tier detail: semantic search requires at least the Basic tier. The Free tier doesn't support it. Vector search is available on all tiers, including Free. This is the kind of detail the exam tests.

Let me also discuss AI Search tier selection because the exam asks about it. The Free tier is for development and testing — 3 indexes, 50 megabytes storage, 10,000 documents. Basic supports 15 indexes and 2 gigabytes. Standard S1 supports 50 indexes and 25 gigabytes per partition, with up to 12 partitions and 12 replicas. Standard S2 and S3 offer even more capacity. Storage Optimized L1 and L2 are for workloads with massive data volumes.

The key capacity concepts are indexes (how many separate search collections you need), storage (total size of your indexed data), replicas (copies of your index for query throughput and high availability), and partitions (shards of your index for increased storage). Adding replicas increases query throughput — two replicas can handle twice the query load. Adding partitions increases storage — two partitions doubles your maximum index size. For high availability, Microsoft recommends at least 2 replicas for read-only workloads and 3 replicas for read-write workloads.

The exam might ask about tier selection. If a company has 100 gigabytes of documents to index, the Free tier (50 megabytes) and Basic tier (2 gigabytes) are too small. Standard S1 with enough partitions (4 partitions gives 100 gigabytes) would work. If they also need high availability, they'd need multiple replicas, which increases cost.

The pricing model for AI Search is per-unit, where a unit is the combination of partitions and replicas. A Standard S1 service with 3 replicas and 2 partitions uses 6 units (3 times 2). Understanding how replicas, partitions, and units relate to capacity and cost is important for capacity planning questions.

## Document Intelligence: Prebuilt versus Custom Models

Document Intelligence, formerly Form Recognizer, extracts structured data from documents. It offers three main approaches.

Prebuilt models are ready-to-use models trained on specific document types. The available prebuilt models include prebuilt-invoice for extracting data from invoices (vendor name, total amount, line items), prebuilt-receipt for receipts (merchant name, transaction date, total, items), prebuilt-idDocument for identity documents (name, date of birth, document number), prebuilt-tax.us.w2 for W-2 tax forms, prebuilt-healthInsuranceCard for health insurance cards, prebuilt-businessCard for business cards, prebuilt-layout for extracting the general layout structure (tables, paragraphs, selection marks) from any document, and prebuilt-read for extracting raw text with its location.

Custom models are trained on your own labeled documents for domain-specific extraction. There are two types of custom models. Template models work best for fixed-layout documents where fields are always in the same position — like a specific company's invoice template. They need a minimum of 5 labeled training documents. Neural models work with variable-layout documents where the structure can differ between instances. They're more flexible but require more training data.

The analysis workflow follows an asynchronous pattern, especially via REST. You send a POST request with the document to the analyze endpoint. The service returns a 202 response with an Operation-Location header containing a URL. You then poll that URL with GET requests until the status is "succeeded." The results include the extracted fields, their values, confidence scores, and bounding boxes showing where each field was found in the document.

Using the SDK, this is simpler. You call "begin_analyze_document" with the model ID and document, and get back a poller that you wait on. The result contains the same information as the REST response.

Let me walk through the SDK pattern in more detail because the exam shows this code. In Python, you'd import DocumentAnalysisClient and AzureKeyCredential from the azure.ai.formrecognizer package. You create a client by passing the endpoint and credential. Then you open your document file, call client.begin_analyze_document with the model ID (like "prebuilt-invoice") and the document stream. This returns a poller, and you call poller.result() to wait for and get the result.

The result object has a documents array, where each document has a doc_type (like "invoice") and a fields dictionary. Each field has a value, a confidence score, and a content property (the raw text). For an invoice, the fields might include "VendorName," "InvoiceTotal," "InvoiceDate," "BillingAddress," and "Items." The "Items" field is a list of line items, each with its own subfields like "Description," "Quantity," "UnitPrice," and "Amount."

For the prebuilt-layout model, the result includes a different structure. Instead of named fields, it returns pages (with lines and words), tables (with rows, columns, and cells), paragraphs, and selection marks (like checkboxes). Layout analysis is useful when you want to understand the structure of a document without extracting specific fields.

The prebuilt-read model is even simpler — it just extracts text with its position. It's like the Read API in Azure AI Vision but with additional capabilities for document-specific scenarios.

Custom model training in Document Intelligence Studio involves uploading sample documents, labeling the fields you want to extract (by drawing bounding boxes around field values and assigning field names), and training the model. The studio provides a visual labeling experience that's intuitive to use. After training, you get accuracy metrics for each field, showing how well the model can locate and extract each piece of information.

There are two custom model types with important differences. Template models (formerly "custom form models") work best with fixed-layout documents — forms where the fields are always in the same position. They need at least 5 labeled training documents and are fast to train. Neural models work with variable-layout documents — the structure can differ between instances, and the model uses semantic understanding rather than positional matching. Neural models require at least 1 labeled document (though more is better for accuracy) and take longer to train but handle document variability much better.

The exam might describe a scenario where documents have consistent structure (like a company's standard invoice template) and ask which model type to use — that's template. If the scenario describes varied document layouts that share similar information but in different positions — that's neural.

Here's another important Document Intelligence concept: the layout model. The prebuilt-layout model doesn't extract specific fields like the invoice or receipt models. Instead, it extracts the general structure of any document: text (organized into paragraphs and sections), tables (with rows, columns, and cell content), selection marks (checkboxes and radio buttons), and the overall reading order. This is useful as a first step in processing — you might use layout analysis to understand a document's structure before deciding which specialized model to apply.

The prebuilt-read model is the simplest — it just extracts text and its location. It's equivalent to OCR. Use it when you need raw text extraction without any structural analysis.

For custom model training in Document Intelligence Studio, the workflow is: create a project, connect to your training data (stored in Azure Blob Storage), label your documents (draw bounding boxes around fields and assign field names), train the model, evaluate the results, and deploy. The studio provides a visual labeling interface with tools for drawing bounding boxes, assigning field names, and handling multi-page documents.

The labeling process for custom models is particularly important to understand. For template models, you label fields by drawing a bounding box around the field value and assigning a field name. The model learns the position of each field relative to the page layout. For neural models, you also label fields, but the model uses the semantic content around the field (headers, labels, context) rather than just position. This is why neural models can handle variable layouts.

For the exam, understand the complete Document Intelligence model hierarchy: prebuilt-read (text only), prebuilt-layout (text plus structure), prebuilt-invoice (invoice-specific fields), prebuilt-receipt (receipt-specific fields), prebuilt-idDocument (ID card fields), prebuilt-tax.us.w2 (W-2 fields), prebuilt-healthInsuranceCard (insurance card fields), custom template (your fixed-layout forms), custom neural (your variable-layout forms), and composed (combining multiple custom models).

The file limits for Document Intelligence are explicitly tested. Free tier (F0): 4 megabyte max file size, 2 pages max per invocation. Standard tier (S0): 500 megabyte max file size, 2,000 pages max per invocation. Minimum image size: 50 by 50 pixels. Supported formats include PDF, JPEG, PNG, BMP, TIFF, HEIF, DOCX, XLSX, and PPTX.

These limits come up in specific exam scenarios. For example: "A company needs to process a 100-page PDF invoice. They're using the Free tier of Document Intelligence. What happens?" The answer is that the analysis fails because the Free tier only supports 2 pages per invocation. They'd need to upgrade to Standard tier, which supports up to 2,000 pages.

## Composed Models

Composed models are a powerful feature of Document Intelligence that combine multiple custom models into one. Here's how they work and why they matter.

Imagine you have three different invoice formats from three different vendors. You train a separate custom model for each format. Without composed models, your application would need logic to determine which vendor's invoice it's processing and route it to the correct model. With a composed model, you combine all three custom models into one. When you analyze a document, the composed model automatically determines which sub-model to use and applies it.

The composed model evaluates the document against all its sub-models and uses the one that best matches. The response includes which sub-model was selected, so you know which format was detected.

Let me walk through a practical composed model scenario. Say you have a document processing system that receives invoices from three different vendors: Acme Corp, GlobalTech, and FastShip. Each vendor's invoice has a different layout — different field positions, different formatting, different information hierarchy.

You'd train three separate custom models: acme-invoice-model, globaltech-invoice-model, and fastship-invoice-model. Each is trained on labeled examples of that specific vendor's invoices. Then you create a composed model called "all-invoices-model" that combines all three.

When a new invoice arrives, you submit it to the all-invoices-model. The composed model evaluates the document against all three sub-models, selects the one with the highest confidence, and returns the extracted fields using that model's schema. The response includes a "docType" field that tells you which sub-model was used — for example, "acme-invoice-model" — so your application knows which vendor's invoice it just processed.

This eliminates the need for pre-classification logic in your application. Without composed models, you'd need to either visually inspect each invoice to determine the vendor, or build a separate classification step before extraction. Composed models handle both classification and extraction in a single API call.

The limits to know: Free tier supports up to 5 sub-models per composed model. Standard tier supports up to 200 sub-models. The exam might ask about composed model limits, or ask you to recommend composed models when the scenario describes processing multiple document formats through a single pipeline.

One more Document Intelligence concept: the analyze results structure. When analyzing a document, the result includes several important properties. The "content" property contains the full text of the document. The "pages" array describes each page with its dimensions, lines, words, and selection marks. The "tables" array describes extracted tables with their row and column counts, cells, and bounding regions. The "documents" array (for prebuilt and custom models) contains the extracted fields with their values, types, and confidence scores. And the "styles" array identifies handwritten content by describing content with a specific style (like "handwritten") along with the confidence.

Understanding this result structure helps with code-based exam questions where you need to navigate the response to find a specific piece of information.

## Content Understanding: OCR Pipelines and Classification

Content Understanding is a newer addition to the Azure AI landscape, introduced as part of Microsoft Foundry. It provides capabilities for processing various content types — documents, images, video, and audio — through unified pipelines.

OCR pipelines in Content Understanding extract text from images and scanned documents, similar to the Read API but integrated into the Foundry platform.

Document classification automatically categorizes documents by type. This is useful when you receive a mix of document types and need to route them to the appropriate processing pipeline.

Attribute detection identifies characteristics of documents, such as whether text is handwritten versus printed, or what language the document is in.

Entity extraction identifies and extracts specific entities from documents, similar to NER but applied to document content.

Table extraction identifies and extracts tabular data from documents, preserving the row-column structure.

Image extraction pulls out embedded images from complex documents.

The key difference between Content Understanding and Document Intelligence is the scope and approach. Document Intelligence focuses on extracting specific fields from known document types. Content Understanding takes a broader approach, providing general-purpose content analysis across multiple modalities (documents, images, video, audio) within the Foundry framework.

Let me elaborate on when to use Content Understanding versus Document Intelligence because this distinction is exam-relevant.

Use Document Intelligence when you have a specific document type — like invoices, receipts, or tax forms — and you need to extract specific, named fields. Document Intelligence has prebuilt models for common document types and lets you train custom models for domain-specific forms. It excels at structured data extraction with high accuracy for known fields.

Use Content Understanding when you need general-purpose content processing across different content types. If your workflow involves processing a mix of documents, images, videos, and audio, and you need to classify, summarize, and extract information from all of them through a unified pipeline, Content Understanding is the better fit. It's integrated into the Foundry platform and designed for multimodal content processing workflows.

The exam might present a scenario like "A company receives customer communications via email (text), voice messages (audio), and faxed documents (images). They need a unified pipeline to classify, transcribe, and extract key information from all communication types." This would be a Content Understanding scenario because of the multimodal nature.

Contrast that with "A company needs to process thousands of invoices from three different vendors and extract the vendor name, invoice total, and line items." That's Document Intelligence because it's focused on extracting specific fields from a specific document type.

Content Understanding also supports advanced document classification — automatically categorizing incoming documents into types before processing. If you receive a mix of invoices, purchase orders, contracts, and correspondence, Content Understanding can classify each document and route it to the appropriate processing pipeline. While Document Intelligence's composed models provide some routing capability, Content Understanding's classification is more general-purpose and handles a wider variety of content types.

---

# Exam Strategy Chapter

Now that we've covered all six domains in detail, let's talk about how to actually take and pass this exam. Exam strategy matters just as much as knowledge.

I've seen many well-prepared candidates fail not because they didn't know the material, but because they ran out of time, misread questions, or panicked on unfamiliar question formats. The strategies in this chapter are based on common patterns from the AI-102 exam and Microsoft certification exams in general.

Let me start with the exam format and timing.

## Format and Timing

You'll face approximately 58 questions in 120 minutes. That works out to about 2 minutes per question, which sounds generous but can get tight, especially with case studies and long scenario questions.

At the very beginning of the exam, you'll be asked to choose Python or C# as your programming language for code-based questions. This choice is permanent — you cannot switch during the exam. Choose the language you're most comfortable reading. You don't need to be an expert coder, but you need to be able to read code snippets and understand what they do.

Let me give you specific advice on the language choice. If you work with Python regularly, choose Python. Python code on the exam typically involves importing SDK packages, creating client objects, calling methods, and processing results. The code is usually 10 to 30 lines and follows predictable patterns.

If you work with C# regularly, choose C#. The C# code follows similar patterns but with C# syntax — using statements, var declarations, async/await patterns, and method chaining.

If you're comfortable with both, I'd recommend Python because the code is generally more concise and readable, and most Azure AI SDK examples in Microsoft documentation use Python.

Here's what code questions look like: they might show you a function that creates an AI client, calls an analysis method, and processes the results, with one or two lines replaced by blanks. You need to fill in the missing code from a list of options. Or they might show you complete code and ask what the output would be. Or they might show you code with an error and ask you to identify the fix.

The question types include multiple choice (single answer and multiple answer), drag-and-drop ordering, hot area (click on the correct area of a diagram or code snippet), and case studies. Case studies present a scenario with multiple related questions. Here's an important tip: once you complete a case study section, you cannot go back to it. Make sure you've answered all questions in a case study before moving on.

## Using Microsoft Learn During the Exam

Yes, you can access Microsoft Learn during the exam. A split-screen view lets you browse documentation while answering questions. However, use this sparingly. Navigating to find a specific piece of information in Microsoft Learn takes time, and you don't have much to spare. Use it for looking up specific API parameters, service limits, or configuration details that you don't remember — not for learning new concepts.

The best strategy is to know the material well enough that you only need Microsoft Learn for confirming specific details. If you find yourself looking up every other question, you're not prepared enough.

Here's a practical tip for using Microsoft Learn during the exam. Before the exam, practice navigating Microsoft Learn so you know where things are. Bookmark key pages in your mind: the AI services container deployment page (for environment variable details), the SSML reference page (for element and attribute details), the Content Safety API reference (for severity levels), the AI Search query syntax page (for OData filter syntax), and the Document Intelligence model reference (for file size limits). When you do look something up, go directly to these pages rather than searching broadly.

Also, be aware that Microsoft Learn during the exam is the documentation website, not a search engine or AI assistant. You can browse documentation pages, but you can't use forums, Q&A sites, or external resources. The documentation is comprehensive but not always easy to navigate quickly, so use it as a last resort for specific factual details, not for learning concepts.

## What the Exam Loves to Test

Based on the exam objectives and common feedback, here are the topics that appear most frequently.

Service limits are explicitly tested. Know the file size limits for every service: 4 megabytes for Image Analysis, 6 megabytes for Custom Vision images, 25 megabytes for real-time speech recognition, 1 gigabyte for batch transcription, 4 megabytes for Document Intelligence free tier, 500 megabytes for standard tier, 2 gigabytes for Video Indexer, and 16 megabytes for AI Search push API documents. These numbers come up again and again.

Managed identity is usually the correct answer for authentication questions. When the exam asks "What is the recommended way to authenticate an Azure App Service to an AI service?", the answer is managed identity with DefaultAzureCredential, not API keys.

The three container environment variables — ApiKey, Billing, and Eula — are tested frequently. Know them cold.

SSML elements and attributes are heavily tested. The exam goes into specific details about prosody rates, say-as interpret-as values, and voice styles. Study the SSML section thoroughly.

Chat completions parameters — temperature, top_p, max_tokens, frequency_penalty, and presence_penalty — are tested individually. Know what each one does and its valid range.

Content Safety severity levels (0, 2, 4, 6) and the four categories (Hate, Violence, Sexual, Self-Harm) come up regularly.

Synonyms in Document Intelligence and Custom Question Answering are tested. Synonyms in Document Intelligence allow different field names to be recognized as the same field. In Custom Question Answering, synonyms ensure that different terms are treated as equivalent during matching. The exam might ask about configuring synonyms for improved accuracy in either service.

OData filter syntax for AI Search queries is tested. Know the difference between eq, gt, ge, lt, le, ne, and the any/all collection operators.

The difference between NER and entity linking is a classic trap question.

Prebuilt versus custom model decisions across services (Vision, Language, Document Intelligence) are scenario-based favorites.

Let me add a few more heavily-tested areas that catch people off guard.

The async polling pattern for Document Intelligence and other long-running operations is tested in code questions. Know that you POST a request, get a 202 with Operation-Location header, then GET that URL repeatedly until status is "succeeded." In SDK code, this becomes a "begin_" method that returns a poller, and you call result() on the poller.

Azure AI Search tier limitations are tested. The Free tier has significant limits: 3 indexes, 50 megabytes storage, 10,000 documents. Know that semantic search requires at least the Basic tier. Vector search is available on all tiers.

The Translator service's unique characteristics are tested. Unlike most Cognitive Services that use the cognitiveservices.azure.com domain, the Translator uses api.cognitive.microsofttranslator.com. Also, when creating a Translator resource for document translation, you need a single-service Translator resource with a custom domain (not a multi-service resource).

Batch and rate limits across services are sometimes tested. Text analytics processes up to 25 documents per batch. Custom Vision needs at least 15 images per tag. CLU needs at least 10 utterances per intent. Document Intelligence Free tier processes only 2 pages. These minimums and maximums come up in scenario questions.

Service endpoint patterns differ across services, and the exam tests whether you can identify which service an endpoint belongs to. If the URL contains cognitiveservices.azure.com/language, it's Azure AI Language. If it contains openai.azure.com, it's Azure OpenAI. If it contains search.windows.net, it's Azure AI Search. If it contains cognitiveservices.azure.com/computervision, it's Azure AI Vision. If it contains cognitiveservices.azure.com/formrecognizer, it's Document Intelligence. If it contains cognitiveservices.azure.com/contentsafety, it's Content Safety. If it contains stt.speech.microsoft.com or tts.speech.microsoft.com, it's Azure AI Speech.

## Key Tips for Test Day

Start with the questions you're confident about. Don't spend too long on any single question — mark it for review and come back. Many questions can be eliminated down to two choices, and a careful re-read often reveals the answer.

Read the question carefully. Microsoft exams are notorious for nuanced wording. "Most cost-effective" is different from "fastest to implement." "Requires the least administrative effort" is different from "provides the most control." Pay attention to these qualifiers.

For "choose two" or "choose three" questions, make sure you select the right number of answers. Some candidates miss points by selecting too few.

For code questions, trace through the code line by line. Don't assume you know what it does — read it carefully. Look for subtle details like which API version is being called or which parameters are set.

If you've built at least one end-to-end solution using these Azure AI services, many of the questions will feel intuitive. Hands-on experience is the best preparation for scenario-based questions.

Here are some additional test-taking strategies that can make the difference between passing and failing.

First, manage your time ruthlessly. With 58 questions in 120 minutes, you have roughly 2 minutes per question on average. Simple multiple-choice questions should take about a minute. Complex scenario questions and case studies might take 3 to 5 minutes. Mark difficult questions for review and come back to them if you have time. It's better to answer all questions quickly and come back to review than to spend 10 minutes on one question and run out of time for others.

Second, use the process of elimination aggressively. Microsoft exam questions typically have four answer choices. If you can eliminate two, you have a 50-50 chance even if you're guessing. Look for obviously wrong answers first. An answer that suggests using a deprecated service is wrong. An answer that stores API keys in plain text code is almost always wrong (managed identity is the better choice). An answer that uses the wrong service for the scenario is wrong.

Third, watch for "distractor" answers. These are choices that sound plausible but have a subtle issue. For example, a choice might suggest the right service but with the wrong SKU, or the right approach but with an unnecessary extra step. Read each choice completely before selecting.

Fourth, for case study questions, read the requirements and architecture diagrams carefully. Take notes on key details before answering the questions. Case study questions often reference specific details from the scenario — a specific region, a specific security requirement, a specific data source. Missing these details leads to wrong answers.

Fifth, understand that some questions are "unscored" — they're being piloted for future exams. You won't know which ones are unscored, so treat every question seriously. But this means that getting a few questions wrong doesn't necessarily fail you.

Sixth, if you're torn between two answers and one involves managed identity or DefaultAzureCredential, it's probably the right one. Microsoft strongly favors managed identity in exam answers. Similarly, if one answer suggests storing keys in code and another suggests Key Vault, Key Vault is almost always correct.

Seventh, pay attention to the verb in the question. "Which service should you use?" is asking about service selection. "How should you configure?" is asking about specific settings or parameters. "What should you do first?" is asking about the correct sequence of steps. These different verbs require different types of answers.

## Build at Least One End-to-End Solution

If I could give only one piece of study advice, it would be this: build something real. Create an application that uses multiple Azure AI services together. For example, build a document search application that uses Document Intelligence to extract text from PDFs, Azure AI Search to index the content, Azure OpenAI with RAG to answer questions, and Content Safety to moderate outputs.

The act of building forces you to understand how services connect, how authentication flows work, what the API responses look like, and where things can go wrong. It transforms abstract knowledge into practical understanding, which is exactly what the exam tests.

Here's a concrete project idea that touches multiple exam domains and would give you excellent preparation. Build a "smart document search" application.

Step one (Domain 1): Create an Azure resource group with a multi-service Cognitive Services resource, an Azure OpenAI resource, an AI Search resource, and a Document Intelligence resource. Use Bicep or CLI to provision everything. Configure managed identity on an App Service to access all resources.

Step two (Domain 6): Upload sample documents (PDFs, images with text) to blob storage. Create a Document Intelligence pipeline to extract structured data from invoices and receipts. Set up an AI Search indexer with a skillset that includes OCR, entity recognition, key phrase extraction, and language detection.

Step three (Domain 2): Deploy a GPT-4o model and an embedding model in Azure OpenAI. Generate embeddings for your indexed content. Implement the RAG pattern — query AI Search to find relevant documents, include them in the prompt, and generate grounded responses. Test with different temperature and top_p settings to see the effect.

Step four (Domain 5): Add speech input to your application using speech-to-text, so users can ask questions by voice. Add SSML-powered speech output so the system reads answers back with appropriate prosody and emphasis. Add multilingual support using the Translator service.

Step five (Domain 4): Add image analysis to handle uploaded images — extract text via OCR, generate captions and tags, and include the extracted information in your search index.

Step six (Domain 1 again): Implement Content Safety to moderate user inputs and AI outputs. Configure diagnostic settings for monitoring. Set up alerts for error rates and high token usage.

This single project touches all six domains and gives you hands-on experience with the services, SDKs, and patterns that the exam tests. Even building half of this would put you in a much better position than studying theory alone.

## Top Resources for Final Preparation

The Microsoft Learn free practice assessment is available at the official exam page. Take it multiple times. The questions change each time, and it gives you a good feel for the exam format and difficulty.

The official Microsoft Learn learning paths for AI-102 cover all domains and include hands-on exercises.

The AI-102 study guide, available at aka.ms/ai102-StudyGuide, lists every objective with links to relevant documentation.

Azure AI Services documentation at learn.microsoft.com is your authoritative reference for API details, limits, and configuration.

And of course, hands-on practice in the Azure portal and with the SDKs is irreplaceable.

Let me give you a structured final prep plan for the last week before the exam.

Day one and two: Take the Microsoft Learn practice assessment. Note every question you get wrong. Group your wrong answers by domain.

Day three: Focus on your weakest domain. If you struggled with AI Search queries, spend the day on OData filter syntax and Lucene queries. If you struggled with SSML, spend the day reviewing every element and attribute. Deep dive into the specific areas where you had gaps.

Day four: Do a hands-on lab session. Deploy at least one service and make API calls. Try deploying a container with the three environment variables. Try creating a simple AI Search index with a skillset. Try calling the Content Safety API. The physical act of doing these tasks cements the knowledge in a way that reading cannot.

Day five: Review file size limits for all services. Review the difference between NER and entity linking. Review Content Safety severity levels. Review SSML prosody attributes. Review chat completions parameters. These are the high-frequency exam topics that benefit from last-minute review.

Day six: Take the practice assessment again. You should score higher this time. Review any remaining gaps.

Day seven: Light review only. Read through your notes. Get a good night's sleep. Trust your preparation.

On exam day, arrive early (or set up your testing environment early for online proctored exams). Read each question completely before looking at the answers. Eliminate obviously wrong choices first. Trust your first instinct unless you have a specific reason to change your answer. And remember: you don't need to get every question right. A score of 700 out of 1000 passes, and some questions are unscored pilot items. Focus on demonstrating your knowledge, not achieving perfection.

---

# Summary and Key Takeaways

Let's wrap up with a one-paragraph summary of each domain and the top things to remember.

## Domain Summaries

Domain one, Plan and Manage, is about knowing the Azure AI service landscape, being able to select the right service for each scenario, provisioning resources through the portal, CLI, and Bicep, and securing and monitoring your deployments. The key themes are service selection, multi-service versus single-service resources, container deployment with the three magic environment variables, authentication with managed identity and Key Vault, monitoring with diagnostic settings and Log Analytics, and responsible AI with Content Safety severity levels and prompt shields. This is the largest domain and the foundation for everything else. When you sit down for the exam, expect multiple questions on service selection — they'll give you a business scenario and ask which Azure AI service is the best fit. Also expect questions on security best practices (managed identity wins almost every time), container deployment details (the three environment variables: ApiKey, Billing, Eula), and Content Safety configuration including the four-level severity scale. Cost management questions focus on choosing the right tier, monitoring token usage for OpenAI, and using Azure Cost Management for tracking. The monitoring questions ask about setting up diagnostic settings, creating Log Analytics queries, and configuring alerts for operational metrics.

Domain two, Generative AI, centers on Microsoft Foundry and Azure OpenAI. You need to understand the hub-and-project organizational model, how to deploy and configure models, the chat completions API with all its parameters, token management, the RAG pattern for grounding models in your data, DALL-E for image generation, prompt engineering techniques, and fine-tuning workflows. The chat completions parameters and the RAG pattern are the most heavily tested topics in this domain. Expect questions that show you a set of parameters and ask what behavior they produce — like "If temperature is set to 0 and max_tokens is set to 100, what kind of output should you expect?" The answer would be deterministic output limited to 100 tokens. Also expect questions on the RAG flow — chunking, embedding, indexing, retrieval, and prompt construction. Understand that fine-tuning is for behavior customization (style, format, tone) while RAG is for knowledge augmentation (giving the model access to your specific data). Model evaluation metrics like groundedness, relevance, coherence, and fluency are also testable — know what each measures and when each is most important.

Domain three, Agentic Solutions, is the smallest domain but represents the future of AI engineering. Agents are autonomous systems that use tools to accomplish complex tasks. You need to understand the Agent Service versus Agent Framework distinction, the three tool types (code interpreter, file search, function calling), multi-agent orchestration patterns, and agent safety considerations. Focus on conceptual understanding rather than deep implementation details. The exam tests at a higher level here — which tool is appropriate for a scenario, when to use Agent Service versus Agent Framework, and how multi-agent orchestration works conceptually. Don't expect deep code-level questions on agent implementation, but do know the API flow: create agent, create thread, add message, create run, retrieve response. Understand that code interpreter runs Python in a sandbox, file search provides RAG over uploaded files, and function calling lets agents interact with external systems.

Domain four, Computer Vision, covers image analysis, OCR, custom vision models, and video analysis. Key topics include the Image Analysis 4.0 visual features, the Read API for text extraction, the classification versus object detection decision, Custom Vision training workflow and evaluation metrics (precision, recall, AP), the code-first approach to building models, Video Indexer capabilities, and the file size limits for each service. The file limits are explicitly tested. Expect questions about what the Image Analysis API returns (tags, captions, objects, read text), when to use Custom Vision versus the built-in Image Analysis, the training requirements (minimum 15 images per tag), and how to evaluate model quality. The code-first approach — building a Custom Vision model entirely through SDK calls without using the portal — is a specific exam objective. Video Indexer questions typically ask about which insights it can extract (transcripts, faces, topics, emotions, OCR, brands) and its file limits (2 gigabytes, 4 hours).

Domain five, NLP, is the deepest domain covering text analytics, translation, speech, SSML, CLU, and question answering. The most critical topics are the text analytics capabilities (sentiment, NER, key phrases, PII, language detection), entity linking versus NER, the Translator service (text, document, custom), speech-to-text and text-to-speech, and especially the SSML deep dive — know every element, attribute, and value. CLU concepts (intents, entities, utterances) and Custom Question Answering (knowledge bases, multi-turn, chit-chat) round out this domain. This domain has the widest breadth of any on the exam. SSML alone could generate multiple questions — they might show you SSML markup and ask what it produces, or ask you to identify the correct SSML element for a requirement. CLU questions test the training workflow, evaluation metrics, and the difference between entity types. Custom Question Answering questions focus on knowledge base creation from multiple sources, multi-turn configuration, alternate phrasings, and chit-chat personalities. Translation questions might compare text translation, document translation, and custom translation, asking when each is appropriate.

Domain six, Knowledge Mining, covers Azure AI Search, Document Intelligence, and Content Understanding. For AI Search, master the index schema concepts (field types and attributes), the indexer pipeline, built-in and custom skills, knowledge store projections, and query syntax including OData filters and Lucene operators. For Document Intelligence, know the prebuilt models, custom models, composed models, the async analysis pattern, and file size limits. For Content Understanding, understand its role as a general-purpose content processing service versus the more specialized Document Intelligence. AI Search questions are often the most technically detailed on the exam — they might show you an index schema and ask what queries are possible, or show you a query and ask what results it returns. They might describe an enrichment requirement and ask which skill to use. Document Intelligence questions focus on choosing between prebuilt and custom models, understanding the async polling pattern, knowing the file size limits, and understanding composed models. Content Understanding questions are lighter, typically asking when to use it versus Document Intelligence.

## Top Ten Things to Remember

One: Managed identity with DefaultAzureCredential is the recommended authentication method for production Azure applications accessing AI services. When in doubt, choose managed identity. The exam consistently favors managed identity over API keys for production scenarios. If you see a question about how an App Service, Function App, or Container App should authenticate to an AI service, managed identity is almost always correct. DefaultAzureCredential from the Azure Identity SDK is the specific class that implements this pattern — it works with managed identity in Azure and falls back to developer credentials locally.

Two: The three container environment variables are ApiKey, Billing, and Eula (set to "accept"). Every Azure AI container requires all three to start. If any one is missing, the container fails. ApiKey is your Azure resource's key for billing authentication. Billing is the endpoint URL (like https://myresource.cognitiveservices.azure.com). Eula must literally be set to the word "accept" to acknowledge the license terms. These three variables show up in questions about Docker commands, container deployments, and Azure Container Instances configurations.

Three: Content Safety severity levels are 0 (safe), 2 (low), 4 (medium), and 6 (high), across four categories: Hate, Violence, Sexual, and Self-Harm. Note the values skip odd numbers — they're 0, 2, 4, 6, not 0 through 6. When you configure content filters, you set a threshold: reject anything at or above a certain severity. Strict blocks at 2 or above, moderate at 4 or above, lenient at 6 only. Each category is scored independently, and you can set different thresholds per category.

Four: SSML elements to know cold are voice (select voice), prosody (rate, pitch, volume), break (pause), emphasis (stress), say-as (pronunciation control with interpret-as values), and mstts:express-as (speaking styles). The prosody element's rate attribute accepts x-slow, slow, medium, fast, x-fast, or percentages. The say-as interpret-as attribute accepts date, time, telephone, cardinal, ordinal, characters, and address. The mstts:express-as style attribute accepts values like cheerful, sad, angry, excited, and friendly. These specific values are what the exam tests.

Five: Chat completions parameters — temperature controls randomness (0 to 2), top_p is nucleus sampling (0 to 1, don't combine with temperature), max_tokens limits output length, frequency_penalty reduces repetition (-2 to 2), and presence_penalty encourages topic diversity (-2 to 2). Remember: temperature 0 is deterministic, temperature 2 is maximum creativity. max_tokens controls the OUTPUT only, not the input. And the golden rule: don't adjust both temperature and top_p at the same time — pick one.

Six: File size limits are explicitly tested. The critical ones are 4 megabytes for Image Analysis, 4 megabytes or 500 megabytes for Document Intelligence (free versus standard), 6 megabytes for Custom Vision, 25 megabytes for real-time speech REST, 1 gigabyte for batch transcription, and 2 gigabytes for Video Indexer. Also know the page limits: 2 pages for Document Intelligence Free tier, 2,000 for Standard. And minimum training data: 15 images per tag for Custom Vision, 10 utterances per intent for CLU, 5 labeled documents for custom template models in Document Intelligence.

Seven: The RAG pattern involves chunking documents, generating embeddings, storing in a search index, generating a query embedding at search time, retrieving relevant chunks, and including them in the language model prompt. Know this flow end to end. The key components are an embedding model (like text-embedding-ada-002), a search index (Azure AI Search), and a language model (like GPT-4o). The search can be vector, keyword, or hybrid. The retrieved context is included in the system message or user message. The instruction to only use provided context is crucial for reducing hallucination.

Eight: Entity linking connects entities to Wikipedia articles for disambiguation. Named entity recognition categorizes entities by type. These are different capabilities and the exam tests the distinction. NER tells you "Washington" is a Location. Entity linking tells you it's Washington, D.C. — and provides the Wikipedia URL. If the question asks about disambiguation or connecting to a knowledge base, the answer is entity linking.

Nine: Azure AI Search query syntax includes $filter for OData expressions, $select for field selection, $orderby for sorting, $top and $skip for pagination, queryType "full" for Lucene syntax (wildcards, fuzzy, proximity, boosting), and queryType "semantic" for AI-ranked results. For filtering, know the eq, gt, ge, lt, le, ne operators, the and/or/not logical operators, and the any/all collection operators. For Lucene, know phrase search (quotes), wildcards (asterisk and question mark), fuzzy (tilde with edit distance), and boosting (caret with factor).

Ten: Build at least one end-to-end solution before taking the exam. Hands-on experience transforms memorized facts into practical understanding, and the exam is heavily scenario-based. Even a simple application that chains together Azure AI Search with Azure OpenAI for RAG, adds Content Safety for moderation, and uses managed identity for authentication will give you invaluable practical context. The exam tests real-world scenarios, and nothing prepares you for those like building real-world solutions.

## Bonus: Quick-Fire Review Questions

Let me close with some rapid-fire review questions to test your knowledge. See if you can answer each one before I give the answer.

Question: What are the three required Docker environment variables for Azure AI containers? Answer: ApiKey, Billing, and Eula set to accept.

Question: What is the maximum file size for Image Analysis 4.0? Answer: 4 megabytes.

Question: What Content Safety severity level represents "medium risk"? Answer: 4.

Question: Which parameter should you NOT combine with temperature? Answer: top_p. Don't adjust both simultaneously.

Question: What is the minimum number of training images per tag in Custom Vision? Answer: 15, though 50 or more is recommended.

Question: What is the difference between NER and entity linking? Answer: NER categorizes entities by type. Entity linking disambiguates entities and connects them to Wikipedia articles.

Question: How many pages can Document Intelligence Free tier process per invocation? Answer: 2 pages.

Question: What RBAC role should you assign to an application that only needs to call AI service prediction APIs? Answer: Cognitive Services User.

Question: In SSML, which element controls the speed, pitch, and volume of speech? Answer: The prosody element.

Question: What is the maximum video duration for Azure AI Video Indexer? Answer: 4 hours.

Question: What search type requires at least the Basic tier of Azure AI Search? Answer: Semantic search.

Question: What authentication header do most Cognitive Services use? Answer: Ocp-Apim-Subscription-Key.

Question: What authentication header does Azure OpenAI use? Answer: api-key.

Question: In a CLU project, what is the minimum number of utterances per intent? Answer: 10.

Question: What fine-tuning data format does Azure OpenAI require? Answer: JSONL, which is JSON Lines format.

Question: What are the three types of knowledge store projections? Answer: Table, object, and file projections.

Question: What is the maximum composed model size in Document Intelligence Standard tier? Answer: Up to 200 sub-models.

Question: What SSML element would you use to make the synthesizer spell out letters individually? Answer: say-as with interpret-as set to characters.

Question: In Azure AI Search, what does the facetable field attribute enable? Answer: Faceted navigation — showing value counts for filtering, like product categories with result counts.

Question: What is the recommended authentication method for production Azure applications accessing AI services? Answer: Managed identity with DefaultAzureCredential.

If you got most of these right, you're in good shape for the exam. If you missed several, go back and review those specific topics. Use these questions as a diagnostic tool to identify your remaining gaps.

That's it. You've now heard a comprehensive walkthrough of every major topic on the AI-102 exam. Go build something, take the practice assessment, review the areas where you're weakest, and then go pass that exam. Good luck.

---

*This audio study guide is based on the AI-102 skills measured as of December 23, 2025, with Microsoft Foundry branding. The exam retires June 30, 2026. Always check the official Microsoft exam page for the most current objectives.*

## Final Thoughts

As you finish listening to this guide, remember that the AI-102 exam is fundamentally about making decisions. Which service to use, which authentication method to implement, which deployment type to choose, which model to train, which query syntax to write. Every question on the exam presents a scenario and asks you to make the best decision.

The way to prepare for decision-making questions is not just memorization — it's understanding the trade-offs. Why is managed identity better than API keys? Because it eliminates credential management, reduces the risk of key leakage, and simplifies key rotation. Why is RAG better than fine-tuning for incorporating company data? Because data changes frequently and RAG doesn't require retraining, provides source attribution, and is cheaper to maintain.

If you understand the "why" behind each best practice, you can reason through unfamiliar scenarios on the exam. If you only memorize the "what," you'll struggle when the exam presents scenarios you haven't seen before.

The Azure AI landscape is evolving rapidly. Services get renamed (Form Recognizer became Document Intelligence, Azure AI Studio became Microsoft Foundry), new capabilities are added (agents, Content Understanding, vector search), and best practices evolve. But the fundamental patterns remain stable: provision resources, authenticate securely, call APIs, process results, monitor performance, and implement responsible AI practices.

These patterns are what the AI-102 exam ultimately tests. Master the patterns, understand the services, practice with hands-on labs, and you'll be well-prepared to pass.

Thank you for listening to this guide. Now go build something amazing with Azure AI, and good luck on your exam.

---

*End of AI-102 Audio Study Guide*
*Total exam objectives covered: 72*
*Domains covered: 6 of 6*
*Version: December 23, 2025 skills measured*

## Acknowledgments and Additional Notes

This study guide was created as a companion to the AI-102 certification preparation course materials. It draws from the official Microsoft exam objectives, the AI-102 study guide, Microsoft Learn documentation, and practical hands-on experience with Azure AI services.

Remember that Azure AI services are continuously evolving. While the core concepts tested on the exam remain stable, specific features, API versions, and service names may change. Always verify current documentation when implementing solutions in production.

The AI-102 exam represents a snapshot of the Azure AI platform at a specific point in time. As of the December 2025 skills update, the exam reflects the Microsoft Foundry branding, the addition of agentic solutions, the integration of Content Understanding, and the evolution of vector and hybrid search in Azure AI Search. These represent the latest trends in enterprise AI engineering.

Whether you're listening to this guide on your first pass or your fifth review, I hope it's given you a comprehensive understanding of what to expect on exam day. The combination of conceptual knowledge, practical experience, and exam strategy will give you the best chance of success.

Good luck, future Azure AI Engineer Associate!

One last thing: if you're using this guide with text-to-speech technology to actually listen to it as audio, the total listening time at natural speech speed (about 120 to 150 words per minute) will be approximately four to five and a half hours. That's about right for a comprehensive exam prep guide — similar to an audiobook. Consider breaking it into sessions: listen to two or three chapters per day over a week, reviewing the practice questions at the end. Repetition builds retention, and hearing the material multiple times will help you internalize the concepts for exam day.
