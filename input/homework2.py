import streamlit as st

def main():
    st.title("Homework Instructions for Week 2")
    st.markdown(
        """
        ### Submission Requirements for Each Tutorial:
        - **Format:** One-page summary per tutorial (PDF or DOCX).
        - **Content:**
          - Briefly restate the tutorial’s goal.
          - Summarize the steps you followed (tools, scripts, parameters).
          - Describe any challenges or modifications.
          - Provide reflections and key insights.
          - Explain how the methods or findings could support your research.
        
        **Submit** your summaries in Coospace under Week 2 Modelling and Simulation Question by the posted due date.
        ---
        ## Homework Tasks
        ### **Task 1: Tutorial 1 – Basic Dataset Download & overview.py**
        **Objective:**  
        - Learn to download an earthquake dataset and run a script (`overview.py`) that prints basic DataFrame information and generates initial plots (histogram and scatter plot).
        
        **Your Steps:**
        1. Download the dataset (e.g., `earthquakes.csv`) via the provided dataset page or the USGS API.
        2. Open a new Google Colab notebook, mount your Google Drive, and upload the CSV file (e.g., to `/content/sample_data/`).
        3. Run the `overview.py` script and capture the output.
        4. Reflect on observations (distribution shape, outliers, data range).
        
        **Deliverable:**  
        One-page summary of your process, outputs, and reflections.
        ---
        ### **Task 2: Tutorial 2 – Mean, Median, and Mode Exploration**
        **Objective:**  
        - Explore central tendency measures by generating multiple earthquake datasets with varying parameters.
        
        **Your Steps:**
        1. Create at least three different datasets by adjusting start date, end date, or minimum magnitude.
        2. Run the `stats_overview.py` script on each dataset to compute the mean, median, and mode of earthquake magnitudes.
        3. Compare how these measures change between datasets.
        4. Reflect on which measure is most stable and why.
        
        **Deliverable:**  
        One-page summary detailing your parameter choices, results, and insights.
        ---
        ### **Task 3: Tutorial 3 – Filtering NDVI/Spectral Bands to Isolate Land Covers**
        **Objective:**  
        - Learn to filter satellite imagery to isolate specific land cover types (water, forest, or crops) using NDVI or other spectral bands.
        
        **Your Steps:**
        1. Use the provided NDVI filtering script (e.g., `ndvi_filter.py`) to apply thresholds and extract polygons representing water, forest, or crop areas.
        2. Run the script in Colab and adjust thresholds to see how the extracted features change.
        3. Reflect on the effectiveness of the filtering process.
        
        **Deliverable:**  
        One-page summary of your experiments, filter performance observations, and any suggested improvements.
        ---
        ### **Task 4: Tutorial 4 – Abraham Reef Coral Isotope Data (Group Task)**
        **Objective:**  
        - Collaboratively analyze coral isotope data to understand paleoclimatic signals.
        
        **Your Steps:**
        1. In a group of 5, run the `coral_overview.py` and `coral_analysis.py` scripts in Colab.
        2. Split responsibilities among group members (data loading, plotting δ¹⁸O and δ¹³C, filtering by date range, computing correlations).
        3. Discuss and combine your findings to prepare a cohesive summary.
        4. Clearly indicate each group member’s contributions.
        
        **Deliverable:**  
        One-page group summary describing data trends, correlations observed, and paleoclimatic interpretations.
        ---
        ### **Task 5: Additional Task – Applying Fuzzy Set Theory to the NDVI Dataset**
        **Objective:**  
        - Apply fuzzy set theory to manage uncertainty in NDVI classification.
        
        **Your Steps:**
        1. Use the provided fuzzy sets script (from Tutorial 7) or develop your own that loads the NDVI dataset (e.g., `S2_NDVI2.tif`).
        2. Define fuzzy membership functions for NDVI categories (e.g., water, sparse vegetation, dense vegetation).
        3. Experiment with adjusting membership thresholds (e.g., modifying the boundaries in your functions) and visualize the resulting curves.
        4. Reflect on how fuzzy sets can help handle uncertainty in NDVI-based land cover classification.
        
        **Deliverable:**  
        One-page summary including code modifications, plots, and a discussion of how fuzzy sets improved your understanding of data uncertainty.
        ---
        **Overall Submission Instructions:**
        - Submit one-page summaries (PDF or DOCX) for each of the five tasks.
        - Ensure clarity and conciseness—focus on key results and insights rather than large code dumps.
        - Optionally include small plots or screenshots if they help clarify your findings.
        - Group Task (Task 4) must clearly indicate individual contributions.
        
        **Good luck, and happy exploring!**
        """
    )

if __name__ == "__main__":
    main()
