import os
from typing import List
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class VectorStore:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """Initialize the vector store with a sentence transformer model."""
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.chunks = []
        
    def add_documents(self, chunks: List[str]):
        """Add documents to the vector store."""
        # Encode chunks
        embeddings = self.model.encode(chunks)
        
        # Create FAISS index
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(np.array(embeddings).astype('float32'))
        
        # Store chunks
        self.chunks = chunks
        
    def search(self, query: str, k: int = 3) -> List[str]:
        """Search for the k most similar chunks to the query."""
        if not self.index:
            return []
            
        # Encode query
        query_embedding = self.model.encode([query])
        
        # Search
        distances, indices = self.index.search(
            np.array(query_embedding).astype('float32'), 
            k
        )
        
        # Return chunks
        return [self.chunks[i] for i in indices[0]] 