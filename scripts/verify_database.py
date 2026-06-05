import sqlite3
import pandas as pd

conn = sqlite3.connect("bluestock_mf.db")

tables = [
    "fact_nav",
    "fact_transactions",
    "fact_performance"
]

for table in tables:
    query = f"SELECT COUNT(*) AS row_count FROM {table}"
    result = pd.read_sql(query, conn)

    print("\n" + "=" * 40)
    print(table)
    print(result)

conn.close()