SELECT * FROM world.retail_store_sales_cleaned;
desc world.retail_store_sales_cleaned;

ALTER TABLE world.retail_store_sales_cleaned
MODIFY `Transaction Date` DATE;
-- now the table is ok 

-- Find total revenue generated.
select sum(`Total Spent`) as total_revenue
 from world.retail_store_sales_cleaned; 

-- Top 5 Products by Revenue
select Category, sum(`Total Spent`) as total_revenue
from  world.retail_store_sales_cleaned
group by Category
order by total_revenue desc
limit 5;

-- Find which product sold the most units.
select Category, sum(Quantity) as total_count_of_quantity
from world.retail_store_sales_cleaned
group by Category
order by total_count_of_quantity desc
limit 1;

-- Monthly Sales Trend
select DATE_FORMAT(`Transaction Date`, '%Y-%m') AS month, sum(`Total Spent`) as revenue
from world.retail_store_sales_cleaned
group by month
order by month;

-- Top Customers (3 customers)
select `Customer ID`, sum(quantity) as quantity_buy
from world.retail_store_sales_cleaned
group by `Customer ID` 
order by Quantity_buy desc
limit 3;

-- online and in store total revenue
select Location , sum(`Total Spent`) as revenue 
from world.retail_store_sales_cleaned
group by Location;

-- total transaction through various payment methods
select `Payment Method` , sum(`Total Spent`) as revenue 
from world.retail_store_sales_cleaned
group by `Payment Method`;

-- Find average value per order.
SELECT AVG(`Total Spent`) AS avg_order_value
FROM world.retail_store_sales_cleaned;

-- high Value Orders Show orders where: total spent > average order value
SELECT *
FROM world.retail_store_sales_cleaned
WHERE `Total Spent` > (
    SELECT AVG(`Total Spent`)
    FROM world.retail_store_sales_cleaned
);

