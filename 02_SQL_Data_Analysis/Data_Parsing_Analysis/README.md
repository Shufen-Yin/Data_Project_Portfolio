# Data Parsing & Analysis
> Parse CSV/JSON/XML customer feedback, clean, load into SQLite, and perform basic analysis.

---

## Overview
 Parse and validate CSV / JSON / XML data  
- Load into SQLite staging tables  
- Analyze:
  - Top customers by average rating  
  - Key complaint keywords  
  - Monthly rating trends  

> **Note:** `error_log.txt` is created every time the script runs, even if there are no errors.

---

## Project Structure
```
├── data/
│   ├── customer_survey.csv
│   ├── web_feedback.json
│   └── external_reviews.xml
├── data_parsing_analysis.py
├── README.md
├── error_log.txt   # created automatically

```
---

## Quick Start

```bash
-  git clone https://github.com/Shufen-Yin/Data_Project_Portfolio.git
-  cd 02_SQL_Data_Analysis
-  python data_parsing_analysis.py
```

**Example Analysis**

**Top Customers:**
```
customer_id | avg_rating | reviews
1           | 5.0        | 3
2           | 4.0        | 3
3           | 2.33       | 3
```

Keyword Counts: 
damaged: 2, late: 3, defective: 1

Monthly Rating Trend: 
2025-01: 4.2 (10), 2025-02: 3.8 (8)

**Tech Highlights**

Python, CSV/JSON/XML parsing, data validation, SQLite, basic analysis



