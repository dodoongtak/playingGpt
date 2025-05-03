# File: app.py
import streamlit as st
from quiz_generator import generate_quiz

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

# Add book reference link
st.sidebar.markdown("---")
st.sidebar.markdown("📚 **Read the Book**")
st.sidebar.markdown(
    "🔗 [The Tale of Peter Rabbit](https://www.gutenberg.org/cache/epub/14838/pg14838.txt)"
)
st.sidebar.markdown("""
> ℹ️ **Note:** This book is copyright-free and available on Project Gutenberg.  
> This quiz is designed as a fun comprehension exercise for kids aged 4-8.
""")

# Main area
st.title("🎮 QuizGPT Kids Edition")
st.write("Welcome! Select a difficulty and answer the questions.")

# Load quiz questions for the selected difficulty
quiz_questions = generate_quiz(difficulty)

# Display all questions
user_answers = []
for i, q in enumerate(quiz_questions):
    st.write(f"**Question {i+1}:** {q['question']}")
    user_answer = st.radio(
        f"Select your answer for Question {i+1}:",
        q["options"],
        key=f"q{i}"
    )
    user_answers.append(user_answer)

# Submit button
if st.button("Submit Quiz"):
    # Score the quiz
    score = 0
    for i, q in enumerate(quiz_questions):
        if user_answers[i] == q["options"][q["answer_idx"]]:
            score += 1
            st.write(f"✅ Question {i+1}: Correct!")
        else:
            st.write(f"❌ Question {i+1}: Incorrect. The correct answer was: {q['options'][q['answer_idx']]}")

    # Display total score
    st.write(f"**Your Score: {score} out of {len(quiz_questions)}**")

    # Optionally, add a "Try Again" button
    if st.button("Try Again"):
        st.experimental_rerun()

st.info("Stay tuned for fun quizzes and learning games! 👶🧠")