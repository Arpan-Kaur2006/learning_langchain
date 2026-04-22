# Agentic Research Assistant 🤖

An advanced AI-powered research engine built with **LangChain** and **Google Gemini**. This project moves beyond simple prompting to create a structured, "agentic" system capable of processing information into machine-readable formats.

## 🚀 Day 1 Progress: Structured Output Control
The core foundation of any agentic system is the ability to communicate with other software. Today, I successfully implemented **Structured Output Parsing**.

### Key Achievements:
* **LCEL Implementation:** Utilized LangChain Expression Language (LCEL) to chain Prompts, LLMs, and Parsers.
* **JSON Enforcement:** Engineered prompts to force the LLM to return valid JSON objects instead of unstructured text.
* **Data Integration:** Integrated `JsonOutputParser` to automatically convert LLM responses into Python dictionaries for seamless backend processing.

### Tech Stack:
* **Language:** Python 3.x
* **Framework:** LangChain
* **LLM:** Google Gemini 1.5 Flash (via `langchain-google-genai`)
* **Environment:** `python-dotenv` for secure API key management

## 🛠️ How it works
Current execution flow:
`Input (Topic) -> PromptTemplate -> Gemini LLM -> JsonOutputParser -> Python Dictionary`

---
*Next Step: Implementing Conversation Memory to handle multi-turn research dialogues.*
## 📅 Day 2: The Infinite Memory Update

### 🚀 Overview
Today, I moved the project from "Short-term memory" to **"Persistent Cloud Memory."** The assistant no longer forgets the conversation when the script is restarted.

### 🛠️ Tech Stack Added
- **Vector Database:** [Pinecone](https://www.pinecone.io/) (Serverless Cloud)
- **Embeddings:** `gemini-embedding-001`
- **Orchestration:** LangChain (VectorStore & Retrieval Chains)

### 🧠 Core Concepts Implemented
- **Semantic Retrieval:** Instead of keyword matching, the system uses high-dimensional math (vectors) to find related ideas in past conversations.
- **Fixed Context Overhead ($k=3$):** To prevent LLM context window overflow, the system only retrieves the top 3 most relevant interactions.
- **State Persistence:** Conversation state is stored in the cloud, allowing for cross-session continuity.

### 🧪 Verification Test
- **Test:** Told the AI about "Quantum Computing," restarted the script, and asked about "AI Research."
- **Result:** The AI successfully referenced the previous Quantum Computing session to provide a unified research context.