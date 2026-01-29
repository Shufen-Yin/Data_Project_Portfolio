"""
API / NLP Extension Demo
Purpose: Optional project to demonstrate NLP, keyword extraction, and simulated API usage
"""

import sqlite3
import pandas as pd

from textblob import TextBlob
from collections import Counter
import matplotlib.pyplot as plt

# -------- Connect to database --------
db_path = "ecommerce_feedback.db"
conn = sqlite3.connect(db_path)


# -------- Load staging table --------
table_name = "staging_feedback"  # Replace with actual table name
df = pd.read_sql(f"SELECT * FROM {table_name};", conn)
print("Tables in database:\n", pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn))
print("\nData preview:\n", df.head())

# -------- Sentiment Analysis --------
if 'comments' in df.columns:
    df['sentiment'] = df['comments'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
    print("\nSentiment preview:\n", df[['comments', 'sentiment']].head())

    avg_sentiment = df['sentiment'].mean()
    print(f"\nAverage sentiment: {avg_sentiment:.2f}")

    # Histogram
    plt.hist(df['sentiment'], bins=10, color='skyblue', edgecolor='black')
    plt.title("Comments Sentiment Distribution")
    plt.xlabel("Sentiment Polarity")
    plt.ylabel("Count")
    plt.savefig("example_output.png")
    plt.show()
else:
    print("\nNo 'comments' column found for sentiment analysis.")

# -------- Keyword Extraction --------
def extract_keywords(text_series, top_n=10):
    words = " ".join(str(x).lower() for x in text_series if x).split()
    stopwords = {'the', 'and', 'a', 'an', 'of', 'to', 'in', 'for', 'is', 'it', 'on', 'this', 'that'}
    filtered_words = [w.strip(".,!?") for w in words if w not in stopwords]
    return Counter(filtered_words).most_common(top_n)

if 'comments' in df.columns:
    top_keywords = extract_keywords(df['comments'])
    print("\nTop Keywords:\n", top_keywords)

# -------- Simulated API Call --------
def simulated_api_call(comment):
    sentiment = TextBlob(str(comment)).sentiment.polarity
    return {"comment": comment, "sentiment_score": sentiment, "status": "processed"}

if 'comments' in df.columns:
    api_results = df['comments'].apply(simulated_api_call)
    print("\nSimulated API results preview:\n", api_results.head(5))

# -------- Close connection --------
conn.close()
