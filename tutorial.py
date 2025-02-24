import streamlit as st

# Replace this string with the actual content of your 'tutorials/overview.py' script.
# For demonstration, a brief placeholder is used here.
OVERVIEW_PY_CONTENT = """\"\"\"
overview.py - Demonstration script

This script reads 'earthquakes.csv' from disk, prints a quick overview,
and generates a bar chart plus a scatter plot.
\"\"\"

import pandas as pd
import matplotlib.pyplot as plt
import sys

def main():
    # Example logic
    data_file = 'earthquakes.csv'
    print(f'Reading data from {data_file}...')
    df = pd.read_csv(data_file)
    print(df.head())

    # Create and save a bar chart (placeholder)
    plt.figure()
    df['magnitude'].plot(kind='bar')
    plt.title('Earthquake Magnitudes')
    plt.savefig('bar_chart.png')
    print('Bar chart saved as bar_chart.png')

    # Create and save a scatter plot (placeholder)
    plt.figure()
    plt.scatter(df['longitude'], df['latitude'], c=df['magnitude'], cmap='viridis')
    plt.colorbar(label='Magnitude')
    plt.title('Earthquake Locations')
    plt.savefig('scatter_plot.png')
    print('Scatter plot saved as scatter_plot.png')

if __name__ == '__main__':
    main()
"""

def main():
    """
    The Tutorials page contains 6 tabs, one for each tutorial.
    Tutorial 1 includes detailed instructions plus the ability
    to view or download the 'tutorials/overview.py' file.
    Tutorials 2-6 are placeholders you can fill in later.
    """
    st.title("Tutorials")
    st.write(
        """
        Explore step-by-step guides for different parts of your geological data workflow.
        Use the tabs below to switch between tutorials.
        """
    )

    # Create 6 tabs for 6 tutorials
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Tutorial 1: General Overview",
        "Tutorial 2",
        "Tutorial 3",
        "Tutorial 4",
        "Tutorial 5",
        "Tutorial 6"
    ])

    # ──────────────────────────────────────────────────────────────────────────
    # Tutorial 1 Content
    # ──────────────────────────────────────────────────────────────────────────
    with tab1:
        st.subheader("Tutorial 1: General Overview")
        st.markdown(
            """
            **Objective**: Learn how to download an earthquake dataset within a specified time range
            as `earthquakes.csv`, upload it into a Google Colab environment, and run an existing Python
            script to generate basic plots and overview statistics.

            ---
            ### Steps

            1. **Download the Dataset**  
               - Navigate to the **Dataset** page (or your Earthquake Data Downloader).
               - Choose the desired start/end dates and minimum magnitude, then click "Fetch Data".
               - After previewing the data, use the "Download Data as CSV" button to save the file locally 
                 as `earthquakes.csv`.
            
            2. **Open a New Colab Notebook**  
               - Go to [Google Colab](https://colab.research.google.com/) and create a new notebook.  
               - In the left sidebar, click the **Files** icon, then **Mount Drive** 
                 (if you want to place the file in your Google Drive).
            
            3. **Upload/Move the CSV File**  
               - Suppose you mount your Google Drive at `/content/drive`.  
               - Place your `earthquakes.csv` inside a directory such as `/content/drive/MyDrive/`. 
               - Alternatively, you can upload directly to the Colab environment:
                 - Click the **Files** icon, then **Upload**, and choose `earthquakes.csv`.
               - Once uploaded, you might end up with a path like:  
                 `/content/sample_data/earthquakes.csv`
            
            4. **Download or View the `overview.py` Script**  
               - This script contains Python code to read the CSV file, generate summary statistics, 
                 and produce basic charts.
               - You can either download it below or copy the code from within this page.

            5. **Run the `overview.py` Script**  
               - In a Colab cell, run:
                 ```python
                 !python overview.py
                 ```
                 or open `overview.py` in Colab if it's not a standalone script.
            
            6. **Check the Output**  
               - The script should read `earthquakes.csv`, generate a **general overview** of the dataset, 
                 and produce a **bar chart** plus a **scatter plot**.
               - Confirm results by checking the Colab cell output.

            ---
            **Expected Outcome**:
            - A quick summary (count, min/max magnitude, min/max depth, etc.) from your CSV.
            - Visual insights (bar chart, scatter plot) to understand the time range or magnitude distribution.

            **Tips**:
            - Ensure your CSV file path in `overview.py` matches where you uploaded `earthquakes.csv`.
            - If errors occur, double-check the file path and environment setup.

            **Further Exploration**:
            - Fetch a different CSV with changed parameters (dates, min magnitude) and re-run `overview.py`.
            - Customize the script to add more plots or stats.

            ---
            **Need Help?**  
            Contact the instructor or refer to additional tutorials for advanced usage.
            """
        )

        # Add an expander to show or hide the 'overview.py' code.
        with st.expander("View the overview.py Script"):
            st.code(OVERVIEW_PY_CONTENT, language="python")

        # Provide a download button for the script file.
        st.download_button(
            label="Download overview.py",
            data=OVERVIEW_PY_CONTENT,
            file_name="overview.py",
            mime="text/plain"
        )

    # ──────────────────────────────────────────────────────────────────────────
    # Tutorial 2 Content (Placeholder)
    # ──────────────────────────────────────────────────────────────────────────
    with tab2:
        st.subheader("Tutorial 2")
        st.markdown(
            """
            **Coming Soon**: Content for Tutorial 2 will be added here.
            Feel free to insert instructions for your second tutorial.
            """
        )

    # ──────────────────────────────────────────────────────────────────────────
    # Tutorial 3 Content (Placeholder)
    # ──────────────────────────────────────────────────────────────────────────
    with tab3:
        st.subheader("Tutorial 3")
        st.markdown(
            """
            **Coming Soon**: Content for Tutorial 3 will be added here.
            """
        )

    # ──────────────────────────────────────────────────────────────────────────
    # Tutorial 4 Content (Placeholder)
    # ──────────────────────────────────────────────────────────────────────────
    with tab4:
        st.subheader("Tutorial 4")
        st.markdown(
            """
            **Coming Soon**: Content for Tutorial 4 will be added here.
            """
        )

    # ──────────────────────────────────────────────────────────────────────────
    # Tutorial 5 Content (Placeholder)
    # ──────────────────────────────────────────────────────────────────────────
    with tab5:
        st.subheader("Tutorial 5")
        st.markdown(
            """
            **Coming Soon**: Content for Tutorial 5 will be added here.
            """
        )

    # ──────────────────────────────────────────────────────────────────────────
    # Tutorial 6 Content (Placeholder)
    # ──────────────────────────────────────────────────────────────────────────
    with tab6:
        st.subheader("Tutorial 6")
        st.markdown(
            """
            **Coming Soon**: Content for Tutorial 6 will be added here.
            """
        )

if __name__ == "__main__":
    main()
