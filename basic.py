import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io  # For creating in-memory file-like objects

def generate_dataset(num_samples: int, foram_std: float, variation: int) -> pd.DataFrame:
    """
    Generates a synthetic paleoenvironmental dataset with:
      - Foraminifera_Count (some random distribution with possible outliers),
      - Calcite_Percentage (simulates carbonate content),
      - Depth_m (incremental starting at 100).

    The 'variation' parameter introduces outliers randomly.
    """
    # Baseline means
    mean_foram = 25
    mean_calcite = 45
    calcite_std = 3

    # Depth Range
    depth_start = 100
    depth_values = list(range(depth_start, depth_start + num_samples))
    
    # Normal distribution for Foraminifera Counts
    foram_counts = np.random.normal(loc=mean_foram, scale=foram_std, size=num_samples)
    foram_counts = np.clip(foram_counts, a_min=0, a_max=None)  # Avoid negative values

    # Normal distribution for Calcite Percentage
    calcite_perc = np.random.normal(loc=mean_calcite, scale=calcite_std, size=num_samples)
    calcite_perc = np.clip(calcite_perc, a_min=0, a_max=100)  # Restrict to 0-100%

    # Round for clarity
    foram_counts = [round(val) for val in foram_counts]
    calcite_perc = [round(val, 1) for val in calcite_perc]

    # Introduce "variation" outliers
    outlier_indices = np.random.choice(num_samples, size=variation, replace=False)
    for idx in outlier_indices:
        if np.random.rand() < 0.5:
            # High outlier for Foraminifera
            foram_counts[idx] += np.random.randint(50, 200)
        else:
            # Low outlier for Calcite
            calcite_perc[idx] = max(0, calcite_perc[idx] - np.random.randint(20, 45))
    
    data = {
        "Sample_ID": [f"S{i+1}" for i in range(num_samples)],
        "Depth_m": depth_values,
        "Foraminifera_Count": foram_counts,
        "Calcite_Percentage": calcite_perc
    }
    return pd.DataFrame(data)

def basic_statistics_page():
    """
    Main function for the "Basic Statistics" page.
    It includes dataset generation, histograms, box plots, correlation, etc.
    """
    st.title("Basic Statistics")
    st.write(
        """
        This page allows you to **generate a synthetic dataset** with 
        foraminifera counts, calcite percentages, and depths. 
        Then you can **visualize** histograms, box plots, and correlation heatmaps 
        to understand outliers, skew, and relationships.
        """
    )
    
    # Sidebar Controls for dataset generation
    st.sidebar.title("Basic Stats - Dataset Controls")
    num_samples = st.sidebar.slider("Number of Samples", 20, 200, 100, step=5)
    foram_std = st.sidebar.slider("Std Dev for Foraminifera", 0.1, 50.0, 5.0, step=0.1)
    variation = st.sidebar.slider("Variation (Outliers)", 0, 10, 2, step=1)

    generate_button = st.sidebar.button("Generate & Analyze Dataset")

    if generate_button:
        # Generate Dataset
        df = generate_dataset(num_samples, foram_std, variation)
        
        # Offer CSV Download
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False)
        csv_data = csv_buffer.getvalue()
        
        st.download_button(
            label="Download CSV",
            data=csv_data,
            file_name="paleo_dataset.csv",
            mime="text/csv"
        )

        # Show Data & Stats
        st.header("1. Data Overview")
        col1, col2 = st.columns([1, 2])
        with col1:
            st.subheader("Dataset Preview")
            st.dataframe(df.head(10))
            st.caption("First 10 rows for a quick look.")
        with col2:
            st.subheader("Summary Statistics")
            st.write(df.describe())
            st.caption("Check for extreme values or big differences in mean vs. median.")

        # Calculate some stats for the visuals
        mean_foram = df['Foraminifera_Count'].mean()
        median_foram = df['Foraminifera_Count'].median()
        mean_calcite = df['Calcite_Percentage'].mean()
        median_calcite = df['Calcite_Percentage'].median()

        # Histograms
        st.header("2. Distributions (Histograms)")
        col3, col4 = st.columns(2)

        with col3:
            st.subheader("Foraminifera Distribution")
            fig_foram_hist = plt.figure(figsize=(5, 4))
            plt.hist(df['Foraminifera_Count'], bins=10, color='skyblue', edgecolor='black')
            plt.axvline(mean_foram, color='red', linestyle='dashed', linewidth=1, label=f"Mean: {mean_foram:.2f}")
            plt.axvline(median_foram, color='green', linestyle='dotted', linewidth=1, label=f"Median: {median_foram:.2f}")
            plt.title("Foraminifera Counts")
            plt.xlabel("Counts")
            plt.ylabel("Frequency")
            plt.legend()
            st.pyplot(fig_foram_hist)

        with col4:
            st.subheader("Calcite Distribution")
            fig_calcite_hist = plt.figure(figsize=(5, 4))
            plt.hist(df['Calcite_Percentage'], bins=10, color='lightgreen', edgecolor='black')
            plt.axvline(mean_calcite, color='red', linestyle='dashed', linewidth=1, label=f"Mean: {mean_calcite:.2f}")
            plt.axvline(median_calcite, color='green', linestyle='dotted', linewidth=1, label=f"Median: {median_calcite:.2f}")
            plt.title("Calcite Percentage")
            plt.xlabel("Calcite (%)")
            plt.ylabel("Frequency")
            plt.legend()
            st.pyplot(fig_calcite_hist)

        # Box Plots
        st.header("3. Box Plots & Outlier Detection")
        col5, col6 = st.columns(2)

        with col5:
            st.subheader("Foraminifera Box Plot")
            fig_foram_box = plt.figure(figsize=(4, 6))
            plt.boxplot(df['Foraminifera_Count'], patch_artist=True, boxprops=dict(facecolor='lightblue'))
            plt.title("Foraminifera Box Plot")
            plt.ylabel("Foraminifera Count")
            st.pyplot(fig_foram_box)

        with col6:
            st.subheader("Calcite Box Plot")
            fig_calcite_box = plt.figure(figsize=(4, 6))
            plt.boxplot(df['Calcite_Percentage'], patch_artist=True, boxprops=dict(facecolor='lightcoral'))
            plt.title("Calcite Box Plot")
            plt.ylabel("Calcite Percentage")
            st.pyplot(fig_calcite_box)

        # Scatter Plots vs. Depth
        st.header("4. Relationship with Depth")
        col7, col8 = st.columns(2)
        with col7:
            st.subheader("Foraminifera vs Depth")
            fig_foram_depth = plt.figure(figsize=(5, 4))
            plt.scatter(df["Foraminifera_Count"], df["Depth_m"], color='blue', alpha=0.7)
            plt.gca().invert_yaxis()
            plt.title("Foraminifera vs. Depth (m)")
            plt.xlabel("Foraminifera Count")
            plt.ylabel("Depth (m)")
            st.pyplot(fig_foram_depth)

        with col8:
            st.subheader("Calcite vs Depth")
            fig_calcite_depth = plt.figure(figsize=(5, 4))
            plt.scatter(df["Calcite_Percentage"], df["Depth_m"], color='green', alpha=0.7)
            plt.gca().invert_yaxis()
            plt.title("Calcite % vs. Depth (m)")
            plt.xlabel("Calcite (%)")
            plt.ylabel("Depth (m)")
            st.pyplot(fig_calcite_depth)

        # Correlation Analysis
        st.header("5. Correlation & Combined Analysis")
        st.write("Investigate how foraminifera counts correlate with calcite percentages.")
        fig_corr = plt.figure(figsize=(4, 3))
        sns.heatmap(df[['Foraminifera_Count', 'Calcite_Percentage']].corr(),
                    annot=True, cmap='coolwarm', vmin=-1, vmax=1)
        plt.title("Correlation Heatmap")
        st.pyplot(fig_corr)

        st.write("### Overlaid Histograms")
        fig_overlay = plt.figure(figsize=(7, 4))
        plt.hist(df['Foraminifera_Count'], bins=12, alpha=0.5, label='Foraminifera', color='blue')
        plt.hist(df['Calcite_Percentage'], bins=12, alpha=0.5, label='Calcite %', color='orange')
        plt.title("Overlaid Distributions")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.legend()
        st.pyplot(fig_overlay)

        st.info(
            """
            **Insights**:
            - **Outliers** can skew mean/median.
            - **Scatter vs. Depth** can reveal layering or transitions in the stratigraphic column.
            - **Correlation** indicates if foraminifera increases/decreases with calcite (a higher correlation
              might mean they co-vary in certain depositional environments).
            """
        )
    else:
        st.warning("Use the sidebar to generate and analyze your dataset. Click the button to proceed.")
