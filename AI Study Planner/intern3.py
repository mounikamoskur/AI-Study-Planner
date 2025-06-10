import streamlit as st
import pandas as pd

# Function to generate the study plan
def generate_study_plan(topic, study_hours, difficulty, days):
    study_plan = []
    tasks = {
        "Beginner": [
            "Read basic concepts",
            "Watch intro videos",
            "Take notes",
            "Practice simple exercises"
        ],
        "Intermediate": [
            "Deep dive into subtopics",
            "Solve practice problems",
            "Attempt quizzes",
            "Summarize learnings"
        ],
        "Advanced": [
            "Work on case studies",
            "Implement mini-projects",
            "Take mock assessments",
            "Review and optimize solutions"
        ]
    }

    for i in range(days):
        topic_part = f"{topic} - Part {i+1}"
        task = tasks[difficulty][i % len(tasks[difficulty])]
        study_plan.append({
            "Day": f"Day {i+1}",
            "Topic": topic_part,
            "Task": task,
            "Study Hours": f"{study_hours} hrs"
        })

    return pd.DataFrame(study_plan)

# Streamlit UI
st.set_page_config(page_title="StudBud: AI Study Planner", page_icon="📚", layout="centered")
st.title("📚 StudBud: AI Study Planner")
st.subheader("Create a smart, efficient, and personalized study schedule")

# Input fields
topic = st.text_input("📘 Enter the topic or subject:")
study_hours = st.slider("⏱️ Hours you can study per day:", 1, 10, 3)
difficulty = st.selectbox("📊 Select difficulty level:", ["Beginner", "Intermediate", "Advanced"])
days = st.slider("📅 How many days do you want the plan for?", 1, 30, 7)

# Button to generate the plan
if st.button("🚀 Generate Study Plan"):
    if not topic.strip():
        st.warning("⚠️ Please enter a topic to proceed.")
    else:
        with st.spinner("Generating your study plan..."):
            df = generate_study_plan(topic.strip(), study_hours, difficulty, days)
            st.success("✅ Study plan generated successfully!")
            st.dataframe(df, use_container_width=True)

# Info box
st.info("💡 Fill in your preferences and click the button to get your AI-generated study schedule.")
