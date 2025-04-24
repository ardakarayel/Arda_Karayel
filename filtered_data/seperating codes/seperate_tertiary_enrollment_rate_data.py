# seperate tertiary enrollment rate data for each country



import pandas as pd

happiness_df = pd.read_csv("Countries' Happiness Data 2017.csv")
happiness_countries = set(happiness_df["Country"].str.strip())

with open("API_SE.TER.ENRR_DS2_en_csv_v2_23897.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()

countries = []
enrollments = []

for line in lines[5:]:
    parts = line.strip().split(",")
    country = parts[0].strip('"')
    if country in happiness_countries and len(parts) > 61:
        try:
            value = float(parts[61].strip().strip('"'))
            countries.append(country)
            enrollments.append(value)
        except ValueError:
            continue

print(f"{'Country':<60} {'Tertiary Enrollment (%)':>25}")
print("-" * 85)
for country, rate in zip(countries, enrollments):
    print(f"{country:<60} {rate:>25.2f}")
