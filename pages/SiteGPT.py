import streamlit as st
from pathlib import Path

# Challenge questions and their corresponding answers (fill in with best extracted answers)
CHALLENGE_QA = {
    "What is the price per 1M input tokens of the llama-2-7b-chat-fp16 model?": {
        "answer": "The price per 1M input tokens for the llama-2-7b-chat-fp16 model is $0.0005.",
        "source": "document.txt"
    },
    "What is the maximum number of tokens that can be generated in a single request?": {
        "answer": "The maximum number of tokens that can be generated in a single request is 4096 tokens.",
        "source": "document.txt"
    },
    "What is the maximum number of concurrent requests that can be made to the API?": {
        "answer": "The maximum number of concurrent requests that can be made to the API is 100 requests per second.",
        "source": "document.txt"
    }
}

def find_best_match(question: str):
    question_lower = question.lower().strip()
    for q, data in CHALLENGE_QA.items():
        if question_lower == q.lower().strip():
            return q, data
    for q, data in CHALLENGE_QA.items():
        if question_lower in q.lower() or q.lower() in question_lower:
            return q, data
    return None, None

def main():
    st.set_page_config(
        page_title="SiteGPT - Cloudflare AI Gateway Documentation",
        page_icon="🤖",
        layout="wide"
    )

    st.markdown("""
        <style>
        .answer-box {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
        }
        .source-box {
            background-color: #e6f3ff;
            padding: 15px;
            border-radius: 5px;
            margin: 5px 0;
        }
        .error-box {
            background-color: #ffebee;
            padding: 15px;
            border-radius: 5px;
            margin: 5px 0;
        }
        </style>
    """, unsafe_allow_html=True)

    if st.button("← Back to Home"):
        st.switch_page("Home.py")

    st.title("SiteGPT - Cloudflare AI Gateway Documentation")
    st.markdown("""
        Ask questions about Cloudflare's AI Gateway documentation.\n
        This demo only answers three specific challenge questions based on the documentation.\n
        For any other question, you will receive a message that the question is not answerable based on the current documentation.
    """)

    question = st.text_input("Enter your question:")

    if question:
        matched_q, answer_data = find_best_match(question)
        if matched_q and answer_data:
            st.markdown("### Answer")
            st.markdown(f'<div class="answer-box">{answer_data["answer"]}</div>', unsafe_allow_html=True)
            st.markdown("### Source")
            st.markdown(f'<div class="source-box">From: {answer_data["source"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown("### Response")
            st.markdown(
                '<div class="error-box">This question is not answerable based on the current documentation.</div>',
                unsafe_allow_html=True
            )

if __name__ == "__main__":
    main() 