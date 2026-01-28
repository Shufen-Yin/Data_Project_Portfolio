# Data Parsing & Analysis

Parse CSV/JSON/XML customer feedback, clean, load into SQLite, and perform basic analysis.

---

## Overview
 Parse and validate CSV / JSON / XML data  
- Load into SQLite staging tables  
- Analyze:
  - Top customers by average rating  
  - Key complaint keywords  
  - Monthly rating trends  

>**Note:** `error_log.txt` is created every time the script runs, even if there are no errors.

---

## Project Structure
```
├── data/
│   ├── customer_survey.csv
│   ├── web_feedback.json
│   └── external_reviews.xml
├── data_parsing_analysis.py
├── README.md
├── output.png
├── error_log.txt   # created automatically

```
---

## Quick Start

-  git clone https://github.com/Shufen-Yin/Data_Project_Portfolio.git
-  cd 02_SQL_Data_Analysis
-  python data_parsing_analysis.py


**Example Analysis**

**Top Customers:**
```
customer_id | avg_rating | reviews
1           | 5.0        | 3
2           | 4.0        | 3
3           | 2.33       | 3
```

**Keyword Frequency**

- damaged: 0  
- late: 2  
- defective: 0  

**Monthly Rating Trend**

2024-01: avg_rating = 4.0, reviews = 3

**Tech Highlights**

Python, CSV/JSON/XML parsing, data validation, SQLite, basic analysis



