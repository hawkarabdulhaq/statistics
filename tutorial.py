import streamlit as st
import requests

def fetch_script_contents(script_url):
    """
    Fetches the raw content of a Python script from a given URL.
    Returns the script text or an empty string if the fetch fails.
    """
    try:
        response = requests.get(script_url)
        if response.status_code == 200:
            return response.text
        else:
            st.error(f"Failed to fetch script from {script_url} (status code: {response.status_code})")
            return ""
    except Exception as e:
        st.error(f"An error occurred while fetching the script: {e}")
        return ""

def main():
    """
    The Tutorials page contains 6 tabs, one for each tutorial.
    Tutorial 1 includes detailed instructions, plus a way to view/download the 'overview.py' script.
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
            **Objective**: Learn how to download an earthquake dataset (`earthquakes.csv`), 
            upload it into Google Colab, and run an existing Python script to generate 
            plots and a summary overview.

            ---
            ### Steps

            1. **Download the Dataset**  
               - Navigate to the Dataset page (or Earthquake Data Downloader).
               - Select the desired start/end dates and minimum magnitude, then click "Fetch Data".
               - After previewing, click "Download Data as CSV" to save it as `earthquakes.csv`.
            
            2. **Open a New Colab Notebook**  
               - Go to [Google Colab](https://colab.research.google.com/) and create a new notebook.  
               - Optionally, mount Google Drive if you prefer using `/content/drive/...`.
            
            3. **Upload/Move the CSV File**  
               - For example, place `earthquakes.csv` in `/content/sample_data/` 
                 or in `/content/drive/MyDrive/`, etc.
               - Confirm the path in Colab so you know where the CSV resides.
            
            4. **Download or Use the `overview.py` Script**  
               - This script reads `earthquakes.csv`, generates summary stats, 
                 and produces a bar chart & scatter plot. 
               - (Scroll down on this page to **view** or **download** the `overview.py` script.)
            
            5. **Run the `overview.py` Script**  
               - In a Colab cell, run:  
                 ```bash
                 !python overview.py
                 ```
                 or open `overview.py` in Colab and run its cells (if it's a notebook).
            
            6. **Check the Output**  
               - You should see a general overview of quake data and some basic plots.

            ---
            **Expected Outcome**:
            - A quick summary of earthquake data (count, min/max magnitude, min/max depth, etc.).
            - A bar chart or scatter plot to visualize the data distribution.

            **Tips**:
            - Make sure the CSV path in `overview.py` matches your Colab environment location.
            - If you run into errors, check the file path or environment setup.

            **Further Exploration**:
            - Modify the date range or min magnitude in the Dataset page to get new data.
            - Extend `overview.py` to create additional plots or deeper analytics.

            ---
            """
        )

        st.markdown("### View or Download `overview.py`")

        # Provide a text input or a fixed URL to the raw script
        # e.g., "https://raw.githubusercontent.com/username/repository/main/tutorials/overview.py"
        default_script_url = st.text_input(
            "Paste the URL to `overview.py`:",
            value="https://raw.githubusercontent.com/username/repository/main/tutorials/overview.py"
        )

        if st.button("Fetch and Show Script"):
            script_contents = fetch_script_contents(default_script_url)
            if script_contents:
                st.code(script_contents, language="python")

                # Provide a download button for the script
                st.download_button(
                    label="Download overview.py",
                    data=script_contents,
                    file_name="overview.py",
                    mime="text/x-python"
                )

    # ──────────────────────────────────────────────────────────────────────────
    # Tutorial 2 Content (Placeholder)
    # ──────────────────────────────────────────────────────────────────────────
    with tab2:
        st.subheader("Tutorial 2")
        st.markdown(
            """
            **Coming Soon**: Content for Tutorial 2 will be added here.
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
