# Import libraries
import pandas as pd

# Load dataset
food_df = pd.read_csv("datasets/food_insecurity/StateAndCountyData.csv")
food_df.columns = food_df.columns.str.strip()

# Keep only California data
food_df = food_df[food_df["State"] == "CA"].copy()

# Keep only poverty rate variable
food_clean = food_df[food_df["Variable_Code"] == "POVRATE15"].copy()

# Select relevant columns
food_clean = food_clean[["FIPS", "County", "Value"]]

# Rename column for clarity
food_clean = food_clean.rename(columns={"Value": "poverty_rate"})

# Format FIPS codes
food_clean["FIPS"] = food_clean["FIPS"].astype(str).str.zfill(5)

# Reset index
food_clean = food_clean.reset_index(drop=True)

# Convert poverty rate column to numeric
food_clean["poverty_rate"] = pd.to_numeric(
    food_clean["poverty_rate"],
    errors="coerce"
)

# Validation checks
print("Missing values:")
print(food_clean.isna().sum())

print("\nDuplicate FIPS count:")
print(food_clean["FIPS"].duplicated().sum())

print("\nColumn data types:")
print(food_clean.dtypes)

# Save cleaned dataset
food_clean.to_csv(
    "datasets/cleaned/food_insecurity_cleaned.csv",
    index=False
)

print("\nCleaned dataset saved successfully.")