# 🇧🇩 Multilingual RAG System (Bangla + English)
A simple Retrieval-Augmented Generation system that answers Bangla & English queries from an HSC Bangla 1st Paper PDF.

## 🛠 Used Tools
- PyPDF2 → PDF text extraction
- LangChain → Chunking
- ChromaDB → Vector storage
- Sentence Transformers → Multilingual embedding
- FastAPI → Simple REST API

## 🚀 How to Run (MacBook / Linux)
```bash
python3 -m venv rag-env
source rag-env/bin/activate
pip install -r requirements.txt
python app.py
```

## 💬 Sample Queries
| Query | Answer |
|-------|--------|
| অনুপমের ভাষায় সুপুরুষ কাকে বলা হয়েছে? | শম্ভুনাথ |
| বিয়ের সময় কল্যাণীর বয়স কত ছিল? | ১৫ বছর |

## ⚙️ Chunking Strategy
- Character-based chunks: 500 chars
- Overlap: 50 chars

## 🔍 Embedding Model
`distiluse-base-multilingual-cased-v2`

## ❓ Questions Answered
- Text extraction: PyPDF2
- Chunking: 500 chars with 50 overlap
- Embedding: Multilingual model (Bangla+English)
- Similarity: Cosine similarity via ChromaDB

## 🛜 Optional: Run API
```bash
uvicorn api:app --reload
```

POST to `http://localhost:8000/ask` with:
```json
{
  "question": "কল্যাণীর বয়স কত ছিল?"
}
```
