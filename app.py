import streamlit as st
import basic
import axiom
import prob
import dataset
import dataset2
import tutorial1
import tutorial2
import tutorial3
import tutorial4
import tutorial5
import tutorial6
import tutorial7
import tutorial8
import homework
import homework2
import homeproject
import capstone_project  # ✅ NEW: Capstone Project

st.set_page_config(
    layout="wide",
    page_title="Multi-Page App: Home | Tutorials | Projects",
    initial_sidebar_state="expanded"
)

def home_page():
    st.image("banner.png", use_container_width=True)
    st.title("Welcome to ABDULHAQ Hawkar's Learning Portal")
    st.markdown("""
        **This portal is created by ABDULHAQ Hawkar**  
        for dynamic learning of statistical applications in geology.

        **Contact**: [hawkar.ali.abdulhaq@szte.hu](mailto:hawkar.ali.abdulhaq@szte.hu)
    """)

def main():
    st.sidebar.title("Access Key")
    password = st.sidebar.text_input("Enter Password:", type="password")
    if password != "stat2025":
        st.warning("Incorrect password. Please try again.")
        st.stop()

    st.sidebar.title("Navigation")

    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "Home"

    pages = [
        "Home", "Basic Statistics", "Probability Axioms", "Probability (Fossil A & B)",
        "Dataset", "Dataset 2", "Tutorial 1", "Tutorial 2", "Tutorial 3", "Tutorial 4",
        "Homework 1", "Tutorial 5", "Tutorial 6", "Tutorial 7", "Tutorial 8",
        "Homework 2", "Home Project", "Capstone Project"  # ✅ Added Capstone Project
    ]

    for page in pages:
        if st.sidebar.button(page):
            st.session_state["current_page"] = page

    page_router = {
        "Home": home_page,
        "Basic Statistics": basic.basic_statistics_page,
        "Probability Axioms": axiom.main,
        "Probability (Fossil A & B)": prob.main,
        "Dataset": dataset.main,
        "Dataset 2": dataset2.main,
        "Tutorial 1": tutorial1.main,
        "Tutorial 2": tutorial2.main,
        "Tutorial 3": tutorial3.main,
        "Tutorial 4": tutorial4.main,
        "Homework 1": homework.main,
        "Tutorial 5": tutorial5.main,
        "Tutorial 6": tutorial6.main,
        "Tutorial 7": tutorial7.main,
        "Tutorial 8": tutorial8.main,
        "Homework 2": homework2.main,
        "Home Project": homeproject.main,
        "Capstone Project": capstone_project.main  # ✅ Routing added
    }

    page_router[st.session_state["current_page"]]()

if __name__ == "__main__":
    main()
