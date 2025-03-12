import streamlit as st

def tutorial7_page():
    """
    Tutorial 7: Applying Fuzzy Set Theory, Distribution Fitting, and Bayesian Updating to Elevation Data

    In this tutorial you will:
    - Use fuzzy sets to manage uncertainty in defining topographical categories.
    - Compute statistical parameters and fit probability distributions to elevation data.
    - Apply Bayesian inference to update elevation predictions with new data.

    Work individually for about 40 minutes. Experiment with different parameters,
    compare results, and write a short reflection on your findings.
    """
    st.title("Tutorial 7: Elevation Data Analysis and Uncertainty")

    st.markdown(
        """
        **Objective:**  
        Use advanced probabilistic and fuzzy logic techniques to understand and model elevation data.
        
        **Your Tasks:**  
        1. **Fuzzy Sets**: Define fuzzy membership functions for categories such as “lowland,” “upland,” and “highland.”  
        2. **Distribution Fitting**: Compute mean, median, mode, variance, skewness, and kurtosis; fit probability distributions; and visualize the PDF and CDF.  
        3. **Bayesian Updating**: Update elevation predictions using Bayesian methods as new data points become available.

        Use the provided **XYZ elevation dataset** (`input/Elevation_backup.xyz`) for all parts.  
        Spend about 40 minutes on this tutorial, experimenting with parameter adjustments and reflecting on your results.
        """
    )

    # Create three tabs for the three parts
    tab1, tab2, tab3 = st.tabs(["Fuzzy Sets", "Distribution Fitting", "Bayesian Updating"])

    # ──────────────────────────────────────────────────────────────
    # Tab 1: Fuzzy Sets for Elevation
    # ──────────────────────────────────────────────────────────────
    with tab1:
        st.subheader("Fuzzy Sets for Elevation")
        st.markdown(
            """
            **Overview:**  
            In this section, you will define fuzzy membership functions for elevation categories.  
            For example, you may define:
            - **Lowland**: A fuzzy set for elevations roughly below 350 m.
            - **Upland**: A fuzzy set for mid-elevations (e.g., 350–400 m).
            - **Highland**: A fuzzy set for elevations roughly between 400 and 410 m, with fuzzy boundaries.

            **Your Task:**  
            - Create fuzzy membership functions using Python (you may use linear or Gaussian functions).  
            - Visualize these functions to see how membership changes with elevation.
            
            **Example Code:**  
            Below is an example script to generate and plot fuzzy membership functions.
            """
        )

        fuzzy_script = """\
import numpy as np
import matplotlib.pyplot as plt

def linear_membership(x, a, b):
    \"\"\"Linear membership: 0 for x <= a, 1 for x >= b, linear between.\"\"\"
    return np.clip((x - a) / (b - a), 0, 1)

# Define an elevation range for plotting
elevations = np.linspace(300, 450, 500)

# Define fuzzy membership functions for three classes:
# Lowland: 300 - 350 (membership decreases after 350)
lowland = 1 - linear_membership(elevations, 300, 350)
# Upland: 350 to 400 (peaks in the middle)
upland = linear_membership(elevations, 350, 375) * (1 - linear_membership(elevations, 375, 400))
# Highland: 400 to 410 (sharp transition)
highland = linear_membership(elevations, 400, 410)

plt.figure(figsize=(10, 5))
plt.plot(elevations, lowland, label='Lowland', color='blue')
plt.plot(elevations, upland, label='Upland', color='orange')
plt.plot(elevations, highland, label='Highland', color='green')
plt.title("Fuzzy Membership Functions for Elevation Categories")
plt.xlabel("Elevation (m)")
plt.ylabel("Membership Degree")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
"""
        st.code(fuzzy_script, language="python")

        st.markdown(
            """
            **Reflection:**  
            - Experiment with different parameters (a, b) in the membership functions.
            - Discuss in your group: How do these fuzzy sets help manage uncertainty in topographical classifications?
            """
        )

    # ──────────────────────────────────────────────────────────────
    # Tab 2: Statistical Analysis & Distribution Fitting
    # ──────────────────────────────────────────────────────────────
    with tab2:
        st.subheader("Statistical Analysis & Distribution Fitting")
        st.markdown(
            """
            **Overview:**  
            In this section, you'll analyze the elevation dataset by computing basic statistics and fitting probability distributions.

            **Your Tasks:**  
            1. Load the elevation dataset (`input/Elevation_backup.xyz`), which is tab-delimited.
            2. Compute basic statistics: min, max, mean, median, variance, skewness, and kurtosis.
            3. Plot a histogram of the elevation values.
            4. Compute and plot the **Probability Density Function (PDF)** and **Cumulative Distribution Function (CDF)**.
            5. Fit candidate distributions (e.g., normal, lognormal, exponential) to the data and discuss which fits best.

            **Example Code:**
            """
        )

        distribution_script = """\
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, skew, kurtosis

# Load the elevation dataset
DATA_FILE = 'input/Elevation_backup.xyz'
df = pd.read_csv(DATA_FILE, sep='\\t', header=None, names=['longitude', 'latitude', 'elevation'])
df.dropna(inplace=True)

elev = df['elevation']

# Basic statistics
print("Min:", elev.min())
print("Max:", elev.max())
print("Mean:", elev.mean())
print("Median:", elev.median())
print("Variance:", elev.var())
print("Skewness:", skew(elev))
print("Kurtosis:", kurtosis(elev))

# Histogram
plt.figure(figsize=(10, 5))
counts, bins, _ = plt.hist(elev, bins=30, color='lightblue', edgecolor='black', alpha=0.7)
plt.title("Elevation Histogram")
plt.xlabel("Elevation (m)")
plt.ylabel("Frequency")
plt.grid(alpha=0.3)

# Fit a normal distribution
mu, std = norm.fit(elev)
pdf = norm.pdf(bins, mu, std)
plt.plot(bins, pdf * (bins[1]-bins[0]) * len(elev), 'r--', label='Normal fit')
plt.legend()
plt.show()

# Cumulative Distribution Function (CDF)
cdf = np.cumsum(counts) / len(elev)
plt.figure(figsize=(10, 5))
plt.plot(bins[:-1], cdf, marker='o', linestyle='-', color='green')
plt.title("Cumulative Distribution Function (CDF)")
plt.xlabel("Elevation (m)")
plt.ylabel("Cumulative Probability")
plt.grid(alpha=0.3)
plt.show()
"""
        st.code(distribution_script, language="python")

        st.markdown(
            """
            **Discussion:**  
            - How well does the normal distribution fit the data?  
            - What does the skewness and kurtosis tell you about the elevation distribution?
            - Consider trying other distributions (lognormal, exponential) and comparing fits.
            """
        )

    # ──────────────────────────────────────────────────────────────
    # Tab 3: Bayesian Updating for Elevation Uncertainty
    # ──────────────────────────────────────────────────────────────
    with tab3:
        st.subheader("Bayesian Updating for Elevation Prediction")
        st.markdown(
            """
            **Overview:**  
            In this section, you'll apply Bayesian inference to update your predictions for high elevation events.
            
            **Your Tasks:**  
            1. Assume a prior probability for an elevation event (e.g., elevation > 400 m).
            2. Incorporate new sample data from the dataset to update your belief using Bayesian updating.
            3. Compute and plot the **posterior distribution**.
            
            **Example Scenario:**  
            - Prior: You assume the probability of elevation > 400 m is 0.3.
            - New data from your dataset suggests that 35% of points are above 400 m.
            - Use Bayes’ theorem to update the probability.
            
            **Steps in the Script:**
            1. Load the elevation dataset (`input/Elevation_backup.xyz`).
            2. Define the event A: elevation > 400 m.
            3. Compute the likelihood of new observations given the event.
            4. Update the prior using Bayes’ theorem.
            5. Visualize the posterior distribution.
            
            **Estimated Time: ~20 minutes**
            """
        )

        bayesian_script = """\
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load elevation dataset
DATA_FILE = 'input/Elevation_backup.xyz'
df = pd.read_csv(DATA_FILE, sep='\\t', header=None, names=['longitude', 'latitude', 'elevation'])
df.dropna(inplace=True)
elev = df['elevation']

# Define the event: elevation > 400 m
threshold = 400
event_data = elev > threshold
observed_prob = event_data.mean()  # likelihood from data

# Assume a prior probability (e.g., 30%)
prior = 0.3
print("Prior probability P(Elevation > 400 m):", prior)
print("Observed probability from data:", observed_prob)

# Bayes' updating (for a simple binary event with a Beta prior)
# If we assume a Beta(a, b) prior, then the posterior is Beta(a + successes, b + failures)
# For a noninformative prior, we might use Beta(1,1) which is uniform.
# Here, we update based on the observed successes and failures.
a_prior, b_prior = 1, 1
successes = event_data.sum()
failures = len(event_data) - successes

a_post = a_prior + successes
b_post = b_prior + failures

# The posterior mean is then:
posterior_mean = a_post / (a_post + b_post)
print("Posterior mean probability:", posterior_mean)

# Plot the posterior distribution
from scipy.stats import beta
x = np.linspace(0, 1, 100)
posterior_pdf = beta.pdf(x, a_post, b_post)

plt.figure(figsize=(8, 5))
plt.plot(x, posterior_pdf, 'b-', lw=2, label=f'Beta({a_post}, {b_post})')
plt.axvline(posterior_mean, color='red', linestyle='dashed', label=f'Posterior Mean={posterior_mean:.3f}')
plt.title("Posterior Distribution for P(Elevation > 400 m)")
plt.xlabel("Probability")
plt.ylabel("Density")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
"""
        st.code(bayesian_script, language="python")

        st.markdown(
            """
            **Discussion & Reflection:**
            - Compare your **prior** assumption (e.g., 0.3) with the **posterior** mean.
            - How does new data influence your updated probability?
            - What might cause differences between your prior and posterior?
            - Reflect on how Bayesian methods allow for continual updating as more data become available.
            - Write a brief summary of your findings (3–5 sentences).

            **Estimated Time for this Tab:** ~20 minutes
            """
        )

def main():
    tutorial7_page()

if __name__ == "__main__":
    main()
