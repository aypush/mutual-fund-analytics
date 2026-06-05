import pandas as pd
from pathlib import Path

# Folder containing all CSV files
raw_path = Path("data/raw")

# Get all CSV files
csv_files = raw_path.glob("*.csv")

for file in csv_files:

    print("\n" + "=" * 60)
    print(f"FILE: {file.name}")

    # Load dataset
    df = pd.read_csv(file)

    # Basic Info
    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(list(df.columns))

    print("\nData Types:")
    print(df.dtypes)

    # Missing values (sorted for clarity)
    print("\nMissing Values:")
    print(df.isnull().sum().sort_values(ascending=False))

    # Duplicate rows
    dup = df.duplicated().sum()
    print("\nDuplicate Rows:")
    print(dup)

    # Quick sanity stats (only numeric)
    print("\nNumeric Summary:")
    df.select_dtypes(include=["number"]).describe().T

    # Preview
    print("\nFirst 5 Rows:")
    print(df.head())

    df = pd.read_csv("data/raw/01_fund_master.csv")

report = f"""
DATA QUALITY REPORT

Shape: {df.shape}

Missing Values:
{df.isnull().sum().to_string()}

Duplicate Rows: {df.duplicated().sum()}

Numeric Summary:
{df.select_dtypes(include=["number"]).describe().to_string()}
"""

with open("reports/data_quality_summary.txt", "w") as f:
    f.write(report)

print("Data quality report saved.")