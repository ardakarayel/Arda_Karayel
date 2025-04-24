#Bar chart with tertiary enrollment and happiness score with 2 part

import numpy as np
import matplotlib.pyplot as plt

split_index = len(final_countries) // 2

country_splits = [final_countries[:split_index], final_countries[split_index:]]
enrollment_splits = [final_enrollments[:split_index], final_enrollments[split_index:]]
score_splits = [final_scores[:split_index], final_scores[split_index:]]

for i in range(2):
    x = np.arange(len(country_splits[i]))
    scaled_scores = [s * 10 for s in score_splits[i]]

    plt.figure(figsize=(14, 6))
    plt.bar(x - 0.2, enrollment_splits[i], width=0.4, label="Tertiary Enrollment (%)", color="skyblue")
    plt.bar(x + 0.2, scaled_scores, width=0.4, label="Happiness Score x10", color="salmon")

    plt.xticks(ticks=x, labels=country_splits[i], rotation=90)
    plt.title(f"Tertiary Enrollment vs Happiness Score (x10) by Country - Part {i+1}")
    plt.xlabel("Country")
    plt.ylabel("Value")
    plt.legend()
    plt.tight_layout()
    plt.show()
