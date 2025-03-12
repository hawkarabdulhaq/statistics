import streamlit as st

def tutorial5_page():
    """
    Tutorial 5: Visualizing and Understanding Topographical Data with Probability

    This tutorial introduces you to probability fundamentals by working with 
    elevation data. You will load and preprocess XYZ elevation data, define an event 
    space (e.g., elevations exceeding a chosen threshold), and visualize the PDF 
    and CDF of the elevation values.

    **Your Group Task (Spend ~40 minutes):**
    1. **Download** the dataset from `input/Elevation_backup.xyz`.  
       The file is tab-delimited with columns: longitude, latitude, elevation.
    2. **Open a new Google Colab notebook** and upload the dataset.
    3. **Run the provided script** (below) to:
       - Load and preprocess the data.
       - Compute basic statistics.
       - Plot the histogram, PDF, and CDF of the elevation values.
       - Compute the probability that elevation exceeds a given threshold (e.g., 400 m).
    4. **Discuss as a group** (5 students collaborate):
       - How do the PDF and CDF help you understand the distribution of elevation?
       - What is the probability that a random location has an elevation above your chosen threshold?
       - Reflect on whether the elevation distribution is skewed, multimodal, or normal.
       - Write a short group summary (3–5 sentences) explaining your findings and any implications for topographical analysis.

    **Instructions for Google Colab:**
    1. Run:
       ```bash
       !pip install pandas numpy matplotlib
       !python elevation_analysis.py
       ```
       (Make sure to adjust the file path if needed.)
    """
    st.title("Tutorial 5: Visualizing and Understanding Topographical Data with Probability")

    st.markdown(
        """
        **Objective:**
        - Learn to analyze elevation data using probability concepts.
        - Compute the probability of an elevation event (e.g., elevation > 400 m).
        - Visualize the probability density function (PDF) and cumulative distribution function (CDF).

        **Group Task (Approx. 40 minutes):**
        1. **Download** `input/Elevation_backup.xyz` (a tab-delimited file with longitude, latitude, elevation).
        2. **Upload** the dataset to your Google Colab environment.
        3. **Run** the following script (`elevation_analysis.py`) in Colab.
        4. **Record and Discuss:**
           - Basic statistics (min, max, mean, median, standard deviation).
           - The shape of the histogram, PDF, and CDF.
           - The probability that a random point has an elevation above 400 m (or another threshold of your choice).
           - Reflect on the implications for understanding topography.
        """
    )

    st.markdown("---")
    st.subheader("Python Script: elevation_analysis.py")
    elevation_script = """\
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Path to the elevation dataset (XYZ format)
DATA_FILE = 'input/Elevation_backup.xyz'

def main():
    # 1. Load the dataset
    # The file is tab-delimited, without a header. We assign columns: longitude, latitude, elevation.
    df = pd.read_csv(DATA_FILE, sep='\\t', header=None, names=['longitude', 'latitude', 'elevation'])
    df.dropna(inplace=True)
    
    # Print basic info
    print("=== Elevation Data Overview ===")
    print("Data Shape:", df.shape)
    print("First 5 Rows:")
    print(df.head())
    
    # 2. Compute basic statistics for elevation
    elev_min = df['elevation'].min()
    elev_max = df['elevation'].max()
    elev_mean = df['elevation'].mean()
    elev_median = df['elevation'].median()
    elev_std = df['elevation'].std()
    
    print("\\n=== Elevation Statistics ===")
    print(f"Min: {elev_min:.2f}")
    print(f"Max: {elev_max:.2f}")
    print(f"Mean: {elev_mean:.2f}")
    print(f"Median: {elev_median:.2f}")
    print(f"Standard Deviation: {elev_std:.2f}")
    
    # 3. Define an event: Elevation greater than a threshold
    threshold = 400  # You may adjust this threshold
    event_probability = (df['elevation'] > threshold).mean()
    print(f"\\nProbability that elevation > {threshold} m: {event_probability:.3f}")
    
    # 4. Create a histogram of elevation data
    plt.figure(figsize=(10, 5))
    counts, bins, patches = plt.hist(df['elevation'], bins=30, color='lightblue', edgecolor='black', alpha=0.7)
    plt.title("Elevation Histogram")
    plt.xlabel("Elevation (m)")
    plt.ylabel("Frequency")
    
    # 5. Compute PDF (Probability Density Function)
    bin_width = bins[1] - bins[0]
    pdf = counts / (counts.sum() * bin_width)
    
    plt.figure(figsize=(10, 5))
    plt.plot(bins[:-1], pdf, marker='o', linestyle='-', color='blue')
    plt.title("Probability Density Function (PDF)")
    plt.xlabel("Elevation (m)")
    plt.ylabel("Density")
    plt.grid(alpha=0.3)
    
    # 6. Compute CDF (Cumulative Distribution Function)
    cdf = np.cumsum(pdf * bin_width)
    plt.figure(figsize=(10, 5))
    plt.plot(bins[:-1], cdf, marker='o', linestyle='-', color='green')
    plt.title("Cumulative Distribution Function (CDF)")
    plt.xlabel("Elevation (m)")
    plt.ylabel("Cumulative Probability")
    plt.grid(alpha=0.3)
    
    # Show all plots
    plt.show()
    
    print("\\n=== Analysis Complete ===")
    
if __name__ == '__main__':
    main()
"""
    st.code(elevation_script, language="python")

    st.markdown(
        """
        ---
        **Your Task:**
        1. **Run the Script**: Upload `input/Elevation_backup.xyz` to your Colab environment and run `!python elevation_analysis.py`.
        2. **Experiment**: 
           - Adjust the elevation threshold (currently 400 m) in the script.
           - Change the number of bins in the histogram and observe how the PDF and CDF plots change.
        3. **Reflect & Collaborate**:
           - As a group, discuss how the elevation distribution informs you about the topography.
           - Answer these questions:
             - How does changing the threshold affect the probability of an event?
             - Is the distribution of elevations skewed or symmetrical? Why might that be?
             - Which visualization (histogram, PDF, CDF) gives you the best insight into the elevation data?
           - Write a brief summary (3–5 sentences) of your findings.
        
        **Enjoy exploring topographical data with probability concepts!**
        """
    )

def main():
    tutorial5_page()

if __name__ == "__main__":
    main()
