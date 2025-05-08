import streamlit as st

def capstone_project_page():
    st.title("🎓 Capstone Project: Reservoir Quality Classification & Clustering")

    st.header("📘 Project Overview")
    st.markdown("""
    This **Capstone Project** invites your team to collaboratively explore and classify reservoir layers 
    from multiple wells using the statistical, probabilistic, and clustering tools you’ve learned.

    **Objective**:  
    Use real subsurface data to classify reservoir quality zones (high, medium, low) using statistical trends, 
    K-means clustering, and Bayesian/fuzzy logic.

    **Provided Data**:
    - [Well 1](https://github.com/hawkarabdulhaq/statistics/blob/main/input/Well-1.xlsx)
    - [Well 2](https://github.com/hawkarabdulhaq/statistics/blob/main/input/Well-2.xlsx)

    *(Three more wells will follow.)*

    **Team Size**: 5 students  
    **Deadline**: 2 weeks  
    **Deliverables**: PDF report + code (.ipynb or .py)
    """)

    st.header("🧩 Tasks and Python Implementation Suggestions")

    st.markdown("""
    ### 🔍 1. Data Cleaning & Preparation
    - **Tools**: `pandas`, `numpy`
    - Read Excel: `pd.read_excel()`
    - Clean zero/missing values: `df.replace()`, `df.dropna()`
    - Apply log transform: `np.log10(df['Permeability'])`

    ### 📊 2. Statistical Analysis
    - **Tools**: `pandas`, `matplotlib`, `seaborn`
    - Describe stats: `df.describe()`
    - Histogram: `plt.hist()` or `sns.histplot()`
    - Boxplot: `sns.boxplot()`
    - Depth trend: `plt.plot(depth, porosity)`

    ### 📈 3. K-Means Clustering
    - **Tools**: `sklearn.preprocessing.StandardScaler`, `sklearn.cluster.KMeans`
    - Normalize: `StandardScaler().fit_transform()`
    - Apply K-means: `KMeans(n_clusters=3).fit()`
    - Add cluster labels: `df['Cluster'] = kmeans.labels_`
    - Depth vs Cluster: `plt.scatter(depth, cluster)`

    ### 📐 4. Cross-Well Comparison
    - **Tools**: `matplotlib`, `seaborn`
    - Compare depth profiles of clusters across wells.
    - Use side-by-side plots: `plt.subplot(1,2,...)`

    ### 🧠 5. Geological Interpretation
    - Map clusters to geological meaning (facies, flow zones).
    - Support with plots or cross sections.
    - Add annotations: `plt.text()`, `plt.annotate()`

    ### 🔮 6. Threshold-Based Productivity Classification
    - **Tools**: `numpy`, `matplotlib`
    - Define thresholds (e.g., porosity > 0.12).
    - Use logic: `np.where(df['Porosity'] > 0.12, "Good", "Poor")`
    - Apply Bayes' Rule manually or with `scipy.stats.bayes_mvs()`

    ### 🌫️ 7. Fuzzy Logic Classification
    - **Tools**: `numpy`, `matplotlib`
    - Define fuzzy sets using linear functions.
    - Membership: `np.clip((x - a) / (b - a), 0, 1)`
    - Plot: `plt.plot(x, membership_function)`

    ### 🔗 8. Correlation & Feature Relationships
    - **Tools**: `seaborn`, `pandas`
    - Correlation matrix: `df.corr()`
    - Heatmap: `sns.heatmap()`
    - Pairplot: `sns.pairplot(df[['Porosity', 'Permeability']])`

    ### 📊 9. Visual Storytelling & Presentation
    - **Tools**: `matplotlib`, `seaborn`, `folium` (optional), `Streamlit` (bonus)
    - Use clear titles, labels, legends: `plt.title()`, `plt.xlabel()`, etc.
    - Color code zones, save high-res images: `plt.savefig()`
    - (Optional) Interactive: `folium.Map()`, `st.pyplot()`, `st.map()`

    """)

    st.header("📤 Final Submission")
    st.markdown("""
    Your submission must include:
    - ✅ Final report (PDF)
    - ✅ Python script or Colab notebook
    - ✅ Member names and contributions

    **Submit to**: Coospace > Capstone Project Folder
    """)

    st.success("Use this project to demonstrate your full journey through modeling, statistics, probability, and geoscientific insight. Make it clear, collaborative, and creative!")

def main():
    capstone_project_page()

if __name__ == "__main__":
    main()
