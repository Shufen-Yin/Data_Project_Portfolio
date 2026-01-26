# SQL Data Analysis Projects

This folder contains two SQL data analysis projects, demonstrating database design, ETL, and analysis skills.

---

## 1️ Customer_Feedback_DB

- **Content:** `Customer_Feedback_DB.sql`  
- **Description:** SQL Server database for customer feedback. Creates tables, staging tables, views, and a stored procedure for CSV import.  
- **Skills:** 
  - SQL Server table design with primary/foreign keys  
  - Aggregation (AVG, COUNT), GROUP BY, TOP N  
  - CASE for sentiment classification  
  - Stored procedure and ETL automation  
- **How to run:** Open in SQL Server Management Studio (SSMS) and execute the script.  
- **See also:** `Customer_Feedback_DB/README.md` for details and screenshots.

---

## 2️ data_parsing_analysis

- **Content:** `data_parsing_analysis.py`  
- **Description:** Python script to parse CSV/JSON/XML customer feedback, load into SQLite staging tables, and perform analysis (top customers, keywords, monthly trends).  
- **Skills:** 
  - Python data parsing & cleaning  
  - SQLite database operations  
  - SQL queries with UNION ALL, aggregation, and sorting  
  - Basic data analysis and insight  
- **How to run:**  
```bash
python data_parsing_analysis.py

See also: `data_parsing_analysis/README.md` and report for screenshots and examples.

