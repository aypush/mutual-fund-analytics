import pandas as pd
import matplotlib.pyplot as plt

# Load data
holdings = pd.read_csv(
    "data/raw/09_portfolio_holdings.csv"
)

# Aggregate sector weights
sector_weights = (
    holdings
    .groupby("sector")["weight_pct"]
    .sum()
    .sort_values(ascending=False)
)

# Plot
plt.figure(figsize=(8,8))

wedges, texts, autotexts = plt.pie(
    sector_weights,
    labels=sector_weights.index,
    autopct="%1.1f%%"
)

# Create donut
centre_circle = plt.Circle(
    (0,0),
    0.70,
    fc="white"
)

fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title("Sector Allocation Across Funds")

plt.tight_layout()

plt.savefig(
    "reports/sector_allocation_donut.png",
    dpi=300
)

plt.show()

print("Sector allocation chart saved.")