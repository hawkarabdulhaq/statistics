import streamlit as st

# Collaborative Home Project: Elevation-Based Risk Mapping
def homeproject_page():
    st.title("🏔️ Collaborative Project: Elevation-Based Risk Mapping")

    st.info("This is a **group project** to be completed collaboratively by **5 students**. Each student should clearly document their individual contributions.")

    # ──────────────────────────────────────────────
    # 1. Project Overview and Objectives
    # ──────────────────────────────────────────────
    st.header("📚 Project Overview")
    st.markdown("""
    **Objectives:**
    - Understand how elevation influences natural hazards such as floods and landslides.
    - Apply statistical methods (conditional probability, Bayesian inference) to develop hazard risk maps.

    **Dataset:**
    - Utilize the provided elevation data in dataset 2 (`Elevation_backup.xyz`).

    **Tools & Libraries:**
    - Python, Google Colab
    - NumPy, pandas, matplotlib, rasterio, folium

    **Project Duration:** Approximately **6 hours** in total
    """)

    # ──────────────────────────────────────────────
    # 2. Group Structure & Task Allocation
    # ──────────────────────────────────────────────
    st.header("👥 Group Structure & Task Allocation")
    st.markdown("""
    Divide the following roles among the five group members clearly:

    1. **Data Preparation Specialist**: Data loading, initial exploration, summary statistics.
    2. **Visualization Expert**: Creating histograms, scatter plots, and risk zone visuals.
    3. **Risk Zone Analyst**: Defining elevation thresholds and justifying risk zones.
    4. **Probability Analyst**: Calculating conditional probabilities and interpreting results.
    5. **Bayesian Analyst**: Performing Bayesian updating and generating interactive risk maps.

    Clearly document each member's contribution in your final report.
    """)

    # ──────────────────────────────────────────────
    # 3. Tasks and Deliverables
    # ──────────────────────────────────────────────
    st.header("📌 Tasks and Deliverables")

    st.subheader("🔎 1. Data Preparation & Exploration")
    st.markdown("""
    - Load the elevation dataset (`Elevation_backup.xyz`).
    - Compute and document mean, median, min, max, and standard deviation.
    - Visualize data with:
        - Elevation histogram
        - Scatter plot of elevation vs. spatial coordinates
    **Deliverable:** Brief summary (~1 paragraph) of data quality and key observations.
    **Estimated Time:** 60 min
    """)

    st.subheader("🌐 2. Defining Elevation Thresholds for Risk Zones")
    st.markdown("""
    - Define elevation-based thresholds (e.g., Lowland ≤ 395m, Highland > 405m).
    - Justify chosen thresholds through literature or data patterns.
    - Provide visualizations of these zones on scatter plots/maps.
    **Deliverable:** Rationale (½ page) and visualizations for chosen thresholds.
    **Estimated Time:** 60 min
    """)

    st.subheader("📈 3. Conditional Probability Analysis")
    st.markdown("""
    - Calculate probabilities such as:
        - $P(\text{Flood Risk} | \text{Latitude} > threshold)$
        - $P(\text{Landslide Risk} | \text{Elevation} \; range)$
    - Experiment with different spatial thresholds.
    **Deliverable:** Summary tables and/or graphs of conditional probabilities.
    **Estimated Time:** 90 min
    """)

    st.subheader("🔄 4. Bayesian Updating of Risk Predictions")
    st.markdown("""
    - Apply Bayesian inference to refine hazard predictions with additional data (e.g., hypothetical rainfall, proximity to rivers).
    - Generate and present updated risk maps.
    **Deliverable:** Interactive or static Bayesian-updated risk maps.
    **Estimated Time:** 90 min
    """)

    st.subheader("📝 5. Interpretation and Final Report")
    st.markdown("""
    - Summarize the project's findings:
        - How did Bayesian updating affect risk assessment?
        - Discuss practical implications of your risk mapping.
        - Acknowledge limitations and propose improvements.

    **Final Deliverable:** Concise PDF report (1–2 pages) containing:
    - Initial exploration insights
    - Risk zone definitions and justifications
    - Conditional probability results
    - Bayesian updated maps
    - Individual student contributions
    - Reflection and recommendations

    **Estimated Time:** 60 min
    """)

    # ──────────────────────────────────────────────
    # Submission Guidelines
    # ──────────────────────────────────────────────
    st.header("✅ Submission Guidelines")
    st.markdown("""
    Your group submission must clearly indicate:

    - **Names and roles** of all 5 participants.
    - Clearly defined individual contributions.
    - Organized PDF report with visuals and concise explanations.

    Submit the report on Coospace as instructed.

    **Total Estimated Project Time:** ~6 hours
    """)

    st.success("Best of luck! Collaborate effectively and enjoy your project.")

# Main page loader
def main():
    homeproject_page()

if __name__ == "__main__":
    main()
