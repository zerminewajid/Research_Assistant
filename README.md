---
title: Research Assistant
emoji: 🔬
colorFrom: gray
colorTo: blue
sdk: docker
pinned: false
---
# 🔬 AI Research Assistant

> **Multi-Agent RAG System** — Research any paper topic and get an AI-generated report with an interactive visualization demo.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-black?style=flat-square&logo=flask)
![CrewAI](https://img.shields.io/badge/CrewAI-1.11-orange?style=flat-square)
![LangGraph](https://img.shields.io/badge/LangGraph-0.2-green?style=flat-square)
![FAISS](https://img.shields.io/badge/FAISS-Vector_DB-purple?style=flat-square)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.1-red?style=flat-square)

---

## 🚀 Live Demo

🔗 **[Try it here →]([https://your-render-link.onrender.com](https://huggingface.co/spaces/zermeenewajid/research-assistant))**

---

## 🧠 What It Does

Enter any research paper topic → 3 AI agents collaborate to research, write, and review a full report → an interactive visualization demo is generated if the topic matches a known AI/ML domain.

**Works for any domain** — AI, economics, biology, social science, etc. If no demo is available for a topic, nothing is shown.

---

## 🏗️ Architecture

```
User Input (Topic)
        ↓
   Flask REST API  (/research)
        ↓
   LangGraph State Machine
   ┌────────────────────────────────┐
   │  Researcher Agent  (CrewAI)    │  ← searches FAISS vector store
   │          ↓                     │
   │  Writer Agent      (CrewAI)    │  ← structures the report
   │          ↓                     │
   │  Critic Agent      (CrewAI)    │  ← reviews + finalizes
   └────────────────────────────────┘
        ↓
   /detect-demo endpoint
        ↓
   LLM decides if interactive demo is appropriate
        ↓
   JSON response → Browser renders report + demo
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Web Server** | Flask 3.0 |
| **Agent Framework** | CrewAI 1.11 |
| **Pipeline Orchestration** | LangGraph 0.2 |
| **Vector Database** | FAISS (local, CPU) |
| **Embeddings** | HuggingFace `all-MiniLM-L6-v2` |
| **LLM** | Groq `llama-3.1-8b-instant` (free) |
| **Frontend** | Vanilla HTML/CSS/JS + Canvas API |

---

## 🎮 Interactive Demos

The app uses the LLM itself to detect whether an interactive demo is appropriate for the topic — no hardcoded keywords. Supported visualizations:

| Topic | Demo |
|-------|------|
| Transformers / Attention | Self-attention token visualizer |
| CNN / Computer Vision | Convolutional feature map drawer |
| LSTM / GRU / RNN | Gate mechanism slider |
| Federated Learning | FedAvg round simulator |
| RAG / Vector Search | Semantic similarity ranker |
| MLOps / Deployment | Pipeline stage tracker |
| Any other domain | No demo (null output) |

---

## 🛠️ Local Setup

```bash
# 1. Clone
git clone https://github.com/zerminewajid/Research_Assistant.git
cd Research_Assistant

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add API key
cp .env.example .env
# Add your Groq key: https://console.groq.com/keys

# 5. Run
python app.py
# Visit http://localhost:5000
```

---

## 📁 Project Structure

```
Research_Assistant/
├── app.py                  # Flask server + API endpoints
├── pipeline/
│   ├── agents.py           # CrewAI agent definitions
│   ├── graph.py            # LangGraph state machine
│   └── state.py            # Pipeline state schema
├── rag/
│   └── vectorstore.py      # FAISS vector store
├── templates/
│   └── index.html          # Frontend (UI + interactive demos)
├── requirements.txt
└── .env.example
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Serves the web UI |
| `POST` | `/research` | Runs the 3-agent pipeline |
| `POST` | `/detect-demo` | LLM decides if demo is appropriate |

---

## 👩‍💻 Author

**Zermine Wajid**
BS Artificial Intelligence — GIK Institute of Engineering Sciences and Technology (GIKI)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin)]([https://linkedin.com/in/yourprofile](https://www.linkedin.com/in/zermine-wajid-a206b01b9/))
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat-square&logo=github)]([https://github.com/zerminewajid](https://github.com/zerminewajid))

---

## ⭐ If you found this useful, give it a star!
