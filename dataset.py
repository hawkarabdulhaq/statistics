import streamlit as st
import pandas as pd
import requests
from datetime import datetime
import io

###########################
# Earthquake Data Helpers #
###########################
@st.cache_data(show_spinner=True)
def fetch_earthquake_data(starttime, endtime, minmagnitude):
    """
    Fetches earthquake data from USGS API in GeoJSON format.
    Returns a dictionary (parsed JSON).
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
        st.error("Error fetching earthquake data. Please try again.")
        return None
    return response.json()

@st.cache_data(show_spinner=True)
def parse_earthquake_data(data):
    """
    Converts GeoJSON earthquake data into a Pandas DataFrame.
    Includes columns:
      - time (UTC)
      - magnitude
      - place
      - longitude, latitude, depth
    """
    features = data.get("features", [])
    records = []
    for f in features:
        props = f.get("properties", {})
        geom = f.get("geometry", {})
        coords = geom.get("coordinates", [None, None, None])
        
        event_time_ms = props.get("time")  # Epoch in ms
        if event_time_ms:
            event_time = datetime.utcfromtimestamp(event_time_ms / 1000).strftime("%Y-%m-%d %H:%M:%S")
        else:
            event_time = None
        
        record = {
            "time": event_time,
            "magnitude": props.get("mag"),
            "place": props.get("place"),
            "longitude": coords[0],
            "latitude": coords[1],
            "depth": coords[2]
        }
        records.append(record)
    return pd.DataFrame(records)


########################
# NOAA Paleo Helpers   #
########################
@st.cache_data(show_spinner=True)
def search_ice_core_studies(keyword):
    """
    Searches NOAA Paleoclimatology database for studies by keyword.
    Returns JSON structure with studies if successful.
    """
    search_url = "https://www.ncei.noaa.gov/access/paleo-search/study/search.json"
    params = {"keywords": keyword}
    resp = requests.get(search_url, params=params)
    if resp.status_code == 200:
        return resp.json()
    else:
        st.error("Error searching NOAA database. Try another keyword.")
        return None

@st.cache_data(show_spinner=True)
def fetch_study_details(study_id):
    """
    Fetches the details of a specific study by studyId.
    Returns JSON with the full study metadata.
    """
    url = f"https://www.ncei.noaa.gov/access/paleo-search/study/{study_id}.json"
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    else:
        st.error("Error fetching study details.")
        return None

########################
# Main Streamlit App   #
########################
def main():
    st.title("Data Explorer: Earthquake & Ice Core CO₂")
    
    tab1, tab2 = st.tabs(["Earthquake Data", "Ice Core CO₂ Data"])

    #####################
    # Tab 1: Earthquakes
    #####################
    with tab1:
        st.subheader("1. USGS Earthquake Data")
        st.write("Retrieve earthquake events in a specified date range with a minimum magnitude, then download as CSV.")
        
        # Sidebar-like controls in the main area for clarity
        start_date = st.date_input("Start Date", value=pd.to_datetime("2024-01-01"))
        end_date = st.date_input("End Date", value=pd.to_datetime("2024-02-01"))
        min_magnitude = st.number_input("Minimum Magnitude", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
        
        if st.button("Fetch Earthquake Data"):
            start_str = start_date.strftime("%Y-%m-%d")
            end_str = end_date.strftime("%Y-%m-%d")
            
            with st.spinner("Fetching earthquake data from USGS..."):
                eq_data = fetch_earthquake_data(start_str, end_str, min_magnitude)
                if eq_data:
                    df_eq = parse_earthquake_data(eq_data)
                    if df_eq.empty:
                        st.warning("No earthquake data found for these parameters.")
                    else:
                        st.success(f"Fetched {len(df_eq)} earthquake events.")
                        st.dataframe(df_eq.head(10))
                        
                        # CSV download
                        csv_data = df_eq.to_csv(index=False).encode("utf-8")
                        st.download_button(
                            label="Download Earthquakes CSV",
                            data=csv_data,
                            file_name="earthquakes.csv",
                            mime="text/csv"
                        )

    #####################
    # Tab 2: Ice Core CO2
    #####################
    with tab2:
        st.subheader("2. NOAA Paleoclimatology Data (Ice Core CO₂)")
        st.write("Search the NOAA Paleo database by keyword, then retrieve a chosen study's data file.")

        keyword = st.text_input("Search Keyword:", value="ice core CO2")
        if st.button("Search Studies"):
            with st.spinner("Searching NOAA Paleoclimatology studies..."):
                search_results = search_ice_core_studies(keyword)
                if search_results and "study" in search_results:
                    studies = search_results["study"]
                    if not studies:
                        st.warning("No studies found for this keyword.")
                    else:
                        # Let the user pick a study from results
                        st.success(f"Found {len(studies)} studies.")
                        
                        # Create a list of (label, value) for selectbox
                        study_options = [
                            (f"ID {s['studyId']}: {s['site']['siteName']} - {s['studyName']}", s['studyId'])
                            for s in studies
                        ]
                        # Sort by ID or name as needed
                        study_options_sorted = sorted(study_options, key=lambda x: x[1])
                        
                        # Let user select
                        selected_label = st.selectbox(
                            "Select a Study to Retrieve:",
                            options=[opt[0] for opt in study_options_sorted]
                        )
                        # Find the corresponding ID
                        selected_study_id = None
                        for label, val in study_options_sorted:
                            if label == selected_label:
                                selected_study_id = val
                                break
                        
                        if selected_study_id:
                            if st.button("Retrieve Study Data"):
                                with st.spinner("Fetching study details..."):
                                    study_data = fetch_study_details(selected_study_id)
                                    if study_data and "study" in study_data:
                                        st.success("Study details retrieved.")
                                        # Attempt to fetch a data file URL
                                        # Sometimes multiple dataFile entries exist
                                        data_files = []
                                        try:
                                            data_files = study_data["study"][0]["site"][0]["dataFile"]
                                        except (KeyError, IndexError):
                                            pass

                                        if not data_files:
                                            st.warning("No data files found for this study.")
                                        else:
                                            # For simplicity, let's just pick the first dataFile URL
                                            file_url = data_files[0]["url"]
                                            file_label = data_files[0].get("fileDescription", "Data File")
                                            st.write(f"**Selected File:** {file_label}")
                                            st.write(f"**URL:** {file_url}")
                                            
                                            # Fetch the data file
                                            file_resp = requests.get(file_url)
                                            if file_resp.status_code == 200:
                                                file_content = file_resp.text
                                                st.text_area("File Preview", file_content[:1000], height=200)
                                                
                                                # Provide a download button
                                                st.download_button(
                                                    label="Download Study Data",
                                                    data=file_content.encode("utf-8"),
                                                    file_name="study_data.txt",
                                                    mime="text/plain"
                                                )
                                            else:
                                                st.error("Could not retrieve the data file.")
                                    else:
                                        st.warning("Study details are empty or invalid.")
                else:
                    st.error("No valid response from NOAA search. Check your keyword or try again.")


if __name__ == "__main__":
    main()
