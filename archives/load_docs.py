from typing import List
import re

def split_into_chunks(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """Split text into overlapping chunks."""
    # Clean text
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    chunks = []
    current_chunk = []
    current_size = 0
    
    for sentence in sentences:
        sentence_size = len(sentence.split())
        
        if current_size + sentence_size > chunk_size and current_chunk:
            # Join current chunk and add to chunks
            chunks.append(' '.join(current_chunk))
            
            # Start new chunk with overlap
            overlap_words = current_chunk[-int(overlap/2):]
            current_chunk = overlap_words
            current_size = sum(len(word.split()) for word in overlap_words)
        
        current_chunk.append(sentence)
        current_size += sentence_size
    
    # Add the last chunk if it exists
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    return chunks

def load_document(file_path: str) -> List[str]:
    """Load and process a document into chunks."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        return split_into_chunks(text)
    except Exception as e:
        print(f"Error loading document: {e}")
        return [] 