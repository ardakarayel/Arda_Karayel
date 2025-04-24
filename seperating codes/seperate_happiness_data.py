# seperate happiness data for each country

import pandas as pd

happiness_df = pd.read_csv("Countries' Happiness Data 2017.csv")

matched_countries = set(countries)
filtered = happiness_df[happiness_df["Country"].isin(matched_countries)][
    ["Country", "Happiness.Score", "Economy..GDP.per.Capita.", "Freedom", "Health..Life.Expectancy."]
]

print(f"{'Country':<40} {'Happiness Score':>17} {'GDP per Capita':>17} {'Freedom':>12} {'Life Expectancy':>18}")
print("-" * 110)

for _, row in filtered.iterrows():
    country = row['Country']
    score = float(row['Happiness.Score'])
    gdp = float(row['Economy..GDP.per.Capita.'])
    freedom = float(row['Freedom'])
    life_exp = float(row['Health..Life.Expectancy.'])

    print(f"{country:<40} {score:>17.2f} {gdp:>17.2f} {freedom:>12.2f} {life_exp:>18.2f}")
