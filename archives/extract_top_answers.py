import re

qa = {}
with open("Ranked_Answer.txt", "r", encoding="utf-8") as f:
    content = f.read()

questions = re.split(r"={10,}\n", content)
for qblock in questions:
    if not qblock.strip():
        continue
    lines = qblock.strip().splitlines()
    question = None
    answer = None
    for i, line in enumerate(lines):
        if line.startswith("Question: "):
            question = line.replace("Question: ", "").strip()
        if line.startswith("Rank 1 Answer Chunk:"):
            answer = lines[i+1].strip() if i+1 < len(lines) else ""
    if question and answer:
        qa[question] = answer

for q, a in qa.items():
    print(f"Q: {q}\nA: {a}\n{'-'*40}") 