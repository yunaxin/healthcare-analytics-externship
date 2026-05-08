# Importing libraries
import numpy as np
import pandas as pd

df = pd.read_csv('datasets/breast_cancer/incd.csv', skiprows=8)
df.columns = df.columns.str.strip()

# Replace missing data
df = df.replace("N/A", np.nan)

# Remove summary rows and footnote numbers ("7")
df = df[~df["County"].str.contains("California|US", na=False)]
df["County"] = df["County"].str.replace(r"\(\d+\)", "", regex=True).str.strip()

# Fix FIPS
df["FIPS"] = df["FIPS"].astype(str)
df["FIPS"] = df["FIPS"].str.replace(".0", "", regex=False)
df["FIPS"] = df["FIPS"].str.zfill(5)

# Convert columns to numbers
rate_col = "Age-Adjusted Incidence Rate([rate note]) - cases per 100,000"
late_col = "Percent of Cases with Late Stage"
count_col = "Average Annual Count"

# Convert columns to numeric values and coerce invalid entries to NaN
df[rate_col] = pd.to_numeric(df[rate_col], errors='coerce')
df[late_col] = pd.to_numeric(df[late_col], errors='coerce')
df[count_col] = pd.to_numeric(df[count_col], errors='coerce')

# Convert incidence rate column into a NumPy array
rates = df[rate_col].values

# Compute the average and maximum rate
avg_rate = np.nanmean(rates)
max_rate = np.nanmax(rates)

# Keep only realistic values (rate can't be negative)
df = df[df[rate_col].isna() | (df[rate_col] >= 0)]

# Normalize incidence rate (0-1 scale)
rates = df[rate_col].values

min_rate = np.nanmin(rates)
max_rate = np.nanmax(rates)

# Save cleaned dataset
df.to_csv("datasets/cleaned/incd_cleaned.csv", index=False)