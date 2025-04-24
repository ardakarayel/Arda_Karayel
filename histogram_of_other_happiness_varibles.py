#histogram of other happiness variables

import seaborn as sns
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(18, 6))

variables = [gdp, freedom, life_exp]
labels = ["GDP per Capita", "Freedom", "Life Expectancy"]
colors = ["lightgreen", "lightcoral", "lightskyblue"]

for ax, data, label, color in zip(axes, variables, labels, colors):
    sns.histplot(data, bins=10, kde=True, color=color, edgecolor='black', ax=ax)
    ax.set_title(f"Distribution of {label}")
    ax.set_xlabel(label)
    ax.set_ylabel("Number of Countries")

plt.tight_layout()
plt.show()
