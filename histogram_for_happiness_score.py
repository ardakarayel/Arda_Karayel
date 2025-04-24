#Histgoram for Happiness Score

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.histplot(final_scores, bins=10, kde=True, color='salmon', edgecolor='black')
plt.title("Distribution of Happiness Score (2017)")
plt.xlabel("Happiness Score")
plt.ylabel("Number of Countries")
plt.grid(True)
plt.tight_layout()
plt.show()
