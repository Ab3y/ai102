# AI-102 Self-Paced Training Course

**Developing Solutions for Microsoft Azure AI**

---

## Course Overview

| Attribute | Details |
|-----------|---------|
| **Certification** | Microsoft Certified: Azure AI Engineer Associate |
| **Exam Code** | AI-102 |
| **Passing Score** | 700 / 1000 |
| **Duration** | 120 minutes, ~58 questions |
| **Prerequisite** | Azure fundamentals + proficiency in Python or C# |
| **Format** | Multiple choice, case studies, drag-and-drop, code fill-in |
| **Important** | You choose Python or C# at the start of the exam — you **cannot switch** mid-exam |

This self-paced course is organized into **6 modules** aligned with the AI-102 exam domains. Each module contains lessons, knowledge checks, hands-on labs, and exam tips.

---

## Exam Domain Weights

| # | Domain | Weight | Module |
|---|--------|--------|--------|
| 1 | Plan and Manage an Azure AI Solution | 15–20% | [Module 1](module-1-plan-manage/overview.md) |
| 2 | Implement Generative AI Solutions | 15–20% | [Module 2](module-2-generative-ai/overview.md) |
| 3 | Implement Agentic AI Solutions | 5–10% | [Module 3](module-3-agentic-solutions/overview.md) |
| 4 | Implement Computer Vision Solutions | 15–20% | [Module 4](module-4-computer-vision/overview.md) |
| 5 | Implement Natural Language Processing Solutions | 25–30% | [Module 5](module-5-nlp/overview.md) |
| 6 | Implement Knowledge Mining and Document Intelligence Solutions | 10–15% | [Module 6](module-6-knowledge-mining/overview.md) |

---

## Recommended Study Plan

### Weeks 1–2: Plan & Manage (Module 1)
- [ ] Complete all lessons in Module 1
- [ ] Deploy Azure AI Services multi-service resource
- [ ] Configure authentication (keys, Entra ID, managed identity)
- [ ] Set up monitoring with Azure Monitor and diagnostic logging
- [ ] Configure content safety filters and responsible AI settings
- [ ] Implement network security (VNet, private endpoints)
- [ ] Score 80%+ on Module 1 knowledge check

### Weeks 3–4: Generative AI (Module 2)
- [ ] Complete all lessons in Module 2
- [ ] Deploy an Azure OpenAI Service resource and models (GPT, DALL-E, Whisper)
- [ ] Implement Retrieval-Augmented Generation (RAG) with Azure AI Search
- [ ] Build and orchestrate a project in Azure AI Foundry
- [ ] Fine-tune a model and evaluate performance
- [ ] Implement prompt engineering and system message patterns
- [ ] Score 80%+ on Module 2 knowledge check

### Week 5: Agentic Solutions (Module 3)
- [ ] Complete all lessons in Module 3
- [ ] Build an AI agent with Azure AI Agent Service
- [ ] Implement tool calling and function definitions
- [ ] Configure multi-agent orchestration workflows
- [ ] Score 80%+ on Module 3 knowledge check

### Weeks 6–7: Computer Vision (Module 4)
- [ ] Complete all lessons in Module 4
- [ ] Analyze images using Azure AI Vision (tags, captions, objects, people)
- [ ] Train a custom image classification / object detection model
- [ ] Implement Face API detection and verification
- [ ] Configure Azure Video Indexer for video analysis
- [ ] Implement optical character recognition (OCR)
- [ ] Score 80%+ on Module 4 knowledge check

### Weeks 8–9: Natural Language Processing (Module 5)
- [ ] Complete all lessons in Module 5
- [ ] Implement text analytics (sentiment, key phrases, entity recognition, PII detection)
- [ ] Configure speech-to-text and text-to-speech with Speech Services
- [ ] Build a Conversational Language Understanding (CLU) model
- [ ] Implement custom question answering
- [ ] Configure speech translation
- [ ] Score 80%+ on Module 5 knowledge check

### Weeks 10–11: Knowledge Mining & Document Intelligence (Module 6)
- [ ] Complete all lessons in Module 6
- [ ] Build an Azure AI Search index with built-in and custom skillsets
- [ ] Implement a knowledge store and enrichment pipeline
- [ ] Analyze documents with Azure AI Document Intelligence (prebuilt + custom models)
- [ ] Implement Azure AI Content Understanding
- [ ] Score 80%+ on Module 6 knowledge check

### Week 12: Final Prep
- [ ] Review all quick reference cards in [docs/quick-reference-cards.md](../docs/quick-reference-cards.md)
- [ ] Complete all practice questions in [docs/practice-questions.md](../docs/practice-questions.md)
- [ ] Re-take any knowledge checks where you scored below 80%
- [ ] Take the [official practice assessment](https://learn.microsoft.com/credentials/certifications/exams/ai-102/practice/assessment?assessment-type=practice&assessmentId=61)
- [ ] Schedule your exam

---

## How to Use This Course

### Each Module Contains

| Component | Description |
|-----------|-------------|
| **overview.md** | Module overview, learning objectives, key concepts |
| **Lessons** | Deep-dive content with architecture diagrams, SDK code samples, and decision matrices |
| **Knowledge Check** | 10–15 scenario-based questions per module with explanations |
| **Labs** | Hands-on exercises deploying real Azure AI resources |

### Study Approach

1. **Read the lesson** — understand the service capabilities and when to use each one
2. **Study the diagrams** — architecture patterns and data flows appear frequently on the exam
3. **Do the lab** — deploy real resources and write code against the SDKs
4. **Take the knowledge check** — identify gaps before moving on
5. **Review exam tips** — know the keyword patterns that signal specific answers

### Key Principle

> The AI-102 exam tests **implementation knowledge** — not just concepts but code patterns, API calls, and service configuration. Expect questions that show code snippets and ask you to fill in the correct SDK method, parameter, or configuration value.

---

## Prerequisites & Setup

### Required Knowledge
- Azure fundamentals (resource groups, subscriptions, RBAC)
- Proficiency in **Python** or **C#** (you will choose one for the exam)
- Basic REST API concepts (HTTP methods, JSON payloads, status codes)
- Familiarity with JSON and YAML configuration files

### Required Tools
- **Python 3.10+** with pip (or .NET 8 SDK if choosing C#)
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) 2.x
- [VS Code](https://code.visualstudio.com/) with extensions:
  - Python / C#
  - Azure Tools
  - REST Client
  - Jupyter
- Azure subscription (free trial or Pay-As-You-Go)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (for containerized AI services)
- [Git](https://git-scm.com/)

### Lab Cost Estimate
Most labs use Azure AI free tiers where available. Estimated cost for all labs: **$30–$60** if completed within 2–3 weeks and resources are deleted promptly.

> **Tip:** Create a dedicated resource group for each module and delete it when you finish the module's labs.

---

## Cross-Cutting Themes

These principles apply to EVERY module and EVERY exam question:

### Responsible AI
- Content safety filters are **on by default** for Azure OpenAI — know how to configure severity thresholds
- Transparency notes must be reviewed before deploying Face API, Speech, and other sensitive services
- Fairness, reliability, privacy, inclusiveness, and accountability — know the six Microsoft Responsible AI principles
- Content filtering categories: hate, sexual, violence, self-harm

### Managed Identity Pattern
Use managed identity for ALL service-to-service authentication. If a question offers managed identity as an option, it is almost always correct. Avoid key-based auth when managed identity is available.

### Microsoft Foundry Branding (December 2025 Update)
- **Azure AI Studio** is now **Azure AI Foundry**
- **Azure AI Studio projects** are now **Azure AI Foundry projects**
- **Azure AI Hub** is now **Azure AI Foundry hub**
- The exam may reference either name — they are the same service

### SDK vs REST API Patterns
- Know when the exam expects SDK code vs REST calls
- Python SDK packages: `azure-ai-vision`, `azure-cognitiveservices-speech`, `azure-ai-textanalytics`, `azure-search-documents`, `openai`, `azure-ai-formrecognizer`
- C# SDK namespaces: `Azure.AI.Vision`, `Microsoft.CognitiveServices.Speech`, `Azure.AI.TextAnalytics`, `Azure.Search.Documents`, `Azure.AI.OpenAI`, `Azure.AI.FormRecognizer`

### Prebuilt vs Custom Model Decisions
| Choose Prebuilt When | Choose Custom When |
|---------------------|--------------------|
| Standard use case (general text, common documents) | Domain-specific terminology or entities |
| Quick time to production | Higher accuracy needed for your data |
| No labeled training data available | Labeled training data is available |
| Budget or time constrained | Unique classification categories |

---

## Official Microsoft Learn Learning Paths

Complete these learning paths alongside each course module for the best results.

| # | Learning Path | Duration | Maps to |
|---|--------------|----------|---------|
| 1 | [Prepare to develop AI solutions on Azure](https://learn.microsoft.com/training/paths/prepare-for-ai-engineering/) | 2 hr | Module 1 |
| 2 | [Create and manage Azure AI Services](https://learn.microsoft.com/training/paths/provision-manage-azure-cognitive-services/) | 3 hr | Module 1 |
| 3 | [Develop Generative AI solutions with Azure OpenAI Service](https://learn.microsoft.com/training/paths/develop-ai-solutions-azure-openai/) | 4 hr | Module 2 |
| 4 | [Build AI apps and agents with Azure AI Foundry](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/) | 3 hr | Modules 2 & 3 |
| 5 | [Create computer vision solutions with Azure AI Vision](https://learn.microsoft.com/training/paths/create-computer-vision-solutions-azure-cognitive-services/) | 4 hr | Module 4 |
| 6 | [Develop natural language processing solutions](https://learn.microsoft.com/training/paths/develop-language-solutions-azure-ai/) | 5 hr | Module 5 |
| 7 | [Implement knowledge mining with Azure AI Search](https://learn.microsoft.com/training/paths/implement-knowledge-mining-azure-cognitive-search/) | 4 hr | Module 6 |
| 8 | [Document Intelligence and Content Understanding](https://learn.microsoft.com/training/paths/extract-data-from-forms-document-intelligence/) | 3 hr | Module 6 |

---

## Progress Tracker

| Module | Status | Knowledge Check Score | Labs Completed |
|--------|--------|----------------------|----------------|
| 1 — Plan and Manage | Not Started | ___% | ___ / ___ |
| 2 — Generative AI | Not Started | ___% | ___ / ___ |
| 3 — Agentic Solutions | Not Started | ___% | ___ / ___ |
| 4 — Computer Vision | Not Started | ___% | ___ / ___ |
| 5 — Natural Language Processing | Not Started | ___% | ___ / ___ |
| 6 — Knowledge Mining & Document Intelligence | Not Started | ___% | ___ / ___ |
| **Practice Assessment** | Not Taken | ___% | |
| **Exam Date** | _____________ | | |

> **Practice Assessment:** [Take the free Microsoft practice assessment](https://learn.microsoft.com/credentials/certifications/exams/ai-102/practice/assessment?assessment-type=practice&assessmentId=61) after completing all modules.

---

## External Resources

| Resource | Link |
|----------|------|
| AI-102 Exam Page | [Official Exam Page](https://learn.microsoft.com/credentials/certifications/exams/ai-102/) |
| AI-102 Study Guide | [aka.ms/AI102-StudyGuide](https://aka.ms/AI102-StudyGuide) |
| Free Practice Assessment | [Practice Assessment](https://learn.microsoft.com/credentials/certifications/exams/ai-102/practice/assessment?assessment-type=practice&assessmentId=61) |
| Exam Sandbox (try the format) | [aka.ms/examdemo](https://aka.ms/examdemo) |
| Azure AI Services Documentation | [learn.microsoft.com/azure/ai-services](https://learn.microsoft.com/azure/ai-services/) |
| Azure OpenAI Service Docs | [learn.microsoft.com/azure/ai-services/openai](https://learn.microsoft.com/azure/ai-services/openai/) |
| Azure AI Foundry Documentation | [learn.microsoft.com/azure/ai-studio](https://learn.microsoft.com/azure/ai-studio/) |
| Azure Architecture Center — AI | [learn.microsoft.com/azure/architecture/ai-ml](https://learn.microsoft.com/azure/architecture/ai-ml/) |
| Responsible AI Resources | [learn.microsoft.com/azure/ai-services/responsible-use-of-ai-overview](https://learn.microsoft.com/azure/ai-services/responsible-use-of-ai-overview/) |
| Microsoft Learning AI-102 Labs | [Lab Exercises](https://microsoftlearning.github.io/mslearn-ai-services/) |
| Microsoft Learning AI-102 Source | [GitHub Repository](https://github.com/MicrosoftLearning/mslearn-ai-services) |
