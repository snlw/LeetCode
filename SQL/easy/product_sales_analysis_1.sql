-- https://leetcode.com/problems/product-sales-analysis-i/submissions/1299862135
SELECT product_name, year, price
FROM Sales
LEFT JOIN Product on Sales.product_id = Product.product_id
