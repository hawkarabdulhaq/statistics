import streamlit as st

def tutorial_page():
    """
    A single-page tutorial showing steps to:
    1) Download 'earthquakes.csv'
    2) Use Google Colab
    3) Run 'overview.py' for a quick dataset summary
    """
    st.title("Tutorial 1: General Overview")

    st.markdown(
        """
        This tutorial guides you through:
        
        1. **Downloading** the **earthquakes.csv** dataset.  
        2. **Opening** a new **Google Colab** notebook and mounting your Google Drive.  
        3. **Placing** the CSV file (e.g., `/content/sample_data/earthquakes.csv`).  
        4. **Downloading** and running the **`overview.py`** script in Colab to get a quick summary and plots.
        
        ---
        ### Step-by-Step Instructions
        
        1. **Get `earthquakes.csv`**  
           - Use our **dataset page** (or the USGS API directly) to generate your custom dataset.  
           - Click "Download CSV" to save it locally.
        
        2. **Open Google Colab**  
           - Go to [https://colab.research.google.com/](https://colab.research.google.com/).  
           - Create a **New Notebook** in Colab.
        
        3. **Mount Your Google Drive**  
           - In Colab, run:
             ```python
             from google.colab import drive
             drive.mount('/content/drive')
             ```
           - Move your `earthquakes.csv` to a location such as `/content/sample_data/earthquakes.csv`.
        
        4. **Download `overview.py`**  
           - Save the script (shown below) as `overview.py`.  
           - Place `overview.py` in the same directory where it can read `/content/sample_data/earthquakes.csv`.
        
        5. **Run `overview.py` in Colab**  
           - In a Colab cell:
             ```python
             !python overview.py
             ```
           - The output includes **basic DataFrame info**, **histogram** of magnitudes, and a **scatter plot** of magnitude vs. depth.
        
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
df['time'] = pd.to_datetime(df['time'])

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

# Plot a scatter plot of Magnitude vs. Depth
plt.figure(figsize=(8, 5))
plt.scatter(df['magnitude'], df['depth'], color='green', alpha=0.7)
plt.title("Magnitude vs. Depth")
plt.xlabel("Magnitude")
plt.ylabel("Depth (km)")
plt.show()
"""
    st.code(overview_code, language="python")

    st.markdown(
        """
        ---
        Once you run `overview.py` in Colab, you’ll see the printed **dataset shape**, 
        **head**, **describe**, plus **two plots**:
        
        1. A **histogram** illustrating the distribution of earthquake magnitudes.  
        2. A **scatter plot** comparing magnitude and depth.

        **Happy Learning!**
        """
    )

def main():
    tutorial_page()

if __name__ == "__main__":
    main()
