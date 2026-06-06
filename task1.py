import pandas as pd

df = pd.read_csv("expenses.csv")

# Task 1 — answer these questions in code:
# 1. How many rows are in this data?
# 2. What are all the unique categories?
# 3. What is the total amount spent overall?
# 4. What is the total spent per category?
# 5. Which category has the highest spending?
print(df)
# 1: How many rows are in this data?
no_of_rows=len(df)


# 2. What are all the unique categories?
unique_categories=df["category"].unique()
print(unique_categories)

# 3. What is the total amount spent overall?
total_amount=df["amount"].sum()
print(total_amount)

# 4. What is the total spent per category?
spent_by_category= df.groupby("category")["amount"].sum().reset_index()
print(spent_by_category)

# 5. Which category has the highest spending?
highest_spend_category = spent_by_category[spent_by_category["amount"]==spent_by_category["amount"].max()]
print(highest_spend_category)