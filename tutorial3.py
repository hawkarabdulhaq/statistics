import streamlit as st

def tutorial3_page():
    """
    Tutorial 3: Filtering Data for Water, Forest, and Crops (Approx. 40-Minute Activity)

    Students will:
    1) Acquire a multi-band satellite image (e.g., Sentinel-2).
    2) Filter and threshold certain bands (e.g., NDVI for vegetation, MNDWI for water).
    3) Generate simple masks to highlight different land covers (forest, crops, etc.).
    4) Visualize and compare the masks, then reflect on how well they differentiate features.
    """

    # Display the banner image
    st.image(
        "https://raw.githubusercontent.com/hawkarabdulhaq/statistics/main/input/NDVI.png", 
        use_container_width=True
    )

    st.title("Tutorial 3: Filtering Data for Water, Forest, and Crops")

    # Create tabs; the first tab contains our filtering script
    tabs = st.tabs(["Tab 1: Filtering Script"])

    with tabs[0]:
        st.markdown(
            """
            This tutorial lets you **explore spectral band filtering** to identify water, 
            forest, or crop areas from a **satellite image** (e.g., **Sentinel-2**). 
            You’ll **download** the imagery, **run** a Python script in **Google Colab** to:
            
            - **Compute** simple indices (NDVI, MNDWI, etc.).
            - **Apply** thresholds to create **masks** for water, forest, or crops.
            - **Visualize** the results and **reflect** on how well they separate land covers.

            ---
            ### Approximate Time: ~40 Minutes
            1. **(5–10 min)** Acquire multi-band imagery (e.g., from Earth Engine exports).  
            2. **(5–10 min)** Set up Colab, place the image file in your environment.  
            3. **(10–15 min)** Run the filtering script, experiment with thresholds, generate masks.  
            4. **(5–10 min)** Write a short reflection about your results.

            By the end, you should see how **band-specific filters** can highlight different surface features.

            ---
            **Data**:  
            - We have uploaded a sample NDVI file: **`S2_NDVI2.tif`**  
              ([GitHub Link](https://github.com/hawkarabdulhaq/statistics/blob/main/input/S2_NDVI2.tif), 
               [Google Drive Link](https://drive.google.com/file/d/1IkSC2TLisPAeBYP1OTFdlShLI-HiuEIL/view?usp=drive_link))  
            - Place it in `/content/sample_data/` in Colab if you'd like to modify/inspect it.

            ---
            ### Step 1: Acquire/Set Up the Data
            - Download **`S2_NDVI2.tif`** (or your own multi-band image).
            - Move it to `/content/sample_data/` in Colab.

            ### Step 2: Run the Script Below
            - Copy into a file named **`band_filter.py`**.
            - In Colab:
              ```python
              !python band_filter.py
              ```
            - Adjust band indices or thresholds to differentiate land covers.

            **Your Task**:
            1. Tweak NDVI thresholds to separate forest/crops from bare land.  
            2. If you have SWIR, compute **MNDWI** for water detection.  
            3. Check the resulting masks. Reflect on misclassifications or edge cases.

            ---
            ### `band_filter.py` Script
            Below is the code referencing `S2_NDVI2.tif`; feel free to rename or modify as needed:
            """
        )

        script_code = """\
import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Path to your multi-band TIF (can be NDVI or multi-band if you have separate B3,B4,B8, etc.)
tif_path = '/content/sample_data/S2_NDVI2.tif'

def main():
    # 1. Open the multi-band raster
    with rasterio.open(tif_path) as src:
        band_count = src.count
        print(f'File has {band_count} band(s).')

        # Example usage: if band_count >= 3, we might read indices for Green/Red/NIR
        # Adjust these according to your actual file layout:
        # green_band = src.read(2).astype(float)  # B3
        # red_band   = src.read(3).astype(float)  # B4
        # nir_band   = src.read(4).astype(float)  # B8
        #
        # If S2_NDVI2.tif is already a single-band NDVI, you might skip direct NDVI calc.
        # For demonstration, let's assume we have a single-band NDVI:
        ndvi_data = src.read(1).astype(float)
        
        # NDVI-based threshold for vegetation
        veg_threshold = 
