#box plot of literacy rate

with open("API_SE.ADT.LITR.ZS_DS2_en_csv_v2_19396.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find header and index of 2017
for i, line in enumerate(lines):
    if "2017" in line:
        header = line.strip().split(",")
        year_index = [j for j, col in enumerate(header) if col.strip('"') == "2017"][0]
        data_start = i + 1
        break

# Match with happiness countries
happiness_df = pd.read_csv("Countries' Happiness Data 2017.csv")
happiness_countries = set(happiness_df["Country"].str.strip())

# Extract literacy values for matched countries
literacy_rates = []

for line in lines[data_start:]:
    parts = line.strip().split(",")
    country = parts[0].strip('"')
    if country in happiness_countries and len(parts) > year_index:
        try:
            value = float(parts[year_index].strip().strip('"'))
            literacy_rates.append(value)
        except ValueError:
            continue

# Plot boxplot for literacy
plt.figure(figsize=(8, 5))
plt.boxplot(literacy_rates, patch_artist=True,
            boxprops=dict(facecolor='lightgreen'),
            medianprops=dict(color='darkgreen'),
            whiskerprops=dict(color='gray'),
            capprops=dict(color='gray'))

plt.title("Boxplot: Adult Literacy Rate (%) (2017)")
plt.ylabel("Adult Literacy Rate (%)")
plt.grid(True)
plt.tight_layout()
plt.show()
