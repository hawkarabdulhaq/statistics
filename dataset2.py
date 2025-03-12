import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from scipy.interpolate import griddata

def main():
    st.title("Dataset 2: Elevation Data Visualization")
    st.markdown(
        """
        This page visualizes the elevation data stored in `input/Elevation_backup.xyz` as a colorful 3D surface plot.
        The dataset contains three columns: **longitude**, **latitude**, and **elevation**.
        """
    )
    
    # Define the file path for the dataset
    file_path = "input/Elevation_backup.xyz"
    
    # Load the dataset
    try:
        df = pd.read_csv(file_path, delim_whitespace=True, header=None, names=["lon", "lat", "elevation"])
        st.subheader("Dataset Preview")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return
    
    # Create a grid for interpolation
    lon_min, lon_max = df["lon"].min(), df["lon"].max()
    lat_min, lat_max = df["lat"].min(), df["lat"].max()
    
    # Define grid resolution (adjust as needed)
    grid_resolution = 100
    grid_lon, grid_lat = np.mgrid[lon_min:lon_max:complex(0, grid_resolution), lat_min:lat_max:complex(0, grid_resolution)]
    
    # Interpolate elevation data onto the grid
    grid_elev = griddata(
        points=df[["lon", "lat"]].values,
        values=df["elevation"].values,
        xi=(grid_lon, grid_lat),
        method="cubic"
    )
    
    # Create a colorful 3D surface plot with Plotly
    fig = go.Figure(data=[go.Surface(
        x=grid_lon,
        y=grid_lat,
        z=grid_elev,
        colorscale='Viridis',
        colorbar=dict(title="Elevation (m)")
    )])
    
    # Adjust the layout to reduce vertical exaggeration by scaling down the z-axis
    fig.update_layout(
        title="3D Elevation Surface",
        scene=dict(
            xaxis_title='Longitude',
            yaxis_title='Latitude',
            zaxis_title='Elevation',
            aspectratio=dict(x=1, y=1, z=0.3)  # Reduced vertical exaggeration
        )
    )
    
    st.subheader("3D Surface Visualization")
    st.plotly_chart(fig, use_container_width=True)
    
    # Provide a download button for the dataset
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
