import streamlit as st

def homework_page():
    """
    Homework Instructions for Tutorials:
    - Students create a one-page result for each tutorial.
    - Summaries include steps taken, key insights, and applications in research.
    - Submission in Coospace (Week 2 Modelling and Simulation Question).
    """

    st.title("Homework Instructions")

    st.markdown(
        """
        ## Submit a One-Page Result for Each Tutorial

        You are required to **submit** a concise (one-page) summary for **each** of the Tutorials:
        1. **Tutorial 1**: Basic dataset download & `overview.py`.
        2. **Tutorial 2**: Mean, median, mode exploration with multiple datasets.
        3. **Tutorial 3**: Filtering NDVI or spectral bands to isolate water/forest/crops.
        4. **Tutorial 4**: Abraham Reef Coral Isotope Data (Group Task).
        
        ---
        ### What to Include in Each One-Page Result

        1. **Tutorial Expectations**  
           - Briefly restate the **goal** of the tutorial (e.g., “We aimed to learn about filtering NDVI,” 
             or “We explored multiple earthquake datasets to see how mean/median/mode can shift.”).

        2. **Your Steps**  
           - Outline how you **performed** the tasks (tools, scripts, parameters).  
           - Mention any **challenges** or modifications you made.

        3. **Reflections and Key Insights**  
           - Highlight **findings** (e.g., did you find a strong correlation, unexpected outliers, 
             success in isolating water areas?).  
           - Note any **surprises** or confirmations about the data or technique.

        4. **Research Applications**  
           - How could these methods or insights support your **research** or **project**?  
           - E.g., “Using NDVI filtering might help me identify suitable reforestation zones,” 
             or “Coral isotopes can clarify past climatic changes relevant to my climate model.”

        ---
        ### Submission

        1. **Format**: One page per tutorial (PDF or docx).
        2. **Where**: Submit each summary in **Coospace** under **Week 2 Modelling and Simulation Question**.
        3. **Deadline**: Please follow the posted due date in the course announcements.

        ---
        ### Tips

        - **Concise**: Aim for clarity. Avoid large code dumps; focus on results & reflection.
        - **Screen Captures**: Optional. You can include small plots or screenshots if it helps clarify results.
        - **Group Task**: For **Tutorial 4** (Abraham Reef Coral Isotope Data), ensure each group submission 
          identifies **who** contributed which portion.
        
        **Good luck**, and thank you for all your efforts! 
        """
    )

def main():
    homework_page()

if __name__ == "__main__":
    main()
