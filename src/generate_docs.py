import os

DOCS_DIR = "data/documents"
os.makedirs(DOCS_DIR, exist_ok=True)

topics = [
    "Artificial Intelligence",
    "Machine Learning",
    "Deep Learning",
    "Natural Language Processing",
    "Computer Vision",
    "Data Science",
    "Information Retrieval",
    "Neural Networks",
    "Big Data",
    "Cloud Computing",
    "Cyber Security",
    "Blockchain",
    "Internet of Things",
    "Software Engineering",
    "Distributed Systems"
]

for i in range(1, 101):
    topic = topics[i % len(topics)]
    content = (
        f"{topic} is an important area in modern computer science. "
        f"It focuses on solving real-world problems using advanced computational techniques. "
        f"This field has applications in industry, research, and everyday technology."
    )

    with open(f"{DOCS_DIR}/doc{i}.txt", "w", encoding="utf-8") as f:
        f.write(content)

print("100 documents generated successfully!")
