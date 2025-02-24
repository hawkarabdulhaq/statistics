import streamlit as st

def tutorial_page():
    """
    A page showcasing 6 tabs for tutorials. 
    """
    st.title("Tutorials")

    # Create 6 tabs
    tabs = st.tabs([
        "Tutorial 1: General Overview",
        "Tutorial 2: Filter by Time Window",
        "Tutorial 3",
        "Tutorial 4",
        "Tutorial 5",
        "Tutorial 6"
    ])

    # ───────────────────────────────────────────────────────────────────
    # TAB 1: GENERAL OVERVIEW
    # ───────────────────────────────────────────────────────────────────
    with tabs[0]:
        st.subheader("Tutorial 1: General Overview")

        st.markdown(
            """
            This tutorial guides you through:
            1. Downloading the **earthquakes.csv** dataset within a specified time range from the **USGS Earthquake API**.
            2. Opening a **new Google Colab** notebook and mounting your Google Drive.
            3. Storing the CSV file at a path like `**/content/sample_data/earthquakes.csv**`.
            4. Downloading and running the **`overview.py`** script in Colab to get a quick summary and plots.

            ---
            **Detailed Steps**:
            
            1. **Acquire `earthquakes.csv`**  
               - Use our **`dataset.py`** page (or the USGS API query) to generate your earthquake data.  
               - Download it locally as `earthquakes.csv`.
            
            2. **Open Google Colab**  
               - Go to [https://colab.research.google.com/](https://colab.research.google.com/)  
               - Create a **New Notebook**.

            3. **Mount Your Google Drive**  
               - In Colab, run:
                 ```python
                 from google.colab import drive
                 drive.mount('/content/drive')
                 ```
               - Copy your `earthquakes.csv` file into a location such as `/content/sample_data/earthquakes.csv`. 

            4. **Download `overview.py`**  
               - Save the script below as `overview.py`.  
               - Ensure it's in the same Colab environment so you can run it.

            5. **Run `overview.py` in Colab**  
               - In a code cell, do:
                 ```python
                 !python overview.py
                 ```
               - Check the output in the Colab cell logs.

            6. **Analyze Results**  
               - You’ll see **data info** (shape, head, describe).  
               - A **histogram** of quake magnitudes.  
               - A **scatter plot** of magnitude vs. depth.

            ---
            **Sample `overview.py`**:
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
            That’s it for **Tutorial 1**! Once you run `overview.py` in Colab, you should see printed summaries and the two plots. 
            Enjoy exploring your earthquake data!
            """
        )

    # ───────────────────────────────────────────────────────────────────
    # TAB 2: FILTER BY TIME WINDOW
    # ───────────────────────────────────────────────────────────────────
    with tabs[1]:
        st.subheader("Tutorial 2: Filter & Explore Specific Time Windows")

        st.markdown(
            """
            **Objective**: Let students pick a smaller time window to see if there are any interesting patterns.

            **Approach**:
            1. Filter the DataFrame for events **within a narrower date range** (e.g., one week, one day, or specific days).
            2. Re-run the same printing commands (shape, head, describe) and compare results with the original dataset.
            3. Generate the histogram and scatter plot again to see how the distribution changes with fewer events.

            ---
            **Example**: Suppose you only want events from `2024-01-10` to `2024-01-15`. 
            In `overview.py`, right after loading `df`, you could add:
            ```python
            # Convert 'time' to datetime if not already done:
            df['time'] = pd.to_datetime(df['time'])

            # Filter by time range
            start_date = '2024-01-10'
            end_date   = '2024-01-15'

            filtered_df = df[(df['time'] >= start_date) & (df['time'] < end_date)]

            print("\\nFiltered Dataset Shape:", filtered_df.shape)
            print(filtered_df.head())

            # Now re-run the histogram and scatter plot on 'filtered_df' instead of 'df'
            # e.g., filtered_df['magnitude'] ...
            ```
            Compare the new shape with the original. Are there fewer events? 
            Does the magnitude distribution look different?

            ---
            **Map Visualization**:
            You could **map** these filtered events to see if they cluster in certain regions.
            A simple example with **folium**:
            ```python
            import folium

            # Center map roughly over the world
            m = folium.Map(location=[0, 0], zoom_start=2)

            for i, row in filtered_df.iterrows():
                # Make sure your 'latitude' and 'longitude' columns exist!
                popup_text = f"M: {row['magnitude']}, Depth: {row['depth']} km"
                folium.CircleMarker(
                    location=[row['latitude'], row['longitude']],
                    radius=3,
                    color='red',
                    fill=True,
                    fill_color='red',
                    popup=popup_text
                ).add_to(m)

            # Save to HTML
            m.save('filtered_map.html')
            print("Map saved as filtered_map.html. Open it locally to view.")
            ```
            This way, you can see if quakes in a narrower time window are 
            concentrated in a specific region or distributed globally.
            """
        )

    # ───────────────────────────────────────────────────────────────────
    # TAB 3: PLACEHOLDER
    # ───────────────────────────────────────────────────────────────────
    with tabs[2]:
        st.subheader("Tutorial 3")
        st.write("Content for Tutorial 3 goes here...")

    # ───────────────────────────────────────────────────────────────────
    # TAB 4: PLACEHOLDER
    # ───────────────────────────────────────────────────────────────────
    with tabs[3]:
        st.subheader("Tutorial 4")
        st.write("Content for Tutorial 4 goes here...")

    # ───────────────────────────────────────────────────────────────────
    # TAB 5: PLACEHOLDER
    # ───────────────────────────────────────────────────────────────────
    with tabs[4]:
        st.subheader("Tutorial 5")
        st.write("Content for Tutorial 5 goes here...")

    # ───────────────────────────────────────────────────────────────────
    # TAB 6: PLACEHOLDER
    # ───────────────────────────────────────────────────────────────────
    with tabs[5]:
        st.subheader("Tutorial 6")
        st.write("Content for Tutorial 6 goes here...")

def main():
    """
    Runs the tutorial page directly if this file is executed alone.
    """
    tutorial_page()

if __name__ == "__main__":
    main()
