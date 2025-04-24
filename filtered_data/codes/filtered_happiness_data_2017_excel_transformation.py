# Raw data to Filtered file for Happiness Data
import pandas as pd

happiness_df = pd.read_csv("Countries' Happiness Data 2017.csv")


matched_countries = set(countries)

filtered = happiness_df[happiness_df["Country"].isin(matched_countries)][
    ["Country", "Happiness.Score", "Economy..GDP.per.Capita.", "Freedom", "Health..Life.Expectancy."]
]

output_countries = []
happiness_scores = []
gdps = []
freedoms = []
life_exps = []

for _, row in filtered.iterrows():
    output_countries.append(row['Country'])
    happiness_scores.append(float(row["Happiness.Score"]))
    gdps.append(float(row["Economy..GDP.per.Capita."]))
    freedoms.append(float(row["Freedom"]))
    life_exps.append(float(row["Health..Life.Expectancy."]))

df = pd.DataFrame({
    "Country": output_countries,
    "Happiness.Score": happiness_scores,
    "Economy..GDP.per.Capita.": gdps,
    "Freedom": freedoms,
    "Health..Life.Expectancy.": life_exps
})

df.to_excel("Filtered_Happiness_Data_2017.xlsx", index=False)
