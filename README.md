# Custom_rag_ai_assistant
This project is to show how to fine-tune Gemma models without spending a dime on infrastructure during the dev phase.

An end-to-end, privacy-first Retrieval-Augmented Generation (RAG) web application engineered to transform chaotic business documents—PDFs, raw Excel spreadsheets, and internal operational policies—into clear, actionable change management strategies. 

Powered by Google Gemma's open-weights architecture and styled dynamically via Streamlit, this assistant serves as an enterprise-grade development lab designed to optimize small-to-medium business workflows safely.

---
## 🔒 The Enterprise Edge: Why Gemma Beats Custom GPTs

When deploying corporate AI solutions, the two biggest bottlenecks are usually **data privacy violations** and **unpredictable recurring API costs**. 

* **The Problem with Closed Solutions:** With traditional commercial setups like OpenAI's "Custom GPTs," an enterprise is forced to upload proprietary files, internal operational policies, and sensitive client logs directly to a public, third-party cloud.
* **The Gemma Solution:** By using open-weights models like Gemma, organizations can construct tailored AI systems that run **completely locally** or inside a ring-fenced, private, secure server environment. For risk-conscious businesses, this architecture eliminates data leakage risks entirely.

> 🛠️ **Zero-Cost Infrastructure Development:** This project leverages the Kaggle cloud environment as a powerful data science lab. By utilizing Kaggle's free access to dedicated cloud GPUs (such as NVIDIA T4 and P100 architectures), developers can parse raw business data, engineer Python pipelines, and validate Gemma models without spending a dime on infrastructure during the prototype and dev phases.

---

## 🧠 Architectural Framework: What is RAG?

This system is built using a **Retrieval-Augmented Generation (RAG)** architecture. Instead of relying solely on what the AI learned during its initial training, a RAG framework allows the model to dynamically look up facts from a custom pile of messy files (PDFs, Excel spreadsheets, compliance logs) in real time. 

It grounds the model's answers directly in your corporate data, eliminating "hallucinations" while ensuring your actual files never train a public model.

### Data Flow & Processing Pipeline

```text
┌─────────────────────────────┐      ┌─────────────────────────────┐      ┌─────────────────────────────┐
│    1. Kaggle Cloud Lab      │      │      2. Local Engine        │      │    3. Streamlit Frontend     │
│                             │      │                             │      │                             │
│ Handles heavy computation   │ ───> │ VS Code terminal bridges    │ ───> │ Interactive chatbot UI     │
│ and processes raw model     │      │ connections and executes    │      │ where end users drag & drop │
│ weights without local drain │      │ Python automation scripts.  │      │ files and trigger prompts.  │
└─────────────────────────────┘      └─────────────────────────────┘      └─────────────────────────────┘
```
---
## Features & File Intake Capabilities
Drop-and-Chat Interface: Instantly processes unstructured and messy business files including:

📋 CSV & Excel: Financial sheets, inventory logs, company rosters, and metrics.

📝 TXT & Documents: Standard operating procedures (SOPs), onboarding guidelines, and local business goals.

Smart Tokenization Slicing: Avoids common tensor errors by extracting structural keys directly into target execution arrays.

---
## Instructions for End Users
Follow these simple steps to run the application locally on your desktop machine:

1. Acquire your Secure API Routing Key
Navigate to Google AI Studio and log in with your credentials.

Click Get API Key in the upper-left navigation panel.

Select Create API Key in new project and copy the unique string generated.

2. Launch the Application Window
Open your local project directory terminal in VS Code and initialize the application server: python -m streamlit run app.py

3. Prompt and Analyze Data
Paste your secure Google API Key into the configuration input field hidden safely on the sidebar.

Type out your operational query in the main text box (e.g., Transitioning a boutique storefront from Excel logs to automated management tools).

Optional: Drag and drop your local spreadsheet or policy document directly into the upload bay.

Click Generate Strategy to stream your automated change management roadmap down your screen.
