from turbovec import TurboQuantIndex
from sentence_transformers import SentenceTransformer

# Load embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Load data
with open("data/docs.txt") as f:
    texts = [line.strip() for line in f.readlines() if line.strip()]

# Create embeddings
vectors = embedder.encode(texts)

# Build index
index = TurboQuantIndex(dim=len(vectors[0]), bit_width=4)
index.add(vectors)

# Save index
index.write("index/index.tq")

print("✅ Index built successfully!")
