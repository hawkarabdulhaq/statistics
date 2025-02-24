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
    - dict: The GeoJSON response as a Python dictionary.
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
    Parses the GeoJSON earthquake data and converts it into a pandas DataFrame.
    
    Extracted fields include:
      - time: Event time (converted from epoch to human-readable format).
      - magnitude: The earthquake magnitude.
      - place: The location description.
      - longitude, latitude, depth: Coordinates from the event's geometry.
    
    Returns:
    - pd.DataFrame: DataFrame containing the extracted earthquake data.
    """
    features = data.get("features", [])
    if not features:
        return pd.DataFrame()
    
    records = []
    for feature in features:
        properties = feature.get("properties", {})
        geometry = feature.get("geometry", {})
        coordinates = geometry.get("coordinates", [None, None, None])
        # Convert epoch time (in ms) to a human-readable format.
        event_time = properties.get("time")
        if event_time:
            event_time = datetime.utcfromtimestamp(event_time / 1000).strftime("%Y-%m-%d %H:%M:%S")
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
    st.title("Earthquake Data Downloader")
    st.write("Download earthquake event data from the USGS as CSV.")
    
    # Sidebar for parameter inputs.
    st.sidebar.header("Query Parameters")
    start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2024-01-01"))
    end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2024-02-01"))
    min_magnitude = st.sidebar.number_input("Minimum Magnitude", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    
    # Button to trigger data fetching.
    if st.sidebar.button("Fetch Data"):
        # Format dates as strings in 'YYYY-MM-DD'
        start_str = start_date.strftime("%Y-%m-%d")
        end_str = end_date.strftime("%Y-%m-%d")
        
        with st.spinner("Fetching earthquake data..."):
            data = fetch_earthquake_data(start_str, end_str, min_magnitude)
            
            if data:
                df = parse_earthquake_data(data)
                if df.empty:
                    st.warning("No earthquake data found for these parameters.")
                else:
                    st.success(f"Fetched {len(df)} earthquake events.")
                    st.subheader("Data Preview (First 10 Records)")
                    st.dataframe(df.head(10))
                    
                    # Create CSV for download.
                    csv_data = df.to_csv(index=False).encode("utf-8")
                    st.download_button(
                        label="Download Data as CSV",
                        data=csv_data,
                        file_name="earthquakes.csv",
                        mime="text/csv"
                    )
            else:
                st.error("Failed to fetch data. Please try again with different parameters.")

if __name__ == "__main__":
    main()
