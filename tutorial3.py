import streamlit as st

def tutorial3_page():
    """
    Tutorial 3: NDVI Analysis & Filtering
    """
    # Display the banner image for Tutorial 3
    st.image(
        "https://raw.githubusercontent.com/hawkarabdulhaq/statistics/main/input/NDVI.png",
        use_container_width=True
    )

    st.title("Tutorial 3: NDVI Analysis & Filtering")

    # Create two tabs
    tab1, tab2 = st.tabs(["Script Overview", "Tutorial Activity"])

    with tab1:
        st.subheader("Tab 1: NDVI Analysis Script")
        st.markdown(
            """
            Below is a **Colab-friendly** Python script (`ndvi_analysis.py`) that:
            1. **Reads** a single-band NDVI GeoTIFF.  
            2. **Computes** basic statistics (min, max, mean, median, std).  
            3. **Plots** a histogram of NDVI values, marking the mean & median.  
            4. **Shows** a reference bar of typical NDVI ranges.  

            **Usage in Colab**:
            1. `!pip install rasterio matplotlib numpy` (if not already installed).  
            2. Place your NDVI GeoTIFF (e.g., `S2_NDVI.tif`) in the same folder or update `NDVI_TIF` in the script.  
            3. Run `!python ndvi_analysis.py` from a Colab cell.
            """
        )

        code_block = """\
# ndvi_analysis.py

import rasterio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Path to your single-band NDVI TIF
NDVI_TIF = '/content/sample_data/S2_NDVI.tif'

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
        st.code(code_block, language="python")

        st.markdown(
            """
            Run **`!python ndvi_analysis.py`** inside Colab (after installing `rasterio`, `matplotlib`, `numpy`)
            to see your NDVI stats, distribution, and a reference bar for typical NDVI ranges.
            """
        )

    with tab2:
        st.subheader("Tab 2: Tutorial Activity (~40 Minutes)")
        st.markdown(
            """
            ### Objective
            - Practice **analyzing** a single-band NDVI image, computing statistics,
              and **interpreting** typical NDVI range categories.

            ### Steps
            1. **Download** your NDVI GeoTIFF (from Earth Engine or another source).  
            2. **Upload** it to Colab (e.g., `/content/sample_data/S2_NDVI.tif`).
            3. Copy the script (`ndvi_analysis.py`) from **Tab 1** into Colab.
            4. Adjust the **`NDVI_TIF`** path to your file, then run `!python ndvi_analysis.py`.

            ### Your Tasks

            1. **Explore Multiple NDVI Scenes**  
               - If possible, generate **2–3** different NDVI images (e.g., from different dates or areas).
               - Run the script on each image, compare stats (min, max, mean, median).

            2. **Interpret the Reference Bar**  
               - Look at the histogram vs. the typical NDVI ranges (water, bare, dense vegetation).
               - Does your histogram align with the reference categories, or do you see unexpected clusters?

            3. **Write a Short Summary (3–5 sentences)**  
               - Note how the NDVI distribution changes across your images.
               - Mention if you found large areas in negative NDVI (e.g., water) or high NDVI (dense vegetation).
               - Suggest at least **one** improvement or further analysis (e.g., combining NDVI with other indices).

            ### Time Estimate (~40 minutes)
            - **5–10 min** uploading & running `ndvi_analysis.py` for the first image.
            - **10–15 min** repeating for additional NDVI images & collecting stats.
            - **5–10 min** writing a reflection on your findings (histogram shape, min/max, typical ranges).
            - **(Optional)** Explore more advanced NDVI thresholds or compare NDVI across seasons.

            **Have fun** experimenting with NDVI and seeing how real data matches (or deviates from) typical spectral assumptions!
            """
        )

def main():
    tutorial3_page()

if __name__ == "__main__":
    main()
