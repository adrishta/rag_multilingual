from fastapi import FastAPI
from pydantic import BaseModel
from preprocess import extract_text
from vectorstore import build_knowledge_base
from query_engine import answer_question

text = extract_text("data/hsc26_bangla.pdf")
collection = build_knowledge_base(text)

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask(query: Query):
    answer = answer_question(query.question, collection)
    return {"answer": answer}
