import streamlit as st

# Home Project Page: Elevation-Based Risk Mapping
def homeproject_page():
    st.title("🏔️ Elevation-Based Risk Mapping Project")

    # ──────────────────────────────────────────────
    # 1. Project Introduction
    # ──────────────────────────────────────────────
    st.header("📚 1. Project Introduction")
    st.markdown("""
    **Purpose**:
    - Understand how elevation influences natural hazards (floods, landslides).
    - Use statistical methods (conditional probability, Bayesian inference) to create hazard risk maps.

    **Dataset**:
    - Use `Elevation_backup.xyz` (longitude, latitude, elevation).

    **Tools Needed**:
    - Python, Google Colab.
    - Libraries: NumPy, pandas, matplotlib, rasterio, folium.

    **Estimated Time**: 30 min
    """)

    # ──────────────────────────────────────────────
    # 2. Data Preparation & Initial Exploration
    # ──────────────────────────────────────────────
    st.header("🔬 2. Data Preparation & Initial Exploration")
    st.markdown("""
    **Tasks**:
    - Load elevation data (`Elevation_backup.xyz`).
    - Calculate basic statistics: mean, median, min/max elevations.
    - Visualize:
        - Histogram of elevation values.
        - Scatter plot (elevation vs. coordinates).

    **Output**:
    - Brief summary (~1 paragraph) of data observations and quality.

    **Estimated Time**: 60 min
    """)

    # ──────────────────────────────────────────────
    # 3. Defining Elevation Thresholds for Risk Zones
    # ──────────────────────────────────────────────
    st.header("🎯 3. Defining Elevation Thresholds for Risk Zones")
    st.markdown("""
    **Tasks**:
    - Define clear elevation thresholds for risk zones (e.g., lowland ≤395m, highland >405m).
    - Visualize these zones with scatter plots/maps.
    - Provide rationale based on data or literature.

    **Output**:
    - Explanation (½ page) of chosen thresholds with visuals.

    **Estimated Time**: 45 min
    """)

    # ──────────────────────────────────────────────
    # 4. Calculating Conditional Probabilities
    # ──────────────────────────────────────────────
    st.header("📈 4. Calculating Conditional Probabilities")
    st.markdown("""
    **Tasks**:
    - Compute conditional probabilities such as:
        - $P(\text{Flood Risk Zone} | \text{Latitude} > threshold)$
        - $P(\text{Landslide Risk Zone} | \text{Elevation} \; range)$
    - Experiment with various latitude/longitude thresholds.
    - Visualize conditional probabilities.

    **Output**:
    - Summary table or graph of conditional probability findings.

    **Estimated Time**: 90 min
    """)

    # ──────────────────────────────────────────────
    # 5. Bayesian Updating of Risk Maps
    # ──────────────────────────────────────────────
    st.header("🔄 5. Bayesian Updating of Risk Maps")
    st.markdown("""
    **Tasks**:
    - Use Bayesian inference to update hazard predictions with hypothetical new data (e.g., rainfall, river proximity).
    - Example Bayesian updating formula:

    $$
    P(\text{Hazard}|\text{New Data}) = \frac{P(\text{New Data}|\text{Hazard}) \cdot P(\text{Hazard})}{P(\text{New Data})}
    $$

    - Generate updated risk maps (Folium or raster plots).

    **Output**:
    - Interactive/static Bayesian updated risk maps.

    **Estimated Time**: 75 min
    """)

    # ──────────────────────────────────────────────
    # 6. Interpretation, Reflection, and Reporting
    # ──────────────────────────────────────────────
    st.header("🗒️ 6. Interpretation, Reflection, and Reporting")
    st.markdown("""
    **Tasks**:
    - Summarize key findings (~½–1 page):
        - How Bayesian updating influenced risk assessments.
        - Potential real-world applications.
    - Discuss limitations or uncertainties.
    - Suggest improvements or further data.

    **Final Output**:
    - Concise document (PDF):
        - Initial observations
        - Risk zone justification
        - Conditional probabilities
        - Bayesian updated risk map visuals
        - Summary reflection & applications

    **Estimated Time**: 60 min
    """)

    # ──────────────────────────────────────────────
    # Deliverables Checklist
    # ──────────────────────────────────────────────
    st.header("📝 Deliverables Checklist")
    st.markdown("""
    Ensure your submission includes:

    - [ ] Data exploration summary.
    - [ ] Defined elevation-based risk zones (with justification).
    - [ ] Conditional probability calculations (tables/plots).
    - [ ] Bayesian updated risk map visualization.
    - [ ] Reflection and interpretation.

    **Total Estimated Project Time**: ~6 hours
    """)

    st.success("Good luck, and enjoy your analysis!")

# Main page loader for Streamlit app
def main():
    homeproject_page()

if __name__ == "__main__":
    main()
