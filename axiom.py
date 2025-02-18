# axiom.py

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

def generate_random_drillholes(total_holes: int, n_high: int, n_medium: int, n_low: int) -> pd.DataFrame:
    """
    Generates a random set of drill holes with assigned ore-grade categories.
    
    Args:
        total_holes (int): Total number of drill holes to place.
        n_high (int): Number of High-grade holes.
        n_medium (int): Number of Medium-grade holes.
        n_low (int): Number of Low-grade holes.
    
    Returns:
        pd.DataFrame: A DataFrame with columns:
            - 'Drill Hole': Name or ID for each hole.
            - 'Grade Category': One of High, Medium, Low, or Unassigned.
            - 'X_Coord', 'Y_Coord': Random 2D coordinates for plotting.
    """
    # Create labels based on user inputs
    grade_labels = (["High"] * n_high) + (["Medium"] * n_medium) + (["Low"] * n_low)
    
    # Fill remainder with 'Unassigned' if total_holes > sum of assigned categories
    remainder = total_holes - len(grade_labels)
    if remainder > 0:
        grade_labels += ["Unassigned"] * remainder
    
    # Shuffle for random distribution of categories
    np.random.shuffle(grade_labels)
    
    # Generate random X, Y coordinates (range: -50 to +50)
    x_coords = np.random.randint(-50, 51, size=total_holes)
    y_coords = np.random.randint(-50, 51, size=total_holes)
    
    # Build the DataFrame
    data = {
        "Drill Hole": [f"Hole_{i+1}" for i in range(total_holes)],
        "Grade Category": grade_labels,
        "X_Coord": x_coords,
        "Y_Coord": y_coords
    }
    return pd.DataFrame(data)

def display_probability_axioms_ui(
    assigned_total: int,
    high_count: int,
    medium_count: int,
    low_count: int,
    p_high: float,
    p_medium: float,
    p_low: float
):
    """
    Displays a user-friendly UI explaining Probability Axioms in Action
    and Geological & Risk Context in a visually appealing layout.
    
    Args:
        assigned_total (int): Number of drill holes that have assigned categories (High, Medium, Low).
        high_count (int): Count of High-grade holes.
        medium_count (int): Count of Medium-grade holes.
        low_count (int): Count of Low-grade holes.
        p_high (float): Probability of selecting a High-grade hole from the assigned set.
        p_medium (float): Probability of selecting a Medium-grade hole.
        p_low (float): Probability of selecting a Low-grade hole.
    """

    # --- Probability Axioms Section ---
    with st.expander("📊 Probability Axioms in Action", expanded=True):
        # Top summary in columns
        col1, col2, col3, col4 = st.columns([1.2, 1, 1, 1])
        
        with col1:
            st.markdown("### Total Assigned Holes")
            st.write(f"**{assigned_total}**")
        
        with col2:
            st.markdown("### High-Grade")
            st.write(f"**{high_count}** (P = {p_high})")
        
        with col3:
            st.markdown("### Medium-Grade")
            st.write(f"**{medium_count}** (P = {p_medium})")
        
        with col4:
            st.markdown("### Low-Grade")
            st.write(f"**{low_count}** (P = {p_low})")

        # Optional: If you're using Streamlit >= 1.22, st.divider() adds a horizontal rule
        try:
            st.divider()
        except AttributeError:
            # If st.divider is not available in older Streamlit, just ignore it
            pass

        # Probability Axioms Explanation
        st.subheader("1) Non-Negativity")
        st.write("- All probabilities must be ≥ 0.")
        st.write(f"- Example: **P(High)** = {p_high} (which is indeed ≥ 0).")

        st.subheader("2) Total Probability = 1")
        total_prob = p_high + p_medium + p_low
        st.write("- For mutually exclusive, exhaustive categories:")
        st.latex(r"P(\text{High}) + P(\text{Medium}) + P(\text{Low}) = 1")
        st.write(f"- In this scenario: {p_high} + {p_medium} + {p_low} = **{total_prob:.2f}**")
        st.info("If this sum is ≈ 1.0, the categories cover all possible outcomes for the assigned holes.")

        st.subheader("3) Additive Rule")
        p_high_or_low = p_high + p_low
        st.write("- When events cannot overlap (mutually exclusive):")
        st.latex(r"P(\text{High OR Low}) = P(\text{High}) + P(\text{Low})")
        st.write(f"- Numerically: {p_high} + {p_low} = **{p_high_or_low:.2f}**")

    # --- Geological & Risk Context Section ---
    with st.expander("⛏️ Geological & Risk Context", expanded=True):
        st.write("""
        - **Economic Feasibility**: A higher proportion of High-grade ore 
          might be lucrative, but costs for deeper drilling, environmental impact, 
          and market fluctuations must be considered.
        - **Geotechnical Risks**: High-grade zones may correlate with 
          heavily fractured rock, impacting slope stability or underground workings.
        - **Exploration Strategy**: 
          - Example: If 40% of holes are High-grade, you might expand drilling 
            to confirm that zone’s continuity.  
          - Even a 20% Low-grade proportion can be significant if it extends 
            in volume or is easy to process.
        - **Efficient Resource Allocation**: 
          Probability helps decide drill-site prioritization, budget, 
          and timeline. If 'High or Low' is 60%, factor in the risk 
          of encountering mostly low-value ore.
        """)

        st.warning("""
        In real projects, data are more complex (multiple intervals per hole, 
        continuous grade values, advanced geostatistics, etc.). 
        Still, the **fundamental probability axioms** remain critical 
        for consistent, transparent analyses.
        """)

        # Key question
        st.write("### Key Question")
        st.info("""
        **How do basic probability axioms help us formalize uncertainty in geological exploration?**

        By ensuring probabilities remain coherent (no negatives, they sum to 1, 
        and mutually exclusive events are correctly handled). This structure 
        lets us systematically gauge the likelihood of finding high-grade ore, 
        informing data-driven decisions on risk and feasibility.
        """)

def main():
    """
    Main function to demonstrate an interactive app that generates
    random drill holes and applies probability axioms.
    """
    st.title("Dynamic Subsurface Ore Deposit Exploration (Enhanced UI)")

    st.write("""
    This **interactive Streamlit app** simulates a simplified subsurface ore deposit.
    You can adjust how many total holes are drilled and how many are classified as 
    High, Medium, or Low grade. We'll then demonstrate **basic probability axioms** 
    to quantify the uncertainty of selecting a High-grade hole at random.
    """)

    # -----------------------------
    # 1. User Controls in Sidebar
    # -----------------------------
    st.sidebar.header("User Inputs")
    total_holes = st.sidebar.slider(
        label="Total Drill Holes",
        min_value=1,
        max_value=30,
        value=5,
        step=1
    )
    n_high = st.sidebar.number_input(
        label="Number of High-grade Holes",
        min_value=0,
        max_value=total_holes,
        value=2,
        step=1
    )
    n_medium = st.sidebar.number_input(
        label="Number of Medium-grade Holes",
        min_value=0,
        max_value=total_holes,
        value=2,
        step=1
    )
    n_low = st.sidebar.number_input(
        label="Number of Low-grade Holes",
        min_value=0,
        max_value=total_holes,
        value=1,
        step=1
    )

    # Check if sum of assigned categories exceeds total holes
    if (n_high + n_medium + n_low) > total_holes:
        st.sidebar.error("Sum of High, Medium, and Low cannot exceed the total number of holes!")
        st.stop()

    # --------------------------------------------
    # 2. Generate and Display the Drill Holes Data
    # --------------------------------------------
    df = generate_random_drillholes(total_holes, n_high, n_medium, n_low)

    st.subheader("Drill Holes Dataset")
    st.write("""
    Below is the dataset showing each drill hole's **ore-grade category** 
    and random **2D coordinates** (for illustrative mapping).
    If High + Medium + Low < Total, the remainder are labeled **'Unassigned'**.
    """)
    st.dataframe(df)

    # -------------------------------------------
    # 3. Plot the Drill Holes in 2D Space
    # -------------------------------------------
    st.subheader("2D Layout of Drill Holes")
    st.write("Each point corresponds to a drill hole, colored by its Grade Category.")

    color_scale = alt.Scale(
        domain=["High", "Medium", "Low", "Unassigned"],
        range=["red", "orange", "green", "gray"]
    )

    chart = (
        alt.Chart(df)
        .mark_circle(size=100)
        .encode(
            x="X_Coord:Q",
            y="Y_Coord:Q",
            color=alt.Color("Grade Category:N", scale=color_scale),
            tooltip=["Drill Hole", "Grade Category"]
        )
        .properties(width=600, height=400)
        .interactive()
    )
    st.altair_chart(chart, use_container_width=True)

    # ------------------------------------
    # 4. Probability Calculations & Axioms
    # ------------------------------------
    # Filter out 'Unassigned' holes
    assigned_df = df[df["Grade Category"] != "Unassigned"]
    assigned_total = len(assigned_df)

    # Compute probabilities
    if assigned_total > 0:
        high_count = len(assigned_df[assigned_df["Grade Category"] == "High"])
        medium_count = len(assigned_df[assigned_df["Grade Category"] == "Medium"])
        low_count = len(assigned_df[assigned_df["Grade Category"] == "Low"])
        
        p_high = round(high_count / assigned_total, 3)
        p_medium = round(medium_count / assigned_total, 3)
        p_low = round(low_count / assigned_total, 3)
    else:
        # If no holes are assigned, probabilities are zero
        high_count = medium_count = low_count = 0
        p_high = p_medium = p_low = 0

    # Display the Probability Axioms UI
    display_probability_axioms_ui(
        assigned_total,
        high_count,
        medium_count,
        low_count,
        p_high,
        p_medium,
        p_low
    )

if __name__ == "__main__":
    main()
