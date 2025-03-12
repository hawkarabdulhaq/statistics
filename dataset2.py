import streamlit as st
import pandas as pd

def main():
    st.title("Dataset 2: Elevation Data Visualization")
    st.markdown("This page visualizes the elevation data stored in `input/Elevation_backup.xyz`. \
The dataset consists of three columns: longitude, latitude, and elevation.")

    # Define the file path
    file_path = "input/Elevation_backup.xyz"

    # Load the dataset using pandas
    try:
        # Read the file assuming whitespace-delimited values and assign column names
        df = pd.read_csv(file_path, delim_whitespace=True, header=None, names=["lon", "lat", "elevation"])
        st.subheader("Dataset Preview")
        st.dataframe(df)
        
        # Display a map using latitude and longitude columns
        st.subheader("Map View")
        # st.map requires a DataFrame with columns 'lat' and 'lon'
        st.map(df[["lat", "lon"]])
    except Exception as e:
        st.error(f"Error loading dataset: {e}")

    # Provide a download button for the dataset
    st.subheader("Download the Dataset")
    try:
        # Open and read the file content
        with open(file_path, "r") as f:
            file_contents = f.read()
        st.download_button(
            label="Download Elevation Data",
            data=file_contents,
            file_name="Elevation_backup.xyz",
            mime="text/plain"
        )
    except Exception as e:
        st.error(f"Error reading file for download: {e}")

if __name__ == "__main__":
    main()
