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
    Displays the Home page with a banner, a welcome message, and footer.
    """
    # Display banner image
    st.image("banner.png", use_column_width=True)

    # Home title and welcome message
    st.title("Welcome to the Geological Learning Portal")
    st.markdown(
        """
        **This portal is made by Abdulhaq Hawkar**  
        as an accessory supplement material for students to engage in dynamic learning and interact with examples of statistics in geology.

        For any questions, please contact:  
        **[hawkar.ali.abdulhaq@szte.hu](mailto:hawkar.ali.abdulhaq@szte.hu)**
        """
    )
    
    st.markdown("---")
    st.subheader("Navigation Instructions")
    st.write(
        """
        Use the buttons in the sidebar to navigate through the portal:
        
        - **Basic Statistics**: Generate a synthetic paleoenvironmental dataset, explore basic statistics, visualize distributions, and analyze data.
        - **Probability Axioms**: Delve into Bayes’ theorem, conditional probabilities, and related real-world examples.
        - **Probability (Fossil A & B)**: Interactively explore how fossil presence/absence data are used to calculate co-occurrence probabilities.
        """
    )
    
    st.markdown("---")
    # Add an interactive element, for example a poll or a question.
    st.info("Feel free to click the navigation buttons on the sidebar to start exploring!")

    # Footer (displayed at the bottom of the Home page)
    st.markdown(
        """
        <hr>
        <div style="text-align: center; font-size: 0.9em;">
            © 2023 Abdulhaq Hawkar | For any inquiries, contact <a href="mailto:hawkar.ali.abdulhaq@szte.hu">hawkar.ali.abdulhaq@szte.hu</a>
        </div>
        """,
        unsafe_allow_html=True
    )

def main():
    """
    Main controller for page navigation using button-based approach.
    There are four pages:
      - Home
      - Basic Statistics (from basic.py)
      - Probability Axioms (from axiom.py)
      - Probability (Fossil A & B) (from prob.py)
    """
    st.sidebar.title("Navigation via Buttons")

    # Initialize session state if not present
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "Home"

    # Navigation buttons in the sidebar
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
