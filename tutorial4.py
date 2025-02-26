import streamlit as st

def tutorial4_page():
    """
    Tutorial 4: Abraham Reef Coral Isotope Data (Group Task)

    Two Tabs:
    1) Coral Isotope Overview (Reads dataset, plots basic time series).
    2) Advanced Analysis (Filtering, correlation, side-by-side timeseries).

    Group Collaboration Notes:
    - 5 students collaborate to complete tasks.
    - Each student can take on sub-tasks (e.g., data reading, plotting, 
      interpretation, correlation, etc.).
    """

    st.title("Tutorial 4: Abraham Reef Coral Isotope Data (Group Task)")

    # Create two tabs
    tab1, tab2 = st.tabs(["Coral Isotope Overview", "Advanced Analysis"])

    # ─────────────────────────────────────────────────────────────────────
    # TAB 1: CORAL ISOTOPE OVERVIEW
    # ─────────────────────────────────────────────────────────────────────
    with tab1:
        st.subheader("Tab 1: Coral Isotope Overview")
        st.markdown(
            """
            **Group Task (~20 minutes):**  
            Five students can split responsibilities:
            - **Student A**: Acquire or confirm the `abraham_reef.txt` data file in Colab.
            - **Student B**: Implement the reading logic, ensuring comment lines (`#`) are ignored.
            - **Student C**: Plot **δ¹⁸O** vs. time, interpret the range of values.
            - **Student D**: Plot **δ¹³C** vs. time, discuss any observed trends.
            - **Student E**: Summarize the dataset’s shape, earliest & latest years, potential anomalies.

            **Objectives**:
            1. **Read** the Abraham Reef Coral Data (`age`, `d18O`, `d13C`).  
            2. **Plot** two line charts (δ¹⁸O and δ¹³C) over `age`.  
            3. **Share** a short reflection:  
               - Any big changes or outliers in the isotopes?  
               - Are there multi-decade trends?

            **Steps** in Google Colab:
            ```bash
            !pip install pandas matplotlib numpy
            !python coral_overview.py
            ```
            Make sure the file path to `abraham_reef.txt` is correct.
            """
        )

        overview_script = """\
# coral_overview.py

import pandas as pd
import matplotlib.pyplot as plt

# Path to your coral data file (tab-delimited)
DATA_FILE = '/content/abraham_reef.txt'

def main():
    # 1) Read the coral data
    df = pd.read_csv(DATA_FILE, sep='\\t', comment='#', names=['age','d18O','d13C'], header=None)
    df.dropna(inplace=True)

    # Convert to numeric
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['d18O'] = pd.to_numeric(df['d18O'], errors='coerce')
    df['d13C'] = pd.to_numeric(df['d13C'], errors='coerce')
    df.dropna(inplace=True)

    # Overview
    print("=== Abraham Reef Coral Data: HEAD ===")
    print(df.head())
    print(f"Data Range: {len(df)} records from {df['age'].min()} to {df['age'].max()} AD")

    # 2) Plot δ¹⁸O
    plt.figure(figsize=(10,5))
    plt.plot(df['age'], df['d18O'], color='blue', label='δ¹⁸O')
    plt.title('Coral δ¹⁸O over Time')
    plt.xlabel('Year AD')
    plt.ylabel('δ¹⁸O (permil VPDB)')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()

    # 3) Plot δ¹³C
    plt.figure(figsize=(10,5))
    plt.plot(df['age'], df['d13C'], color='green', label='δ¹³C')
    plt.title('Coral δ¹³C over Time')
    plt.xlabel('Year AD')
    plt.ylabel('δ¹³C (permil VPDB)')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()

    print("\\n=== Overview Complete ===")

if __name__ == '__main__':
    main()
"""
        st.code(overview_script, language="python")

        st.markdown(
            """
            **Reflection:**  
            - Did the δ¹⁸O or δ¹³C show any abrupt changes around certain decades?  
            - Any multi-year cycles visible?  
            - Share your findings with the **group**.
            """
        )

    # ─────────────────────────────────────────────────────────────────────
    # TAB 2: ADVANCED ANALYSIS
    # ─────────────────────────────────────────────────────────────────────
    with tab2:
        st.subheader("Tab 2: Advanced Analysis (Filtering & Correlation)")
        st.markdown(
            """
            **Group Task (~20 minutes)**:
            - **Student A**: Decide a filtering year range (e.g., 1700–1800).
            - **Student B**: Implement code to filter the dataset by `age`.
            - **Student C**: Calculate correlation (Pearson's r) between δ¹⁸O and δ¹³C in that range.
            - **Student D**: Plot a side-by-side timeseries of δ¹⁸O & δ¹³C for that sub-period.
            - **Student E**: Create a scatter plot, interpret correlation sign & magnitude.

            **Objective**:
            1. **Filter** the dataset by a chosen date range.
            2. **Compute** correlation (r) between δ¹⁸O and δ¹³C.
            3. **Plot** both isotopes side-by-side to see if they co-vary over certain decades.
            4. **Scatter** plot to visualize relationship strength.

            **Steps** in Google Colab:
            ```bash
            !pip install pandas matplotlib numpy
            !python coral_analysis.py
            ```
            Adjust date range as needed.
            """
        )

        analysis_script = """\
# coral_analysis.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Path to the Abraham Reef coral data file
DATA_FILE = '/content/abraham_reef.txt'

# Filter range
START_YEAR = 1700
END_YEAR   = 1800

def main():
    # 1) Read the data
    df = pd.read_csv(DATA_FILE, sep='\\t', comment='#', names=['age','d18O','d13C'], header=None)
    df.dropna(inplace=True)

    # Convert to numeric
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['d18O'] = pd.to_numeric(df['d18O'], errors='coerce')
    df['d13C'] = pd.to_numeric(df['d13C'], errors='coerce')
    df.dropna(inplace=True)

    # 2) Filter the dataset
    df_range = df[(df['age'] >= START_YEAR) & (df['age'] <= END_YEAR)]
    if df_range.empty:
        print(f"No data found between {START_YEAR} and {END_YEAR}. Try different years.")
        return

    # 3) Correlation
    corr = df_range['d18O'].corr(df_range['d13C'])
    print(f"Correlation (Pearson) δ¹⁸O vs δ¹³C in {START_YEAR}-{END_YEAR}: r={corr:.3f}")

    # 4) Timeseries plot
    plt.figure(figsize=(10,6))
    plt.plot(df_range['age'], df_range['d18O'], color='blue', label='δ¹⁸O')
    plt.plot(df_range['age'], df_range['d13C'], color='green', label='δ¹³C')
    plt.xlabel('Year AD')
    plt.ylabel('Isotope Value (permil VPDB)')
    plt.title(f'Coral Isotopes ({START_YEAR}-{END_YEAR})')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()

    # 5) Scatter plot
    plt.figure(figsize=(6,6))
    plt.scatter(df_range['d18O'], df_range['d13C'], c='purple', alpha=0.7)
    plt.xlabel('δ¹⁸O')
    plt.ylabel('δ¹³C')
    plt.title(f'd18O vs. d13C, r={corr:.3f}')
    plt.grid(True, alpha=0.3)
    plt.show()

    print("\\n=== Advanced Analysis Complete ===")

if __name__ == '__main__':
    main()
"""
        st.code(analysis_script, language="python")

        st.markdown(
            """
            **Discussion (~5–10 min)**:
            1. Does correlation change if you pick **different** time ranges?
            2. Which isotope seems more **variable**—δ¹⁸O or δ¹³C?
            3. Could these changes relate to **temperature** or **carbon cycle** shifts?

            Encourage students to **compare** multiple intervals (e.g., 1650–1700, 1800–1850) 
            and see if correlation or variance changes. 
            
            **Team Output**:
            - A **short summary** (3–5 sentences) describing the correlation patterns. 
            - Possible **physical or environmental** reasons for isotopic signals.

            **Total Time for Tutorial 4**: ~40 minutes 
            (20 for overview, 20 for advanced tasks, plus reflection).
            """
        )

def main():
    tutorial4_page()

if __name__ == "__main__":
    main()
