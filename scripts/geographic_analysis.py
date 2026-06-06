import pandas as pd
import matplotlib.pyplot as plt

# Load data
investors = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

# Total investment by state
state_amount = (
    investors
    .groupby("state")["amount_inr"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))

state_amount.plot(kind="barh")

plt.title("Investment Amount by State")
plt.xlabel("Amount (₹)")
plt.ylabel("State")

plt.tight_layout()

plt.savefig(
    "reports/investment_by_state.png",
    dpi=300
)

plt.show()

print("State investment chart saved.")

tier_counts = investors["city_tier"].value_counts()

plt.figure(figsize=(8, 6))

plt.pie(
    tier_counts,
    labels=tier_counts.index,
    autopct="%1.1f%%"
)

plt.title("T30 vs B30 Investor Distribution")

plt.savefig(
    "reports/t30_b30_distribution.png",
    dpi=300
)

plt.show()

print("T30/B30 chart saved.")