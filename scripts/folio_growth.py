import pandas as pd
import matplotlib.pyplot as plt

# Load data
folios = pd.read_csv(
    "data/raw/06_industry_folio_count.csv"
)

# Convert month
folios["month"] = pd.to_datetime(
    folios["month"]
)

# Plot
plt.figure(figsize=(12,6))

plt.plot(
    folios["month"],
    folios["total_folios_crore"],
    marker="o"
)

# Highest point
max_row = folios.loc[
    folios["total_folios_crore"].idxmax()
]

plt.annotate(
    f'{max_row["total_folios_crore"]} Cr',
    (
        max_row["month"],
        max_row["total_folios_crore"]
    )
)

plt.title("Mutual Fund Industry Folio Growth")

plt.xlabel("Month")
plt.ylabel("Total Folios (Crore)")

plt.tight_layout()

plt.savefig(
    "reports/folio_growth.png",
    dpi=300
)

plt.show()

print("Folio growth chart saved.")