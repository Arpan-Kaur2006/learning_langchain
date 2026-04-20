# 🧠 LangChain + Gemini Prompt Engineering Demo

## 📌 Overview

This project demonstrates how to use **LangChain with Google's Gemini API** to build a structured and reusable prompt pipeline.

It focuses on:

* Prompt Engineering
* Prompt Templates
* LangChain Chains

---

## ⚙️ How It Works

1. A **PromptTemplate** is created with a variable `{topic}`.
2. The template is combined with the LLM using a **chain (`|`) operator**.
3. Input is passed dynamically using a dictionary.
4. The LLM generates a structured response.

---

## 💻 Code Explanation

* `ChatGoogleGenerativeAI` → connects LangChain to Gemini API
* `PromptTemplate` → creates reusable prompts
* `chain = prompt | llm` → builds a pipeline
* `invoke()` → executes the pipeline
* `.content` → extracts the final response

---

## 🚀 Example Output

Input:

```
topic = "dogs"
```

Output:

* Dogs are loyal animals
* They are commonly kept as pets

---

## 🔐 Note

API keys are managed using environment variables (`os.getenv`) for security and should not be hardcoded.

---

## 📚 Learning Outcome

This project builds a foundation for:

* RAG systems
* AI agents
* Automated research tools
