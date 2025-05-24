
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

happiness_df = pd.read_excel("Filtered_Happiness_Data_2017 (1).xlsx")[['Country', 'Happiness.Score']]
pm25_df = pd.read_excel("PM2.5_2017_Countries.xlsx")



merged_df = pd.merge(happiness_df, pm25_df, on='Country')

pearson_corr, pearson_p = pearsonr(merged_df['PM2.5_2017'], merged_df['Happiness.Score'])
spearman_corr, spearman_p = spearmanr(merged_df['PM2.5_2017'], merged_df['Happiness.Score'])


// UPDATES FOR EXTRA DATA
print("Air Pollution (PM2.5) vs Happiness Score (2017)")
print(f"Pearson Correlation Coefficient (r): {round(pearson_corr, 4)}")
print(f"Pearson P-value                   : {round(pearson_p, 4)}\n")
print(f"Spearman Correlation Coefficient (ρ): {round(spearman_corr, 4)}")
print(f"Spearman P-value                     : {round(spearman_p, 4)}")


forest_df = pd.read_csv("Forest_Area__2017__-_All_Valid_Countries.csv")
happiness_df = pd.read_excel("Filtered_Happiness_Data_2017 (1).xlsx")

merged_df = pd.merge(happiness_df, forest_df, left_on="Country", right_on="Country Name")

forest = merged_df["2017"]
happiness = merged_df["Happiness.Score"]

pearson_corr, pearson_p = pearsonr(forest, happiness)

spearman_corr, spearman_p = spearmanr(forest, happiness)

print("Forest Area vs Happiness Score (Pearson Correlation)")
print(f"Correlation Coefficient (r): {pearson_corr:.4f}")
print(f"P-value                 : {pearson_p:.4e}")
print()

print("Forest Area vs Happiness Score (Spearman Correlation)")
print(f"Correlation Coefficient (ρ): {spearman_corr:.4f}")
print(f"P-value                   : {spearman_p:.4e}")



arable_df = pd.read_csv("arable_land_2017.csv")
happiness_df = pd.read_excel("Filtered_Happiness_Data_2017 (1).xlsx")

arable_df["arable_log"] = np.log1p(arable_df["arable_land_percent"])
scaler = StandardScaler()
arable_df["arable_log_scaled"] = scaler.fit_transform(arable_df[["arable_log"]])

merged = happiness_df.merge(arable_df, left_on="Country", right_on="country", how="inner")

pearson_r, pearson_p = pearsonr(merged["arable_log_scaled"], merged["Happiness.Score"])
spearman_r, spearman_p = spearmanr(merged["arable_log_scaled"], merged["Happiness.Score"])

print("* Arable Land vs Happiness Score (Log + Scaled)\n")

print("   Pearson Correlation")
print(f"   Correlation Coefficient (r): {pearson_r:.4f}")
print(f"   P-value                    : {pearson_p:.4f}\n")

print("   Spearman Correlation")
print(f"   Correlation Coefficient (ρ): {spearman_r:.4f}")
print(f"   P-value                    : {spearman_p:.4f}")




coast_df = pd.read_csv("coastlines.csv")
happiness_df = pd.read_excel("Filtered_Happiness_Data_2017 (1).xlsx")

coast_df = coast_df[["country", "coast_to_area_wf"]].dropna()
coast_df.columns = ["Country", "coast_ratio"]

coast_df["coast_log"] = np.log1p(coast_df["coast_ratio"])
scaler = StandardScaler()
coast_df["coast_log_scaled"] = scaler.fit_transform(coast_df[["coast_log"]])

merged = happiness_df.merge(coast_df, on="Country", how="inner")

pearson_r, pearson_p = pearsonr(merged["coast_log_scaled"], merged["Happiness.Score"])
spearman_r, spearman_p = spearmanr(merged["coast_log_scaled"], merged["Happiness.Score"])

print("* Coastline Ratio vs Happiness Score (Log + Scaled)\n")

print("   Pearson Correlation")
print(f"   Correlation Coefficient (r): {pearson_r:.4f}")
print(f"   P-value                    : {pearson_p:.5f}\n")

print("   Spearman Correlation")
print(f"   Correlation Coefficient (ρ): {spearman_r:.4f}")
print(f"   P-value                    : {spearman_p:.5f}")

