# Box plot of tertiary and happiness data
import pandas as pd

# Load happiness data
happiness_df = pd.read_csv("Countries' Happiness Data 2017.csv")
happiness_countries = set(happiness_df["Country"].str.strip())

# Reload tertiary data
with open("API_SE.TER.ENRR_DS2_en_csv_v2_23897.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Get countries with tertiary enrollment and happiness
final_countries = []
final_enrollments = []
final_scores = []

for line in lines[5:]:
    parts = line.strip().split(",")
    country = parts[0].strip('"')
    if country in happiness_countries and len(parts) > 61:
        try:
            enrollment = float(parts[61].strip().strip('"'))
            score_row = happiness_df[happiness_df["Country"] == country]
            if not score_row.empty:
                score = float(score_row["Happiness.Score"].values[0])
                final_countries.append(country)
                final_enrollments.append(enrollment)
                final_scores.append(score)
        except:
            continue

# Plot separate boxplots
import matplotlib.pyplot as plt

# Boxplot: Tertiary Enrollment separately
plt.figure(figsize=(8, 5))
plt.boxplot(final_enrollments, patch_artist=True,
            boxprops=dict(facecolor='skyblue'),
            medianprops=dict(color='darkblue'),
            whiskerprops=dict(color='gray'),
            capprops=dict(color='gray'))

plt.title("Boxplot: Tertiary Enrollment (%) (2017)")
plt.ylabel("Tertiary Enrollment (%)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Boxplot: Happiness Score separately
plt.figure(figsize=(8, 5))
plt.boxplot(final_scores, patch_artist=True,
            boxprops=dict(facecolor='lightcoral'),
            medianprops=dict(color='darkred'),
            whiskerprops=dict(color='gray'),
            capprops=dict(color='gray'))

plt.title("Boxplot: Happiness Score (2017)")
plt.ylabel("Happiness Score")
plt.grid(True)
plt.tight_layout()
plt.show()
