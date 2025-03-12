import streamlit as st

def tutorial7_page():
    """
    Tutorial 7: Applying Fuzzy Set Theory to Elevation Data

    In this tutorial, you'll learn how to manage uncertainty in topographical data by using
    fuzzy set theory. You will:
    1. Load an XYZ elevation dataset.
    2. Define fuzzy membership functions for elevation categories (e.g., Lowland, Upland, Highland).
    3. Compute and visualize fuzzy membership values over a defined elevation range.
    
    **Task (Approximately 40 minutes):**
    - Experiment with the parameters in the fuzzy membership functions.
    - Discuss how these fuzzy sets help handle vagueness in defining topographical features.
    - Write a short summary (3–5 sentences) describing:
        - How the membership functions change with different parameters.
        - What the fuzzy boundaries tell you about uncertainty in elevation classification.
    """

    st.title("Tutorial 7: Applying Fuzzy Set Theory to Elevation Data")
    
    tab1, tab2 = st.tabs(["Fuzzy Sets Script", "Fuzzy Sets Activity"])

    # ──────────────────────────────────────────────────────────────
    # TAB 1: FUZZY SETS SCRIPT
    # ──────────────────────────────────────────────────────────────
    with tab1:
        st.subheader("Fuzzy Sets Script for Elevation Data")
        st.markdown(
            """
            The following script is designed to be run in Google Colab.
            It will:
            1. Load the elevation dataset from `/content/sample_data/Elevation_backup.xyz`.
            2. Determine the plotting range based on the data.
            3. Define fuzzy membership functions for 'Lowland', 'Upland', and 'Highland' categories.
            4. Compute fuzzy membership values over the plotting range.
            5. Plot the fuzzy membership functions.
            
            To run this script in Colab:
            1. Ensure you have installed the required libraries:
               ```bash
               !pip install numpy matplotlib
               ```
            2. Upload your `Elevation_backup.xyz` file to `/content/sample_data/`.
            3. Copy the script below into a file named `fuzzy_elevation.py`.
            4. Run it using:
               ```bash
               !python fuzzy_elevation.py
               ```
            """
        )

        fuzzy_script = """\
import numpy as np
import matplotlib.pyplot as plt

def linear_membership(x, a, b):
    \"\"\" 
    Linear membership function.
    Returns 0 for values x <= a, 1 for values x >= b, and a linear interpolation in between.
    \"\"\"
    return np.clip((x - a) / (b - a), 0, 1)

# ---------------------------------------------------------------------------
# Step 1: Load the elevation dataset
# ---------------------------------------------------------------------------
print("Loading elevation dataset from '/content/sample_data/Elevation_backup.xyz' ...")
# The file is expected to be tab-delimited with three columns: longitude, latitude, elevation.
data = np.loadtxt('/content/sample_data/Elevation_backup.xyz', delimiter='\t')
print("Dataset loaded successfully.")
print(f"Total records: {data.shape[0]}")

# Extract the elevation column (third column)
elevations_data = data[:, 2]
print("Extracted elevation data from the third column.")

# ---------------------------------------------------------------------------
# Step 2: Determine the plotting range based on the dataset
# ---------------------------------------------------------------------------
min_data_elev = elevations_data.min()
max_data_elev = elevations_data.max()
min_elev = np.floor(min_data_elev) - 5  # add a margin of 5 m below the min elevation
max_elev = np.ceil(max_data_elev) + 5   # add a margin of 5 m above the max elevation
print(f"Elevation data ranges from {min_data_elev:.2f} m to {max_data_elev:.2f} m.")
print(f"Plotting range set from {min_elev:.2f} m to {max_elev:.2f} m.")

# Generate an array of elevations for plotting fuzzy membership functions.
elevations = np.linspace(min_elev, max_elev, 500)
print("Generated an array of 500 evenly spaced elevation values for plotting.")

# ---------------------------------------------------------------------------
# Step 3: Define fuzzy membership functions for elevation categories
# ---------------------------------------------------------------------------
print("\\nDefining fuzzy membership functions...")

def low_membership(elev):
    \"\"\" 
    Fuzzy membership for 'Lowland' category:
    Full membership (1) for elevations ≤ 395 m; then linearly decreasing to 0 at 400 m.
    \"\"\"
    return np.where(elev <= 395, 1, np.clip((400 - elev) / (400 - 395), 0, 1))

def medium_membership(elev):
    \"\"\" 
    Fuzzy membership for 'Upland' category:
    A triangular membership function that starts at 0 at 395 m,
    reaches full membership (1) at 400 m, and decreases back to 0 at 405 m.
    \"\"\"
    mem = np.zeros_like(elev)
    # Rising edge: from 395 to 400 m
    mask1 = (elev > 395) & (elev <= 400)
    mem[mask1] = (elev[mask1] - 395) / (400 - 395)
    # Falling edge: from 400 to 405 m
    mask2 = (elev > 400) & (elev < 405)
    mem[mask2] = (405 - elev[mask2]) / (405 - 400)
    return np.clip(mem, 0, 1)

def high_membership(elev):
    \"\"\" 
    Fuzzy membership for 'Highland' category:
    Zero membership for elevations ≤ 400 m; then increases linearly to 1 at 405 m.
    \"\"\"
    return np.where(elev <= 400, 0, np.where(elev >= 405, 1, np.clip((elev - 400) / (405 - 400), 0, 1)))

print("Fuzzy membership functions defined for Lowland, Upland, and Highland.")

# ---------------------------------------------------------------------------
# Step 4: Compute fuzzy membership values over the plotting range
# ---------------------------------------------------------------------------
print("\\nComputing fuzzy membership values for the defined elevation range...")
low_vals = low_membership(elevations)
medium_vals = medium_membership(elevations)
high_vals = high_membership(elevations)
print("Fuzzy membership values computed.")

# ---------------------------------------------------------------------------
# Step 5: Plot the fuzzy membership functions
# ---------------------------------------------------------------------------
print("\\nPlotting fuzzy membership functions...")

plt.figure(figsize=(10, 5))
plt.plot(elevations, low_vals, label='Lowland', color='blue')
plt.plot(elevations, medium_vals, label='Upland', color='orange')
plt.plot(elevations, high_vals, label='Highland', color='green')
plt.title("Fuzzy Membership Functions for Elevation Categories")
plt.xlabel("Elevation (m)")
plt.ylabel("Membership Degree")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

print("\\nPlot displayed successfully. The graph shows the membership degrees for each elevation category.")
"""
        st.code(fuzzy_script, language="python")

    # ──────────────────────────────────────────────────────────────
    # TAB 2: FUZZY SETS ACTIVITY
    # ──────────────────────────────────────────────────────────────
    with tab2:
        st.subheader("Fuzzy Sets Activity & Reflection")
        st.markdown(
            """
            **Activity Overview:**
            
            1. **Run the provided fuzzy sets script** (`fuzzy_elevation.py`) in Google Colab.
            2. **Experiment** with the parameters in the fuzzy membership functions:
               - Try changing the values in the `low_membership`, `medium_membership`, and `high_membership` functions.
               - For example, adjust the thresholds (e.g., change 395/400/405 to different numbers) and observe how the membership curves change.
            3. **Visualize** the new membership functions and compare them to the original ones.
            4. **Reflect:** Write a short summary (3–5 sentences) discussing:
               - How your adjustments affected the fuzzy boundaries.
               - Which settings best capture the inherent uncertainty in elevation classification.
               - Any challenges or insights you encountered.

            **Estimated Time for Activity:** ~40 minutes

            **Group Discussion (Optional):**
            - Share your findings with peers or discuss in an online forum.
            - Consider potential applications of fuzzy sets in managing topographical uncertainty.

            **Instructions for Google Colab:**
            - Ensure required libraries are installed:
              ```bash
              !pip install numpy matplotlib
              ```
            - Upload your `Elevation_backup.xyz` file to `/content/sample_data/`.
            - Copy the script from Tab 1 into a file named `fuzzy_elevation.py` and run it.
            """
        )

def main():
    tutorial7_page()

if __name__ == "__main__":
    main()
