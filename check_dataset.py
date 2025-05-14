import pandas as pd

# Load dataset
data = pd.read_csv("dataset_jurusan.csv")

# Tampilkan distribusi jurusan
print("Distribusi jurusan:")
print(data["Jurusan"].value_counts())

# Tampilkan jumlah total sampel
print(f"\nTotal sampel: {len(data)}")