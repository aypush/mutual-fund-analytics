import pandas as pd

performance = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

print(performance.head())

print("\nDataset Info:")
print(performance.info())

print("\nMissing Values:")
print(performance.isnull().sum())

print("\nExpense Ratio Summary:")
print(performance["expense_ratio_pct"].describe())

invalid_expense = performance[
    (performance["expense_ratio_pct"] < 0.1) |
    (performance["expense_ratio_pct"] > 2.5)
]

print("\nInvalid Expense Ratio Records:")
print(len(invalid_expense))

print("\nReturn Summary:\n")

print(
    performance[
        [
            "return_1yr_pct",
            "return_3yr_pct",
            "return_5yr_pct"
        ]
    ].describe()
)

print("\nUnique Risk Grades:")
print(performance["risk_grade"].unique())

performance.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("\nScheme Performance dataset saved successfully.")