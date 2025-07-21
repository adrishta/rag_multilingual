from preprocess import extract_text
from vectorstore import build_knowledge_base
from query_engine import answer_question

text = extract_text("data/hsc26_bangla.pdf")
collection = build_knowledge_base(text)

while True:
    question = input("\n❓ প্রশ্ন করো (Bangla/English): ")
    answer = answer_question(question, collection)
    print(f"🧠 উত্তর: {answer}")
