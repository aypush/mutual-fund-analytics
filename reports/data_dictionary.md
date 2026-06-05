# Mutual Fund Analytics Data Dictionary

## 1. fund_master

| Column | Description |
|----------|-------------|
| amfi_code | Unique mutual fund scheme identifier |
| fund_house | Asset Management Company |
| scheme_name | Name of the mutual fund scheme |
| category | Fund category |
| sub_category | Detailed category |
| expense_ratio_pct | Expense ratio percentage |
| risk_category | Risk classification |

---

## 2. nav_history

| Column | Description |
|----------|-------------|
| amfi_code | Scheme identifier |
| date | NAV date |
| nav | Net Asset Value |

---

## 3. scheme_performance

| Column | Description |
|----------|-------------|
| amfi_code | Scheme identifier |
| return_1yr_pct | 1-year return |
| return_3yr_pct | 3-year return |
| return_5yr_pct | 5-year return |
| alpha | Alpha metric |
| beta | Beta metric |
| sharpe_ratio | Risk-adjusted return metric |
| expense_ratio_pct | Fund expense ratio |
| aum_crore | Assets Under Management |

---

## 4. investor_transactions

| Column | Description |
|----------|-------------|
| investor_id | Investor identifier |
| transaction_date | Transaction date |
| transaction_type | SIP / Lumpsum / Redemption |
| amount_inr | Transaction amount |
| state | Investor state |
| city | Investor city |
| age_group | Investor age category |
| gender | Investor gender |
| kyc_status | KYC verification status |

---

## Data Sources

- MFAPI.in
- Internal Mutual Fund Dataset
- Simulated Investor Transaction Data
