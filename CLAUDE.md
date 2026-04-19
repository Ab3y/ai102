# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is Abe's AI-102 (Azure AI Engineer Associate) certification study repository. Contains study materials, practice questions, hands-on labs (Python + C# + REST), Bicep IaC templates, and reference materials organized around 6 exam domains.

**Exam:** AI-102 — Designing and Implementing a Microsoft Azure AI Solution
**Skills measured version:** December 23, 2025 (Microsoft Foundry branding)
**Retires:** June 30, 2026

### Exam Domains

1. Plan and manage an Azure AI solution (20–25%)
2. Implement generative AI solutions (15–20%)
3. Implement an agentic solution (5–10%)
4. Implement computer vision solutions (10–15%)
5. Implement NLP solutions (15–20%)
6. Implement knowledge mining & info extraction (15–20%)

## Key Directories

- `course/` — Self-paced training course with 6 modules, lessons, and knowledge checks
- `docs/` — Exam objectives, practice questions, quick reference cards, reference architectures
- `infra/` — Bicep templates for provisioning Azure AI resources
- `scripts/python/` — Python SDK samples organized by AI service area
- `scripts/rest-api/` — REST API examples using .http files
- `scripts/powershell/` — Azure provisioning and management scripts
- `images/` — Architecture diagrams

## Commands

### Python SDK Samples
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows
pip install -r requirements.txt
python scripts/python/<area>/<script>.py
```

### Bicep Deployment
```bash
az deployment group create --resource-group ai102-labs-rg --template-file infra/<template>.bicep
```

### REST API Examples
Use VS Code REST Client extension with `.http` files in `scripts/rest-api/`.

## Technology Preferences

- **Language:** Python 3.10+ (primary), C# for selected scenarios
- **IaC:** Bicep (not ARM templates)
- **AI SDKs:** azure-ai-vision, azure-ai-textanalytics, azure-cognitiveservices-speech, openai, azure-search-documents, azure-ai-formrecognizer
- **Auth:** Managed identity everywhere, Key Vault for secrets
- **Containers:** Docker for AI Services containerized deployments

## Response Format Guidelines

1. Be **DECISIVE** — single best recommendation with justification
2. Be **OPINIONATED** — make strong technology choices based on the exam's expectations
3. End implementation responses with **three prioritized next steps**:
   - [IMMEDIATE] — Action to do now
   - [SHORT-TERM] — Follow-up within days
   - [LONG-TERM] — Strategic consideration
4. **CONTEXT EFFICIENCY** — bullet points over paragraphs, focus on actionable details

## Cross-Cutting Principles

Every code sample and lab should:
- Use managed identity (not API keys in code) where possible
- Include proper error handling and logging
- Reference the specific exam objective it maps to
- Follow Responsible AI principles (content safety, fairness)
- Include cleanup commands to avoid Azure charges

## Key Files

- `course/syllabus.md` — 12-week study plan with progress tracker
- `course/hands-on-labs.md` — Complete lab walkthrough index
- `docs/ai102-objective-domain.md` — Full exam objectives mapped to modules
- `docs/practice-questions.md` — 100+ scenario-based practice questions
- `docs/quick-reference-cards.md` — Service comparison cheat sheets
- `ai102-course-flow.md` — 6-segment instructor schedule
- `ai102-punchlist.md` — Teaching checklist per segment

## External Resources

- [AI-102 Exam Page](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-engineer/)
- [AI-102 Study Guide](https://aka.ms/ai102-StudyGuide)
- [Azure AI Services Docs](https://learn.microsoft.com/en-us/azure/ai-services/)
- [Azure OpenAI Docs](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [MS Learn AI-102 Course](https://learn.microsoft.com/en-us/training/courses/ai-102t00)
