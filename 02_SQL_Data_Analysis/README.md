# SQL Data Analysis Projects

This folder contains SQL data analysis projects demonstrating database design, ETL, and analysis skills.

---

## 1️⃣ Customer_Feedback_DB

- **Content:**  
  [`customer_feedback_db.sql`](Customer_Feedback_DB/customer_feedback_db.sql)

- **Description:**  
  SQL Server database for customer feedback analysis. Includes table design, staging tables, views, and a stored procedure for CSV import.

- **Skills:**  
  - SQL Server table design (Primary / Foreign Keys)  
  - Database Design & ERD (Lucidchart)  
  - Aggregation (`AVG`, `COUNT`), `GROUP BY`, `TOP N`  
  - `CASE` for sentiment classification  
  - Stored procedure & ETL automation  

- **How to run:**  
  Open in **SQL Server Management Studio (SSMS)** and execute the script.

- **See also:**  
  - 📄 [`Customer_Feedback_DB/README.md`](Customer_Feedback_DB/README.md)  
  - 🧩 ERD & diagrams: [`Customer_Feedback_DB/docs/`](Customer_Feedback_DB/docs/)

---

## 2️⃣ Data_Parsing_Analysis

- **Content:**  
  [`data_parsing_analysis.py`](Data_Parsing_Analysis/data_parsing_analysis.py)

- **Description:**  
  Python script that parses CSV / JSON / XML customer feedback, loads data into SQLite staging tables, and performs analysis (top customers, keywords, trends).

- **Skills:**  
  - Python data parsing & cleaning  
  - SQLite database operations  
  - SQL queries (`UNION ALL`, aggregation, sorting)  
  - Basic data analysis and insights  

- **How to run:**  
  ```bash
  python data_parsing_analysis.py

  
**See also:**
-  📄 data_parsing_analysis/README.md

-  📊 Analysis report and screenshots in the same folder

