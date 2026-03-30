import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("ab_data.csv")

# Create improvement column
df["Improvement"] = df["Post_Score"] - df["Pre_Score"]

# Split groups
control = df[df["Group"] == "Control"]["Improvement"]
treatment = df[df["Group"] == "Treatment"]["Improvement"]

# Run t-test
t_stat, p_value = stats.ttest_ind(control, treatment)

print("T-statistic:", t_stat)
print("P-value:", p_value)

# --- VISUALIZATION STARTS HERE ---

import numpy as np

x_control = np.random.normal(1, 0.04, len(control))
x_treatment = np.random.normal(2, 0.04, len(treatment))

plt.scatter(x_control, control, alpha=0.7)
plt.scatter(x_treatment, treatment, alpha=0.7)

# Plot mean lines
plt.hlines(control.mean(), 0.85, 1.15)
plt.hlines(treatment.mean(), 1.85, 2.15)

# Labels
plt.xticks([1, 2], ["Control", "Treatment"])
plt.ylabel("Score Improvement")
plt.title("A/B Test Results: Individual Improvements and Group Averages")

plt.show()