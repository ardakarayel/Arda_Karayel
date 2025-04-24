#Scatter plot with happiness variables

import matplotlib.pyplot as plt

# Filter and align happiness data for only the matched countries
happiness_filtered = happiness_df[happiness_df["Country"].isin(final_countries)]

# Prepare X variables and Y (Happiness Score)
gdp = happiness_filtered["Economy..GDP.per.Capita."].astype(float).tolist()
freedom = happiness_filtered["Freedom"].astype(float).tolist()
life_exp = happiness_filtered["Health..Life.Expectancy."].astype(float).tolist()
happy = happiness_filtered["Happiness.Score"].astype(float).tolist()
countries_scatter = happiness_filtered["Country"].tolist()

# Set up scatter plots for each factor
fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharey=True)

factors = [gdp, freedom, life_exp]
labels = ["GDP per Capita", "Freedom", "Life Expectancy"]

for ax, x, label in zip(axes, factors, labels):
    ax.scatter(x, happy, color="dodgerblue", marker='x')
    ax.set_xlabel(label)
    ax.set_ylabel("Happiness Score")
    ax.set_title(f"Happiness vs {label}")


plt.tight_layout()
plt.show()
