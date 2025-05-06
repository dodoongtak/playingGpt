import os
import json
from typing import List, Dict
import requests
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

def call_llama3(prompt: str) -> str:
    """Call LLaMA3 via Ollama API."""
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )
        response.raise_for_status()
        return response.json()["response"].strip()
    except Exception as e:
        print(f"Error calling LLaMA3: {e}")
        return "I encountered an error while processing your request."

def map_step(question: str, chunk: str) -> str:
    """Generate an answer for a single chunk using LLaMA3."""
    prompt = f"""You are an expert assistant for Cloudflare's AI Gateway documentation.

Context:
{chunk}

Question: {question}

Answer using only the information in the context above. If the answer is not present, say "I don't know."
"""
    return call_llama3(prompt)

def rerank_step(question: str, answers: List[str]) -> int:
    """Select the best answer from multiple candidates using LLaMA3."""
    numbered_answers = "\n".join([f"{i+1}. {a}" for i, a in enumerate(answers)])
    prompt = f"""You are an expert assistant for Cloudflare's AI Gateway documentation.

Question: {question}

Here are several possible answers:
{numbered_answers}

Which answer best and most accurately answers the question, based only on the information provided? Reply with the number only.
"""
    try:
        best_idx = int(call_llama3(prompt).strip()) - 1
        return best_idx if 0 <= best_idx < len(answers) else 0
    except:
        return 0  # Default to first answer if parsing fails

def map_rerank_answer(question: str, chunks: List[str]) -> str:
    """Generate and select the best answer using Map and Re-Rank strategy."""
    # Map: Generate an answer for each chunk
    answers = [map_step(question, chunk) for chunk in chunks]
    
    # Re-Rank: Select the best answer
    best_idx = rerank_step(question, answers)
    return answers[best_idx]

class RAGPipeline:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = None
        self.documents = []
        self.chunk_size = 500
        self.chunk_overlap = 50

    def load_documents(self, file_path: str) -> None:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        chunks = self._split_text(text)
        self.documents = chunks
        embeddings = self.model.encode(chunks)
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings.astype('float32'))

    def _split_text(self, text: str):
        words = text.split()
        chunks = []
        for i in range(0, len(words), self.chunk_size - self.chunk_overlap):
            chunk = ' '.join(words[i:i + self.chunk_size])
            chunks.append(chunk)
        return chunks

    def retrieve(self, query: str, k: int = 3):
        if not self.index:
            return []
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(query_embedding.astype('float32'), k)
        return [self.documents[i] for i in indices[0]] 