from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import streamlit as st

# Load the model (same model used in embedding.py)
model = SentenceTransformer('all-MiniLM-L6-v2')

def search_query(query, embedded_chunks):
    """
    Search the query against stored document embeddings and return top 3 results.
    """
    if query:
        # Embed the query
        query_embedding = model.encode([query])

        # Extract document embeddings
        doc_embeddings = [doc['embedding'] for doc in embedded_chunks]

        # Compute cosine similarity between query and all document embeddings
        similarities = cosine_similarity(query_embedding, doc_embeddings)[0]

        # Rank top 3 results based on similarity scores
        top_indices = np.argsort(similarities)[-3:][::-1]

        results = []
        for i in top_indices:
            doc = embedded_chunks[i]
            score = similarities[i]
            results.append({
                "page": doc['page'],
                "score": score,
                "text": doc['text'][:300]  # Show the first 300 characters of the result
            })

        return results
    return None
