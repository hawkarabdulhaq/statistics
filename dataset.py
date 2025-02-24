import streamlit as st
import pandas as pd
import requests
from datetime import datetime
from datetime import date

# ──────────────────────────────────────────────────────────────────────────
# 1. Data Fetching and Parsing for Earthquakes
# ──────────────────────────────────────────────────────────────────────────

@st.cache_data(show_spinner=True)
def fetch_earthquake_data(starttime, endtime, minmagnitude):
    """
    Fetches earthquake data from the USGS API based on provided parameters.
    
    API Source: https://earthquake.usgs.gov/fdsnws/event/1/
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
        st.error("Error fetching earthquake data. Please check your parameters and try again.")
        return None
    return response.json()

@st.cache_data(show_spinner=True)
def parse_earthquake_data(data):
    """
    Parses the GeoJSON earthquake data and converts it into a pandas DataFrame.
    Extracted fields include:
      - time (converted from epoch to human-readable),
      - magnitude,
      - place,
      - longitude, latitude, depth.
    """
    features = data.get("features", [])
    if not features:
        return pd.DataFrame()
    
    records = []
    for feature in features:
        properties = feature.get("properties", {})
        geometry = feature.get("geometry", {})
        coordinates = geometry.get("coordinates", [None, None, None])
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

# ──────────────────────────────────────────────────────────────────────────
# 2. Data Fetching and Parsing for Minerals
# ──────────────────────────────────────────────────────────────────────────

@st.cache_data(show_spinner=True)
def fetch_minerals_data(commodity):
    """
    Fetches mineral site data from the USGS MRDS (Mineral Resources Data System)
    based on a specified commodity (e.g., 'Gold').

    API Source: https://mrdata.usgs.gov/arcgis/rest/services/MineralResources/MRDS/MapServer/0
    """
    base_url = "https://mrdata.usgs.gov/arcgis/rest/services/MineralResources/MRDS/MapServer/0/query"
    params = {
        "where": f"commodity='{commodity}'",
        "outFields": "site_name,commodity,latitude,longitude",
        "f": "geojson"
    }
    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        st.error("Error fetching mineral data. Please check your parameters and try again.")
        return None
    return response.json()

@st.cache_data(show_spinner=True)
def parse_minerals_data(data):
    """
    Parses the GeoJSON minerals data and converts it into a pandas DataFrame.
    Extracted fields:
      - site_name
      - commodity
      - latitude, longitude
    """
    features = data.get("features", [])
    if not features:
        return pd.DataFrame()
    
    records = []
    for feature in features:
        props = feature.get("properties", {})
        geom = feature.get("geometry", {})
        coords = geom.get("coordinates", [None, None])
        record = {
            "site_name": props.get("site_name"),
            "commodity": props.get("commodity"),
            "latitude": coords[1],
            "longitude": coords[0]
        }
        records.append(record)
    
    return pd.DataFrame(records)

# ──────────────────────────────────────────────────────────────────────────
# 3. Streamlit UI with Two Tabs: Earthquake & Minerals
# ──────────────────────────────────────────────────────────────────────────

def main():
    st.title("USGS Data Downloader")
    st.write("Select a tab below to fetch data on Earthquakes or Minerals from the USGS.")

    tab1, tab2 = st.tabs(["Earthquake", "Minerals"])
    
    with tab1:
        st.subheader("Earthquake Data")
        st.markdown("**Source:** [USGS Earthquake Hazards Program](https://earthquake.usgs.gov/)")

        # Sidebar-like controls inside the tab (or you can keep them inline)
        col_eq1, col_eq2, col_eq3 = st.columns(3)
        with col_eq1:
            start_date = st.date_input("Start Date (YYYY-MM-DD)", value=date(2024, 1, 1))
        with col_eq2:
            end_date = st.date_input("End Date (YYYY-MM-DD)", value=date(2024, 2, 1))
        with col_eq3:
            min_magnitude = st.number_input("Min Magnitude", min_value=0.0, max_value=10.0, value=5.0, step=0.1)

        if st.button("Fetch Earthquake Data"):
            start_str = start_date.strftime("%Y-%m-%d")
            end_str = end_date.strftime("%Y-%m-%d")
            with st.spinner("Fetching earthquake data..."):
                data = fetch_earthquake_data(start_str, end_str, min_magnitude)
                if data:
                    df_eq = parse_earthquake_data(data)
                    if df_eq.empty:
                        st.warning("No earthquake data found with those parameters.")
                    else:
                        st.success(f"Fetched {len(df_eq)} earthquake events.")
                        st.dataframe(df_eq.head(10))

                        # Download as CSV
                        csv_data_eq = df_eq.to_csv(index=False).encode("utf-8")
                        st.download_button(
                            label="Download Earthquake Data as CSV",
                            data=csv_data_eq,
                            file_name="earthquakes.csv",
                            mime="text/csv"
                        )

    with tab2:
        st.subheader("Mineral Data")
        st.markdown("**Source:** [USGS Mineral Resources Data System](https://mrdata.usgs.gov/)")

        col_min1, col_min2 = st.columns([2,1])
        with col_min1:
            commodity = st.text_input("Enter Commodity (e.g. 'Gold')", value="Gold")
        with col_min2:
            if st.button("Fetch Mineral Data"):
                with st.spinner("Fetching mineral data..."):
                    data = fetch_minerals_data(commodity)
                    if data:
                        df_min = parse_minerals_data(data)
                        if df_min.empty:
                            st.warning("No mineral site data found for this commodity.")
                        else:
                            st.success(f"Fetched {len(df_min)} mineral site records.")
                            st.dataframe(df_min.head(10))

                            # Download as CSV
                            csv_data_min = df_min.to_csv(index=False).encode("utf-8")
                            st.download_button(
                                label="Download Mineral Data as CSV",
                                data=csv_data_min,
                                file_name="minerals.csv",
                                mime="text/csv"
                            )

if __name__ == "__main__":
    main()
