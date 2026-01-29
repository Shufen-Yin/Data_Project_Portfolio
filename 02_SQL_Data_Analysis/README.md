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

## 2. Data Parsing & ETL Analysis (Python + SQL)

**Multi-Format Data Parsing and SQL-Based Analysis Pipeline**

- **Core File:**
   [ data_parsing_analysis.py](Data_Parsing_Analysis/data_parsing_analysis.py)
---

### Project Overview
Designed and implemented a Python-based ETL pipeline to ingest customer feedback data from multiple source formats (CSV, JSON, XML), normalize and load the data into SQLite staging tables, and perform analytical SQL queries to generate business insights.  
The pipeline is designed to be easily extended to additional data sources or production databases.

---

### Key Features
- Parsed and standardized heterogeneous data formats into a unified schema  
- Implemented staging tables to support structured analysis  
- Combined Python processing with SQL analytics for flexible querying  
- Automated end-to-end execution via a single Python script  

---

### Key Skills & Techniques
- Data parsing and transformation (CSV, JSON, XML)  
- ETL pipeline design and automation  
- SQLite database operations and schema management  
- SQL analytics using aggregation, `UNION ALL`, and ordering  
- Insight extraction (top customers, keyword frequency, trend analysis)  

---

### How to Run
```bash
python data_parsing_analysis.py
```
- **Project Assets:**  
  - [Project README](Data_Parsing_Analysis/README.md)  
  - [Outputs](Data_Parsing_Analysis/Outputs/)

**What This Project Demonstrates**

-  End-to-end data workflows: raw data → staging → analysis → insights

-  Practical ETL and SQL skills applicable to analytics and data engineering roles

-  Integration of Python and SQL for scalable data pipelines

-  Clear documentation and reproducible results

-  A foundation that can be extended to API-based ingestion or basic NLP text analysis
