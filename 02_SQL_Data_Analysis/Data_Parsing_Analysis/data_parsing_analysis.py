"""
Data Parsing & Analysis
Author: Shufen Yin
Description:
Parse CSV, JSON, and XML customer feedback files, validate data, load into SQLite staging tables,
and perform basic analysis including top customers, complaint keywords, sentiment classification, and monthly rating trends.
"""
import os
import csv
import json
import sqlite3
import xml.etree.ElementTree as ET
from datetime import datetime

# paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

CSV_FILE = os.path.join(DATA_DIR, "customer_survey.csv")
JSON_FILE = os.path.join(DATA_DIR, "web_feedback.json")
XML_FILE = os.path.join(DATA_DIR, "external_reviews.xml")

DB_PATH = os.path.join(BASE_DIR, "ecommerce_feedback.db")
ERROR_LOG_FILE = os.path.join(BASE_DIR, "error_log.txt")


def log_error(source, record_id, message):
    with open(ERROR_LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{source}] Record {record_id}: {message}\n")


def validate_date(date_str):
    if not date_str or not date_str.strip():
        return None
    for fmt in ("%Y-%m-%d", "%d-%m-%Y"):
        try:
            return datetime.strptime(date_str.strip(), fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    raise ValueError(f"Invalid date format: {date_str}")


def create_tables(cursor):
    cursor.executescript("""
    DROP TABLE IF EXISTS survey_staging;
    DROP TABLE IF EXISTS web_staging;
    DROP TABLE IF EXISTS external_staging;

    CREATE TABLE survey_staging (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id TEXT,
        rating INTEGER,
        comments TEXT,
        review_date TEXT
    );

    CREATE TABLE web_staging (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id TEXT,
        rating INTEGER,
        comments TEXT,
        review_date TEXT
    );

    CREATE TABLE external_staging (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id TEXT,
        rating INTEGER,
        comments TEXT,
        review_date TEXT
    );
    """)


def parse_csv(file_path, cursor):
    with open(file_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, start=1):
            try:
                customer_id = row.get("customer_id")
                rating = int(row.get("rating", 0))
                comments = row.get("comments", "")
                review_date = row.get("review_date", "")

                if not customer_id or rating not in range(1, 6):
                    raise ValueError("Missing or invalid customer_id / rating")

                parsed_date = validate_date(review_date)

                cursor.execute(
                    "INSERT INTO survey_staging (customer_id, rating, comments, review_date) VALUES (?, ?, ?, ?)",
                    (customer_id, rating, comments, parsed_date)
                )
            except Exception as e:
                log_error("CSV", i, str(e))


def parse_json(file_path, cursor):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for i, record in enumerate(data, start=1):
        try:
            customer_id = record.get("customer_id")
            rating = int(record.get("rating", 0))
            comments = record.get("comments", "")
            review_date = record.get("review_date", "")

            if not customer_id or rating not in range(1, 6):
                raise ValueError("Missing or invalid customer_id / rating")

            parsed_date = validate_date(review_date)

            cursor.execute(
                "INSERT INTO web_staging (customer_id, rating, comments, review_date) VALUES (?, ?, ?, ?)",
                (customer_id, rating, comments, parsed_date)
            )
        except Exception as e:
            log_error("JSON", i, str(e))


def parse_xml(file_path, cursor):
    tree = ET.parse(file_path)
    root = tree.getroot()

    for i, review in enumerate(root.findall("review"), start=1):
        try:
            customer_id = review.findtext("customer_id")
            rating = int(review.findtext("rating", "0"))
            comments = review.findtext("comments", "")
            review_date = review.findtext("review_date", "")

            if not customer_id or rating not in range(1, 6):
                raise ValueError("Missing or invalid customer_id / rating")

            parsed_date = validate_date(review_date)

            cursor.execute(
                "INSERT INTO external_staging (customer_id, rating, comments, review_date) VALUES (?, ?, ?, ?)",
                (customer_id, rating, comments, parsed_date)
            )
        except Exception as e:
            log_error("XML", i, str(e))


def run_analysis(cursor):
    print("\nTop customers by average rating")
    cursor.execute("""
        SELECT customer_id, AVG(rating) AS avg_rating, COUNT(*) AS reviews
        FROM (
            SELECT * FROM survey_staging
            UNION ALL
            SELECT * FROM web_staging
            UNION ALL
            SELECT * FROM external_staging
        )
        GROUP BY customer_id
        ORDER BY avg_rating DESC
        LIMIT 5;
    """)
    for row in cursor.fetchall():
        print(row)

    print("\nKeyword frequency")
    keywords = ["damaged", "late", "defective"]
    for kw in keywords:
        cursor.execute("""
            SELECT COUNT(*) FROM (
                SELECT comments FROM survey_staging
                UNION ALL
                SELECT comments FROM web_staging
                UNION ALL
                SELECT comments FROM external_staging
            ) WHERE comments LIKE ?;
        """, (f"%{kw}%",))
        print(f"{kw}: {cursor.fetchone()[0]}")

    print("\nMonthly rating trend")
    cursor.execute("""
        SELECT substr(review_date, 1, 7) AS month, AVG(rating), COUNT(*)
        FROM (
            SELECT * FROM survey_staging
            UNION ALL
            SELECT * FROM web_staging
            UNION ALL
            SELECT * FROM external_staging
        )
        WHERE review_date IS NOT NULL
        GROUP BY month
        ORDER BY month;
    """)
    for row in cursor.fetchall():
        print(row)


def main():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    create_tables(cur)

    parse_csv(CSV_FILE, cur)
    parse_json(JSON_FILE, cur)
    parse_xml(XML_FILE, cur)

    conn.commit()

    print("Data parsing completed")
    run_analysis(cur)

    conn.close()
    print("\nAll done")


if __name__ == "__main__":
    main()
