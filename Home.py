import streamlit as st

# Set page config
st.set_page_config(
    page_title="GPT Apps Launcher",
    page_icon="🚀",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        height: 100px;
        font-size: 1.5rem;
        margin: 1rem 0;
    }
    .app-title {
        text-align: center;
        color: #1E88E5;
        margin-bottom: 2rem;
    }
    .app-description {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.markdown('<h1 class="app-title">🚀 Welcome to GPT Apps</h1>', unsafe_allow_html=True)
st.markdown('<p class="app-description">Choose your experience below</p>', unsafe_allow_html=True)

# Create two columns for the apps
col1, col2 = st.columns(2)

# QuizGPT Card
with col1:
    st.markdown("### 🎮 QuizGPT Kids Edition")
    st.markdown("""
    - Fun reading comprehension quizzes
    - Perfect for young readers
    - Based on classic children's stories
    """)
    if st.button("Launch QuizGPT", key="quizgpt"):
        st.switch_page("pages/QuizGPT.py")

# SiteGPT Card
with col2:
    st.markdown("### 🤖 SiteGPT Doc Q&A")
    st.markdown("""
    - Ask questions about documentation
    - Powered by local RAG
    - No API keys required
    """)
    if st.button("Launch SiteGPT", key="sitegpt"):
        st.switch_page("pages/SiteGPT.py")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Made with ❤️ by @dodoongtak</p>
    <p><a href="https://github.com/dodoongtak/playingGpt" target="_blank">View on GitHub</a></p>
</div>
""", unsafe_allow_html=True) 