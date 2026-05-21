DROP TABLE IF EXISTS sales_cleaned;

CREATE TABLE sales_cleaned (
    order_id VARCHAR(20),
    amount NUMERIC,
    profit NUMERIC,
    quantity INTEGER,
    category VARCHAR(50),
    sub_category VARCHAR(50),
    payment_mode VARCHAR(50)
);