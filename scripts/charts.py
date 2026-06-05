import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# Load Data
# ==========================================

performance = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

# ==========================================
# 1. Average Return by Category
# ==========================================

category_return = (
    performance
    .groupby("category")["return_3yr_pct"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

category_return.plot(kind="bar")

plt.title("Average 3-Year Return by Category")
plt.xlabel("Category")
plt.ylabel("Average 3-Year Return (%)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "reports/category_return.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==========================================
# 2. Top 10 Funds by 3-Year Return
# ==========================================

top10 = performance.nlargest(10, "return_3yr_pct")

plt.figure(figsize=(12, 6))

plt.barh(
    top10["scheme_name"],
    top10["return_3yr_pct"]
)

plt.title("Top 10 Funds by 3-Year Return")
plt.xlabel("Return (%)")

plt.tight_layout()

plt.savefig(
    "reports/top10_funds_return.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==========================================
# 3. Average Return by Fund House
# ==========================================

fund_house_return = (
    performance
    .groupby("fund_house")["return_3yr_pct"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

fund_house_return.plot(kind="bar")

plt.title("Average Return by Fund House")
plt.xlabel("Fund House")
plt.ylabel("Return (%)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "reports/fund_house_return.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==========================================
# 4. Expense Ratio vs Return
# ==========================================

plt.figure(figsize=(8, 6))

plt.scatter(
    performance["expense_ratio_pct"],
    performance["return_3yr_pct"]
)

plt.xlabel("Expense Ratio (%)")
plt.ylabel("3-Year Return (%)")

plt.title("Expense Ratio vs Return")

plt.tight_layout()

plt.savefig(
    "reports/expense_vs_return.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nAll charts saved successfully in reports folder!")