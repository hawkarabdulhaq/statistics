import streamlit as st

def tutorial_page():
    """
    Tutorial 1: General Overview (Approx. 40-Minute Activity)

    Students will:
    1) Download 'earthquakes.csv' from the dataset page.
    2) Set up Google Colab and mount their drive.
    3) Place 'earthquakes.csv' in an accessible location (e.g., /content/sample_data/).
    4) Download and run 'overview.py' to get a quick dataset summary and initial plots.
    5) Complete a short reflective task involving histogram interpretation and data insights.
    """

    st.title("Tutorial 1: General Overview")

    st.markdown(
        """
        Welcome to **Tutorial 1**, where you’ll learn the basics of working with 
        your **earthquake dataset** in **Google Colab**. By the end of this session, 
        you will have:
        
        - Downloaded an **earthquakes.csv** file from our dataset page (or the USGS API).
        - Set up a **Colab** notebook to read and analyze the data.
        - Run **`overview.py`** to print out summary info and generate two basic plots.

        ---
        ### Approximate Time: ~40 Minutes
        Here's how we'll fill that time:
        1. **(5-10 min)** Acquire and download the dataset.
        2. **(5-10 min)** Set up Colab environment, mount Drive, place CSV.
        3. **(10-15 min)** Run and examine `overview.py` outputs, interpret the histogram and scatter plot.
        4. **(5-10 min)** Reflect on the results with a short written task.
        
        Let's begin!
        """
    )

    st.markdown(
        """
        ---
        ### Step 1: Get `earthquakes.csv`
        - Go to our **dataset page** (or use the USGS API) to create your earthquake data.
        - Download the resulting **CSV** file (e.g., `earthquakes.csv`) locally.

        ---
        ### Step 2: Open Google Colab & Mount Drive
        - Go to [Google Colab](https://colab.research.google.com/).
        - In a **New Notebook**, run:
          ```python
          from google.colab import drive
          drive.mount('/content/drive')
          ```
        - Upload your **`earthquakes.csv`** file to `/content/sample_data/` or another folder in Colab.

        ---
        ### Step 3: Download `overview.py`
        - Copy the script (shown below) into a file named **`overview.py`**.
        - Make sure `overview.py` and `earthquakes.csv` are in the **same folder** so one can read the other.

        ---
        ### Step 4: Run `overview.py` in Colab
        - In a code cell, type:
          ```python
          !python overview.py
          ```
        - This script prints out:
          1. **Dataset Shape**: Number of rows and columns.
          2. **First 5 Rows**: Quick preview of your data.
          3. **Summary Statistics**: `df.describe()`.
          4. **Histogram** of earthquake magnitudes.
          5. **Scatter Plot** of Magnitude vs. Depth.

        ---
        ### Your 40-Minute Task

        **After you run `overview.py`, do the following**:

        1. **Observe the Histogram**: 
           - Are there any peaks or clusters of magnitude?
           - Does the distribution seem skewed or roughly symmetrical?
           - Jot down 2-3 observations.

        2. **Look at the Scatter Plot (Magnitude vs. Depth)**:
           - Are deeper quakes generally higher or lower in magnitude?
           - Any outliers (unusually large magnitude or extreme depths)?

        3. **Write a Short Paragraph (3–5 sentences)**:
           - Summarize the main patterns you see.
           - State how many total quake events your dataset has.
           - Note any surprises or questions you’d explore further.

        This reflective portion ensures you spend enough time **thinking** about the data, 
        not just running commands. The entire process—downloading, running, and writing— 
        should take around **40 minutes** total.

        ---
        ### The `overview.py` Script
        """
    )

    overview_code = """\
import pandas as pd
import matplotlib.pyplot as plt

# Define the path to the CSV file
file_path = '/content/sample_data/earthquakes.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Convert the 'time' column to datetime format for better handling (optional)
if 'time' in df.columns:
    df['time'] = pd.to_datetime(df['time'], errors='coerce')

# Display basic information about the dataset
print("Dataset Shape:", df.shape)
print("\\nFirst 5 Rows:")
print(df.head())
print("\\nSummary Statistics:")
print(df.describe())

# Plot a histogram of the earthquake magnitudes
plt.figure(figsize=(8, 5))
plt.hist(df['magnitude'], bins=10, color='skyblue', edgecolor='black')
plt.title("Earthquake Magnitude Distribution")
plt.xlabel("Magnitude")
plt.ylabel("Frequency")
plt.show()

# Plot a scatter plot of Magnitude vs. Depth (if 'depth' column exists)
if 'depth' in df.columns:
    plt.figure(figsize=(8, 5))
    plt.scatter(df['magnitude'], df['depth'], color='green', alpha=0.7)
    plt.title("Magnitude vs. Depth")
    plt.xlabel("Magnitude")
    plt.ylabel("Depth (km)")
    plt.show()
else:
    print("\\nNo 'depth' column found in CSV—skipping scatter plot.")
"""
    st.code(overview_code, language="python")

    st.markdown(
        """
        ---
        **Ready to Explore?**
        
        1. **Run** `overview.py` multiple times if you change your dataset (e.g., 
           a different date range or min magnitude).
        2. **Document** your observations—this reflection is key to understanding 
           how your data is distributed.
        3. **Share** your short paragraph with peers or your instructor to discuss 
           what your dataset reveals.
        
        **Good luck and happy exploring!**
        """
    )

def main():
    tutorial_page()

if __name__ == "__main__":
    main()
