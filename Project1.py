# Importing necessary libraries
import pandas as pd

# Reading Excel File
my_data = pd.read_excel("Dataset for Data Analytics.xlsx")

# Identifying Missing Values
print("Missing Values:\n--------------------" )
print(my_data.isnull().sum())
print("\n--------------------" )


# Handling Missing Values
my_data["CouponCode"]= my_data["CouponCode"].fillna("No Coupon",inplace=True)
print("\nAfter Handling Missing values:\n--------------------" )
print(my_data.isnull().sum())
print("\n--------------------" )

# Identifying duplicates based on CustomerID
print("Duplicates before cleaning:", my_data["CustomerID"].duplicated().sum())

# Remove duplicates based on CustomerID
my_data.drop_duplicates(subset=["CustomerID"], keep="first", inplace=True)
print("Duplicates after cleaning:", my_data["CustomerID"].duplicated().sum())
print("----------------")

# Convert Date column to datetime format
my_data["Date"] = pd.to_datetime(my_data["Date"], errors="coerce")
# Standardize date format
my_data["Date"] = my_data["Date"].dt.strftime("%Y-%m-%d")

# Removing extra spaces from the text columns
text_cols = my_data.select_dtypes(include=["str"]).columns
for col in text_cols:
    my_data[col] = my_data[col].astype(str).str.strip()

# Validation Checks

# Check for duplicate CustomerIDs
duplicate_ids = my_data["CustomerID"].duplicated().sum()

# Check for invalid dates
invalid_dates = pd.to_datetime(my_data["Date"], errors="coerce").isna().sum()

print("\nVALIDATION RESULTS\n------------------")
print(f"Duplicate CustomerIDs: {duplicate_ids}")
print(f"Invalid Date Formats: {invalid_dates}")

assert duplicate_ids == 0, "Duplicate IDs still exist!"
assert invalid_dates == 0, "Invalid date formats still exist!"
print("------------------------")

print("Proof completed:")
print("Zero duplicate CustomerIDs")
print("Zero incorrectly formatted dates")

my_data.to_excel("Dataset_Cleaned.xlsx", index=False)