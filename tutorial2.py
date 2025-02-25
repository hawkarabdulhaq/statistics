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
        In this tutorial, you'll **actively explore** how **mean**, **median**, 
        and **mode** vary for different subsets of earthquake data. 
        You’ll practice downloading multiple datasets, analyzing them in 
        **Google Colab**, and **comparing** your results.

        ---
        ## Objectives:
        1. **Generate multiple CSV files** from the dataset page (or the USGS API) by varying the **start date**, **end date**, or **minimum magnitude**.
        2. **Compute** mean, median, and mode for each dataset using a Python script in Colab.
        3. **Visualize** magnitude distributions (histograms, bar charts).
        4. **Reflect** on how outliers, time periods, or magnitude thresholds affect the central tendencies.

        By the end, you should have a clear understanding of **which measures** (mean, median, mode) 
        are more stable or more influenced by extremes in your quake data.

        ---
        ### Step 1: Collect Multiple Datasets
        - Go to your dataset page (or USGS API) 
        - Pick **3 different parameter sets** (e.g., different time windows or different minimum magnitudes).
        - Download each as a **unique** `earthquakes_1.csv`, `earthquakes_2.csv`, `earthquakes_3.csv`.

        **Example**:
        - **Dataset A**: Start = 2024-01-01, End = 2024-01-15, Min Magnitude = 4  
        - **Dataset B**: Start = 2024-01-15, End = 2024-02-01, Min Magnitude = 4  
        - **Dataset C**: Start = 2024-01-01, End = 2024-02-01, Min Magnitude = 5

        (Feel free to choose your own parameters.)

        ---
        ### Step 2: Prepare Google Colab
        - Go to [Google Colab](https://colab.research.google.com/) 
        - Create a **new notebook**.
        - Mount drive:
          ```python
          from google.colab import drive
          drive.mount('/content/drive')
          ```
        - Upload each CSV to `/content/sample_data/` or any folder you want.

        ---
        ### Step 3: Run the `stats_overview.py` Script
        - Copy the script below into a file named **`stats_overview.py`**.
        - In Colab, do:
          ```python
          !python stats_overview.py
          ```
        - Modify the `csv_path` variable if your files are named differently (e.g., `earthquakes_2.csv`).

        **Your Task**:
        1. For **each** dataset, run the script (adjust the code each time to point to the correct file).  
        2. **Record** mean, median, and mode of quake magnitudes in a small table or notes.  
        3. Observe the **histogram** and **bar chart** for each dataset. Are there outliers? Is there a clear mode?

        ---
        ### Step 4: Reflect & Compare (Spend ~20 minutes)
        - How does **time window** or **minimum magnitude** influence the mean vs. median?
        - Is the **mode** stable, or does it change drastically with dataset parameters?
        - Did you notice any skew in the distribution or an unusual number of outliers?

        Write a short paragraph (5–10 sentences) summarizing:
        - Which measure (mean, median, mode) changed the most across your datasets?
        - Did the histogram shapes differ significantly? Why might that be?

        ---
        ### `stats_overview.py` Script
        This script calculates mean, median, mode for `magnitude` 
        and shows a histogram + a bar chart for potential discrete modes.
        """
    )

    script_code = """\
import pandas as pd
import matplotlib.pyplot as plt
from statistics import mode, StatisticsError

# Path to your CSV file (adjust as needed for each dataset)
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

    # 2. Summary stats from pandas
    print("\\nSummary Statistics (pandas describe):")
    print(df.describe())

    # 3. Compute mean, median, mode manually for 'magnitude'
    magnitudes = df['magnitude'].dropna()
    mean_val = magnitudes.mean()
    median_val = magnitudes.median()

    try:
        mode_val = mode(magnitudes)
    except StatisticsError:
        # Occurs if there's no single unique mode
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

    # 5. Optional bar chart for discrete magnitude approach
    # For demonstration, let's round magnitudes to nearest 0.5
    mag_rounded = magnitudes.round(1)
    counts = mag_rounded.value_counts().sort_index()

    plt.figure(figsize=(7, 4))
    plt.bar(counts.index.astype(str), counts.values, color='orange', edgecolor='black')
    plt.title("Rounded Magnitude Counts")
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
        ## Wrap-Up

        **Estimated Time**: ~40 minutes  
        - **~10 min** generating and downloading multiple CSV files.  
        - **~10 min** running each dataset in Colab, capturing mean, median, mode, and the plots.  
        - **~20 min** reflecting and **writing** a short comparison of how your data changed across the different parameter sets.

        By following these steps, you'll gain **hands-on** experience in:
        - Adjusting dataset parameters (time range, min. magnitude).
        - Understanding **central tendencies** in real-world geological data.
        - Recognizing how **mean**, **median**, and **mode** respond to outliers or distribution skew.

        **Enjoy** your exploration!
        """
    )

def main():
    tutorial2_page()

if __name__ == "__main__":
    main()
