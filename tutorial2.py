import streamlit as st

def tutorial2_page():
    """
    Tutorial 2: Mean, Median, and Mode with 3D Extrusion Visualization
    """
    # Display the banner image from GitHub
    st.image(
        "https://raw.githubusercontent.com/hawkarabdulhaq/statistics/main/input/02.jpg", 
        use_container_width=True
    )

    st.title("Tutorial 2: Mean, Median, and Mode with 3D Extrusion Visualization")

    st.markdown(
        """
        In this tutorial, you'll learn how to:
        
        1. **Compute basic statistics** (mean, median, and mode) for earthquake magnitudes.  
        2. **Visualize** the data in a **3D extruded** view using earthquake **magnitude** (base area) and **depth** (height).  
        3. Execute the script (named **`3d_extrusion.py`**) in **Google Colab** after placing your dataset.

        ---
        **Steps**:
        
        **1. Acquire `earthquakes.csv`**  
        - From the **dataset** page (or via the USGS API directly).  
        - Make sure the CSV has `latitude`, `longitude`, `magnitude`, and `depth`. Optionally `time`.

        **2. Open Google Colab**  
        - Navigate to [Google Colab](https://colab.research.google.com/).  
        - Create a new notebook and run:
          ```python
          from google.colab import drive
          drive.mount('/content/drive')
          ```
        - Place `earthquakes.csv` into `/content/sample_data/` or your desired folder.

        **3. World Map (Optional)**  
        - The script references a `world_map.png`.  
        - If you don't provide it, a warning appears, but the 3D quake extrusions still render.

        **4. Download & Run `3d_extrusion.py`**  
        - Copy the script below into a file named `3d_extrusion.py`.  
        - In Colab, run:
          ```python
          !python 3d_extrusion.py
          ```
        - This prints **mean, median, mode** of quake magnitudes & extrudes each event in 3D.

        ---
        ### `3d_extrusion.py` Script
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

    # 5. Place the world map at z=-1 if available
    try:
        map_img = plt.imread(world_map_path)
        ny, nx, _ = map_img.shape
        lon_lin = np.linspace(-180, 180, nx)
        lat_lin = np.linspace(-90, 90, ny)
        X, Y = np.meshgrid(lon_lin, lat_lin)
        Z = np.full_like(X, -1.0)

        map_img_float = map_img[::-1,:,:].astype(float) / 255.0
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

    # 7. Axis bounds
    depth_max = df['depth'].max()
    ax.set_xlim(-180, 180)
    ax.set_ylim(-90, 90)
    ax.set_zlim(-1.5, depth_max * scale_height * 1.5)
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.set_zlabel("Depth Extrusion")

    # 8. Colorbar for magnitude
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
        **Interpreting the Results**:
        
        - **Mean**: The average quake magnitude.  
        - **Median**: The "middle" quake magnitude when sorted—half are smaller, half are bigger.  
        - **Mode**: The most frequently appearing magnitude (if there's a single dominant value).  
        
        In the **3D** view:
        - **Base area** of each square ~ `sqrt(magnitude)`.  
        - **Height** ~ `depth`.  
        - **Color** ~ `magnitude` (colormap from blue=low to red=high).
        
        This approach blends **basic statistics** with **visual geospatial context**, 
        letting you see patterns in magnitude and depth simultaneously.
        
        **Enjoy exploring your data** and seeing how mean, median, and mode 
        can highlight different aspects of quake distributions!
        """
    )

def main():
    tutorial2_page()

if __name__ == "__main__":
    main()
