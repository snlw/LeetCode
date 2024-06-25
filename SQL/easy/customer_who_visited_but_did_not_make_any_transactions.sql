-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/submissions/1299876594/?envType=study-plan-v2&envId=top-sql-50
SELECT DISTINCT customer_id, COUNT(*) as count_no_trans
FROM Visits
LEFT JOIN Transactions ON Visits.visit_id = Transactions.visit_id
WHERE Transactions.transaction_id IS NULL
GROUP BY customer_id
