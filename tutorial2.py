import streamlit as st

def tutorial2_page():
    """
    Tutorial 2: Mean, Median, and Mode of Earthquake Magnitudes
    """
    # Display the banner image from GitHub
    st.image(
        "https://raw.githubusercontent.com/hawkarabdulhaq/statistics/main/input/02.jpg", 
        use_container_width=True
    )

    st.title("Tutorial 2: Mean, Median, and Mode of Earthquake Magnitudes")

    st.markdown(
        """
        This tutorial shows you how to:
        
        - **Download** an earthquake dataset (`earthquakes.csv`).  
        - **Compute** the **mean**, **median**, and **mode** of earthquake magnitudes.  
        - **Visualize** magnitudes in a histogram and identify any common magnitude values (discrete or near-discrete data).

        ---
        ### Getting Started in Google Colab
        
        1. **Obtain `earthquakes.csv`**  
           - Use your **dataset page** (or the USGS API) to generate and download a CSV.  
           - Ensure the file has **at least**: `magnitude` (plus optional `time`, `latitude`, `longitude`, `depth`).

        2. **Open a Colab Notebook**  
           - Go to [Google Colab](https://colab.research.google.com/).  
           - Create a new notebook and run:
             ```python
             from google.colab import drive
             drive.mount('/content/drive')
             ```
           - Place `earthquakes.csv` into `/content/sample_data/` (or your preferred folder).

        3. **Download & Run `stats_overview.py`**  
           - Copy the code below into a file named **`stats_overview.py`**.  
           - In Colab, run:
             ```python
             !python stats_overview.py
             ```
           - The script prints **mean, median, mode** and shows two plots:  
             - A **histogram** of magnitudes.  
             - A **bar chart** showing discrete magnitude counts (useful for checking if a mode stands out).

        ---
        ### `stats_overview.py` Script
        Below is a minimal script focusing on central tendencies and simple plots:
        """
    )

    script_code = """\
import pandas as pd
import matplotlib.pyplot as plt
from statistics import mode, StatisticsError

# Path to your CSV
csv_path = '/content/sample_data/earthquakes.csv'

def main():
    # 1. Read dataset
    df = pd.read_csv(csv_path)
    if 'magnitude' not in df.columns:
        print("ERROR: CSV must contain a 'magnitude' column.")
        return

    print("Dataset Shape:", df.shape)
    print("\\nFirst 5 Rows:")
    print(df.head())

    # 2. Basic stats
    print("\\nSummary Statistics (Pandas describe):")
    print(df.describe())

    # 3. Compute mean, median, mode for 'magnitude'
    magnitudes = df['magnitude'].dropna()
    mean_val = magnitudes.mean()
    median_val = magnitudes.median()

    try:
        mode_val = mode(magnitudes)
    except StatisticsError:
        # If there's no unique mode or multiple equally common values
        mode_val = "Multiple or No Unique Mode"

    print(f"\\nMean Magnitude: {mean_val:.3f}")
    print(f"Median Magnitude: {median_val:.3f}")
    print(f"Mode Magnitude: {mode_val}")

    # 4. Plot a histogram of magnitudes
    plt.figure(figsize=(7, 4))
    plt.hist(magnitudes, bins=10, color='skyblue', edgecolor='black')
    plt.title("Earthquake Magnitude Distribution")
    plt.xlabel("Magnitude")
    plt.ylabel("Frequency")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    # 5. Optional: If magnitude data is near-integer, a bar chart can illustrate discrete counts
    # Round to nearest 0.1 or integer for demonstration
    rounded_mags = magnitudes.round()
    counts = rounded_mags.value_counts().sort_index()

    plt.figure(figsize=(7, 4))
    plt.bar(counts.index.astype(str), counts.values, color='orange', edgecolor='black')
    plt.title("Rounded Magnitude Counts (Approx. Mode)")
    plt.xlabel("Rounded Magnitude")
    plt.ylabel("Count")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    print("\\nClose the plots to end the script.")

if __name__ == '__main__':
    main()
"""
    st.code(script_code, language="python")

    st.markdown(
        """
        ---
        **Interpreting Mean, Median, & Mode**:
        
        - **Mean**: The average value. Quakes with very high or low magnitude can skew this measure.  
        - **Median**: The middle value when sorted. More robust if outliers exist.  
        - **Mode**: The most frequently occurring value. Useful for discrete or near-discrete data.  

        These statistics provide **central tendency** insights.  
        The histogram and bar chart help visualize the distribution of magnitudes, revealing:
        
        - **Skewness** (long tails?).  
        - **Common magnitude bins** (spikes in the bar chart?).  
        - **Outliers** or unusual patterns.

        **Experiment** by selecting different start/end times or minimum magnitudes in your dataset page, 
        then re-run this script to see how central tendencies change!
        """
    )

def main():
    tutorial2_page()

if __name__ == "__main__":
    main()
