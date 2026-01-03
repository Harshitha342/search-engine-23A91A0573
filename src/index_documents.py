import os
import json
import numpy as np
from sentence_transformers import SentenceTransformer
from tqdm import tqdm

DATA_DIR = "data/documents"
INDEX_DIR = "index"
MODEL_NAME = "all-MiniLM-L6-v2"


def index_documents():
    if not os.path.exists(DATA_DIR):
        raise FileNotFoundError(
            "Document directory not found. Please ensure data/documents exists."
        )

    os.makedirs(INDEX_DIR, exist_ok=True)

    model = SentenceTransformer(MODEL_NAME)

    documents = []
    metadata = []

    for filename in tqdm(os.listdir(DATA_DIR), desc="Reading documents"):
        if filename.endswith(".txt"):
            file_path = os.path.join(DATA_DIR, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read().strip()
                if text:
                    documents.append(text)
                    metadata.append({
                        "filename": filename,
                        "text": text
                    })

    if not documents:
        raise ValueError("No valid text documents found for indexing.")

    embeddings = model.encode(
        documents,
        batch_size=16,
        show_progress_bar=True
    )

    np.save(os.path.join(INDEX_DIR, "embeddings.npy"), embeddings)

    with open(os.path.join(INDEX_DIR, "metadata.json"), "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)

    print("Indexing completed successfully.")


if __name__ == "__main__":
    index_documents()
