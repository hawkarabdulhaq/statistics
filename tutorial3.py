import streamlit as st

def tutorial3_page():
    """
    Tutorial 3: NDVI Analysis & Advanced Filtering

    This page has two tabs:
    1) NDVI Analysis (Plots histogram, shows NDVI range bar).
    2) Advanced Filtering Script (Extract polygons for a given NDVI range, display in Folium).
    """

    # Banner image for Tutorial 3
    st.image(
        "https://raw.githubusercontent.com/hawkarabdulhaq/statistics/main/input/NDVI.png",
        use_container_width=True
    )

    st.title("Tutorial 3: NDVI Analysis & Filtering")

    tab1, tab2 = st.tabs(["Tab 1: NDVI Analysis Script", "Tab 2: Filtering Script"])

    # ────────────────────────────────────────────────────────────────────
    # TAB 1: NDVI ANALYSIS SCRIPT
    # ────────────────────────────────────────────────────────────────────
    with tab1:
        st.subheader("NDVI Analysis Script")
        st.markdown(
            """
            In **Tab 1**, you see a **Colab**-friendly Python script to:
            1. **Read** a single-band NDVI GeoTIFF.
            2. **Compute** NDVI stats (min, max, mean, median, etc.).
            3. **Plot** a histogram and a reference bar for typical NDVI ranges.

            **Usage in Colab**:
            ```bash
            !pip install rasterio matplotlib numpy
            !python ndvi_analysis.py
            ```
            Make sure your NDVI file path is correct.
            """
        )

        ndvi_analysis_script = """\
# ndvi_analysis.py

import rasterio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Path to your single-band NDVI TIF
NDVI_TIF = 'https://github.com/hawkarabdulhaq/statistics/blob/main/input/S2_NDVI2.tif'

def main():
    # 1) Read NDVI GeoTIFF
    with rasterio.open(NDVI_TIF) as src:
        ndvi_data = src.read(1).astype(float)
        ndvi_transform = src.transform
        ndvi_crs = src.crs
        ndvi_nodata = src.nodata
        
        print("=== NDVI Raster Info ===")
        print("CRS:", ndvi_crs)
        print("Transform:", ndvi_transform)
        print("Raster shape (rows, cols):", ndvi_data.shape)
        print("NoData value:", ndvi_nodata)

        # Mask out NoData if present
        if ndvi_nodata is not None:
            ndvi_data = np.ma.masked_equal(ndvi_data, ndvi_nodata)

    # Flatten and remove any NaNs
    ndvi_values = ndvi_data.compressed() if np.ma.is_masked(ndvi_data) else ndvi_data.ravel()
    ndvi_values = ndvi_values[~np.isnan(ndvi_values)]

    if ndvi_values.size == 0:
        print("No valid NDVI pixels found. Exiting.")
        return

    # 2) Basic Statistics
    ndvi_min = ndvi_values.min()
    ndvi_max = ndvi_values.max()
    ndvi_mean = ndvi_values.mean()
    ndvi_median = np.median(ndvi_values)
    ndvi_std = ndvi_values.std()
    p25 = np.percentile(ndvi_values, 25)
    p75 = np.percentile(ndvi_values, 75)

    print("\\n=== NDVI Statistics ===")
    print(f"Min: {ndvi_min:.3f}")
    print(f"Max: {ndvi_max:.3f}")
    print(f"Mean: {ndvi_mean:.3f}")
    print(f"Median: {ndvi_median:.3f}")
    print(f"Std Dev: {ndvi_std:.3f}")
    print(f"25th percentile: {p25:.3f}")
    print(f"75th percentile: {p75:.3f}")

    # 3) Plot a histogram of NDVI
    plt.figure(figsize=(10, 5))
    plt.hist(ndvi_values, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
    plt.title("NDVI Distribution")
    plt.xlabel("NDVI Value")
    plt.ylabel("Count")

    # Mean / Median lines
    plt.axvline(ndvi_mean, color='red', linestyle='dashed', linewidth=1, label=f"Mean={ndvi_mean:.3f}")
    plt.axvline(ndvi_median, color='green', linestyle='dotted', linewidth=1, label=f"Median={ndvi_median:.3f}")
    plt.legend()
    plt.show()

    # 4) Reference Bar: Typical NDVI Ranges
    ndvi_classes = [
        (-1.0,  0.0, "Water or snow",       'blue'),
        ( 0.0,  0.2, "Bare soil/urban",     'tan'),
        ( 0.2,  0.4, "Low vegetation",      'yellowgreen'),
        ( 0.4,  0.6, "Moderate vegetation", 'green'),
        ( 0.6,  1.0, "Dense vegetation",    'darkgreen')
    ]

    plt.figure(figsize=(8, 2))
    ax = plt.gca()
    ax.set_xlim(-1, 1)
    ax.set_ylim(0, 1)
    ax.set_title("Typical NDVI Ranges", fontsize=12)

    for (start, end, label, color) in ndvi_classes:
        width = end - start
        rect = patches.Rectangle((start, 0), width, 1, facecolor=color, edgecolor='black')
        ax.add_patch(rect)
        mid_x = (start + end) / 2
        ax.text(
            mid_x, 
            0.5, 
            label, 
            ha='center', 
            va='center', 
            rotation=90,
            rotation_mode='anchor',
            fontsize=9, 
            color='white' if color in ['blue','green','darkgreen'] else 'black'
        )

    ax.set_xticks([-1, -0.5, 0, 0.5, 1])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.set_xlabel("NDVI Value")
    plt.show()

    print("\\n=== Analysis Complete ===")
    print("Displayed histogram and typical NDVI range reference figure with vertical labels.")

if __name__ == "__main__":
    main()
"""
        st.code(ndvi_analysis_script, language="python")

    # ────────────────────────────────────────────────────────────────────
    # TAB 2: FILTERING SCRIPT
    # ────────────────────────────────────────────────────────────────────
    with tab2:
        st.subheader("Filtering Script (NDVI Range Polygons)")
        st.markdown(
            """
            In **Tab 2**, we have a more **advanced** script to:
            1. Filter a single-band NDVI TIF by a given NDVI range (e.g., 0.3–0.7).
            2. Convert those filtered areas to **polygons**.
            3. Reproject them to EPSG:4326.
            4. Display them on a **Folium** map in Colab.

            **Usage in Colab**:
            ```bash
            !pip install rasterio shapely pyproj folium
            !python ndvi_filter.py
            ```
            Make sure you update the `NDVI_TIF` path, `NDVI_LOW`, and `NDVI_HIGH` as needed.
            """
        )

        filter_script = """\
# ndvi_filter.py
# In Colab:
# !pip install rasterio shapely pyproj folium

import rasterio
import rasterio.features
import rasterio.warp
from shapely.geometry import shape, mapping
from shapely.ops import transform
from pyproj import Transformer
import folium
import numpy as np

# FILE PATH to your NDVI GeoTIFF (assumed single-band)
NDVI_TIF = '/content/sample_data/S2_NDVI.tif'

# NDVI range
NDVI_LOW = 0.3
NDVI_HIGH = 0.7

def main():
    # 1) Open NDVI TIF
    with rasterio.open(NDVI_TIF) as ndvi_src:
        ndvi_data = ndvi_src.read(1).astype(float)
        ndvi_transform = ndvi_src.transform
        ndvi_crs = ndvi_src.crs

        # Handle NoData if present
        ndvi_nodata = ndvi_src.nodata
        if ndvi_nodata is not None:
            ndvi_data = np.ma.masked_equal(ndvi_data, ndvi_nodata)

        # Create a boolean mask for NDVI in [NDVI_LOW, NDVI_HIGH]
        mask = (ndvi_data >= NDVI_LOW) & (ndvi_data <= NDVI_HIGH)

    # 2) Convert the boolean mask to polygons
    polygons = []
    for geom, val in rasterio.features.shapes(
        mask.astype(np.uint8),
        transform=ndvi_transform
    ):
        if val == 1:
            polygons.append(shape(geom))

    print(f"Extracted {len(polygons)} polygons where {NDVI_LOW} <= NDVI <= {NDVI_HIGH}.")

    # 3) Reproject polygons to EPSG:4326 for Folium
    target_crs = 'EPSG:4326'
    transformer = Transformer.from_crs(ndvi_crs.to_string(), target_crs, always_xy=True)

    def reproject_geom(geom):
        return transform(transformer.transform, geom)

    reproj_polygons = [reproject_geom(poly) for poly in polygons if not poly.is_empty]

    # 4) Convert each reprojected polygon to GeoJSON
    features_list = []
    for poly in reproj_polygons:
        if poly.geom_type == 'MultiPolygon':
            for subpoly in poly.geoms:
                feat = {
                    "type": "Feature",
                    "geometry": mapping(subpoly),
                    "properties": {"NDVI_Range": f"{NDVI_LOW}..{NDVI_HIGH}"}
                }
                features_list.append(feat)
        else:
            feat = {
                "type": "Feature",
                "geometry": mapping(poly),
                "properties": {"NDVI_Range": f"{NDVI_LOW}..{NDVI_HIGH}"}
            }
            features_list.append(feat)

    feature_collection = {
        "type": "FeatureCollection",
        "features": features_list
    }

    # 5) Determine map center from polygon bounds
    if reproj_polygons:
        overall_bounds = reproj_polygons[0].bounds
        for poly in reproj_polygons[1:]:
            bx = poly.bounds
            overall_bounds = (
                min(overall_bounds[0], bx[0]),
                min(overall_bounds[1], bx[1]),
                max(overall_bounds[2], bx[2]),
                max(overall_bounds[3], bx[3])
            )
        center_lat = (overall_bounds[1] + overall_bounds[3]) / 2.0
        center_lon = (overall_bounds[0] + overall_bounds[2]) / 2.0
    else:
        center_lon, center_lat = 0, 0

    # 6) Create Folium map
    folium_map = folium.Map(location=[center_lat, center_lon], zoom_start=13)

    # 7) Add polygons as a GeoJson layer
    def style_function(feature):
        return {
            'fillColor': 'purple',
            'color': 'purple',
            'weight': 1,
            'fillOpacity': 0.2
        }

    folium.GeoJson(
        feature_collection,
        name='NDVI Polygons',
        style_function=style_function
    ).add_to(folium_map)

    folium.LayerControl().add_to(folium_map)

    # 8) Display in Colab
    display(folium_map)

if __name__ == "__main__":
    main()
"""
        st.code(filter_script, language="python")

        st.markdown(
            """
            **Time Estimate (~40 minutes)**:
            1. **(5–10 min)** Adjust NDVI range, run script for different NDVI thresholds.
            2. **(10–15 min)** Examine the polygons in Folium—do they match real vegetation or land cover?
            3. **(5–10 min)** Summarize your observations: how well does your NDVI range capture the land cover you want?

            This approach can help you see exactly **where** NDVI meets your criteria, 
            turning raster data into **polygons** for further GIS analysis or map display.
            """
        )

def main():
    tutorial3_page()

if __name__ == "__main__":
    main()
