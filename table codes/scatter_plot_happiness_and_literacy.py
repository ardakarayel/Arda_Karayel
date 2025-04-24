#Scatter plot happiness score x literacy rate

import matplotlib.pyplot as plt


# Load happiness data
happiness_df = pd.read_csv("Countries' Happiness Data 2017.csv")
happiness_countries = set(happiness_df["Country"].str.strip())

# Load literacy data
with open("API_SE.ADT.LITR.ZS_DS2_en_csv_v2_19396.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find header and 2017 index
for i, line in enumerate(lines):
    if "2017" in line:
        header = line.strip().split(",")
        year_index = [j for j, col in enumerate(header) if col.strip('"') == "2017"][0]
        data_start = i + 1
        break

# Extract literacy rates
countries = []
literacy_rates = []

for line in lines[data_start:]:
    parts = line.strip().split(",")
    country = parts[0].strip('"')
    if country in happiness_countries and len(parts) > year_index:
        try:
            value = float(parts[year_index].strip().strip('"'))
            countries.append(country)
            literacy_rates.append(value)
        except ValueError:
            continue

# Get happiness scores for matched countries
happy_scores = []
for country in countries:
    row = happiness_df[happiness_df["Country"] == country]
    if not row.empty:
        happy_scores.append(float(row["Happiness.Score"].values[0]))

# Plot scatter
plt.figure(figsize=(10, 6))
plt.scatter(literacy_rates, happy_scores, color="green", marker='x')
plt.title("Adult Literacy Rate vs Happiness Score (2017)")
plt.xlabel("Adult Literacy Rate (%)")
plt.ylabel("Happiness Score")
plt.grid(True)



plt.tight_layout()
plt.show()
