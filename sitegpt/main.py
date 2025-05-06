import streamlit as st

# Set page config
st.set_page_config(
    page_title="SiteGPT Doc Q&A",
    page_icon="🤖",
    layout="centered"
)

# Title and description
st.title("🤖 SiteGPT Doc Q&A")
st.markdown("""
### Coming Soon!
This page will soon let you ask questions about Cloudflare's AI Gateway documentation using local RAG technology.

#### Features (Coming Soon):
- 📚 Document Q&A using local RAG
- 🔍 Semantic search powered by FAISS
- 🤖 Local LLM inference with LLaMA3
- 🚀 No API keys required!

#### Tech Stack:
- Streamlit for UI
- FAISS for vector search
- sentence-transformers for embeddings
- LLaMA3 via Ollama for LLM
""")

# Back to launcher button
if st.button("← Back to Launcher"):
    st.switch_page("launcher.py") 