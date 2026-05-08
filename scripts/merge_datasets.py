# Merge cleaned datasets

import pandas as pd

# Load cleaned datasets
income_df = pd.read_csv(
    "datasets/cleaned/household_income_cleaned.csv"
)

uninsured_df = pd.read_csv(
    "datasets/cleaned/uninsured_rates_cleaned.csv"
)

poverty_df = pd.read_csv(
    "datasets/cleaned/food_insecurity_cleaned.csv"
)

cancer_df = pd.read_csv(
    "datasets/cleaned/incd_cleaned.csv"
)

# Ensure FIPS columns are strings with leading zeros
income_df["FIPS"] = income_df["FIPS"].astype(str).str.zfill(5)
uninsured_df["FIPS"] = uninsured_df["FIPS"].astype(str).str.zfill(5)
poverty_df["FIPS"] = poverty_df["FIPS"].astype(str).str.zfill(5)
cancer_df["FIPS"] = cancer_df["FIPS"].astype(str).str.zfill(5)

# Merge income and uninsured datasets
df_merge1 = income_df.merge(
    uninsured_df,
    on="FIPS",
    how="inner"
)

# Merge poverty dataset
social_df = df_merge1.merge(
    poverty_df,
    on="FIPS",
    how="inner"
)

# Rename income column
social_df = social_df.rename(columns={
    "median_income": "median_income_$"
})

# Clean cancer dataset column names
cancer_clean = cancer_df.rename(columns={
    "County": "county",
    "2023 Rural-Urban Continuum Codes([rural urban note])": "rural_urban",
    "Age-Adjusted Incidence Rate([rate note]) - cases per 100,000": "incidence_rate",
    "Average Annual Count": "avg_annual_count",
    "Percent of Cases with Late Stage": "percent_late_stage"
})

# Keep relevant cancer columns
cancer_clean = cancer_clean[[
    "FIPS",
    "county",
    "rural_urban",
    "incidence_rate",
    "avg_annual_count",
    "percent_late_stage"
]]

# Merge cancer dataset with social determinants datasets
final_df = cancer_clean.merge(
    social_df,
    on="FIPS",
    how="inner"
)

# Validation checks
print("Final merged dataset shape:")
print(final_df.shape)

print("\nMissing values:")
print(final_df.isna().sum())

print("\nDuplicate FIPS count:")
print(final_df["FIPS"].duplicated().sum())

# Drop duplicate county columns
final_df = final_df.drop(columns=[
    "NAME",
    "county_y",
    "County"
])

# Rename main county column
final_df = final_df.rename(columns={
    "county_x": "county"
})

# Save final merged dataset
final_df.to_csv(
    "datasets/cleaned/final_merged_dataset.csv",
    index=False
)

print("\nFinal merged dataset saved successfully.")