import requests
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Get data
url = "https://data.cdc.gov/resource/bi63-dtpu.json"
response = requests.get(url)
data = response.json()

# Step 2: Convert to DataFrame
df = pd.DataFrame(data)

# Step 3: Keep only relevant columns
df = df[["state", "year", "aadr"]]

# Step 4: Remove missing values
df = df.dropna()

# Step 5: Convert rate column to numeric
df["aadr"] = pd.to_numeric(df["aadr"], errors="coerce")

# Step 6: Show cleaned data
print("\nCLEANED DATA:")
print(df.head())

# Step 7: Analysis
result = df.groupby("state")["aadr"].mean()

print("\nAVERAGE RATE BY STATE:")
print(result.head(50))

# Step 8: Visualization
top_states = result.sort_values(ascending=False).head(50)

top_states.plot(kind="bar")

plt.title("Average Death Rate by State")

plt.show()