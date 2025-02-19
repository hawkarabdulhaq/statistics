import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def create_dataset():
    """
    Creates a dataset of 12 layers. Each row indicates:
      - FossilA (Yes/No): Presence of Fossil A
      - FossilB (Yes/No): Presence of Fossil B
      - Sandstone (Yes/No): Whether the layer is sandstone

    The dataset is deliberately constructed so that:
    - P(A) = 6/12 = 0.50
    - P(B) = 6/12 = 0.50
    - P(A∩B) = 3/12 = 0.25
    - P(A∪B) = 9/12 = 0.75
    - P(B|A) = (A∩B)/P(A) = 0.25 / 0.50 = 0.50
    """
    data = {
        'LayerID':      list(range(1, 13)),
        # Fossil A present in layers: 1,2,4,7,9,12 (6 total)
        'FossilA':      ['Yes','Yes','No','Yes','No','No','Yes','No','Yes','No','No','Yes'],
        # Fossil B present in layers: 2,6,7,8,9,10 (6 total)
        # Overlap with A in layers: 2,7,9 (3 total) => P(A∩B)=3/12=0.25
        'FossilB':      ['No','Yes','No','No','No','Yes','Yes','Yes','Yes','Yes','No','No'],
        # Sandstone can be arbitrary; doesn't affect these probability results.
        'Sandstone':    ['Yes','No','Yes','Yes','No','No','Yes','No','Yes','No','Yes','No']
    }
    return pd.DataFrame(data)

def calculate_probabilities(df):
    """
    Calculates five key probabilities:

    1) P(A): Probability of finding Fossil A in a randomly chosen layer.
       - Computed as (# layers with A) / (total layers).

    2) P(B): Probability of finding Fossil B in a randomly chosen layer.
       - Computed similarly to P(A).

    3) P(A ∩ B): Probability of finding both Fossil A and Fossil B together.
       - Computed as (# layers with both) / (total layers).

    4) P(A ∪ B): Probability of finding at least one fossil (A or B).
       - Uses the Addition Rule: P(A) + P(B) - P(A ∩ B).

    5) P(B|A): Conditional probability of finding Fossil B if Fossil A is known to be present.
       - Computed as [P(A ∩ B)] / [P(A)], if P(A) > 0.
    """
    total_layers = len(df)

    # Convert 'Yes'/'No' to booleans for easier calculation
    df['HasA'] = df['FossilA'].apply(lambda x: x == 'Yes')
    df['HasB'] = df['FossilB'].apply(lambda x: x == 'Yes')

    # Count occurrences
    A_count = df['HasA'].sum()         # # of layers with Fossil A
    B_count = df['HasB'].sum()         # # of layers with Fossil B
    AB_count = ((df['HasA']) & (df['HasB'])).sum()  # # with both A and B

    # Compute probabilities
    pA = A_count / total_layers
    pB = B_count / total_layers
    pA_and_B = AB_count / total_layers
    pA_or_B = pA + pB - pA_and_B  # Addition Rule
    pB_given_A = pA_and_B / pA if pA != 0 else 0.0

    return {
        'P(A)': pA,
        'P(B)': pB,
        'P(A∩B)': pA_and_B,
        'P(A∪B)': pA_or_B,
        'P(B|A)': pB_given_A
    }

def convert_binary(df):
    """
    Converts the 'Yes'/'No' fields to 1/0 for a simple numeric table.
    """
    df_binary = df.copy()
    df_binary['FossilA']   = df_binary['FossilA'].apply(lambda x: 1 if x == 'Yes' else 0)
    df_binary['FossilB']   = df_binary['FossilB'].apply(lambda x: 1 if x == 'Yes' else 0)
    df_binary['Sandstone'] = df_binary['Sandstone'].apply(lambda x: 1 if x == 'Yes' else 0)
    return df_binary[['LayerID','FossilA','FossilB','Sandstone']]

def plot_probabilities(prob_dict):
    """
    Creates a bar chart for the computed probabilities:
    - P(A), P(B), P(A∩B), P(A∪B), P(B|A).
    """
    labels = list(prob_dict.keys())
    values = list(prob_dict.values())

    fig, ax = plt.subplots(figsize=(6,4))
    bars = ax.bar(labels, values, color='cornflowerblue', edgecolor='black')
    ax.set_ylim(0, 1.1)
    ax.set_title('Calculated Probabilities')
    ax.set_xlabel('Probability Measures')
    ax.set_ylabel('Value (0 to 1)')

    # Place numeric labels above the bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height+0.02, f"{height:.2f}",
                ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    return fig

def main():
    st.title("Geological Probability Demo")
    st.subheader("Fossil A and Fossil B Occurrences in 12 Layers")

    # 1. Create the dataset, plus a binary version for easy table display
    df = create_dataset()
    df_binary = convert_binary(df)

    # Show the dataset
    st.write("### 1. Dataset Overview (Numeric Table)")
    st.write("Below, **1** indicates 'Yes' and **0** indicates 'No'.")
    st.table(df_binary)

    # 2. Calculate probability measures
    prob_dict = calculate_probabilities(df)

    # 2A. Explanation of Each Probability
    st.write("### 2. Explanation of Probability Measures")

    st.markdown(
        """
        - **P(A):** Probability that a layer contains Fossil A.
        - **P(B):** Probability that a layer contains Fossil B.
        - **P(A ∩ B):** Probability that both fossils appear **together** in the same layer.
        - **P(A ∪ B):** Probability of finding **at least one** fossil (A or B).
          - Uses the **Addition Rule**: \( P(A) + P(B) - P(A \cap B) \).
        - **P(B | A):** **Conditional Probability** of finding Fossil B given that Fossil A is present.
          - Uses \( P(A \cap B) / P(A) \).
        """
    )

    # 2B. Show the results
    st.write("Below are the **calculated values** for each:")
    for k, v in prob_dict.items():
        st.write(f"- **{k}** = {v:.2f}")

    # 2C. Additional context: exact values in this dataset
    st.info(
        "**How are these exact probabilities derived?**\n\n"
        f"- **P(A)** = 6 out of 12 layers have Fossil A → **0.50**\n"
        f"- **P(B)** = 6 out of 12 layers have Fossil B → **0.50**\n"
        f"- **P(A ∩ B)** = 3 out of 12 layers have both A and B → **0.25**\n"
        f"- **P(A ∪ B)** = 9 out of 12 layers have A or B (or both) → **0.75**\n"
        "  (calculated also by `0.50 + 0.50 - 0.25 = 0.75`)\n"
        f"- **P(B|A)** = (P(A ∩ B)) / P(A) = `0.25 / 0.50` → **0.50**"
    )

    # 3. Visualize these probabilities with a bar chart
    st.write("### 3. Probability Bar Chart")
    fig = plot_probabilities(prob_dict)
    st.pyplot(fig)

    # 4. Why This Matters
    st.markdown(
        """
        ---
        ## Why These Results Are Important

        1. **Fossil Distribution Insights:**
           - Seeing that both *Fossil A* and *Fossil B* occur in half of the layers (0.50 each) 
             helps geologists gauge how common or rare these fossils are in the studied formation.

        2. **Co-occurrence (A ∩ B):**
           - A 0.25 probability means 25% of layers host both fossils together, suggesting 
             overlapping environmental or temporal factors.

        3. **Union (A ∪ B):**
           - With a 0.75 probability, there's a 75% chance any given layer has at least one fossil,
             which is quite high and suggests rich fossil content overall.

        4. **Conditional Probability (B|A):**
           - If you already know a layer has *Fossil A*, there's a 50% chance (*P(B|A)=0.50*) it 
             also contains *Fossil B*. This conditional aspect is vital in practical geology:
             finding *Fossil A* may lead you to suspect *Fossil B* too, prompting more targeted 
             sampling or correlation strategies.

        ---
        ### Explore Further
        - Try editing the dataset to change the number of 'Yes' layers for A or B.
        - Observe how *all* these probabilities adjust accordingly.
        - Add extra columns (like *Fossil C* or *Shale*) to see how more factors 
          influence *co-occurrence* and *conditional probability*.
        """
    )

if __name__ == "__main__":
    main()
