import json
import os
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

INDEX_DIR = "index"
MODEL_NAME = "all-MiniLM-L6-v2"

if not os.path.exists("index/embeddings.npy") or not os.path.exists("index/metadata.json"):
    raise FileNotFoundError(
        "Index files not found. Please run src/index_documents.py first."
    )

def search(query, top_k=5):
    # Load index
    embeddings = np.load(f"{INDEX_DIR}/embeddings.npy")
    with open(f"{INDEX_DIR}/metadata.json", "r", encoding="utf-8") as f:
        metadata = json.load(f)

    # Load model
    model = SentenceTransformer(MODEL_NAME)

    # Encode query
    query_embedding = model.encode([query])

    # Compute cosine similarity
    scores = cosine_similarity(query_embedding, embeddings)[0]

    # Get top-k indices
    top_indices = scores.argsort()[::-1][:top_k]

    results = []
    for idx in top_indices:
        doc = metadata[idx]
        snippet = doc["text"][:200].replace("\n", " ")
        results.append({
            "filename": doc["filename"],
            "score": float(scores[idx]),
            "snippet": snippet
        })

    return results

if __name__ == "__main__":
    query = input("Enter your query: ")
    results = search(query)

    print("\nTop Results:\n")
    for r in results:
        print(f"File: {r['filename']}")
        print(f"Score: {r['score']:.4f}")
        print(f"Snippet: {r['snippet']}...")
        print("-" * 50)
