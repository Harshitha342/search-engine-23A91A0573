from search import search

def batch_search(query_file, top_k=5):
    with open(query_file, "r", encoding="utf-8") as f:
        queries = f.readlines()

    for q in queries:
        q = q.strip()
        if not q:
            continue

        print(f"\nQuery: {q}")
        results = search(q, top_k)

        for r in results:
            print(f"- {r['filename']} | Score: {r['score']:.4f}")

if __name__ == "__main__":
    batch_search("queries.txt")
