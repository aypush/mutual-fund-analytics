-- 1. Top 5 Funds by AUM
SELECT
    scheme_name,
    fund_house,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- 2. Average 3-Year Return
SELECT
    AVG(return_3yr_pct) AS avg_return
FROM fact_performance;


-- 3. Funds with Expense Ratio < 1%
SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;


-- 4. Top 10 Funds by 3-Year Return
SELECT
    scheme_name,
    return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 10;


-- 5. Transaction Count by Type
SELECT
    transaction_type,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type;


-- 6. Total Investment Amount
SELECT
    SUM(amount_inr) AS total_amount
FROM fact_transactions;


-- 7. Transactions by State
SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- 8. Average NAV
SELECT
    AVG(nav) AS average_nav
FROM fact_nav;


-- 9. Highest NAV Recorded
SELECT
    MAX(nav) AS highest_nav
FROM fact_nav;


-- 10. Fund Count by Risk Grade
SELECT
    risk_grade,
    COUNT(*) AS fund_count
FROM fact_performance
GROUP BY risk_grade;