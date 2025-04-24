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

# Output stats for all three datasets
describe_data(enrollment_rates, "Tertiary Enrollment Rate (2017) % 0-100")
describe_data(literacy_rates, "Adult Literacy Rate (2017) % 0-100")
describe_data(happiness_scores, "Happiness Score (2017) 0-10")
