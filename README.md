# Maternal Health Risk Prediction and Pregnancy Assistant Chatbot

An AI-driven decision-support system built to help healthcare workers identify high-risk pregnancies early, particularly in rural and resource-limited settings. The platform integrates a high-precision LightGBM classification model with an intelligent, locally-hosted LLM chatbot using Retrieval-Augmented Generation (RAG) to provide actionable, clinically aligned insights.

## Core Features

* **High-Risk Stratification:** Predicts maternal risk levels using clinically relevant inputs such as blood pressure, hemoglobin, BMI, blood sugar, and obstetric history.
* **Clinical Safety Optimization:** Fine-tuned specifically to maximize recall for high-risk cases to minimize false negatives.
* **Intelligent RAG Chatbot:** A locally hosted medical assistant trained on verified guidelines to assist healthcare workers with real-time query resolution.
* **Robust API Backend:** Fully validated endpoints for fast machine learning inference and streaming chat responses.

---

## Technical Stack

* **Machine Learning:** LightGBM, Scikit-learn, Pandas, NumPy
* **LLM and RAG Pipeline:** LangChain, FAISS (Vector DB), Qwen-3 (Fine-tuned on 1,500 medical Q&A pairs)
* **Backend and Validation:** FastAPI, Pydantic, Python
* **Frontend:** TypeScript

---

## Model Performance Metrics

The classification engine was trained and optimized with a primary focus on clinical safety (reducing missed high-risk cases):

| Metric | Value |
| :--- | :--- |
| **Accuracy** | 98.7% |
| **ROC-AUC** | 0.998 |
| **Recall (High-Risk)** | 98.9% |
| **Precision (High-Risk)** | 97.8% |

---

## System Architecture

1. **Risk Prediction Pipeline:** 
   Patient Vitals/History -> Pydantic Validation -> FastAPI Endpoint -> LightGBM Inference -> Risk Categorization and Confidence Score.
2. **Medical Assistant Chatbot:**
   User Query -> Embedding Generation -> FAISS Vector Search (20K+ Document Corpus) -> Context Injection -> Fine-Tuned Qwen-3 -> Actionable Response.

---

## Installation and Setup

### Prerequisites
* Python 3.9+
* Local environment capable of running quantized LLMs

### Setup Instructions

1. Clone the repository:
```bash
   git clone [https://github.com/yourusername/MaternalAI_backend.git](https://github.com/yourusername/MaternalAI_backend.git)
   cd MaternalAI_backend
