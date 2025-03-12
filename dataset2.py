import streamlit as st
import pandas as pd

def main():
    st.title("Dataset 2: Elevation Data Visualization")
    st.markdown(
        "This page visualizes the elevation data stored in `input/Elevation_backup.xyz`. "
        "The dataset consists of three columns: longitude, latitude, and elevation."
    )
    
    file_path = "input/Elevation_backup.xyz"
    
    # Load the dataset
    try:
        df = pd.read_csv(file_path, delim_whitespace=True, header=None, names=["lon", "lat", "elevation"])
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return
    
    # Create a grid layout with two columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Dataset Preview")
        st.dataframe(df)
    
    with col2:
        st.subheader("Map View")
        # st.map requires a DataFrame with 'lat' and 'lon'
        st.map(df[["lat", "lon"]])
    
    st.markdown("---")
    
    st.subheader("Download the Dataset")
    try:
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
