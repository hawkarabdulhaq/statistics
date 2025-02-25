import streamlit as st

def tutorial3_page():
    """
    Tutorial 3: Filtering Data for Water, Forest, and Crops (Approx. 40-Minute Activity)

    Students will:
    1) Acquire a multi-band satellite image (e.g., Sentinel-2).
    2) Filter and threshold certain bands (e.g., NDVI for vegetation, MNDWI for water).
    3) Generate simple masks to highlight different land covers.
    4) Visualize and compare the masks, then reflect on how well they differentiate features.
    """

    # Display the banner image
    st.image(
        "https://raw.githubusercontent.com/hawkarabdulhaq/statistics/main/input/NDVI.png", 
        use_container_width=True
    )

    st.title("Tutorial 3: Filtering Data for Water, Forest, and Crops")

    st.markdown(
        """
        This tutorial lets you **explore spectral band filtering** to identify water, 
        forest, or crop areas from a **satellite image** (e.g., **Sentinel-2**). 
        You’ll **download** the imagery, **run** a Python script in **Google Colab** to:
        
        - **Compute** simple indices (NDVI, MNDWI, etc.).
        - **Apply** thresholds to create **masks** for water, forest, or crops.
        - **Visualize** the results and **reflect** on how well they separate land covers.

        ---
        ## Approximate Time: ~40 Minutes
        1. **(5–10 min)** Acquire multi-band imagery (e.g., from Earth Engine exports).  
        2. **(5–10 min)** Set up Colab, place the image file in your environment.  
        3. **(10–15 min)** Run the filtering script, experiment with thresholds, generate masks.  
        4. **(5–10 min)** Write a short reflection about your results.

        By the end, you should see how **band-specific filters** can highlight different surface features.
        """
    )

    st.markdown(
        """
        ---
        ### Step 1: Acquire a Multi-Band Satellite Image
        - From **Earth Engine** or another source, download an image (e.g., `S2_clipped.tif`).
        - Ensure it contains **near-infrared** (for vegetation) and **green** or **SWIR** (for water index), 
          and ideally **red** or other relevant bands.

        **Example**: 
        - A **Sentinel-2** image clipped to your study region with bands: B2 (Blue), B3 (Green), B4 (Red), B8 (NIR).

        ---
        ### Step 2: Prepare Google Colab
        - Go to [Google Colab](https://colab.research.google.com/).
        - Create a **new notebook**.
        - Mount drive:
          ```python
          from google.colab import drive
          drive.mount('/content/drive')
          ```
        - Upload your multi-band GeoTIFF (e.g., `S2_clipped.tif`) to `/content/sample_data/`.

        ---
        ### Step 3: Run the `band_filter.py` Script
        - Copy the script below into a file named **`band_filter.py`**.
        - Modify `tif_path` if your file is named differently or in a different folder.
        - In Colab, do:
          ```python
          !python band_filter.py
          ```

        **Your Task**:
        1. Adjust **thresholds** for NDVI to separate forest or crops from bare land.  
        2. Use a **water index** (e.g., MNDWI = (Green - SWIR) / (Green + SWIR)) to try isolating water bodies.  
        3. Examine the resulting **mask plots**. Does water appear cleanly separated? Are there false positives?

        ---
        ### Step 4: Reflect (Spend ~20 minutes)
        - Which threshold values best separated vegetation from non-vegetation?
        - Did your water mask accidentally classify wetlands or water-adjacent crops as water?
        - How might seasonal variations or cloud shadows affect these thresholds?

        Write a **short paragraph** (3–5 sentences) summarizing your observations. 
        Suggest at least **one improvement** (like using different band combinations or more advanced indices).

        ---
        ### `band_filter.py` Script
        This script reads a multi-band TIFF, computes NDVI and MNDWI, thresholds them, 
        and plots the resulting masks in **matplotlib**:
        """
    )

    script_code = """\
import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Path to your multi-band TIFF
tif_path = '/content/sample_data/S2_clipped.tif'

def main():
    # 1. Open the multi-band raster (e.g., Sentinel-2)
    with rasterio.open(tif_path) as src:
        # Read relevant bands
        # Example: B3 (Green) index=2, B4 (Red)=3, B8 (NIR)=7, B11 (SWIR)=10, etc.
        # Adjust indices based on how your file is stored
        green_band = src.read(2).astype(float)  # B3 index might vary
        red_band   = src.read(3).astype(float)  # B4
        nir_band   = src.read(4).astype(float)  # B8, if in the 4th slot
        # If you have SWIR band, read it similarly:
        # swir_band  = src.read(5).astype(float)  # B11 or B12 depends on your file

        # 2. Compute NDVI if Red and NIR are available
        # NDVI = (NIR - Red) / (NIR + Red)
        ndvi_numerator = (nir_band - red_band)
        ndvi_denominator = (nir_band + red_band)
        ndvi = np.divide(ndvi_numerator, ndvi_denominator, out=np.zeros_like(ndvi_numerator), where=ndvi_denominator!=0)

        # 3. Simple NDVI threshold for vegetation (e.g., NDVI > 0.3 is "green")
        veg_mask = ndvi > 0.3

        # 4. Compute MNDWI if Green and SWIR are available
        # MNDWI = (Green - SWIR) / (Green + SWIR)
        # Here we assume you have swir_band read. If not, skip or use placeholder
        # swir_band is not read in this example, but let's pretend:
        # mndwi_numerator = (green_band - swir_band)
        # mndwi_denominator = (green_band + swir_band)
        # mndwi = np.divide(mndwi_numerator, mndwi_denominator, out=np.zeros_like(mndwi_numerator), where=mndwi_denominator!=0)
        # water_mask = mndwi > 0.0  # Adjust as needed

        # For demonstration, let's just skip if no SWIR:
        water_mask = np.zeros_like(green_band, dtype=bool)

        # 5. Plot NDVI and the masks
        plt.figure(figsize=(10, 8))

        # NDVI
        plt.subplot(2, 2, 1)
        plt.imshow(ndvi, cmap='RdYlGn', vmin=-1, vmax=1)
        plt.colorbar(label='NDVI')
        plt.title('NDVI')

        # Vegetation Mask
        plt.subplot(2, 2, 2)
        plt.imshow(veg_mask, cmap='gray')
        plt.title('Vegetation Mask (NDVI > 0.3)')

        # Water Mask (Placeholder if no SWIR)
        plt.subplot(2, 2, 3)
        plt.imshow(water_mask, cmap='Blues')
        plt.title('Water Mask (MNDWI > 0)')

        plt.tight_layout()
        plt.show()

        print("Finished generating NDVI and example masks. Adjust thresholds or add SWIR for MNDWI.")

if __name__ == '__main__':
    main()
"""
    st.code(script_code, language="python")

    st.markdown(
        """
        ---
        ## Wrap-Up
        
        By **adjusting thresholds** for NDVI (or MNDWI), you can test how well basic 
        band filtering can isolate certain land covers. Over ~40 minutes, you should:
        
        - Download or export a multi-band image.
        - Run this script **multiple times** with different threshold values.
        - **Write a short reflection** on how robust these simple thresholds are, 
          what errors you see, and how you might improve them (e.g., multi-band classification).

        **Enjoy experimenting** with spectral filters to reveal water, forest, or crop areas!
        """
    )

def main():
    tutorial3_page()

if __name__ == "__main__":
    main()
