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
    - Load Excel files using `pandas.read_excel()`.
    - Use `.isna()`, `.fillna()`, or `.replace()` to handle missing/zero values.
    - Apply `numpy.log10()` to permeability for transformation.

    ### 📊 2. Statistical Analysis
    - Use `pandas.describe()` for summary statistics.
    - Plot:
        - Histograms using `matplotlib.pyplot.hist()` or `seaborn.histplot()`
        - Boxplots using `seaborn.boxplot()`
        - Line plots by depth with `plt.plot()` for trends

    ### 📈 3. K-Means Clustering (Reservoir Zonation)
    - Normalize features using `sklearn.preprocessing.StandardScaler`.
    - Apply `KMeans` from `sklearn.cluster`.
    - Choose K = 2 or 3; use `elbow method` (`inertia_`) to justify.
    - Visualize clusters with:
        - Depth-colored line plots
        - 2D scatter of porosity vs log-permeability
        - Depth vs. cluster zone (color-coded)

    ### 📐 4. Cross-Well Comparison
    - Use grouped analysis: compare cluster means/depths between wells.
    - Highlight differences in zone thickness or quality.
    - Use `seaborn.catplot()` or `matplotlib` subplots to compare.

    ### 🧠 5. Interpretation & Report
    - Reflect on the geological significance of each cluster.
    - Discuss whether permeability dominates, or porosity plays a bigger role.
    - Bonus (Optional):
        - Try a 3D scatter (`matplotlib.axes3d`)
        - Use `Folium` for spatial plotting if coordinates available.
    """)

    # ─────────────────────────────────────────────────────────
    # Submission
    # ─────────────────────────────────────────────────────────
    st.header("📤 Final Submission")
    st.markdown("""
    - ✅ A **PDF report** with figures, analysis, and geological interpretations.
    - ✅ Python **notebooks or scripts** (`.ipynb` or `.py`) used in your analysis.
    - ✅ A list of group members and **brief description of each student’s contribution**.

    📁 Submit via: **Coospace > Capstone Project Folder**
    """)

    st.success("""
    Your project should demonstrate the integration of everything you've learned: 
    data preprocessing, statistical reasoning, probabilistic analysis, 
    and clustering-based classification. Make it practical, visual, and insightful!
    """)

def main():
    capstone_project_page()

if __name__ == "__main__":
    main()
