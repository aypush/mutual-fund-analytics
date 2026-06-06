import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
nav = pd.read_csv(
    "data/raw/02_nav_history.csv"
)

nav["date"] = pd.to_datetime(
    nav["date"]
)

# Select 10 funds
funds = nav["amfi_code"].unique()[:10]

nav_subset = nav[
    nav["amfi_code"].isin(funds)
]

# Pivot data
pivot_df = nav_subset.pivot(
    index="date",
    columns="amfi_code",
    values="nav"
)

# Daily returns
returns = pivot_df.pct_change()

# Correlation matrix
corr_matrix = returns.corr()

plt.figure(figsize=(10,8))

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm"
)

plt.title("Fund Return Correlation Matrix")

plt.tight_layout()

plt.savefig(
    "reports/correlation_matrix.png",
    dpi=300
)

plt.show()

print("Correlation matrix saved.")