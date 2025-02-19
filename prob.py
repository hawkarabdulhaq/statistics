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
      - num_layers: total number of layers
      - count_A: how many layers contain Fossil A
      - count_B: how many layers contain Fossil B
      - overlap_AB: how many layers have BOTH A and B
      - count_sandstone: how many layers are Sandstone

    Any random assignment beyond these constraints is allocated by shuffling.
    """

    # Basic validation
    if overlap_AB > count_A or overlap_AB > count_B:
        raise ValueError("Overlap (A ∩ B) cannot exceed either count_A or count_B.")

    if count_A > num_layers or count_B > num_layers or count_sandstone > num_layers:
        raise ValueError("Counts cannot exceed the total number of layers.")

    # Create a list of layer IDs
    layer_ids = list(range(1, num_layers + 1))

    # We'll assign overlap_AB layers to have both A and B
    # Then the leftover A-only, leftover B-only, and no-fossil layers
    # Finally, choose which layers are Sandstone (Yes/No).

    # Step 1: Initialize boolean lists
    fossilA = [False] * num_layers
    fossilB = [False] * num_layers

    # Step 2: Shuffle indices to assign randomly
    indices = np.arange(num_layers)
    np.random.shuffle(indices)

    # Overlap (A ∩ B)
    overlap_indices = indices[:overlap_AB]
    for idx in overlap_indices:
        fossilA[idx] = True
        fossilB[idx] = True

    # Step 3: Assign remaining A-only
    remaining_indices = indices[overlap_AB:]
    needed_A_only = count_A - overlap_AB
    if needed_A_only > 0:
        A_only_indices = remaining_indices[:needed_A_only]
        for idx in A_only_indices:
            fossilA[idx] = True
        remaining_indices = remaining_indices[needed_A_only:]

    # Step 4: Assign remaining B-only
    needed_B_only = count_B - overlap_AB
    if needed_B_only > 0:
        B_only_indices = remaining_indices[:needed_B_only]
        for idx in B_only_indices:
            fossilB[idx] = True
        remaining_indices = remaining_indices[needed_B_only:]

    # The rest get no fossils (False, False)

    # Step 5: Randomly choose which layers are Sandstone
    # We shuffle again and pick 'count_sandstone' layers for Sandstone
    sandstone_flags = [False] * num_layers
    sand_indices = np.arange(num_layers)
    np.random.shuffle(sand_indices)
    sand_choice = sand_indices[:count_sandstone]
    for idx in sand_choice:
        sandstone_flags[idx] = True

    data = {
        'LayerID': [f"{i}" for i in layer_ids],
        'FossilA': ["Yes" if a else "No" for a in fossilA],
        'FossilB': ["Yes" if b else "No" for b in fossilB],
        'Sandstone': ["Yes" if s else "No" for s in sandstone_flags]
    }
    return pd.DataFrame(data)

def calculate_probabilities(df):
    """
    Calculates:
      1) P(A)
      2) P(B)
      3) P(A ∩ B)
      4) P(A ∪ B)
      5) P(B | A)
    """
    total_layers = len(df)

    df['HasA'] = df['FossilA'].apply(lambda x: x == 'Yes')
    df['HasB'] = df['FossilB'].apply(lambda x: x == 'Yes')

    A_count = df['HasA'].sum()
    B_count = df['HasB'].sum()
    AB_count = ((df['HasA']) & (df['HasB'])).sum()

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
    Converts 'Yes'/'No' to 1/0 for a straightforward numeric table display.
    """
    df_binary = df.copy()
    df_binary['FossilA']   = df_binary['FossilA'].apply(lambda x: 1 if x == 'Yes' else 0)
    df_binary['FossilB']   = df_binary['FossilB'].apply(lambda x: 1 if x == 'Yes' else 0)
    df_binary['Sandstone'] = df_binary['Sandstone'].apply(lambda x: 1 if x == 'Yes' else 0)
    return df_binary[['LayerID','FossilA','FossilB','Sandstone']]

def plot_probabilities(prob_dict):
    """
    Creates a bar chart for P(A), P(B), P(A∩B), P(A∪B), P(B|A).
    """
    labels = list(prob_dict.keys())
    values = list(prob_dict.values())

    fig, ax = plt.subplots(figsize=(6,4))
    bars = ax.bar(labels, values, color='cornflowerblue', edgecolor='black')
    ax.set_ylim(0, 1.1)
    ax.set_title('Calculated Probabilities')
    ax.set_xlabel('Probability Measures')
    ax.set_ylabel('Value (0 to 1)')

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
    st.subheader("Sidebar Controls for Dataset Configuration")

    # ──────────────── SIDEBAR CONTROLS ────────────────
    st.sidebar.write("## Customize Dataset")
    num_layers = st.sidebar.slider("Total Layers", min_value=1, max_value=30, value=12)
    count_A = st.sidebar.slider("Layers with Fossil A", min_value=0, max_value=num_layers, value=6)
    count_B = st.sidebar.slider("Layers with Fossil B", min_value=0, max_value=num_layers, value=6)

    max_overlap = min(count_A, count_B)
    overlap_AB = st.sidebar.slider("Overlap (A ∩ B)", min_value=0, max_value=max_overlap, value=3)

    count_sandstone = st.sidebar.slider("Layers with Sandstone", min_value=0, max_value=num_layers, value=5)

    # ──────────────── CREATE & DISPLAY DATASET ────────────────
    df = create_dataset(
        num_layers=num_layers,
        count_A=count_A,
        count_B=count_B,
        overlap_AB=overlap_AB,
        count_sandstone=count_sandstone
    )
    df_binary = convert_binary(df)

    st.write("### 1. Generated Dataset (Binary Table)")
    st.caption("(1 = Yes, 0 = No)")
    st.dataframe(df_binary)

    # ──────────────── CALCULATE PROBABILITIES ────────────────
    prob_dict = calculate_probabilities(df)

    st.write("### 2. Probability Measures")
    st.markdown(
        """
        - **P(A):** Probability that a layer contains Fossil A.
        - **P(B):** Probability that a layer contains Fossil B.
        - **P(A ∩ B):** Probability that both fossils appear together.
        - **P(A ∪ B):** Probability of finding at least one fossil (A or B).
          - Addition Rule: \( P(A) + P(B) - P(A \cap B) \).
        - **P(B | A):** Conditional Probability of B given A.
          - \( P(A \cap B) / P(A) \).
        """
    )
    for k, v in prob_dict.items():
        st.write(f"- **{k}** = {v:.2f}")

    # ──────────────── VISUALIZE PROBABILITIES ────────────────
    st.write("### 3. Probability Bar Chart")
    fig = plot_probabilities(prob_dict)
    st.pyplot(fig)

    # ──────────────── EXPLANATION ────────────────
    st.write("---")
    st.markdown(
        """
        ## Interpretation and Teaching Notes

        - Increasing **Layers with Fossil A** (or B) directly raises \( P(A) \) (or \( P(B) \)).
        - Overlap (\(A \cap B\)) heavily influences:
          - **P(A ∩ B)**: Probability of co-occurrence.
          - **P(B|A)**: If the overlap is large compared to how many total layers have A, 
            you get a higher conditional probability.
        - **Sandstone** doesn't affect these fossil probabilities directly,
          but in real scenarios, lithology can affect fossil preservation.

        This interactive setup shows how classical probability rules
        map onto a geological interpretation, where each layer might represent a
        specific stratigraphic interval in a core or outcrop.
        """
    )

if __name__ == "__main__":
    main()
