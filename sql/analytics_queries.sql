-- Total revenue by category
SELECT category, SUM(amount) AS total_revenue
FROM sales_cleaned
GROUP BY category
ORDER BY total_revenue DESC;

-- Top 10 most profitable orders
SELECT order_id, profit
FROM sales_cleaned
ORDER BY profit DESC
LIMIT 10;

-- Quantity sold per sub-category
SELECT sub_category, SUM(quantity) AS total_quantity
FROM sales_cleaned
GROUP BY sub_category
ORDER BY total_quantity DESC;

-- Payment mode distribution
SELECT payment_mode, COUNT(*) AS count
FROM sales_cleaned
GROUP BY payment_mode;