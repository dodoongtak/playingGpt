from rag_llm import RAGPipeline

pipeline = RAGPipeline()
pipeline.load_documents("document.txt")

challenge_questions = [
    "What is the price per 1M input tokens of the llama-2-7b-chat-fp16 model?",
    "What is the maximum number of tokens that can be generated in a single request?",
    "What is the maximum number of concurrent requests that can be made to the API?"
]

with open("Ranked_Answer.txt", "w", encoding="utf-8") as f:
    for q in challenge_questions:
        chunks = pipeline.retrieve(q)
        f.write(f"Question: {q}\n")
        for i, chunk in enumerate(chunks):
            f.write(f"Rank {i+1} Answer Chunk:\n{chunk}\n")
        f.write("="*60 + "\n") 