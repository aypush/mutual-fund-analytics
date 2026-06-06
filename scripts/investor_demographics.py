import pandas as pd
import matplotlib.pyplot as plt

investors = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

age_counts = investors["age_group"].value_counts()

plt.figure(figsize=(8,6))

plt.pie(
    age_counts,
    labels=age_counts.index,
    autopct="%1.1f%%"
)

plt.title("Investor Age Group Distribution")

plt.savefig(
    "reports/age_group_distribution.png",
    dpi=300
)

plt.show()

print("Age Group chart saved.")

gender_counts = investors["gender"].value_counts()

plt.figure(figsize=(8,6))

plt.pie(
    gender_counts,
    labels=gender_counts.index,
    autopct="%1.1f%%"
)

plt.title("Gender Distribution")

plt.savefig(
    "reports/gender_distribution.png",
    dpi=300
)

plt.show()

print("Gender chart saved.")

import seaborn as sns

plt.figure(figsize=(10,6))

sns.boxplot(
    data=investors,
    x="age_group",
    y="amount_inr"
)

plt.title("Investment Amount by Age Group")

plt.xlabel("Age Group")
plt.ylabel("Amount (₹)")

plt.tight_layout()

plt.savefig(
    "reports/amount_by_age_group.png",
    dpi=300
)

plt.show()

print("Amount by Age Group chart saved.")