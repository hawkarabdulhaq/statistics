import streamlit as st

# Import all page modules
import basic
import axiom
import prob
import tutorial8

# ──────────────────────────────────────────────────────────────────────────
# SET PAGE CONFIG (MUST BE FIRST STREAMLIT COMMAND)
# ──────────────────────────────────────────────────────────────────────────
st.set_page_config(
    layout="wide",
    page_title="Multi-Page App: Home | Basic Stats | Probability Axioms | Probability | Tutorial 8",
    initial_sidebar_state="expanded"
)

def home_page():
    st.image("banner.png", use_container_width=True)
    st.title("Welcome to ABDULHAQ Hawkar's Learning Portal")
    st.markdown(
        """
        **This portal is created by ABDULHAQ Hawkar**  
        as an accessory supplement material for students, enabling dynamic learning through interactive examples of statistics in geology.

        For any questions, please contact:  
        **[hawkar.ali.abdulhaq@szte.hu](mailto:hawkar.ali.abdulhaq@szte.hu)**
        """
    )
    st.markdown("---")
    st.subheader("Navigation Instructions")
    st.write(
        """
        Use the buttons in the sidebar to explore:
        
        - **Basic Statistics**: Generate a synthetic paleoenvironmental dataset, analyze basic statistics, and visualize distributions.
        - **Probability Axioms**: Learn about Bayes’ theorem and conditional probabilities through real-world examples.
        - **Probability (Fossil A & B)**: Interactively explore co-occurrence probabilities of fossils.
        - **Tutorial 8**: Apply fuzzy logic to classify terrain using elevation data.
        """
    )
    st.markdown("---")
    st.info("Feel free to click the navigation buttons on the sidebar to start exploring!")
    st.markdown(
        """
        <hr>
        <div style="text-align: center; font-size: 0.9em;">
            © 2023 ABDULHAQ Hawkar | For inquiries, contact <a href="mailto:hawkar.ali.abdulhaq@szte.hu">hawkar.ali.abdulhaq@szte.hu</a>
        </div>
        """, unsafe_allow_html=True
    )

def main():
    # Initialize session state for page navigation if not set
    if "current_page" not in st.session_state:
        st.session_state["current_page"] = "Home"

    # Sidebar navigation buttons
    if st.sidebar.button("Home"):
        st.session_state["current_page"] = "Home"
    if st.sidebar.button("Basic Statistics"):
        st.session_state["current_page"] = "Basic Statistics"
    if st.sidebar.button("Probability Axioms"):
        st.session_state["current_page"] = "Probability Axioms"
    if st.sidebar.button("Probability (Fossil A & B)"):
        st.session_state["current_page"] = "Probability (Fossil A & B)"
    if st.sidebar.button("Tutorial 8"):
        st.session_state["current_page"] = "Tutorial 8"

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
    elif current_page == "Tutorial 8":
        tutorial8.tutorial8_page()

if __name__ == "__main__":
    main()
