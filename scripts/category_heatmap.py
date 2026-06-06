import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
category = pd.read_csv(
    "data/raw/05_category_inflows.csv"
)

# Create pivot table
heatmap_data = category.pivot(
    index="category",
    columns="month",
    values="net_inflow_crore"
)

# Plot
plt.figure(figsize=(14, 8))

sns.heatmap(
    heatmap_data,
    annot=False,
    cmap="YlGnBu"
)

plt.title("Category-wise Net Inflows Heatmap")

plt.tight_layout()

plt.savefig(
    "reports/category_heatmap.png",
    dpi=300
)

plt.show()

print("Category heatmap saved.")