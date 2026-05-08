# Import pandas and numpy
import pandas as pd
import numpy as np

# Load dataset
uninsured = pd.read_csv(
    "datasets/uninsured_rates/ACSST5Y2019.S2702-Data.csv"
)

uninsured.columns = uninsured.columns.str.strip()

# Drop blank or note rows
uninsured = uninsured[uninsured["GEO_ID"].notna()].copy()

# Keep relevant columns
uninsured_clean = uninsured[[
    "GEO_ID",
    "NAME",
    "S2702_C01_001E",   # Total population
    "S2702_C02_001E"    # Uninsured population
]].copy()

# Extract FIPS codes
uninsured_clean["FIPS"] = (
    uninsured_clean["GEO_ID"]
    .astype(str)
    .str[-5:]
)

# Clean county names
uninsured_clean["county"] = (
    uninsured_clean["NAME"]
    .str.replace(" County, California", "", regex=False)
    .str.replace(" County, CA", "", regex=False)
)

# Convert columns to numeric
uninsured_clean["total_pop"] = pd.to_numeric(
    uninsured_clean["S2702_C01_001E"],
    errors="coerce"
)

uninsured_clean["uninsured_pop"] = pd.to_numeric(
    uninsured_clean["S2702_C02_001E"],
    errors="coerce"
)

# Compute uninsured percentage
uninsured_clean["percent_uninsured"] = (
    100 * uninsured_clean["uninsured_pop"]
    / uninsured_clean["total_pop"]
)

# Keep final columns
uninsured_clean = uninsured_clean[[
    "FIPS",
    "county",
    "total_pop",
    "uninsured_pop",
    "percent_uninsured"
]]

# Validation checks
print("Missing values:")
print(uninsured_clean.isna().sum())

print("\nDuplicate FIPS count:")
print(uninsured_clean["FIPS"].duplicated().sum())

print("\nColumn data types:")
print(uninsured_clean.dtypes)

# Save cleaned dataset
uninsured_clean.to_csv(
    "datasets/cleaned/uninsured_rates_cleaned.csv",
    index=False
)

print("\nCleaned uninsured dataset saved successfully.")