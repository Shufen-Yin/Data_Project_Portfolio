-- SQL Data Analyst Portfolio – Customer Feedback DB
-- Fully corrected for SQL Server

-- 1. Drop database if exists and create new one
IF EXISTS (SELECT * FROM sys.databases WHERE name = 'SQL_Data_Analyst')
BEGIN
    PRINT 'Database exists, dropping it...';
    DROP DATABASE SQL_Data_Analyst;
END;
GO

PRINT 'Creating database SQL_Data_Analyst...';
CREATE DATABASE SQL_Data_Analyst;
GO

USE SQL_Data_Analyst;
GO

-- 2. Create main tables if not exists

-- Customers table
IF OBJECT_ID('Customers', 'U') IS NULL
BEGIN
    CREATE TABLE Customers (
        customer_id INT PRIMARY KEY,
        name NVARCHAR(100),
        email NVARCHAR(100),
        region NVARCHAR(50)
    );
    PRINT 'Customers table created.';
END;
GO

-- Products table
IF OBJECT_ID('Products', 'U') IS NULL
BEGIN
    CREATE TABLE Products (
        product_id INT PRIMARY KEY,
        name NVARCHAR(100),
        category NVARCHAR(50),
        price DECIMAL(10,2)
    );
    PRINT 'Products table created.';
END;
GO

-- Reviews table
IF OBJECT_ID('Reviews', 'U') IS NULL
BEGIN
    CREATE TABLE Reviews (
        review_id INT PRIMARY KEY,
        customer_id INT,
        product_id INT,
        rating INT CHECK (rating BETWEEN 1 AND 5),
        comments NVARCHAR(MAX),
        review_date DATE,
        FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
        FOREIGN KEY (product_id) REFERENCES Products(product_id)
    );
    PRINT 'Reviews table created.';
END;
GO

-- 3. Create staging tables for CSV / JSON / XML imports

IF OBJECT_ID('Staging_CustomerSurvey', 'U') IS NULL
BEGIN
    CREATE TABLE Staging_CustomerSurvey (
        review_id INT,
        customer_id INT,
        product_id INT,
        rating INT,
        comments NVARCHAR(MAX),
        review_date NVARCHAR(20)
    );
    PRINT 'Staging_CustomerSurvey table created.';
END;
GO

IF OBJECT_ID('Staging_WebFeedback', 'U') IS NULL
BEGIN
    CREATE TABLE Staging_WebFeedback (
        review_id INT,
        customer_id INT,
        product_id INT,
        rating INT,
        comments NVARCHAR(MAX),
        review_date NVARCHAR(20)
    );
    PRINT 'Staging_WebFeedback table created.';
END;
GO

IF OBJECT_ID('Staging_ExternalReviews', 'U') IS NULL
BEGIN
    CREATE TABLE Staging_ExternalReviews (
        review_id INT,
        customer_id INT,
        product_id INT,
        rating INT,
        comments NVARCHAR(MAX),
        review_date NVARCHAR(20)
    );
    PRINT 'Staging_ExternalReviews table created.';
END;
GO

-- 4. Create views

-- Drop views if exist
IF OBJECT_ID('vw_ProductReviews', 'V') IS NOT NULL
    DROP VIEW vw_ProductReviews;
GO

CREATE VIEW vw_ProductReviews AS
SELECT 
    p.product_id,
    p.name AS product_name,
    p.category,
    AVG(r.rating) AS avg_rating,
    COUNT(r.review_id) AS total_reviews
FROM Products p
LEFT JOIN Reviews r ON p.product_id = r.product_id
GROUP BY p.product_id, p.name, p.category;
GO

IF OBJECT_ID('vw_TopProducts', 'V') IS NOT NULL
    DROP VIEW vw_TopProducts;
GO

CREATE VIEW vw_TopProducts AS
SELECT TOP 10 *
FROM vw_ProductReviews
ORDER BY avg_rating DESC, total_reviews DESC;
GO

-- 5. Example analysis queries

PRINT 'Top 10 Products:';
SELECT * FROM vw_TopProducts;
GO

PRINT 'Common Complaints by Category:';
SELECT 
    p.category,
    SUM(CASE WHEN r.comments LIKE '%damaged%' THEN 1 ELSE 0 END) AS Damaged,
    SUM(CASE WHEN r.comments LIKE '%late%' THEN 1 ELSE 0 END) AS Late,
    SUM(CASE WHEN r.comments LIKE '%defective%' THEN 1 ELSE 0 END) AS Defective
FROM Reviews r
JOIN Products p ON r.product_id = p.product_id
GROUP BY p.category;
GO

PRINT 'Customer Sentiment:';
SELECT 
    review_id, product_id, rating, comments,
    CASE 
        WHEN rating >= 4 THEN 'Positive'
        WHEN rating = 3 THEN 'Neutral'
        ELSE 'Negative'
    END AS sentiment
FROM Reviews;
GO

PRINT 'Trend Analysis by Month:';
SELECT 
    FORMAT(review_date, 'yyyy-MM') AS Month,
    COUNT(*) AS ReviewCount,
    AVG(rating) AS AvgRating
FROM Reviews
GROUP BY FORMAT(review_date, 'yyyy-MM')
ORDER BY Month;
GO

-- 6. Stored procedure example for CSV import

IF OBJECT_ID('ImportCustomerSurvey', 'P') IS NOT NULL
    DROP PROCEDURE ImportCustomerSurvey;
GO

CREATE PROCEDURE ImportCustomerSurvey
    @FilePath NVARCHAR(200)
AS
BEGIN
    DECLARE @sql NVARCHAR(MAX);
    SET @sql = N'
        BULK INSERT Staging_CustomerSurvey
        FROM ''' + @FilePath + '''
        WITH (
            FIRSTROW = 2,
            FIELDTERMINATOR = '','',
            ROWTERMINATOR = ''\n'',
            CODEPAGE = ''65001''
        );';
    EXEC sp_executesql @sql;

    INSERT INTO Reviews (review_id, customer_id, product_id, rating, comments, review_date)
    SELECT review_id, customer_id, product_id, rating, comments, CAST(review_date AS DATE)
    FROM Staging_CustomerSurvey;
END;
GO

PRINT 'Stored procedure ImportCustomerSurvey created successfully.';
GO
