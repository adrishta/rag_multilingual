from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb

def build_knowledge_base(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(text)

    model = SentenceTransformer("sentence-transformers/distiluse-base-multilingual-cased-v2")
    client = chromadb.Client()
    collection = client.create_collection(name="rag_data")

    for i, chunk in enumerate(chunks):
        embedding = model.encode(chunk).tolist()
        collection.add(documents=[chunk], embeddings=[embedding], ids=[str(i)])

    return collection
