import pandas as pd

performance = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

print("\nTOP 10 FUNDS BY 3-YEAR RETURN\n")

top_funds = performance.sort_values(
    by="return_3yr_pct",
    ascending=False
)

print(
    top_funds[
        [
            "scheme_name",
            "fund_house",
            "category",
            "return_3yr_pct",
            "aum_crore"
        ]
    ].head(10)
)

print("\n\nAVERAGE RETURN BY CATEGORY\n")

category_return = (
    performance
    .groupby("category")["return_3yr_pct"]
    .mean()
    .sort_values(ascending=False)
)

print(category_return)

print("\n\nAVERAGE RETURN BY FUND HOUSE\n")

fund_house_return = (
    performance
    .groupby("fund_house")["return_3yr_pct"]
    .mean()
    .sort_values(ascending=False)
)

print(fund_house_return)