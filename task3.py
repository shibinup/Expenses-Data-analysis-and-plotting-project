import pandas as pd
import numpy as np
df = pd.read_csv("expenses_dirty.csv")


# 1. Find how many missing values are in each column
# 2. Fix category names — make all consistent (capitalize)
# 3. Drop rows where category is missing
# 4. Fix the "abc" amount — convert amount column to numeric
#    (hint: use pd.to_numeric with errors='coerce')
# 5. Fill missing amount with the column average
# 6. Remove duplicate rows
# 7. Save the cleaned data as "expenses_cleaned.csv"

print(df)
no_of_missing_value_per_columns=df.isna().sum()
print(no_of_missing_value_per_columns)

# 2. Fix category names — make all consistent (capitalize)

df["category"] = df["category"].str.upper()


# 3. Drop rows where category is missing
df=df.dropna(subset=["category"])
print(df)

# 4. Fix the "abc" amount — convert amount column to numeric
   

df["amount"] = pd.to_numeric(df["amount"],errors="coerce")
print(df)

# 5. Fill missing amount with the column average
df["amount"] = df["amount"].fillna(df["amount"].mean())
print(df)
print("--------------------------")
# 6. Remove duplicate rows
df = df.drop_duplicates()
print(df)
