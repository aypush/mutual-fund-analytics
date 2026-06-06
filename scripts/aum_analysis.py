import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
aum = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)

# Convert date
aum["date"] = pd.to_datetime(aum["date"])

# Extract year
aum["year"] = aum["date"].dt.year

# Keep latest value per fund house per year
aum_yearly = (
    aum.sort_values("date")
       .groupby(["fund_house", "year"])
       .last()
       .reset_index()
)

# Plot
plt.figure(figsize=(14, 7))

sns.barplot(
    data=aum_yearly,
    x="year",
    y="aum_lakh_crore",
    hue="fund_house"
)

plt.title("AUM Growth by Fund House (2022-2025)")
plt.xlabel("Year")
plt.ylabel("AUM (Lakh Crore ₹)")

plt.legend(
    bbox_to_anchor=(1.05, 1),
    loc="upper left"
)

plt.tight_layout()

plt.savefig(
    "reports/aum_growth.png",
    dpi=300
)

plt.show()

print("AUM growth chart saved.")