import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(
    "API_SP.POP.TOTL_DS2_en_csv_v2_406129.csv",
    skiprows=4
)

# Keep country name and latest population year
data = df[["Country Name", "2024"]]

# Remove missing values
data = data.dropna()

# Top 10 countries by population
top10 = data.sort_values(
    by="2024",
    ascending=False
).head(10)

# Plot
plt.figure(figsize=(12,6))

plt.bar(
    top10["Country Name"],
    top10["2024"]
)

plt.title("Top 10 Most Populated Countries (2024)")
plt.xlabel("Country")
plt.ylabel("Population")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("output.png")
plt.show()