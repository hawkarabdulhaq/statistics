import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io  # For creating in-memory file-like objects

def generate_dataset(num_samples: int, foram_std: float, variation: int) -> pd.DataFrame:
    """
    Generate a paleoenvironmental dataset with the specified number of samples,
    standard deviation for Foraminifera counts, and variation (number of outliers).
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

def main():
    # ---------------------------------------------------
    # TOP SECTION: Setting page config & showing banner
    # ---------------------------------------------------
    st.set_page_config(
        page_title="Basic Statistical Understanding",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Display banner image (ensure 'banner.png' is in the same directory or an accessible path)
    st.image("banner.png", use_container_width=True)

    # ------------------ SIDEBAR ------------------
    st.sidebar.title("Dataset Controls")
    st.sidebar.write(
        """
        **Step 1:** Adjust the parameters to generate your dataset.  
        **Step 2:** Click the button below to create and visualize the data.  
        **Step 3:** Download the CSV file if you want to save it locally.
        """
    )
    
    num_samples = st.sidebar.slider("Number of Samples", 20, 200, 100, step=5)
    foram_std = st.sidebar.slider("Std Dev for Foraminifera", 0.1, 50.0, 5.0, step=0.1)
    variation = st.sidebar.slider("Variation (Outliers)", 0, 10, 2, step=1)
    
    with st.sidebar.expander("Additional Info"):
        st.write(
            """
            - **Foraminifera_Count**: Represents fossil abundance; high outliers
              might indicate rich fossil layers or potential data errors.
            - **Calcite_Percentage**: Reflects carbonate content in the sediment.
              Low values may indicate siliciclastic input or dissolution events.
            - **Depth_m**: Depth in meters, starting at 100.
            - **Outliers**: Random anomalies introduced to simulate real-world data issues.
            """
        )
    
    generate_button = st.sidebar.button("Generate & Analyze Dataset")

    # ------------------ MAIN CONTENT ------------------
    st.write(
        """
        This app demonstrates how to generate and interpret a synthetic paleoenvironmental dataset.
        We'll explore **basic statistics**, **outlier detection**, **distributions**, and **correlations** 
        through various **data visualizations** and analyses.
        """
    )
    
    if generate_button:
        # Generate Dataset
        df = generate_dataset(num_samples, foram_std, variation)
        
        # Create a CSV file in memory (not saved locally)
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False)
        csv_data = csv_buffer.getvalue()  # This is the CSV as a string
        
        # Provide a download button for the CSV
        st.download_button(
            label="Download CSV",
            data=csv_data,
            file_name="paleo_dataset.csv",
            mime="text/csv"
        )

        # Part 1: Data Preview & Quick Stats
        st.header("Part 1: Data Overview")
        col1, col2 = st.columns([1, 2])
        with col1:
            st.subheader("Dataset Preview")
            st.dataframe(df.head(10))
            st.caption("First 10 rows for quick inspection.")
        with col2:
            st.subheader("Summary Statistics")
            st.write(df.describe())
            st.caption(
                """
                **Mean, Standard Deviation, Min/Max** for each column.  
                Pay attention to extreme values that might indicate outliers.
                """
            )
        
        # Calculate basic stats
        mean_foram = df['Foraminifera_Count'].mean()
        median_foram = df['Foraminifera_Count'].median()
        mean_calcite = df['Calcite_Percentage'].mean()
        median_calcite = df['Calcite_Percentage'].median()

        with st.expander("Statistical Interpretation Tips"):
            st.markdown(
                f"""
                - **Foraminifera (Mean vs. Median):**  
                  Mean = `{mean_foram:.2f}`, Median = `{median_foram:.2f}`  
                  A big difference could indicate outliers or skew.
                - **Calcite (Mean vs. Median):**  
                  Mean = `{mean_calcite:.2f}`, Median = `{median_calcite:.2f}`  
                  Helps determine if there's a *normal* distribution or a *skewed* one.
                """
            )

        # Part 2: Distributions (Histograms)
        st.header("Part 2: Distribution of Key Variables")
        col3, col4 = st.columns(2)
        
        with col3:
            st.subheader("Histogram: Foraminifera Counts")
            fig_foram_hist = plt.figure(figsize=(5, 4))
            plt.hist(df['Foraminifera_Count'], bins=10, color='skyblue', edgecolor='black')
            plt.axvline(mean_foram, color='red', linestyle='dashed', linewidth=1, label=f"Mean: {mean_foram:.2f}")
            plt.axvline(median_foram, color='green', linestyle='dotted', linewidth=1, label=f"Median: {median_foram:.2f}")
            plt.title("Foraminifera Distribution")
            plt.xlabel("Foraminifera Count")
            plt.ylabel("Frequency")
            plt.legend()
            st.pyplot(fig_foram_hist)
        
        with col4:
            st.subheader("Histogram: Calcite Percentage")
            fig_calcite_hist = plt.figure(figsize=(5, 4))
            plt.hist(df['Calcite_Percentage'], bins=10, color='lightgreen', edgecolor='black')
            plt.axvline(mean_calcite, color='red', linestyle='dashed', linewidth=1, label=f"Mean: {mean_calcite:.2f}")
            plt.axvline(median_calcite, color='green', linestyle='dotted', linewidth=1, label=f"Median: {median_calcite:.2f}")
            plt.title("Calcite Distribution")
            plt.xlabel("Calcite Percentage")
            plt.ylabel("Frequency")
            plt.legend()
            st.pyplot(fig_calcite_hist)

        st.caption(
            """
            **Observations:**  
            - A gap between the red (mean) and green (median) lines often signifies skew or outliers.  
            - Check if the distribution is unimodal or if multiple peaks exist, indicating mixed sediment sources.
            """
        )

        # Part 3: Box Plots
        st.header("Part 3: Box Plots & Outlier Detection")
        col5, col6 = st.columns(2)
        
        with col5:
            st.subheader("Box Plot: Foraminifera Counts")
            fig_foram_box = plt.figure(figsize=(4, 6))
            plt.boxplot(df['Foraminifera_Count'], patch_artist=True, boxprops=dict(facecolor='lightblue'))
            plt.title("Foraminifera Box Plot")
            plt.ylabel("Foraminifera Count")
            st.pyplot(fig_foram_box)
        
        with col6:
            st.subheader("Box Plot: Calcite Percentage")
            fig_calcite_box = plt.figure(figsize=(4, 6))
            plt.boxplot(df['Calcite_Percentage'], patch_artist=True, boxprops=dict(facecolor='lightcoral'))
            plt.title("Calcite Box Plot")
            plt.ylabel("Calcite Percentage")
            st.pyplot(fig_calcite_box)

        st.caption(
            """
            **Interpretation:**  
            - Box plots reveal quartiles (Q1, median, Q3) and potential outliers.  
            - Look for points (if any) lying outside the whiskers—these might be genuine anomalies or errors.
            """
        )

        # Part 4: Relationship with Depth
        st.header("Part 4: Scatter Plots - Relationship with Depth")
        col7, col8 = st.columns(2)
        
        with col7:
            st.subheader("Foraminifera vs. Depth")
            fig_foram_depth = plt.figure(figsize=(5, 4))
            plt.scatter(df["Foraminifera_Count"], df["Depth_m"], c='blue', alpha=0.7)
            plt.gca().invert_yaxis()
            plt.title("Foraminifera Count vs. Depth")
            plt.xlabel("Foraminifera Count")
            plt.ylabel("Depth (m)")
            st.pyplot(fig_foram_depth)
        
        with col8:
            st.subheader("Calcite % vs. Depth")
            fig_calcite_depth = plt.figure(figsize=(5, 4))
            plt.scatter(df["Calcite_Percentage"], df["Depth_m"], c='green', alpha=0.7)
            plt.gca().invert_yaxis()
            plt.title("Calcite Percentage vs. Depth")
            plt.xlabel("Calcite Percentage")
            plt.ylabel("Depth (m)")
            st.pyplot(fig_calcite_depth)

        st.caption(
            """
            **Observations:**  
            - In a real core or well log, you might see transitions from low to high carbonate content,
              indicating shifts in depositional environments.  
            - Sudden spikes may indicate discrete events or outliers in measurement.
            """
        )

        # Part 5: Correlation Analysis
        st.header("Part 5: Correlation & Combined Analysis")
        st.write(
            """
            **Correlation** helps us understand if higher Foraminifera counts generally accompany 
            higher or lower Calcite percentages, and vice versa.  
            A strong correlation (positive or negative) could be geologically significant.
            """
        )
        fig_corr = plt.figure(figsize=(4, 3))
        sns.heatmap(df[['Foraminifera_Count', 'Calcite_Percentage']].corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
        plt.title("Correlation Heatmap")
        st.pyplot(fig_corr)

        st.caption(
            """
            **How to interpret correlation:**  
            - If the correlation is close to +1, the two variables tend to increase together.  
            - If it's near -1, one variable tends to increase while the other decreases.  
            - If it's around 0, there's no clear linear relationship.
            """
        )
        
        st.write("### Overlaid Histograms (Bonus View)")
        st.write("Comparing the distributions of Foraminifera Count and Calcite Percentage in one chart can reveal overall variance.")
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
            **Summary & Teaching Notes:**  
            - This step-by-step approach shows how different visualizations (histograms, box plots, scatter plots, correlation matrix) 
              can be used to glean insights from geological data.  
            - Emphasize how outliers, skew, and correlation can inform or mislead geoscientific interpretations.
            - In real-world scenarios, always consider the geological context (depositional environments, diagenetic processes, etc.) 
              when deciding whether outliers are anomalies or data errors.
            """
        )

    else:
        st.warning("Use the sidebar to generate and analyze your dataset.")

if __name__ == "__main__":
    main()
