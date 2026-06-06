import pandas as pd
import matplotlib.pyplot as plt

# Load data
nav = pd.read_csv(
    "data/raw/02_nav_history.csv"
)

# Convert date
nav["date"] = pd.to_datetime(nav["date"])

# Select 5 representative schemes
selected_funds = [
    119551,
    120503,
    118632,
    119092,
    120841
]

nav_subset = nav[
    nav["amfi_code"].isin(selected_funds)
]

plt.figure(figsize=(14,7))

for code in selected_funds:

    temp = nav_subset[
        nav_subset["amfi_code"] == code
    ]

    plt.plot(
        temp["date"],
        temp["nav"],
        label=str(code)
    )

plt.title("NAV Trends of Major Mutual Funds")
plt.xlabel("Date")
plt.ylabel("NAV")

plt.legend()

plt.tight_layout()

plt.savefig(
    "reports/nav_trends.png",
    dpi=300
)

plt.show()

print("NAV trend chart saved.")