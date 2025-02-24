import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# Use cache_data to prevent re-fetching data unnecessarily.
@st.cache_data(show_spinner=True)
def fetch_earthquake_data(starttime, endtime, minmagnitude):
    """
    Fetches earthquake data from the USGS API based on provided parameters.
    
    Parameters:
    - starttime (str): Start date in 'YYYY-MM-DD' format.
    - endtime (str): End date in 'YYYY-MM-DD' format.
    - minmagnitude (float): Minimum magnitude for events.
    
    Returns:
    - dict: The GeoJSON response as a Python dictionary or None if request fails.
    """
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        "format": "geojson",
        "starttime": starttime,
        "endtime": endtime,
        "minmagnitude": minmagnitude
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        st.error("Error fetching data. Please check your parameters and try again.")
        return None
    return response.json()

@st.cache_data(show_spinner=True)
def parse_earthquake_data(data):
    """
    Parses the GeoJSON earthquake data into a DataFrame.

    Extracted fields include:
      - time: Event time (converted from epoch ms to human-readable).
      - magnitude: Earthquake magnitude.
      - place: Location description.
      - longitude, latitude, depth: Coordinates from the event's geometry.

    Returns:
    - pd.DataFrame: DataFrame containing the parsed earthquake data.
    """
    features = data.get("features", [])
    if not features:
        return pd.DataFrame()

    records = []
    for feature in features:
        properties = feature.get("properties", {})
        geometry = feature.get("geometry", {})
        coordinates = geometry.get("coordinates", [None, None, None])
        
        # Convert epoch time (ms) to human-readable UTC format.
        event_time_ms = properties.get("time")
        if event_time_ms is not None:
            event_time = datetime.utcfromtimestamp(event_time_ms / 1000).strftime("%Y-%m-%d %H:%M:%S")
        else:
            event_time = None
        
        record = {
            "time": event_time,
            "magnitude": properties.get("mag"),
            "place": properties.get("place"),
            "longitude": coordinates[0],
            "latitude": coordinates[1],
            "depth": coordinates[2]
        }
        records.append(record)

    return pd.DataFrame(records)

def main():
    st.title("Earthquake Data Page")
    st.write("Below are two tabs: one for downloading earthquake data, and another for a tutorial on how to use it.")

    tab1, tab2 = st.tabs(["Download Dataset", "Tutorials"])

    # ─────────────────────────────────────────────────────────────────────
    # TAB 1: DOWNLOAD DATASET
    # ─────────────────────────────────────────────────────────────────────
    with tab1:
        st.subheader("Download Earthquake Dataset")
        st.write("Fetch and download earthquake events from the USGS API.")

        # Sidebar-like controls, but placed in main tab for clarity.
        start_date = st.date_input("Start Date", value=pd.to_datetime("2024-01-01"))
        end_date = st.date_input("End Date", value=pd.to_datetime("2024-02-01"))
        min_magnitude = st.number_input("Minimum Magnitude", min_value=0.0, max_value=10.0, value=5.0, step=0.1)

        if st.button("Fetch Earthquakes"):
            start_str = start_date.strftime("%Y-%m-%d")
            end_str = end_date.strftime("%Y-%m-%d")

            with st.spinner("Fetching data from USGS..."):
                data = fetch_earthquake_data(start_str, end_str, min_magnitude)
                if data:
                    df = parse_earthquake_data(data)
                    if df.empty:
                        st.warning("No earthquake data found for these parameters.")
                    else:
                        st.success(f"Fetched {len(df)} earthquake events.")
                        st.dataframe(df.head(10))
                        
                        csv_data = df.to_csv(index=False).encode("utf-8")
                        st.download_button(
                            label="Download as CSV",
                            data=csv_data,
                            file_name="earthquakes.csv",
                            mime="text/csv"
                        )
                else:
                    st.error("Failed to retrieve data. Please try different parameters.")

    # ─────────────────────────────────────────────────────────────────────
    # TAB 2: TUTORIALS
    # ─────────────────────────────────────────────────────────────────────
    with tab2:
        st.subheader("Tutorial 1: General Overview")
        st.markdown(
            """
            Below is a step-by-step guide on how to download and use the **earthquakes.csv** dataset in Google Colab:
            
            1. **Download the Dataset**  
               - Use the _Download Dataset_ tab.  
               - Fetch data for a given timeframe (e.g., 2024-01-01 to 2024-02-01) with a chosen minimum magnitude (e.g., 5).  
               - Click **"Fetch Earthquakes"**.  
               - Preview the data, then click **"Download as CSV"** to save it locally as `earthquakes.csv`.
            
            2. **Upload to Google Colab**  
               - Open a new Colab notebook ([colab.research.google.com](https://colab.research.google.com/)).  
               - Mount your Google Drive or upload the file `earthquakes.csv`.  
               - Ensure you have a path like `/content/sample_data/earthquakes.csv` (or any valid path where your CSV is stored).
            
            3. **Download & Run the `tutorials/overview.py` Script**  
               - Download the Python script `tutorials/overview.py` (provided separately).  
               - In your Colab, upload `overview.py` or place it in the same directory on Google Drive.
               - Run the script in Colab:
                 ```python
                 !python /content/sample_data/overview.py
                 ```
               - Check the terminal output (Colab cell output) for results.
            
            4. **Expected Output**  
               - A **general overview** of your CSV data (like row counts, columns).  
               - A **bar chart** and **scatter plot** summarizing key features (e.g., magnitude distribution, location scatter).
            
            5. **Tips & Next Steps**  
               - Customize `overview.py` to suit your needs.  
               - Explore advanced visualizations or analysis (e.g., clustering, geographic mapping).
               - Always validate your data (e.g., check for missing or strange values).
            """
        )
        st.info("By following the steps above, you can easily integrate the USGS earthquake dataset into your Google Colab environment and experiment with various analyses or visualizations!")

if __name__ == "__main__":
    main()
