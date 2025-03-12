import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def fuzzy_membership_functions():
    """
    Compute fuzzy membership values for a given array of elevations.
    Three functions are defined:
      - Low: Full membership for elevation <= 380, then linearly decreases to 0 at 390.
      - Medium: Triangular; 0 at 380, peak (1) at 395, then 0 at 410.
      - High: 0 for elevation <= 395, then linearly increases to 1 at 405.
    """
    def low_membership(elev):
        # For elev <= 380: 1, for 380< elev <390: decreasing linearly, for elev >= 390: 0
        return np.where(elev <= 380, 1, np.clip((390 - elev) / (390 - 380), 0, 1))

    def medium_membership(elev):
        # Triangular: 0 at 380, peaks at 395, then 0 at 410.
        mem = np.zeros_like(elev)
        mask1 = (elev > 380) & (elev <= 395)
        mem[mask1] = (elev[mask1] - 380) / (395 - 380)
        mask2 = (elev > 395) & (elev < 410)
        mem[mask2] = (410 - elev[mask2]) / (410 - 395)
        return np.clip(mem, 0, 1)

    def high_membership(elev):
        # For elev <= 395: 0, then increasing linearly to 1 at 405, constant for elev >=405
        return np.where(elev <= 395, 0, np.where(elev >= 405, 1, np.clip((elev - 395) / (405 - 395), 0, 1)))

    return low_membership, medium_membership, high_membership

def plot_membership_functions():
    # Create an array of elevations for plotting (from 370 to 420 m)
    elevations = np.linspace(370, 420, 500)
    low_mf, med_mf, high_mf = fuzzy_membership_functions()

    low_vals = low_mf(elevations)
    med_vals = med_mf(elevations)
    high_vals = high_mf(elevations)

    plt.figure(figsize=(10, 5))
    plt.plot(elevations, low_vals, label='Lowland Membership', color='blue')
    plt.plot(elevations, med_vals, label='Upland Membership', color='orange')
    plt.plot(elevations, high_vals, label='Mountainous Membership', color='green')
    plt.title("Fuzzy Membership Functions for Elevation")
    plt.xlabel("Elevation (m)")
    plt.ylabel("Membership Degree")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

def classify_elevation(df, low_mf, med_mf, high_mf):
    """
    For each elevation in the DataFrame, compute fuzzy membership for low, medium, and high,
    then assign a fuzzy class based on the maximum membership.
    Returns a new DataFrame with a 'fuzzy_class' column.
    """
    # Compute memberships
    elevations = df['elevation'].values
    low_vals = low_mf(elevations)
    med_vals = med_mf(elevations)
    high_vals = high_mf(elevations)

    # Stack into a 2D array: each row = [low, medium, high]
    memberships = np.vstack([low_vals, med_vals, high_vals]).T

    # Define class labels
    labels = np.array(["Plain", "Upland", "Mountainous"])
    # For each row, select the label corresponding to the highest membership value
    assigned_classes = [labels[np.argmax(row)] for row in memberships]
    df['fuzzy_class'] = assigned_classes
    return df

def fuzzy_classification_plot(df):
    """
    Plot a scatter plot of the elevation data with fuzzy class color coding.
    Since the dataset has XYZ data, we use longitude and latitude for spatial visualization.
    """
    # Map class to colors
    color_map = {"Plain": "tan", "Upland": "orange", "Mountainous": "darkgreen"}
    colors = df['fuzzy_class'].map(color_map)

    plt.figure(figsize=(8, 6))
    plt.scatter(df['longitude'], df['latitude'], c=colors, alpha=0.7)
    plt.title("Fuzzy Terrain Classification")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

def tutorial8_page():
    st.title("Tutorial 8: Fuzzy Logic Application for Terrain Classification")
    st.markdown(
        """
        **Objective:**  
        Classify terrain into fuzzy categories based on elevation (and optionally latitude and longitude) to manage uncertainty in topographical features.
        
        **In this tutorial, you will:**
        1. **Define fuzzy membership functions** for elevation categories such as "Lowland", "Upland", and "Mountainous".
        2. **Visualize** these membership functions.
        3. **Apply fuzzy classification** on an elevation dataset to label each point.
        4. **Visualize** the spatial distribution of these fuzzy classes.

        **Your Task: (Approx. 40 minutes)**
        - Experiment with the parameters of the fuzzy membership functions.
        - Adjust thresholds to see how the classification changes.
        - Reflect on the effect of uncertainty in defining terrain categories.
        - Write a short summary (3–5 sentences) of your findings.
        """
    )

    # Create two tabs for Tutorial 8
    tab1, tab2 = st.tabs(["Fuzzy Membership Functions", "Fuzzy Classification"])

    # Tab 1: Membership Functions Visualization
    with tab1:
        st.subheader("Fuzzy Membership Functions")
        st.markdown(
            """
            **Overview:**  
            In this section, we define fuzzy membership functions for the following elevation categories:
            - **Lowland**: Full membership for elevations ≤ 380 m, then decreasing to 0 by 390 m.
            - **Upland**: A triangular function that peaks at 395 m, decreasing to 0 at 380 m and 410 m.
            - **Mountainous**: 0 for elevations ≤ 395 m, increasing to full membership at 405 m.
            
            **Task:**  
            - Run the code to visualize these functions.
            - Experiment with changing the threshold values (380, 390, 395, 405, 410) and observe the changes.
            """
        )

        # Display the code
        membership_code = """\
import numpy as np
import matplotlib.pyplot as plt

def low_membership(elev):
    # Full membership for elev <=380; linearly decreases to 0 at 390.
    return np.where(elev <= 380, 1, np.clip((390 - elev) / 10, 0, 1))

def medium_membership(elev):
    # Triangular membership: 0 at 380, peaks at 395 (1), then 0 at 410.
    mem = np.zeros_like(elev)
    mask1 = (elev > 380) & (elev <= 395)
    mem[mask1] = (elev[mask1] - 380) / 15
    mask2 = (elev > 395) & (elev < 410)
    mem[mask2] = (410 - elev[mask2]) / 15
    return np.clip(mem, 0, 1)

def high_membership(elev):
    # 0 for elev <=395; increases linearly to 1 at 405.
    return np.where(elev <= 395, 0, np.where(elev >= 405, 1, np.clip((elev - 395) / 10, 0, 1)))

# Create a range of elevations for visualization
elevations = np.linspace(370, 420, 500)
low_vals = low_membership(elevations)
med_vals = medium_membership(elevations)
high_vals = high_membership(elevations)

plt.figure(figsize=(10,5))
plt.plot(elevations, low_vals, label='Lowland', color='blue')
plt.plot(elevations, med_vals, label='Upland', color='orange')
plt.plot(elevations, high_vals, label='Mountainous', color='green')
plt.title("Fuzzy Membership Functions for Elevation")
plt.xlabel("Elevation (m)")
plt.ylabel("Membership Degree")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
"""
        st.code(membership_code, language="python")

        st.markdown(
            """
            **Experiment:**  
            Try adjusting the numerical thresholds in the functions (e.g., change 380, 390, 395, 405, 410) and re-run the script to see how the membership curves change.
            """
        )

    # Tab 2: Fuzzy Classification on Elevation Data
    with tab2:
        st.subheader("Fuzzy Classification of Elevation Data")
        st.markdown(
            """
            **Overview:**  
            In this section, you will:
            1. Load the elevation dataset from `input/Elevation_backup.xyz`.  
            2. Compute fuzzy memberships for each data point using the functions defined above.
            3. Assign a fuzzy class to each point based on the highest membership (i.e., "Plain" for low, "Upland" for medium, "Mountainous" for high).
            4. Visualize the spatial distribution (using longitude and latitude) colored by fuzzy class.

            **Task:**  
            - Run the script below in Google Colab.
            - Experiment with modifying the membership functions.
            - Observe how the classification counts change.
            """
        )

        classification_script = """\
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define fuzzy membership functions
def low_membership(elev):
    return np.where(elev <= 380, 1, np.clip((390 - elev) / 10, 0, 1))

def medium_membership(elev):
    mem = np.zeros_like(elev)
    mask1 = (elev > 380) & (elev <= 395)
    mem[mask1] = (elev[mask1] - 380) / 15
    mask2 = (elev > 395) & (elev < 410)
    mem[mask2] = (410 - elev[mask2]) / 15
    return np.clip(mem, 0, 1)

def high_membership(elev):
    return np.where(elev <= 395, 0, np.where(elev >= 405, 1, np.clip((elev - 395) / 10, 0, 1)))

# Load the elevation dataset
DATA_FILE = 'input/Elevation_backup.xyz'
df = pd.read_csv(DATA_FILE, sep='\\t', header=None, names=['longitude', 'latitude', 'elevation'])
df.dropna(inplace=True)

# Compute fuzzy memberships for each elevation point
df['low'] = low_membership(df['elevation'].values)
df['medium'] = medium_membership(df['elevation'].values)
df['high'] = high_membership(df['elevation'].values)

# Assign a fuzzy class based on the highest membership value
def assign_class(row):
    memberships = [row['low'], row['medium'], row['high']]
    idx = np.argmax(memberships)
    classes = ["Plain", "Upland", "Mountainous"]
    return classes[idx]

df['fuzzy_class'] = df.apply(assign_class, axis=1)

# Print class distribution
print("Fuzzy Class Distribution:")
print(df['fuzzy_class'].value_counts())

# Scatter plot: since longitude & latitude are nearly constant in this sample,
# we'll plot a simple histogram of elevation with class colors overlaid.
plt.figure(figsize=(10,5))
colors = {"Plain": "tan", "Upland": "orange", "Mountainous": "darkgreen"}
plt.scatter(df['elevation'], np.zeros_like(df['elevation']), 
            c=df['fuzzy_class'].map(colors), alpha=0.7)
plt.xlabel("Elevation (m)")
plt.yticks([])
plt.title("Fuzzy Classification of Elevation")
plt.grid(alpha=0.3)
plt.show()

# Optional: Plot a bar chart of fuzzy class counts
plt.figure(figsize=(6,4))
df['fuzzy_class'].value_counts().plot(kind='bar', color=['tan', 'orange', 'darkgreen'], edgecolor='black')
plt.title("Fuzzy Class Counts")
plt.xlabel("Fuzzy Class")
plt.ylabel("Count")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

print("Fuzzy classification complete.")
"""
        st.code(classification_script, language="python")

        st.markdown(
            """
            **Discussion:**  
            - How do the fuzzy memberships compare to sharp thresholds?  
            - Which category dominates, and is that what you expected based on the data?
            - How might incorporating additional spatial parameters (latitude, longitude) improve classification?
            
            **Task:**  
            Run the script in Colab, experiment by modifying the membership function thresholds, and write a short summary of your findings.
            """
        )

def main():
    tutorial3_page()

if __name__ == "__main__":
    main()
