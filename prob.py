import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def create_dataset(num_layers, count_A, count_B, overlap_AB, count_sandstone):
    """
    Dynamically creates a dataset of `num_layers` layers.
    Each row indicates:
      - FossilA (Yes/No)
      - FossilB (Yes/No)
      - Sandstone (Yes/No)

    The user controls:
      - How many layers exist in total (num_layers).
      - How many layers have Fossil A (count_A).
      - How many layers have Fossil B (count_B).
      - How many layers have BOTH Fossil A & B (overlap_AB).
      - How many layers are Sandstone (count_sandstone).

    Any random assignment beyond these constraints is allocated by shuffling.
    """
    # Basic validation
    if overlap_AB > count_A or overlap_AB > count_B:
        raise ValueError("Overlap (A∩B) cannot exceed either count_A or count_B.")

    if count_A > num_layers or count_B > num_layers or count_sandstone > num_layers:
        raise ValueError("Counts cannot exceed the total number of layers.")

    # Start by creating a list of layer IDs
    layer_ids = list(range(1, num_layers + 1))

    # We will first assign overlap_AB to some random subset of layers
    # Then assign the remaining A-only and B-only sets
    # Then assign any leftover as no fossils
    # Finally, assign which layers are Sandstone.

    # Step 1: Create an empty assignment
    fossilA = [False]*num_layers
    fossilB = [False]*num_layers

    # Step 2: Randomly pick which layers get A∩B
    indices = np.arange(num_layers)
    np.random.shuffle(indices)  # Shuffle indices for random assignment

    # Overlap layers
    overlap_indices = indices[:overlap_AB]
    for idx in overlap_indices:
        fossilA[idx] = True
        fossilB[idx] = True

    # Step 3: Assign additional A-only layers
    remaining_indices = indices[overlap_AB:]
    needed_A_only = count_A - overlap_AB
    if needed_A_only > 0:
        A_only_indices = remaining_indices[:needed_A_only]
        for idx in A_only_indices:
            fossilA[idx] = True

        remaining_indices = remaining_indices[needed_A_only:]

    # Step 4: Assign additional B-only layers
    needed_B_only = count_B - overlap_AB
    if needed_B_only > 0:
        B_only_indices = remaining_indices[:needed_B_only]
        for idx in B_only_indices:
            fossilB[idx] = True

        remaining_indices = remaining_indices[needed_B_only:]

    # The rest have no fossils

    # Step 5: Assign Sandstone
    # We randomly pick 'count_sandstone' from the total layers
    all_indices = np.arange(num_layers)
    np.random.shuffle(all_indices)
    sandstone_flags = [False]*num_layers
    sandstone_selected = all_indices[:count_sandstone]
    for idx in sandstone_selected:
        sandstone_flags[idx] = True

    # Finally build a DataFrame
    data = {
        'LayerID': [f"{i}" for i in layer_ids],
        'FossilA': ["Yes" if a else "No" for a in fossilA],
        'FossilB': ["Yes" if b else "No" for b in fossilB],
        'Sandstone': ["Yes" if s else "No" for s in sandstone_flags]
    }
    df = pd.DataFrame(data)
    return df

def calculate_probabilities(df):
    """
    Calculates five key probabilities:
      1) P(A)
      2) P(B)
      3) P(A ∩ B)
      4) P(A ∪ B)
      5) P(B | A)
    """
    total_layers = len(df)

    # Convert 'Yes'/'No' to booleans for easier calculation
    df['HasA'] = df['FossilA'].apply(lambda x: x == 'Yes')
    df['HasB'] = df['FossilB'].apply(lambda x: x == 'Yes')

    # Count occurrences
    A_count = df['HasA'].sum()
    B_count = df['HasB'].sum()
    AB_count = ((df['HasA']) & (df['HasB'])).sum()

    # Compute probabilities
    if total_layers == 0:
        return {
            'P(A)': 0,
            'P(B)': 0,
            'P(A∩B)': 0,
            'P(A∪B)': 0,
            'P(B|A)': 0
        }
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
        ax.text(
            bar.get_x() + bar.get_width()/2,
            height + 0.02,
            f"{height:.2f}",
            ha='center',
            va='bottom',
            fontsize=9
        )

    plt.tight_layout()
    return fig

def main():
    st.title("Dynamic Geological Probability Demo")
    st.subheader("Customize the Dataset (Fossil A, Fossil B, and Sandstone)")

    st.write("Use the sliders below to define how many layers will have Fossil A, Fossil B, overlap, and sandstone.")

    # 1. Sliders for dataset configuration
    num_layers = st.slider("Total Layers", min_value=1, max_value=30, value=12)
    count_A = st.slider("Layers with Fossil A", min_value=0, max_value=num_layers, value=6)
    count_B = st.slider("Layers with Fossil B", min_value=0, max_value=num_layers, value=6)

    # Overlap: can't exceed the min of count_A or count_B
    max_overlap = min(count_A, count_B)
    overlap_AB = st.slider("Overlap (A ∩ B)", min_value=0, max_value=max_overlap, value=3)

    count_sandstone = st.slider("Layers with Sandstone", min_value=0, max_value=num_layers, value=5)

    # Generate the dataset
    df = create_dataset(
        num_layers=num_layers,
        count_A=count_A,
        count_B=count_B,
        overlap_AB=overlap_AB,
        count_sandstone=count_sandstone
    )

    # Convert to binary for display
    df_binary = convert_binary(df)

    st.write("### 1. Generated Dataset")
    st.dataframe(df_binary)

    # 2. Calculate probability measures
    prob_dict = calculate_probabilities(df)

    st.write("### 2. Probability Measures")
    st.markdown(
        """
        - **P(A):** Probability that a layer contains Fossil A.\n
        - **P(B):** Probability that a layer contains Fossil B.\n
        - **P(A ∩ B):** Probability that both fossils appear **together**.\n
        - **P(A ∪ B):** Probability of finding **at least one** fossil (A or B).\n
          - Uses the Addition Rule: \\( P(A) + P(B) - P(A \\cap B) \\).\n
        - **P(B | A):** **Conditional Probability** of B given A.\n
          - \\( P(A \\cap B) / P(A) \\).
        """
    )

    # Display them
    for k, v in prob_dict.items():
        st.write(f"- **{k}** = {v:.2f}")

    # 3. Probability Bar Chart
    st.write("### 3. Probability Bar Chart")
    fig = plot_probabilities(prob_dict)
    st.pyplot(fig)

    # 4. Explanation
    st.write("---")
    st.markdown(
        """
        ## Why This Matters

        By dynamically adjusting how many layers have Fossil A, Fossil B, 
        and their overlap, you can see how the probabilities shift:

        - **P(A)** & **P(B)** rise or fall based on how frequently each fossil is found.
        - **P(A ∩ B)** grows if you increase overlap (A∩B), reflecting more co-occurrence.
        - **P(A ∪ B)** indicates how often you find at least one fossil — it grows if A and B are both common.
        - **P(B|A)** shows how likely B is if A is already there; it increases if you raise the overlap 
          relative to how many total layers have A.

        This interactive approach helps illustrate **probability rules** in a real-world
        geological context, where each "layer" could be a stratigraphic interval in a core or 
        outcrop, and presence/absence of fossils can guide paleoenvironmental interpretations.
        """
    )

if __name__ == "__main__":
    main()
