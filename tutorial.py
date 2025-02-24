import streamlit as st

def main():
    """
    The Tutorials page contains 6 tabs, one for each tutorial.
    Tutorial 1 includes detailed instructions, while Tutorials 2-6
    are placeholders that you can later expand with relevant content.
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
            
            4. **Download the Tutorials Script**  
               - Download the `tutorials/overview.py` script. This script contains Python code 
                 to read the CSV file, generate summary statistics, create a bar chart, 
                 and produce a scatter plot.
               - Upload this script to the Colab environment (same location as your CSV file).
            
            5. **Run the `overview.py` Script**  
               - In a Colab cell, run:
                 ```python
                 !python overview.py
                 ```
                 or open `overview.py` in Colab and run its cells directly if it's not a standalone script.
            
            6. **Check the Output**  
               - The script should read `earthquakes.csv`, generate a **general overview** of the dataset, 
                 and then display or save a **bar chart** and a **scatter plot**.
               - You can confirm the results by checking the terminal output (the cell output in Colab).

            ---
            **Expected Outcome**:
            - A quick summary of your earthquake data (count, min/max magnitude, 
              min/max depth, etc.).
            - One or more visualizations (bar chart, scatter plot) to help you interpret 
              the time range or magnitude distribution of the earthquakes.

            **Tips**:
            - Make sure your CSV file path in `overview.py` matches the location 
              you used to upload `earthquakes.csv`.
            - If you encounter any errors, double-check the file path and the 
              environment setup (e.g., Colab's working directory).

            **Further Exploration**:
            - Modify the parameters (date range, min magnitude) in the Dataset page 
              to fetch a different CSV and see how your overview changes.
            - Customize the `overview.py` script to include additional plots or 
              statistical analyses.

            ---
            **Need Help?**  
            Contact the instructor or refer to additional tutorials for advanced usage.
            """
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
