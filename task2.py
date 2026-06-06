import pandas as pd
df= pd.read_csv("expenses.csv")

# Task 2 — solve these:

# 1. Filter only "Food" expenses and find total food spend
# 2. Find total spending per MONTH (group by month)
# 3. Which month had the highest spending?
# 4. Find all expenses GREATER than 500
# 5. Find average spending per category
print(df)
# 1. Filter only "Food" expenses and find total food spend
all_foods=df[df["category"]=="Food"]
total_for_foods = all_foods["amount"].sum()
print(all_foods)
print("total for Food==",total_for_foods) 


 #2. Find total spending per MONTH (group by month)
df["date"] = pd.to_datetime(df["date"])
df["month_number"] = df["date"].dt.month  
df["month_name"] = df["date"].dt.month_name()  
grou_by_month = df.groupby(["month_number","month_name"])["amount"].sum().reset_index()
print(grou_by_month)

# 3. Which month had the highest spending?
highest_month = grou_by_month[grou_by_month["amount"]==grou_by_month["amount"].max()]
print("highest spend month ===",highest_month)


# 4. Find all expenses GREATER than 500
expenses_gt_500 = df[df["amount"]>500]
print(expenses_gt_500)

#5. Find average spending per category
avg_per_category = df.groupby("category")["amount"].mean().reset_index()
print(avg_per_category)

