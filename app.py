# File: app.py
import streamlit as st
from quiz_generator import generate_quiz

st.set_page_config(
    page_title="QuizGPT Kids Edition",
    page_icon="🎈",
    layout="centered"
)

# Initialize session states
if 'show_answers' not in st.session_state:
    st.session_state.show_answers = False
if 'quiz_submitted' not in st.session_state:
    st.session_state.quiz_submitted = False

# Sidebar
st.sidebar.title("QuizGPT Kids Edition")
difficulty = st.sidebar.selectbox(
    "Select Difficulty",
    ["Easy", "Medium", "Hard"],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    "🔗 [QuizGPT Kids Edition - by @dodoongtak](https://github.com/dodoongtak/playingGpt)"
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
st.write("🌟 Let's see how much you remember from the story! Good luck and have fun! 🌟")
st.write("Welcome! Select a difficulty and answer the questions.")

# Load quiz questions for the selected difficulty
quiz_questions = generate_quiz(difficulty)

# Display all questions
user_answers = []
for i, q in enumerate(quiz_questions):
    # Create a container for each question
    with st.container():
        st.markdown("---")  # Add a separator
        st.markdown(f"### Question {i+1}")  # Question number as a header
        st.markdown(f"**{q['question']}**")  # Question text in bold
        
        # Add some padding
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Radio buttons for answers
        user_answer = st.radio(
            "Select your answer:",
            q["options"],
            key=f"q{i}",
            index=None  # This ensures no option is pre-selected
        )
        user_answers.append(user_answer)
        
        # Add some padding at the bottom
        st.markdown("<br>", unsafe_allow_html=True)

# Add a separator before the submit button
st.markdown("---")

# Submit button
if st.button("Submit Quiz", type="primary"):
    # Check if all questions are answered
    if None in user_answers:
        st.warning("Please answer all questions before submitting!")
    else:
        # Score the quiz
        score = 0
        for i, q in enumerate(quiz_questions):
            if user_answers[i] == q["options"][q["answer_idx"]]:
                score += 1

        # Display total score
        st.markdown("---")
        st.markdown(f"### Your Score: {score} out of {len(quiz_questions)}")
        
        # Add a button to show correct answers
        if st.button("Show Correct Answers"):
            st.session_state.show_answers = True
            
        # Try Again button - only show after submission
        if st.button("Try Again"):
            # Clear all session states
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            # Clear all radio button selections
            for i in range(len(quiz_questions)):
                if f"q{i}" in st.session_state:
                    del st.session_state[f"q{i}"]
            st.experimental_rerun()

        if score == len(quiz_questions):
            st.balloons()
            st.markdown("🎉 **Amazing! You got all the questions right!** 🎉")
        elif score >= len(quiz_questions) // 2:
            st.markdown("👍 **Great job! Keep practicing to get them all right!**")
        else:
            st.markdown("🌱 **Don't worry! Try again and you'll get better!**")

# Show correct answers if requested
if st.session_state.show_answers:
    st.markdown("---")
    st.markdown("### Review Your Answers")
    for i, q in enumerate(quiz_questions):
        if user_answers[i] == q["options"][q["answer_idx"]]:
            st.success(f"✅ Question {i+1}: Your answer was correct!")
        else:
            st.error(f"❌ Question {i+1}: Your answer was incorrect. The correct answer was: {q['options'][q['answer_idx']]}")

st.info("Stay tuned for fun quizzes and learning games! 👶🧠")

st.progress(sum([a is not None for a in user_answers]) / len(quiz_questions))

st.markdown("<hr style='border-top: 3px solid #ffcc00;'>", unsafe_allow_html=True)