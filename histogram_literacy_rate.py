import seaborn as sns
import matplotlib.pyplot as plt

# Plot  the KDE + Histogram for Adult Literacy Rate
plt.figure(figsize=(10, 6))
sns.histplot(literacy_rates, kde=True, color='lightgreen', edgecolor='black')

plt.title("Adult Literacy Rate Distribution (2017)")
plt.xlabel("Adult Literacy Rate (%)")
plt.ylabel("Number of Countries")
plt.grid(True)
plt.tight_layout()
plt.show()
