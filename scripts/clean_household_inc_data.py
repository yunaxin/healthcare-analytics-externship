# Importing pandas and numpy
import pandas as pd
import numpy as np


# Load dataset
income_df = pd.read_csv("datasets/household_income/ACSST5Y2019.S1901-Data.csv")
income_df.columns = income_df.columns.str.strip()

# Extract FIPS
income_df["FIPS"] = income_df["GEO_ID"].str[-5:]

income_clean = income_df[[
    "FIPS",
    "NAME",
    "S1901_C01_012E"  # Median HouseHold Income
]].copy()

income_clean.rename(columns={
    "S1901_C01_012E": "median_income"
}, inplace=True)

# Convert to Numeric
income_clean["median_income"] = (
    income_clean["median_income"]
        .replace(",", "", regex=True)
)

income_clean["median_income"] = pd.to_numeric(
    income_clean["median_income"],
    errors="coerce"
)

# Clean County Name
income_clean["NAME"] = (
    income_clean["NAME"]
        .str.replace(" County, California", "", regex=False)
)

# Validation checks
print("Missing values:")
print(income_clean.isna().sum())

print("\nColumn data types:")
print(income_clean.dtypes)

# Save cleaned dataset
income_clean.to_csv(
    "datasets/cleaned/household_income_cleaned.csv",
    index=False
)

print("\nCleaned household income dataset saved successfully.")
