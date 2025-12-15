# search-engine-23A91A0573

A semantic search engine using sentence embeddings and cosine similarity



\# Semantic Search Engine



This project implements a semantic search engine that retrieves conceptually similar documents using vector embeddings instead of traditional keyword matching. It serves as a foundational implementation of modern Information Retrieval systems and forms the core of Retrieval-Augmented Generation (RAG) pipelines.



---



\## Objective



To develop a command-line based semantic search system that:

\- Indexes a collection of text documents using sentence embeddings

\- Retrieves the most semantically relevant documents for a given query

\- Ranks results using cosine similarity

\- Supports both single and batch query processing



---



\## Features



\- Semantic document indexing using a pre-trained transformer model

\- Cosine similarity-based ranking

\- Top-k configurable results

\- Query result snippets for quick context

\- Batch query processing

\- Efficient embedding storage using NumPy



---



\## Tech Stack



\- \*\*Programming Language:\*\* Python  

\- \*\*Embedding Model:\*\* all-MiniLM-L6-v2 (Sentence Transformers)  

\- \*\*Numerical Computation:\*\* NumPy  

\- \*\*Similarity Metric:\*\* Cosine Similarity (scikit-learn)  



---## Project Structure



semantic-search-engine/

│

├── data/

│ └── documents/ # 100+ text documents

│

├── src/

│ ├── generate\_docs.py

│ ├── index\_documents.py

│ ├── search.py

│ └── batch\_search.py

│

├── index/ # Generated embeddings (ignored in Git)

├── queries.txt

├── requirements.txt

├── .gitignore

└── README.md





---



\## Setup Instructions



\### 1. Clone the Repository



2\. Create and Activate Virtual Environment

bash

python -m venv venv

source venv/Scripts/activate

3\. Install Dependencies

pip install torch --index-url https://download.pytorch.org/whl/cpu

pip install -r requirements.txt

Dataset Preparation

To generate a sample dataset of 100 text documents:

python src/generate\_docs.py

Documents will be created in:

data/documents/

Indexing Documents

To generate embeddings and build the search index:

python src/index\_documents.py

This creates:



embeddings.npy



metadata.json



(Stored locally and ignored from GitHub)



Running Semantic Search

Single Query Search

bash

Copy code

python src/search.py

Example query:

applications of artificial intelligence

Batch Query Search

Add queries to queries.txt (one per line), then run:

python src/batch\_search.py

Example Output

File: doc12.txt

Score: 0.81

Snippet: Artificial Intelligence is an important area in modern computer science...

Performance Benchmarks

Number of documents indexed: 100



Embedding model: all-MiniLM-L6-v2



Indexing time: ~15–20 seconds



Average query latency: ~100–150 ms



Hardware: CPU-based execution (Windows)



Design Considerations

Embeddings are generated in batches to manage memory usage.



Index files are persisted for fast query-time loading.



Code is modular, separating ingestion, indexing, and search logic.



Future Improvements

Use FAISS for Approximate Nearest Neighbor (ANN) search



Chunk large documents for better semantic granularity



Add a web-based or REST API interface



Integrate with a RAG-based LLM system



Conclusion

This project demonstrates a complete end-to-end semantic search pipeline using modern NLP techniques. It effectively retrieves semantically relevant documents and provides a strong foundation for scalable information retrieval systems.



\## STEP 3: Save README



\## STEP 4: Final Git Commit









