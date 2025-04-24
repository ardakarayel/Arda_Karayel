
#bar chart happiness and literacy rate
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random

# Load happiness data
happiness_df = pd.read_csv("Countries' Happiness Data 2017.csv")
happiness_countries = set(happiness_df["Country"].str.strip())

# Load literacy data
with open("API_SE.ADT.LITR.ZS_DS2_en_csv_v2_19396.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find header and year index
for i, line in enumerate(lines):
    if "2017" in line:
        header = line.strip().split(",")
        year_index = [j for j, col in enumerate(header) if col.strip('"') == "2017"][0]
        data_start = i + 1
        break

# Extract literacy data
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

# Match happiness scores
happy_scores = []
valid_countries = []
valid_lit = []
valid_happy = []

for country, lit in zip(countries, literacy_rates):
    row = happiness_df[happiness_df["Country"] == country]
    if not row.empty:
        happy = float(row["Happiness.Score"].values[0])
        valid_countries.append(country)
        valid_lit.append(lit)
        valid_happy.append(happy * 10)

# Zip for plotting
valid_data = list(zip(valid_countries, valid_lit, valid_happy))

# Shuffle and split
random.seed(42)
random.shuffle(valid_data)

part1 = valid_data[:15]
part2 = valid_data[15:30]

def plot_part(data, title):
    labels, literacy, happiness = zip(*data)
    x = np.arange(len(labels))
    bar_width = 0.4

    plt.figure(figsize=(12, 6))
    plt.bar(x - bar_width/2, literacy, width=bar_width, label="Literacy Rate (%)", color='lightgreen')
    plt.bar(x + bar_width/2, happiness, width=bar_width, label="Happiness Score ×10", color='salmon')

    plt.xticks(x, labels, rotation=90)
    plt.xlabel("Country")
    plt.ylabel("Value")
    plt.title(title)
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()

# Plot them
plot_part(part1, "Literacy Rate vs Happiness Score ×10 - Part 1")
plot_part(part2, "Literacy Rate vs Happiness Score ×10 - Part 2")
