import streamlit as st

def capstone_project_page():
    st.title("🎓 Capstone Project: Reservoir Quality Classification & Clustering")

    # ─────────────────────────────────────────────────────────
    # Introduction
    # ─────────────────────────────────────────────────────────
    st.header("📘 Project Overview")
    st.markdown("""
    This **Capstone Project** invites your team to collaboratively explore and classify reservoir layers 
    from multiple wells using geostatistical and probabilistic tools you learned in this course.

    **Goal**:  
    Analyze porosity and permeability trends from at least two wells and apply **K-means clustering** 
    to classify reservoir quality zones (e.g., high, medium, low potential zones).

    **Data Provided**:
    - [Well 1](https://github.com/hawkarabdulhaq/statistics/blob/main/input/Well-1.xlsx)
    - [Well 2](https://github.com/hawkarabdulhaq/statistics/blob/main/input/Well-2.xlsx)

    *(More wells will be added soon.)*

    **Group Size**: 5 students  
    **Deadline**: Two weeks from the release date  
    **Delivery**: One final PDF report + notebook/script files.
    """)

    # ─────────────────────────────────────────────────────────
    # Tasks Breakdown
    # ─────────────────────────────────────────────────────────
    st.header("🧩 Tasks and Expectations")

    st.markdown("""
    ### 🔍 1. Data Cleaning & Preparation
    - Load the Excel data from both wells.
    - Check for missing or zero porosity/permeability values.
    - Apply log transformation if needed (e.g., `log10(permeability)`).

    ### 📊 2. Statistical Analysis
    - Plot histograms and boxplots for porosity and permeability.
    - Calculate:
        - Mean, Median, Std Dev for both properties
        - Depth range per well
    - Visualize trends with depth.

    ### 📈 3. K-Means Clustering
    - Normalize porosity and log-permeability.
    - Apply K-means clustering (choose K = 2 or 3).
    - Label zones (e.g., High, Medium, Low Reservoir Quality).
    - Visualize the cluster distribution vs. depth.

    ### 📐 4. Cross-Well Comparison
    - Compare cluster characteristics across both wells.
    - Identify if high-quality zones occur at similar depths.
    - Discuss lateral reservoir heterogeneity or continuity.

    ### 🧠 5. Interpretation & Report
    - Justify the number of clusters and choice of features.
    - Provide geological reasoning for cluster meaning.
    - Include visuals: plots, cluster summaries, and interpretations.
    - Optional: If you're familiar, try plotting your clusters using Folium or 3D cross-sections (bonus).

    """)

    # ─────────────────────────────────────────────────────────
    # Submission
    # ─────────────────────────────────────────────────────────
    st.header("📤 Final Submission")
    st.markdown("""
    - ✅ A PDF report with your figures, analysis, and interpretations.
    - ✅ Python notebooks or scripts you used.
    - ✅ Each student’s name and their specific contribution (1 paragraph).

    Submit your work via **Coospace > Capstone Project Folder**.
    """)

    st.success("Your project should demonstrate the integration of everything you've learned: data preprocessing, statistical reasoning, probabilistic thinking, and clustering-based classification.")

def main():
    capstone_project_page()

if __name__ == "__main__":
    main()
