import streamlit as st

def capstone_project_page():
    st.title("🎓 Capstone Project: Reservoir Quality Classification & Clustering")

    st.header("📘 Project Overview")
    st.markdown("""
    This **Capstone Project** asks your team to apply the full pipeline of skills developed in this course—working with geological data, analyzing trends, and classifying zones using clustering.

    **Goal**:  
    Use porosity and permeability data from multiple wells to classify reservoir quality zones (e.g., low, medium, high) and understand their geological significance.

    **Data Provided**:
    - [Well 1](https://github.com/hawkarabdulhaq/statistics/blob/main/input/Well-1.xlsx)
    - [Well 2](https://github.com/hawkarabdulhaq/statistics/blob/main/input/Well-2.xlsx)

    **Group Size**: 5 students  
    **Deadline**: Two weeks from release  
    **Submission**: Final report (PDF) + notebook or script
    """)

    st.header("🧩 Project Tasks and Tools")

    st.markdown("""
    ### 🔍 1. Data Cleaning & Preparation  
    **Tools**: `pandas`, `numpy`  
    - Load the Excel data from both wells.
    - Check for missing values or zero entries in porosity/permeability.
    - Apply a log transformation to permeability if needed.

    **Why**: Clean data is critical for reliable statistical and clustering analysis. Log transforms help manage skewed data like permeability.

    ---

    ### 📊 2. Statistical Analysis  
    **Tools**: `pandas`, `matplotlib`, `seaborn`  
    - Plot histograms and boxplots of porosity and permeability.
    - Calculate key statistics: mean, median, standard deviation.
    - Visualize trends against depth.

    **Why**: Understanding basic data behavior helps determine variability and identify trends or outliers before modeling.

    ---

    ### 📈 3. K-Means Clustering  
    **Tools**: `sklearn`, `pandas`, `matplotlib`  
    - Normalize porosity and log-permeability.
    - Apply K-means clustering (K=2 or 3).
    - Assign and label clusters (e.g., low, medium, high quality).

    **Why**: Clustering helps group data into meaningful zones without subjective thresholds—critical for reservoir classification.

    ---

    ### 📐 4. Cross-Well Comparison  
    **Tools**: `seaborn`, `matplotlib`  
    - Compare cluster distributions across both wells.
    - Analyze whether good-quality zones occur at similar depths.

    **Why**: Helps assess vertical and lateral consistency, which informs reservoir continuity and development strategy.

    ---

    ### 🧠 5. Geological Interpretation  
    **Tools**: `matplotlib`, `numpy`  
    - Describe what each cluster likely represents geologically.
    - Map clusters to depositional or diagenetic processes if possible.

    **Why**: Data has meaning only when interpreted geologically—this connects data science to real-world subsurface behavior.

    ---

    ### 🔮 6. Threshold-Based Productivity Classification  
    **Tools**: `pandas`, `numpy`  
    - Define porosity/permeability thresholds (e.g., >15% or >10⁻¹⁴ m²).
    - Classify zones based on these thresholds and compare with K-means results.

    **Why**: This offers a rule-based alternative to clustering and allows cross-validation of your machine learning classifications.

    ---

    ### 🌫️ 7. Fuzzy Logic Classification  
    **Tools**: `numpy`, `matplotlib`  
    - Define fuzzy membership functions for low/medium/high reservoir quality.
    - Visualize overlap and softness of classifications.

    **Why**: Real-world geological data often has uncertainty. Fuzzy logic allows soft classification and shows transitional zones.

    ---

    ### 🔗 8. Correlation & Feature Relationships  
    **Tools**: `pandas`, `seaborn`  
    - Use correlation matrices or scatter plots to understand relationships.
    - Assess whether porosity and permeability are strongly related.

    **Why**: Feature correlation supports clustering and geological interpretation. It also helps identify which features drive quality.

    ---

    ### 🧭 9. Visual Storytelling & Presentation  
    **Tools**: `matplotlib`, `seaborn`, `streamlit` (optional)  
    - Build plots that clearly explain your findings.
    - Organize your work into a coherent and readable final report.

    **Why**: Insight without communication is wasted. Well-structured plots and summaries allow your team to present findings with confidence.
    """)

    st.header("📤 Final Submission")
    st.markdown("""
    - ✅ PDF report with all findings, plots, and interpretations
    - ✅ Clean, organized code (Colab notebook or script)
    - ✅ Contribution paragraph for each student

    **Submit via**: Coospace → Capstone Project Folder  
    **Deadline**: Two weeks from today
    """)

    st.success("This is your opportunity to show mastery of geostatistical modeling, clustering, and scientific storytelling. Make it collaborative, creative, and professional!")

def main():
    capstone_project_page()

if __name__ == "__main__":
    main()
