#Raw data to filtered file for Adult Literacy Rate

import pandas as pd

happiness_countries = set(happiness_df["Country"].str.strip())

with open("API_SE.ADT.LITR.ZS_DS2_en_csv_v2_19396.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "2017" in line:
        header = line.strip().split(",")
        year_index = [j for j, col in enumerate(header) if col.strip('"') == "2017"][0]
        data_start = i + 1
        break

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

print(f"{'Country':<60} {'Adult Literacy Rate (%)':>25}")
print("-" * 90)
for country, rate in zip(countries, literacy_rates):
    print(f"{country:<60} {rate:>25.2f}")

df = pd.DataFrame({
    "Country": countries,
    "Adult Literacy Rate (%)": literacy_rates
})

df.to_excel("Filtered_Adult_Literacy_2017.xlsx", index=False)
