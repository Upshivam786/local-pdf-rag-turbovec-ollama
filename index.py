
from turbovec import TurboQuantIndex
from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer("all-MiniLM-L6-v2")

with open("data/docs.txt") as f:
texts = [line.strip() for line in f.readlines() if line.strip()]

vectors = embedder.encode(texts)

index = TurboQuantIndex(dim=len(vectors[0]), bit_width=4)
index.add(vectors)

index.write("index/index.tq")

print("✅ Index built successfully!")
