import streamlit as st

# Import all page modules
import basic
import axiom
import prob
import dataset
import tutorial1
import tutorial2  # <-- New tutorial2 page

# ──────────────────────────────────────────────────────────────────────────
# 1. SET PAGE CONFIG (MUST BE FIRST STREAMLIT COMMAND IN THIS SCRIPT)
# ──────────────────────────────────────────────────────────────────────────
st.set_page_config(
    layout="wide",
    page_title="Multi-Page App: Home | Basic Stats | Probability Axioms | Probability | Dataset | Tutorials",
    initial_sidebar_state="expanded"
)

def home_page():
    """
    Displays the Home page with a banner, a welcome message, and an interactive footer.
    """
    # Display banner image using use_container_width
    st.image("banner.png", use_container_width=True)

    # Home title and welcome message
    st.title("Welcome to ABDULHAQ Hawkar's Learning Portal")
    st.markdown(
        """
        **This portal is created by ABDULHAQ Hawkar**  
        to serve as an accessory supplement material for students, enabling dynamic learning through interactive examples of statistics in geology.

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
        - **Probability Axioms**: Dive deeper into Bayes’ theorem, conditional probabilities, and related real-world examples.
        - **Probability (Fossil A & B)**: Interactively explore how fossil presence/absence data is used to calculate co-occurrence probabilities.
        - **Dataset**: Fetch earthquake event data from the USGS API and download the dataset as CSV.
        - **Tutorial 1**: Step-by-step guide for downloading a dataset and running `overview.py`.
        - **Tutorial 2**: Step-by-step guide for mean, median, mode, and a 3D extruded quake visualization.
        """
    )
    
    st.markdown("---")
    st.info("Feel free to click the navigation buttons on the sidebar to start exploring!")

    # Footer displayed at the bottom of the Home page
    st.markdown(
        """
        <hr>
        <div style="text-align: center; font-size: 0.9em;">
            © 2023 ABDULHAQ Hawkar | For inquiries, contact <a href="mailto:hawkar.ali.abdulhaq@szte.hu">hawkar.ali.abdulhaq@szte.hu</a>
        </div>
        """,
        unsafe_allow_html=True
    )

def main():
    """
    Main controller for page navigation.
    There are seven pages:
      - Home
      - Basic Statistics (from basic.py)
      - Probability Axioms (from axiom.py)
      - Probability (Fossil A & B) (from prob.py)
      - Dataset (from dataset.py)
      - Tutorial 1 (from tutorial1.py)
      - Tutorial 2 (from tutorial2.py)
    """
    # Initialize session state for tracking current page
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
    if st.sidebar.button("Dataset"):
        st.session_state["current_page"] = "Dataset"
    if st.sidebar.button("Tutorial 1"):
        st.session_state["current_page"] = "Tutorial 1"
    if st.sidebar.button("Tutorial 2"):
        st.session_state["current_page"] = "Tutorial 2"

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
    elif current_page == "Dataset":
        dataset.main()
    elif current_page == "Tutorial 1":
        tutorial1.main()
    elif current_page == "Tutorial 2":
        tutorial2.main()

if __name__ == "__main__":
    main()
