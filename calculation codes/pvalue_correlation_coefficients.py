
# 1. P-VALUE & PEARSON CORRELATION

import pandas as pd
from scipy.stats import pearsonr, spearmanr

# Load Happiness Data
happiness_df = pd.read_csv("Countries' Happiness Data 2017.csv")

# Match Adult Literacy Rate with Happiness
with open("API_SE.ADT.LITR.ZS_DS2_en_csv_v2_19396.csv", "r", encoding="utf-8") as f:
    lines_lit = f.readlines()

for i, line in enumerate(lines_lit):
    if "2017" in line:
        header = line.strip().split(",")
        lit_index = [j for j, col in enumerate(header) if col.strip('"') == "2017"][0]
        data_start_lit = i + 1
        break

common_lit_scores = []
common_lit_happy = []

for line in lines_lit[data_start_lit:]:
    parts = line.strip().split(",")
    country = parts[0].strip('"')
    try:
        lit_val = float(parts[lit_index].strip().strip('"'))
        row = happiness_df[happiness_df["Country"] == country]
        if not row.empty:
            common_lit_scores.append(lit_val)
            common_lit_happy.append(float(row["Happiness.Score"].values[0]))
    except:
        continue

# Match Tertiary Enrollment with Happiness
with open("API_SE.TER.ENRR_DS2_en_csv_v2_23897.csv", "r", encoding="utf-8") as f:
    lines_enr = f.readlines()

common_enr_scores = []
common_enr_happy = []

for line in lines_enr[5:]:
    parts = line.strip().split(",")
    country = parts[0].strip('"')
    try:
        enr_val = float(parts[61].strip().strip('"'))
        row = happiness_df[happiness_df["Country"] == country]
        if not row.empty:
            common_enr_scores.append(enr_val)
            common_enr_happy.append(float(row["Happiness.Score"].values[0]))
    except:
        continue

# 2. PEARSON CORRELATION RESULTS

def pearson_stats(x, y, label):
    r, p = pearsonr(x, y)
    print(f"\n{label} (Pearson Correlation)")
    print("-" * (len(label) + 26))
    print(f"Correlation Coefficient (r): {r:.4f}")
    print(f"P-value                    : {p:.4e}")

pearson_stats(common_enr_scores, common_enr_happy, "Tertiary Enrollment vs Happiness")
pearson_stats(common_lit_scores, common_lit_happy, "Literacy Rate vs Happiness")

# 3. SPEARMAN CORRELATION RESULTS

def spearman_stats(x, y, label):
    r, p = spearmanr(x, y)
    print(f"\n{label} (Spearman Correlation)")
    print("-" * (len(label) + 27))
    print(f"Correlation Coefficient (ρ): {r:.4f}")
    print(f"P-value                    : {p:.4e}")

spearman_stats(common_enr_scores, common_enr_happy, "Tertiary Enrollment vs Happiness Score")
spearman_stats(common_lit_scores, common_lit_happy, "Literacy Rate vs Happiness Score")
