import streamlit as st

def tutorial2_page():
    """
    A single-page tutorial for mean, median, and mode (Tutorial 2).
    Explains how to run '3d_extrusion.py' in Colab to visualize earthquake data in 3D
    while also computing mean, median, and mode of the magnitudes.
    """

    st.title("Tutorial 2: Mean, Median, and Mode with 3D Extrusion Visualization")

    st.markdown(
        """
        In this tutorial, you'll learn how to:
        
        1. **Compute basic statistics** (mean, median, mode) for earthquake magnitudes.  
        2. **Visualize** the data in a **3D extruded** view using earthquake **magnitude** and **depth**.  
        3. Run the script (named **`3d_extrusion.py`**) in **Google Colab** after setting up your data.

        ---
        **Steps to Follow**:
        
        1. **Obtain `earthquakes.csv`**  
           - Use the previous **`dataset.py`** page or USGS API to download the CSV.  
           - Make sure it has columns: `latitude`, `longitude`, `magnitude`, `depth`, and optionally `time`.

        2. **Open Google Colab & Mount Drive**  
           - Go to [Google Colab](https://colab.research.google.com/).  
           - In a new notebook, run:
             ```python
             from google.colab import drive
             drive.mount('/content/drive')
             ```
           - Upload `earthquakes.csv` to `/content/sample_data/` or a folder you prefer.

        3. **Get a World Map Image**  
           - This script references `world_map.png` for a background.  
           - If you don't have it, the script will print a warning and skip rendering the base map.  
           - (Optional) Place `world_map.png` in the same Colab directory.

        4. **Download & Run `3d_extrusion.py`**  
           - Copy the script below into a file named `3d_extrusion.py`.  
           - In a Colab cell, do:
             ```python
             !python 3d_extrusion.py
             ```
           - This script prints **mean, median, mode** for magnitude and **extrudes** each quake event in 3D.

        ---
        ### The `3d_extrusion.py` Script
        Below is the complete script, which:
        - Reads `earthquakes.csv`
        - Calculates **mean**, **median**, and **mode** of quake magnitudes
        - Creates a **3D** view where each quake is an extruded square:
          - Base area ~ **magnitude**  
          - Height ~ **depth**  
          - Color ~ **magnitude** scale
        """
    )

    script_code = """\
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from statistics import mode

# A world map image in equirectangular projection, covering -180..180 in X, -90..90 in Y
world_map_path = 'world_map.png'

# CSV must have columns: latitude, longitude, magnitude, depth
file_path = '/content/sample_data/earthquakes.csv'

def make_extruded_square(lon, lat, mag, dep, scale_area=0.2, scale_height=0.1):
    \"\"\"
    Creates a 3D extruded square:
      - Centered at (lon, lat).
      - Base area ~ magnitude (side ~ sqrt(mag) * scale_area).
      - Height ~ depth * scale_height.
      - Bottom at z=0, top at z=depth*scale_height.
    Returns a list of 6 faces, each a list of (x, y, z) vertices.
    \"\"\"
    mag = max(mag, 0)
    side = np.sqrt(mag) * scale_area
    half_side = side / 2.0

    z_bottom = 0
    z_top = dep * scale_height

    # Base corners
    A = (lon - half_side, lat - half_side, z_bottom)
    B = (lon + half_side, lat - half_side, z_bottom)
    C = (lon + half_side, lat + half_side, z_bottom)
    D = (lon - half_side, lat + half_side, z_bottom)

    # Top corners
    A_ = (A[0], A[1], z_top)
    B_ = (B[0], B[1], z_top)
    C_ = (C[0], C[1], z_top)
    D_ = (D[0], D[1], z_top)

    return [
        [A, B, C, D],      # bottom
        [A_, D_, C_, B_],  # top
        [A, B, B_, A_],    # side1
        [B, C, C_, B_],    # side2
        [C, D, D_, C_],    # side3
        [D, A, A_, D_]     # side4
    ]

def main():
    # 1. Read dataset
    df = pd.read_csv(file_path)
    needed = {'latitude', 'longitude', 'magnitude', 'depth'}
    if not needed.issubset(df.columns):
        print(f"ERROR: CSV must contain columns: {needed}")
        return

    print("Dataset Shape:", df.shape)
    print("\\nFirst 5 Rows:")
    print(df.head())
    print("\\nSummary Statistics:")
    print(df.describe())

    # 2. Compute mean, median, mode of magnitude
    magnitudes = df['magnitude'].dropna()
    mean_mag = magnitudes.mean()
    median_mag = magnitudes.median()
    # Python's built-in 'statistics.mode' can raise an error if there's more than one mode
    # so we'll handle that carefully.
    try:
        mode_mag = mode(magnitudes)
    except:
        mode_mag = "Multiple modes or no valid data"

    print("\\nMean magnitude:", mean_mag)
    print("Median magnitude:", median_mag)
    print("Mode magnitude:", mode_mag)

    # 3. Convert 'time' if present
    if 'time' in df.columns:
        df['time'] = pd.to_datetime(df['time'], errors='coerce')

    # 4. Prepare figure
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(projection='3d')
    ax.set_title("3D Extruded Earthquake Map\\n(Base area ~ magnitude, height ~ depth, color ~ magnitude)")

    # 5. Place the world map at z=-1
    try:
        map_img = plt.imread(world_map_path)
        ny, nx, _ = map_img.shape

        # Create a mesh for X from -180..180, Y from -90..90
        lon_lin = np.linspace(-180, 180, nx)
        lat_lin = np.linspace(-90, 90, ny)
        X, Y = np.meshgrid(lon_lin, lat_lin)
        Z = np.full_like(X, -1.0)

        # Flip vertical axis of the image if needed
        map_img_float = map_img[::-1,:,:].astype(float) / 255.0

        # Plot the map as a surface
        ax.plot_surface(
            X, Y, Z,
            rstride=1, cstride=1,
            facecolors=map_img_float,
            shade=False
        )

    except FileNotFoundError:
        print("WARNING: 'world_map.png' not found. No base map will be shown.")

    # 6. We'll color each building by magnitude
    from matplotlib.colors import Normalize
    cmap = plt.get_cmap('jet')
    mag_min = df['magnitude'].min()
    mag_max = df['magnitude'].max()
    norm = Normalize(vmin=mag_min, vmax=mag_max)

    # 7. Build extruded squares
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection
    all_faces = []
    face_colors = []

    scale_area = 0.2   # horizontal scaling for squares
    scale_height = 0.1 # vertical scaling for depth

    for _, row in df.iterrows():
        lat = row['latitude']
        lon = row['longitude']
        mag = max(0, row['magnitude'])
        dep = max(0, row['depth'])

        color_rgba = cmap(norm(mag))
        faces = make_extruded_square(lon, lat, mag, dep, scale_area, scale_height)
        all_faces.extend(faces)
        face_colors.extend([color_rgba]*len(faces))

    poly_collection = Poly3DCollection(
        all_faces,
        facecolors=face_colors,
        edgecolors=None,
        linewidths=0,
        alpha=0.8
    )
    ax.add_collection3d(poly_collection)

    # 8. Axis bounds
    lon_min, lon_max = df['longitude'].min(), df['longitude'].max()
    lat_min, lat_max = df['latitude'].min(), df['latitude'].max()
    depth_max = df['depth'].max()

    # Show entire globe or clamp to data. Here, entire globe:
    ax.set_xlim(-180, 180)
    ax.set_ylim(-90, 90)
    # z-limits
    ax.set_zlim(-1.5, depth_max * scale_height * 1.5)

    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.set_zlabel("Depth Extrusion")

    # 9. Colorbar for magnitude
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cb = plt.colorbar(sm, ax=ax, pad=0.1, shrink=0.6)
    cb.set_label("Magnitude")

    print("\\nClose the plot window to end the script.")
    plt.show()

if __name__ == "__main__":
    main()
"""
    st.code(script_code, language="python")

    st.markdown(
        """
        ---
        **How to interpret the results**:
        - **Mean magnitude** tells you the average quake size.
        - **Median magnitude** is the midpoint—half of quakes are smaller, half are larger.
        - **Mode magnitude** is the most frequently occurring magnitude (if a clear single mode exists).
        - The **3D view** extrudes each event based on **magnitude** and **depth**, 
          giving you a tangible sense of where bigger, deeper quakes occur.

        When you run `3d_extrusion.py`, you'll see these statistics printed, 
        followed by a 3D figure. Click on the figure to **rotate** and **explore** 
        quake events in 3D space.
        
        **Enjoy exploring how mean, median, and mode can provide quick insights** 
        into your dataset’s central tendencies, 
        while the 3D extrusions offer a more **visual** perspective of the data.
        """
    )

def main():
    tutorial2_page()

if __name__ == "__main__":
    main()
