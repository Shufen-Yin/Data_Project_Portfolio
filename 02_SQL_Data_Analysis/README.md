# SQL Data Analysis Projects  
Professional Data Analyst Portfolio

This section showcases end-to-end SQL and Python data analysis projects, covering database design, ETL pipelines, and analytical insights derived from structured and semi-structured data.

---

## 1. Customer_Feedback_DB  
Relational Database Design & SQL Analysis

- **Core File:**  
  [customer_feedback_db.sql](Customer_Feedback_DB/customer_feedback_db.sql)

- **Project Overview:**  
  Designed and implemented a SQL Server database to analyze customer feedback data.  
  Demonstrates normalized table design, ETL via staging tables, and analytical queries for customer sentiment and performance insights.

- **Key Skills & Techniques:**  
  - Relational database design (PK / FK, normalization)  
  - ERD modeling (Lucidchart)  
  - SQL aggregation (AVG, COUNT), GROUP BY, TOP N  
  - Conditional logic using CASE for sentiment classification  
  - Stored procedures for automated CSV import (ETL)

- **How to Run:**  
  Execute the script in SQL Server Management Studio (SSMS).

- **Project Assets:**  
  - [Project README](Customer_Feedback_DB/README.md)  
  - [ERD and diagrams](Customer_Feedback_DB/docs/)

---

## 2. Data_Parsing_Analysis  
Multi-Format Data Parsing and SQL Analysis with Python

- **Core File:**  
  [data_parsing_analysis.py](Data_Parsing_Analysis/data_parsing_analysis.py)

- **Project Overview:**  
  Built a Python-based ETL workflow to parse customer feedback data from CSV, JSON, and XML formats, load it into SQLite staging tables, and perform analytical SQL queries to extract insights.

- **Key Skills & Techniques:**  
  - Python data parsing and cleaning  
  - SQLite database operations  
  - SQL analysis using UNION ALL, aggregation, and sorting  
  - Insight generation (top customers, keyword frequency, trends)

- **How to Run:**  
  ```bash
  python data_parsing_analysis.py

Project Assets:
**Project Assets:**
- [Project README](Data_Parsing_Analysis/README.md)
- [Sample output](Data_Parsing_Analysis/output.png)

 **What This Section Demonstrates**

-  End-to-end data workflows: raw data to staging to analysis to insights
-  Practical SQL skills used in real-world analyst roles
-  Integration of Python and SQL for flexible data pipelines
-  Clear documentation and reproducible analysis
