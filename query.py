from turbovec import TurboQuantIndex
from sentence_transformers import SentenceTransformer
import ollama

# Load embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Load index
index = TurboQuantIndex.load("index.tq")

# Query
query = "Explain TurboVec in detail"
q_vec = embedder.encode([query])

# Search
scores, indices = index.search(q_vec, k=3)

# Load original text
with open("data.txt") as f:
    texts = f.readlines()

# Retrieve relevant chunks
retrieved = [texts[i].strip() for i in indices[0]]

# Remove duplicates
retrieved = list(dict.fromkeys(retrieved))

context = "\n".join(retrieved)

print("\n🔍 Retrieved Context:\n")
for i, chunk in enumerate(retrieved, 1):
    print(f"{i}. {chunk}")

# Ask Ollama
response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "system",
            "content": """You are a strict assistant.

Rules:
1. ONLY use the provided context.
2. DO NOT use prior knowledge.
3. If the answer is not fully in the context, say exactly: "Not found in context".
"""
        },
        {
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion: {query}\n\nAnswer:"
        }
    ]
)

print("\n💡 Answer:\n")
print(response['message']['content'])
