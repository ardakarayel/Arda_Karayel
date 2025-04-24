# Scatter plot Happiness Score x Tertiary Enrollment
import pandas as pd
import matplotlib.pyplot as plt

happiness_df = pd.read_csv("Countries' Happiness Data 2017.csv")

countries = []
enrollments = []

with open("API_SE.TER.ENRR_DS2_en_csv_v2_23897.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines[5:]:
    parts = line.strip().split(",")
    country = parts[0].strip('"')
    if len(parts) > 61:
        try:
            value = float(parts[61].strip().strip('"'))
            countries.append(country)
            enrollments.append(value)
        except ValueError:
            continue

matched_countries = set(happiness_df["Country"].str.strip())
final_countries = []
final_enrollments = []
final_scores = []

for country, enr in zip(countries, enrollments):
    row = happiness_df[happiness_df["Country"] == country]
    if not row.empty:
        score = float(row["Happiness.Score"].values[0])
        final_countries.append(country)
        final_enrollments.append(enr)
        final_scores.append(score)

plt.figure(figsize=(10, 6))
plt.scatter(final_enrollments, final_scores, color='dodgerblue', marker ='x')
plt.title("Tertiary Enrollment (%) vs Happiness Score (2017)")
plt.xlabel("Tertiary Enrollment (%)")
plt.ylabel("Happiness Score")
plt.grid(True)


plt.tight_layout()
plt.show()
