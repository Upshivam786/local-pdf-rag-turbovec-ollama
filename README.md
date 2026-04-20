# 🚀 Local PDF RAG System with TurboVec + Ollama

A fully local Retrieval-Augmented Generation (RAG) system that allows you to upload PDFs and query them using an LLM — without any external APIs.

---

## 🔥 Features

* 📄 Upload and query PDFs
* ⚡ Fast vector search using TurboVec (TurboQuant)
* 🧠 Local LLM inference with Ollama
* 🔍 Source-grounded answers with citations
* 🔒 Fully offline (privacy-first)

---

## 🧠 Architecture

PDF → Text → Chunking → Embeddings → TurboVec → Retrieval → LLM → Answer

---

## ⚙️ Setup

### 1. Clone repo

```bash
git clone https://github.com/YOUR_USERNAME/local-pdf-rag-turbovec-ollama.git
cd local-pdf-rag-turbovec-ollama
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install and run Ollama

```bash
ollama pull llama3.2
ollama serve
```

---

## 🚀 Run the app

```bash
streamlit run app.py
```

---

## 💡 Example Use Cases

* Resume analysis
* Research paper Q&A
* Private document search
* Knowledge base assistant

---

## 🧠 Key Learnings

* RAG systems depend more on retrieval than the model
* Chunking strategy impacts answer quality
* Local AI pipelines improve privacy and control
* Handling hallucinations requires strict prompting

---

## 📌 Future Improvements

* PDF text highlighting
* Hybrid search (keyword + vector)
* Persistent indexing
* Multi-document support

---

## ⭐ Tech Stack

* Python
* TurboVec (TurboQuant vector search)
* Sentence Transformers
* Ollama (LLM)
* Streamlit

---

## 🙌 Author

Shivam Upadhyay
