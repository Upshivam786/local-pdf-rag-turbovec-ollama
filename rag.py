from turbovec import TurboQuantIndex
from sentence_transformers import SentenceTransformer
import ollama

# Load embedding model once
embedder = SentenceTransformer("all-MiniLM-L6-v2")

def build_index(texts):
    # create embeddings
    vectors = embedder.encode(texts)

    # build turbovec index
    index = TurboQuantIndex(dim=len(vectors[0]), bit_width=4)
    index.add(vectors)

    return index

def ask(query, index, texts, k=3, model="llama3.2"):
    # encode query
    q_vec = embedder.encode([query])

    # search
    scores, indices = index.search(q_vec, k=k)

    # retrieve context
    retrieved = [texts[i] for i in indices[0]]
    context = "\n".join(retrieved)

    # LLM call
    response = ollama.chat(
        model=model,
        messages=[
            {
                "role": "system",
                "content": """STRICT MODE:
- Answer ONLY from context
- No external knowledge
- If missing: say 'Not found in context'
"""
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion: {query}"
            }
        ]
    )

    return response['message']['content'], retrieved
