import streamlit as st

def capstone_project_page():
    st.title("🎓 Capstone Project: Reservoir Quality Classification & Clustering")

    st.header("📘 Project Overview")
    st.markdown("""
    This **Capstone Project** invites your team to collaboratively explore and classify reservoir layers 
    from multiple wells using geostatistical and probabilistic tools learned throughout the course.

    **Goal**:  
    Analyze porosity and permeability trends from at least two wells and apply **K-means clustering**, 
    **Bayesian probability**, **fuzzy logic**, and **correlation analysis** to define and compare reservoir quality zones.

    **Data Provided**:
    - [Well 1](https://github.com/hawkarabdulhaq/statistics/blob/main/input/Well-1.xlsx)
    - [Well 2](https://github.com/hawkarabdulhaq/statistics/blob/main/input/Well-2.xlsx)

    *(More wells may be added as needed.)*

    **Group Size**: 5 students  
    **Deadline**: Two weeks from the release date  
    **Submission**: One final PDF report + Python script or Colab notebook
    """)

    st.header("🧩 Tasks and Expectations")
    st.markdown("""
    ### 🔍 1. Data Cleaning & Preparation
    - Load Excel files into pandas.
    - Handle missing or invalid porosity/permeability values.
    - Log-transform permeability if necessary.

    ### 📊 2. Statistical Analysis
    - Generate histograms, boxplots.
    - Calculate mean, median, std deviation.
    - Plot variation with depth.

    ### 📈 3. K-Means Clustering
    - Normalize porosity and log-permeability.
    - Use `sklearn.KMeans` (K = 2 or 3).
    - Visualize clusters across depth per well.

    ### 📐 4. Cross-Well Comparison
    - Compare clustering across both wells.
    - Analyze lateral trends and potential continuity.

    ### 🧠 5. Geological Interpretation
    - Justify cluster meanings with geological reasoning.
    - Link to depositional environments or diagenetic features.

    ### 🔮 6. Threshold-Based Productivity Classification
    - Define porosity/permeability cutoffs for "productive zones".
    - Apply **Bayes’ theorem** to update reservoir predictions.

    ### 🌫️ 7. Fuzzy Logic Classification
    - Define fuzzy elevation or porosity classes.
    - Apply membership functions and assign fuzzy zones.

    ### 🔗 8. Correlation & Feature Relationships
    - Use heatmaps or pairplots (`seaborn`) to explore relationships.
    - Discuss implications for feature selection and modeling.

    ### 📊 9. Visual Storytelling & Presentation
    - Design a consistent visual style (titles, color codes, legends).
    - Emphasize clarity in how figures support your interpretation.
    - Optional: Use Streamlit or Folium for interactive visuals.

    """)

    st.header("📤 Final Submission")
    st.markdown("""
    - ✅ PDF report with labeled figures, interpretations, and task results.
    - ✅ Python script(s) or Colab notebook.
    - ✅ Team member names with contributions (1 paragraph each).
    - ✅ Submit to: **Coospace > Capstone Project Folder**
    """)

    st.success("This final project is your opportunity to showcase the full range of skills acquired in modeling and simulation, from statistical logic to geoscientific insight.")

def main():
    capstone_project_page()

if __name__ == "__main__":
    main()
