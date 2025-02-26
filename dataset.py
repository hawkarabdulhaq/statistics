import streamlit as st
import pandas as pd
import requests
from datetime import datetime

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
    st.title("Data Downloads and Resources")

    # Create three tabs
    tab1, tab2, tab3 = st.tabs(["Earthquake Data", "NDVI File", "Coral Isotope Data"])

    # ─────────────────────────────────────────────────────────────────
    # TAB 1: EARTHQUAKE DATA
    # ─────────────────────────────────────────────────────────────────
    with tab1:
        st.subheader("1) Earthquake Data via USGS API")
        st.write("Use the parameter inputs below to fetch quake data from USGS, then download as CSV.")

        start_date = st.date_input("Start Date", value=pd.to_datetime("2024-01-01"))
        end_date = st.date_input("End Date", value=pd.to_datetime("2024-02-01"))
        min_magnitude = st.number_input("Minimum Magnitude", min_value=0.0, max_value=10.0, value=5.0, step=0.1)

        if st.button("Fetch Earthquake Data"):
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
                        
                        csv_data = df.to_csv(index=False).encode("utf-8")
                        st.download_button(
                            label="Download Data as CSV",
                            data=csv_data,
                            file_name="earthquakes.csv",
                            mime="text/csv"
                        )
                else:
                    st.error("Failed to fetch data. Please try again with different parameters.")

    # ─────────────────────────────────────────────────────────────────
    # TAB 2: NDVI FILE
    # ─────────────────────────────────────────────────────────────────
    with tab2:
        st.subheader("2) S2_NDVI2.tif Download")
        st.write("This single-band NDVI GeoTIFF can be used in NDVI-related tutorials.")

        ndvi_url = "https://raw.githubusercontent.com/hawkarabdulhaq/statistics/main/input/S2_NDVI2.tif"
        if st.button("Download NDVI TIF"):
            with st.spinner("Fetching S2_NDVI2.tif from GitHub..."):
                ndvi_response = requests.get(ndvi_url)
                if ndvi_response.status_code == 200:
                    ndvi_file = ndvi_response.content
                    st.download_button(
                        label="Save S2_NDVI2.tif",
                        data=ndvi_file,
                        file_name="S2_NDVI2.tif",
                        mime="application/octet-stream"
                    )
                else:
                    st.error("Failed to fetch S2_NDVI2.tif from GitHub. Please try again later.")

        st.info("Use this `.tif` file in your NDVI tutorials (like Tutorial 3).")

    # ─────────────────────────────────────────────────────────────────
    # TAB 3: CORAL ISOTOPE DATA
    # ─────────────────────────────────────────────────────────────────
    with tab3:
        st.subheader("3) Abraham Reef Coral Isotope Data")
        st.write("Download the `abraham_reef.txt` file for the coral isotope tutorials (e.g., Tutorial 4).")

        reef_url = "https://raw.githubusercontent.com/hawkarabdulhaq/statistics/main/input/abraham_reef.txt"
        if st.button("Download abraham_reef.txt"):
            with st.spinner("Fetching abraham_reef.txt from GitHub..."):
                reef_response = requests.get(reef_url)
                if reef_response.status_code == 200:
                    reef_file = reef_response.content
                    st.download_button(
                        label="Save abraham_reef.txt",
                        data=reef_file,
                        file_name="abraham_reef.txt",
                        mime="text/plain"
                    )
                else:
                    st.error("Failed to fetch abraham_reef.txt from GitHub. Please try again later.")

        st.markdown(
            """
            **Data Description**:  
            Abraham Reef Biannual Coral Isotope data, with columns:
            - `age` (year AD),
            - `d18O` (permil VPDB),
            - `d13C` (permil VPDB).  
            
            Useful for paleoclimate analysis, e.g., **Tutorial 4** (group task).
            """
        )


if __name__ == "__main__":
    main()
