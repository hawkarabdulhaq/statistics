import streamlit as st

def tutorial6_page():
    """
    Tutorial 6: Conditional Probability for Elevation Prediction

    In this tutorial, you will:
    1. Load an XYZ elevation dataset.
    2. Define discrete events:
       - Event A: Elevation > 400 m.
       - Event B: Latitude > 48.1125.
    3. Calculate:
       - P(A): Probability that elevation > 400 m.
       - P(B): Probability that latitude > 48.1125.
       - P(A ∩ B): Joint probability.
       - P(A|B): Conditional probability of high elevation given the latitude condition.
       - P(B|A): Using Bayes’ theorem to update the probability.
    4. Visualize histograms of elevation and latitude.
    5. Reflect on how adjusting these thresholds alters the probabilities.

    **Task**: Spend approximately 40 minutes on this exercise. Try different threshold values, compute the new probabilities, and write a short summary (3–5 sentences) about:
    - How the conditional probabilities change.
    - Which threshold adjustments cause the most significant changes.
    - Potential real-world implications for topographical analysis.
    """

    st.title("Tutorial 6: Conditional Probability for Elevation Prediction")
    
    st.markdown(
        """
        **Objective:**
        
        Use conditional probability to predict the likelihood of high elevation (>400 m) given a specific latitude condition (>48.1125). Apply Bayes’ theorem to update your prediction based on spatial observations.
        
        **Your Task:**
        
        1. **Download** the dataset `input/Elevation_backup.xyz` (which contains columns: longitude, latitude, elevation).
        2. **Run** the provided script (shown below) in a new Google Colab notebook.
        3. **Experiment** with changing the elevation and latitude thresholds.
        4. **Record** your computed probabilities:
           - \(P(\text{Elevation} > 400 \text{ m})\)
           - \(P(\text{Latitude} > 48.1125)\)
           - \(P(\text{Elevation} > 400 \text{ m} \mid \text{Latitude} > 48.1125)\)
           - \(P(\text{Latitude} > 48.1125 \mid \text{Elevation} > 400 \text{ m})\)
        5. **Reflect**: Write a brief summary explaining how threshold variations affected these probabilities, and what that might imply for predicting elevation in a spatial context.
        
        **Estimated Time**: ~40 minutes
        
        ---
        ### `elevation_conditional.py` Script
        Copy the following script into a file named **`elevation_conditional.py`** and run it in Google Colab.
        """
    )

    code_script = """\
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Path to the elevation dataset (XYZ format, tab-delimited)
DATA_FILE = 'input/Elevation_backup.xyz'

# Define thresholds (you can adjust these values)
ELEV_THRESHOLD = 400      # Event A: Elevation > 400 m
LAT_THRESHOLD = 48.1125   # Event B: Latitude > 48.1125

def main():
    # 1. Load the dataset
    # The file is tab-delimited and has no header; we assign column names.
    df = pd.read_csv(DATA_FILE, sep='\\t', header=None, names=['longitude', 'latitude', 'elevation'])
    df.dropna(inplace=True)
    
    total = len(df)
    print("Total records:", total)
    
    # 2. Define events
    # Event A: elevation > ELEV_THRESHOLD
    df['A'] = df['elevation'] > ELEV_THRESHOLD
    # Event B: latitude > LAT_THRESHOLD
    df['B'] = df['latitude'] > LAT_THRESHOLD
    
    # 3. Compute probabilities
    P_A = df['A'].mean()                  # P(A)
    P_B = df['B'].mean()                  # P(B)
    P_A_and_B = (df['A'] & df['B']).mean()  # P(A ∩ B)
    P_A_given_B = P_A_and_B / P_B if P_B > 0 else np.nan
    # Bayes' theorem: P(B|A) = (P(A|B) * P(B)) / P(A)
    P_B_given_A = (P_A_given_B * P_B / P_A) if P_A > 0 else np.nan

    print(f"P(Elevation > {ELEV_THRESHOLD} m) = {P_A:.3f}")
    print(f"P(Latitude > {LAT_THRESHOLD}) = {P_B:.3f}")
    print(f"P(Elevation > {ELEV_THRESHOLD} m and Latitude > {LAT_THRESHOLD}) = {P_A_and_B:.3f}")
    print(f"P(Elevation > {ELEV_THRESHOLD} m | Latitude > {LAT_THRESHOLD}) = {P_A_given_B:.3f}")
    print(f"P(Latitude > {LAT_THRESHOLD} | Elevation > {ELEV_THRESHOLD} m) = {P_B_given_A:.3f}")

    # 4. Plot histograms
    plt.figure(figsize=(12,5))
    
    plt.subplot(1,2,1)
    plt.hist(df['elevation'], bins=15, color='skyblue', edgecolor='black')
    plt.axvline(ELEV_THRESHOLD, color='red', linestyle='dashed', label=f"Threshold = {ELEV_THRESHOLD} m")
    plt.title("Elevation Histogram")
    plt.xlabel("Elevation (m)")
    plt.ylabel("Frequency")
    plt.legend()
    
    plt.subplot(1,2,2)
    plt.hist(df['latitude'], bins=15, color='lightgreen', edgecolor='black')
    plt.axvline(LAT_THRESHOLD, color='red', linestyle='dashed', label=f"Threshold = {LAT_THRESHOLD}")
    plt.title("Latitude Histogram")
    plt.xlabel("Latitude")
    plt.ylabel("Frequency")
    plt.legend()
    
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
"""
    st.code(code_script, language="python")

    st.markdown(
        """
        ---
        **Your Task:**
        1. **Run** the `elevation_conditional.py` script in Google Colab.
        2. **Experiment** with the thresholds:
           - Try different values for **ELEV_THRESHOLD** and **LAT_THRESHOLD**.
           - Observe how \(P(A)\), \(P(B)\), \(P(A \cap B)\), \(P(A|B)\), and \(P(B|A)\) change.
        3. **Reflect** on the results:
           - How does altering the latitude threshold affect the probability of high elevation?
           - What does the conditional probability \(P(A|B)\) tell you about the relationship between elevation and latitude?
           - Use Bayes' theorem to interpret how new spatial observations might update your predictions.
        4. **Write a short summary** (3–5 sentences) of your findings.
        
        **Enjoy exploring conditional probabilities for topographical prediction!**
        """
    )

def main():
    tutorial6_page()

if __name__ == "__main__":
    main()
