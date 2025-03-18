import streamlit as st

def homeproject_page():
    """
    Home-based Project: Elevation-based Land Cover Classification and Risk Assessment
    """

    st.title("🏔️ Home Project: Elevation-based Land Cover Analysis")

    st.markdown(
        """
        ## Project Overview

        **Objective:**
        In this home-based project, you'll work collaboratively in groups to:

        - Classify terrain based on elevation data.
        - Apply conditional probability and fuzzy logic techniques.
        - Identify areas potentially suitable for agriculture, forestry, water bodies, and flood risk.

        ---

        ### Project Duration:
        - **Expected Time**: ~6 hours

        ---

        ### Dataset

        **Dataset provided**:
        - `Elevation_backup.xyz` (longitude, latitude, elevation)

        ---

        ### Group Tasks & Roles:
        Each group should collaborate, discuss, and clearly divide these tasks:

        **Task 1: Data Exploration (1 hour)**
        - Load the elevation data (`Elevation_backup.xyz`) in Google Colab.
        - Visualize the elevation data (histogram and 2D scatter plot).
        - Compute and document basic statistical measures (mean, median, variance).

        **Task 2: Elevation-Based Classification (1 hour)**
        - Define clear elevation categories (e.g., Lowland, Upland, Highland).
        - Classify elevations using conditional statements or clustering.
        - Plot classified areas using a color-coded scatter plot or map visualization.

        **Task 2: Conditional Probability Analysis (1 hour)**
        - Calculate conditional probabilities:
          - Probability of high elevation (>400 m) given specific latitude/longitude ranges.
          - Probability of lowland areas (<380 m) given spatial conditions.
        - Discuss how spatial location affects elevation probabilities.

        **Task 3: Fuzzy Logic Classification (1.5 hours)**
        - Define fuzzy membership functions for elevation classes:
          - Lowland (350–380 m)
          - Upland (380–400 m)
          - Highland (>400 m)
        - Apply fuzzy logic to classify elevation data.
        - Visualize fuzzy membership functions clearly.

        **Task 4: Risk Assessment & Decision-Making (1 hour)**
        - Use fuzzy classifications and conditional probabilities to assess:
          - Agricultural suitability
          - Forestry suitability
          - Flood risk zones
        - Produce maps highlighting each classification clearly.

        **Task 5: Collaborative Reporting & Reflection (1 hour)**
        - Collaboratively write a short report summarizing:
          - Methods used and key findings.
          - How conditional probabilities influenced your understanding of terrain.
          - Practical implications (e.g., flood management, land use planning).

        ---

        ### Project Submission:
        - Prepare a clear, concise **group report (max. 5 pages)** including:
          - Visualizations
          - Statistical summaries
          - Probability calculations
          - Clear explanation of fuzzy logic classifications
          - Short reflection on decision-making implications
        - Include the names of all group members and their specific contributions.

        Submit your report through the class portal before the deadline.

        **For Questions & Guidance:**
        - Contact your instructor at [hawkar.ali.abdulhaq@szte.hu](mailto:hawkar.ali.abdulhaq@szte.hu).

        **Happy collaborating and exploring!**
        """
    )

def main():
    homeproject_page()

if __name__ == "__main__":
    main()
