import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("expenses_cleaned.csv")
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.month

# ── CHART 1 ── Bar Chart
# Total spending per category
# x axis = category, y axis = total amount

# ── CHART 2 ── Pie Chart
# % share of each category in total spending

# ── CHART 3 ── Line Chart
# Monthly spending trend
# x axis = month, y axis = total amount per month

# ── CHART 4 ── Horizontal Bar Chart
# Top 5 highest single expenses
# (hint: sort values, take top 5)
print(df)


# ── CHART 1 ── Bar Chart
# Total spending per category
# x axis = category, y axis = total amount

amount_per_category_group = df.groupby("category")["amount"].sum().reset_index()
print(amount_per_category_group)
plt.bar(amount_per_category_group["category"],amount_per_category_group["amount"], color='skyblue')
plt.title('Amount per Category')
plt.xlabel('Category')
plt.ylabel('Amount')
plt.show()

# ── CHART 2 ── Pie Chart
# % share of each category in total spending
plt.pie(amount_per_category_group["amount"],labels= amount_per_category_group["category"], autopct='%1.1f%%')
plt.show()

# ── CHART 3 ── Line Chart
# Monthly spending trend
# x axis = month, y axis = total amount per month
df["month_name"] = df["date"].dt.month_name() 
amount_per_month = df.groupby(["month","month_name"])["amount"].sum().reset_index()
plt.plot(amount_per_month["month_name"],amount_per_month["amount"],marker='o', linestyle='--', linewidth=2)
plt.show()

# ── CHART 4 ── Horizontal Bar Chart
# Top 5 highest single expenses
# (hint: sort values, take top 5)
print("__________")
top_5 = df.sort_values("amount",ascending=False).head(5)
plt.barh(top_5["category"],top_5["amount"])
plt.show()
