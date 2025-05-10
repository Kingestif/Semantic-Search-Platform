from sentence_transformers import SentenceTransformer
import numpy as np

# Load pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(chunks):
    embeddings = []
    for chunk in chunks:
        text = chunk['text']
        # Generate embedding for each chunk of text
        embedding = model.encode(text)
        embeddings.append({
            "page": chunk['page'],
            "text": text,
            "embedding": embedding
        })
    return embeddings
