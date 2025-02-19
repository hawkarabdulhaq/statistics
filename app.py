import streamlit as st

# Import all page modules
import basic
import axiom
import prob

# ──────────────────────────────────────────────────────────────────────────
# 1. SET PAGE CONFIG (MUST BE FIRST STREAMLIT COMMAND IN THIS SCRIPT)
# ──────────────────────────────────────────────────────────────────────────
st.set_page_config(
    layout="wide",
    page_title="Multi-Page App: Home | Basic Stats | Probability Axioms | Probability",
    initial_sidebar_state="expanded"
)

def home_page():
    """
    Display a simple welcome screen or instructions for the user.
    """
    st.title("Home")
    st.write(
        """
        Welcome to the Multi-Page Geological App!  
        
        **Navigation**: Use the buttons in the sidebar to explore:
        - **Basic Statistics**: Generate a synthetic paleoenvironmental dataset, visualize basic statistics, 
          detect outliers, and interpret distributions.
        - **Probability Axioms**: Dive deeper into Bayes’ theorem, conditional probabilities, and real-world examples.
        - **Probability (Fossil A & B)**: An interactive page to explore how presence/absence data and co-occurrence 
          probabilities are computed in geology.
        
        You can return to this **Home** page at any time using the sidebar.
        """
    )

def main():
    """
    Main controller for page navigation using button-based approach.
    """
    st.sidebar.title("Navigation via Buttons")

    # Initialize session state for tracking current page
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "Home"

    # Create 4 buttons in the sidebar
    if st.sidebar.button("Home"):
        st.session_state["current_page"] = "Home"
    if st.sidebar.button("Basic Statistics"):
        st.session_state["current_page"] = "Basic Statistics"
    if st.sidebar.button("Probability Axioms"):
        st.session_state["current_page"] = "Probability Axioms"
    if st.sidebar.button("Probability (Fossil A & B)"):
        st.session_state["current_page"] = "Probability (Fossil A & B)"

    # Route to the selected page
    current_page = st.session_state["current_page"]

    if current_page == "Home":
        home_page()
    elif current_page == "Basic Statistics":
        basic.basic_statistics_page()
    elif current_page == "Probability Axioms":
        axiom.main()
    elif current_page == "Probability (Fossil A & B)":
        prob.main()


if __name__ == "__main__":
    main()
