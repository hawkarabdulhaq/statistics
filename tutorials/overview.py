import pandas as pd
import matplotlib.pyplot as plt

# Define the path to the CSV file
file_path = '/content/sample_data/earthquakes.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Convert the 'time' column to datetime format for better handling (optional)
df['time'] = pd.to_datetime(df['time'])

# Display basic information about the dataset
print("Dataset Shape:", df.shape)
print("\nFirst 5 Rows:")
print(df.head())
print("\nSummary Statistics:")
print(df.describe())

# Plot a histogram of the earthquake magnitudes
plt.figure(figsize=(8, 5))
plt.hist(df['magnitude'], bins=10, color='skyblue', edgecolor='black')
plt.title("Earthquake Magnitude Distribution")
plt.xlabel("Magnitude")
plt.ylabel("Frequency")
plt.show()

# Plot a scatter plot of Magnitude vs. Depth
plt.figure(figsize=(8, 5))
plt.scatter(df['magnitude'], df['depth'], color='green', alpha=0.7)
plt.title("Magnitude vs. Depth")
plt.xlabel("Magnitude")
plt.ylabel("Depth (km)")
plt.show()
