# File: app.py
import streamlit as st

st.set_page_config(
    page_title="QuizGPT Kids Edition",
    page_icon="🎈",
    layout="centered"
)

# Sidebar
st.sidebar.title("QuizGPT Kids Edition")
difficulty = st.sidebar.selectbox(
    "Select Difficulty",
    ["Easy", "Medium", "Hard"],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    "🔗 [GitHub Repo](https://github.com/dodoongtak/playingGpt)"
)

# Main area
st.title("🎈 QuizGPT Kids Edition")
st.write("Welcome! This playful quiz app for kids is under construction. 🚧")

st.info("Stay tuned for fun quizzes and learning games! 👶🧠")