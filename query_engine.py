from sentence_transformers import SentenceTransformer

def answer_question(question, collection):
    model = SentenceTransformer("sentence-transformers/distiluse-base-multilingual-cased-v2")
    qvec = model.encode(question).tolist()
    results = collection.query(query_embeddings=[qvec], n_results=1)
    return results['documents'][0][0]
