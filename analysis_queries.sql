-- ---------------------------------------------------------
-- Sales Data Analysis Queries
-- These queries are designed to run on the cleaned_sales_data table.
-- ---------------------------------------------------------

-- 1. Total Revenue and Order Count
-- Get the high-level metrics of the entire dataset
SELECT 
    COUNT(DISTINCT OrderID) AS TotalOrders,
    SUM(Quantity) AS TotalItemsSold,
    SUM(TotalRevenue) AS TotalRevenue
FROM 
    cleaned_sales_data;


-- 2. Monthly Sales Trend
-- Analyze how sales perform month over month
SELECT 
    YearMonth,
    COUNT(DISTINCT OrderID) AS NumberOfOrders,
    SUM(TotalRevenue) AS MonthlyRevenue
FROM 
    cleaned_sales_data
GROUP BY 
    YearMonth
ORDER BY 
    YearMonth ASC;


-- 3. Top-Selling Categories by Revenue
-- Identify which product categories drive the most revenue
SELECT 
    Category,
    SUM(Quantity) AS ItemsSold,
    SUM(TotalRevenue) AS CategoryRevenue
FROM 
    cleaned_sales_data
GROUP BY 
    Category
ORDER BY 
    CategoryRevenue DESC;


-- 4. Top 10 Best-Selling Products
-- Drill down into specific products that are popular
SELECT 
    Product,
    Category,
    SUM(Quantity) AS TotalQuantitySold,
    SUM(TotalRevenue) AS TotalRevenue
FROM 
    cleaned_sales_data
GROUP BY 
    Product, Category
ORDER BY 
    TotalRevenue DESC
LIMIT 10;


-- 5. Customer Lifetime Value (Top 10 Customers)
-- Identify our most valuable customers based on total spend
SELECT 
    CustomerID,
    COUNT(DISTINCT OrderID) AS TotalOrders,
    SUM(TotalRevenue) AS TotalSpend,
    AVG(TotalRevenue) AS AverageOrderValue
FROM 
    cleaned_sales_data
GROUP BY 
    CustomerID
ORDER BY 
    TotalSpend DESC
LIMIT 10;


-- 6. Average Basket Size and Value
-- Understand the typical customer purchase
SELECT 
    AVG(ItemsPerOrder) AS AverageBasketSize,
    AVG(RevenuePerOrder) AS AverageOrderValue
FROM (
    SELECT 
        OrderID,
        SUM(Quantity) AS ItemsPerOrder,
        SUM(TotalRevenue) AS RevenuePerOrder
    FROM 
        cleaned_sales_data
    GROUP BY 
        OrderID
) AS OrderSummary;
