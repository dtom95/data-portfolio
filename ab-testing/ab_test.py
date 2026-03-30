import pandas as pd
from scipy import stats

# Load dataset
df = pd.read_csv("ab_data.csv")

# Split groups
control = df[df["Group"] == "Control"]["Post_Score"]
treatment = df[df["Group"] == "Treatment"]["Post_Score"]

# Run t-test
t_stat, p_value = stats.ttest_ind(control, treatment)

# Print results
print("T-statistic:", t_stat)
print("P-value:", p_value)