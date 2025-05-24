import pandas as pd
import statistics

# Load happiness data
happiness_df = pd.read_csv("Countries' Happiness Data 2017.csv")
happiness_scores = happiness_df["Happiness.Score"].dropna().tolist()

# Load literacy data
with open("API_SE.ADT.LITR.ZS_DS2_en_csv_v2_19396.csv", "r", encoding="utf-8") as f:
    lines_lit = f.readlines()

for i, line in enumerate(lines_lit):
    if "2017" in line:
        header = line.strip().split(",")
        lit_index = [j for j, col in enumerate(header) if col.strip('"') == "2017"][0]
        data_start_lit = i + 1
        break

literacy_rates = []
for line in lines_lit[data_start_lit:]:
    parts = line.strip().split(",")
    try:
        value = float(parts[lit_index].strip().strip('"'))
        literacy_rates.append(value)
    except:
        continue

# Load enrollment data
with open("API_SE.TER.ENRR_DS2_en_csv_v2_23897.csv", "r", encoding="utf-8") as f:
    lines_enr = f.readlines()

enrollment_rates = []
for line in lines_enr[5:]:
    parts = line.strip().split(",")
    try:
        value = float(parts[61].strip().strip('"'))
        enrollment_rates.append(value)
    except:
        continue

# Function to calculate and display stats
def describe_data(data, label):
    print(f"\n{label}")
    print("-" * len(label))
    print(f"Count              : {len(data)}")
    print(f"Mean               : {statistics.mean(data):.2f}")
    print(f"Median             : {statistics.median(data):.2f}")
    try:
        print(f"Mode               : {statistics.mode(data):.2f}")
    except statistics.StatisticsError:
        print("Mode               : No unique mode")
    print(f"Variance           : {statistics.variance(data):.2f}")
    print(f"Standard Deviation : {statistics.stdev(data):.2f}")

describe_data(enrollment_rates, "Tertiary Enrollment Rate (2017) % 0-100")
describe_data(literacy_rates, "Adult Literacy Rate (2017) % 0-100")
describe_data(happiness_scores, "Happiness Score (2017) 0-10")

// coastline statistics 

df = pd.read_csv("coastlines.csv")
df = df.dropna(subset=["coast_to_area_wf"])
df["coast_ratio"] = df["coast_to_area_wf"]

data = df["coast_ratio"]

print("- Coastline-to-Area Ratio (2017) % 0–100")
print(f"\nCount : {data.count()}")
print(f"Mean : {data.mean():.2f}")
print(f"Median : {data.median():.2f}")
print(f"Mode : {data.mode().iloc[0]:.2f}")
print(f"Variance : {data.var():.2f}")
print(f"\nStandard Deviation : {data.std():.2f}")

// Arable Land Statistics

df = pd.read_csv("arable_land_2017.csv")
data = df["arable_land_percent"].dropna()

print("- Arable Land Ratio (2017) % 0–100")
print(f"\nCount : {data.count()}")
print(f"Mean : {data.mean():.2f}")
print(f"Median : {data.median():.2f}")
print(f"Mode : {data.mode().iloc[0]:.2f}")
print(f"Variance : {data.var():.2f}")
print(f"\nStandard Deviation : {data.std():.2f}")

// Forest Land Statistics 

forest_df = pd.read_csv("Forest_Area__2017__-_All_Valid_Countries.csv")

forest_data = forest_df["2017"].dropna()

count = forest_data.count()
mean = forest_data.mean()
median = forest_data.median()
try:
    mode_val = mode(forest_data)
except:
    mode_val = "No unique mode"
variance = forest_data.var()
std_dev = forest_data.std()

print("Forest Area Ratio (2017) %0-100")
print(" ")
print(f"Count : {count}")
print(f"Mean : {mean:.2f}")
print(f"Median : {median:.2f}")
print(f"Mode : {mode_val}")
print(f"Variance : {variance:.2f}")
print(f"Standard Deviation : {std_dev:.2f}")

// Air Pollution Statistics

df_pm25 = pd.read_excel("PM2.5_2017_Countries.xlsx")

pm25_stats = {
    'Count': int(df_pm25['PM2.5_2017'].count()),
    'Mean': round(float(df_pm25['PM2.5_2017'].mean()), 2),
    'Median': round(float(df_pm25['PM2.5_2017'].median()), 2),
    'Mode': round(float(df_pm25['PM2.5_2017'].mode()[0]), 2),
    'Variance': round(float(df_pm25['PM2.5_2017'].var()), 2),
    'Standard Deviation': round(float(df_pm25['PM2.5_2017'].std()), 2)
}

for k, v in pm25_stats.items():
    print(f"{k} : {v}")
