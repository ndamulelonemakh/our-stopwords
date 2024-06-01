"""
This script demonstrates how to use the stop words provided in this repo(https://github.com/ndamulelonemakh/our-stopwords) in a model training script.

Prerequisites:
- Python 3.x
- pandas
- scikit-learn

To install the required packages, run:
    pip install pandas scikit-learn

Usage:
    python training_example.py

Author:
    Ndamulelo Nemakhavhani
    2024.06.01
"""

import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# Run the following command on Powershell or Bash to download the stop words JSON lines file from GitHub:
# curl -O https://raw.githubusercontent.com/ndamulelonemakh/our-stopwords/main/za_stopwords.main.jsonl
# Alternatively, you can download it manually

# Load stop words from JSON lines file
stop_words = []
with open('za_stopwords.main.jsonl', 'r', encoding='utf-8') as file:
    for line in file:
        stop_words.append(json.loads(line.strip()))

# Extract Xhosa stop words
xho_stop_words = [word['xho'] for word in stop_words]
print(f'Number of Xhosa stop words: {len(xho_stop_words)}')
print(f'First 10 Xhosa stop words: {xho_stop_words[:10]}')

# Load the dataset from Masakhane news
df = pd.read_csv('https://raw.githubusercontent.com/masakhane-io/masakhane-news/main/data/xho/train.tsv', sep='\t')
text_column = 'text'
labels_column = 'category'

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[text_column], 
                                                    df[labels_column], 
                                                    test_size=0.2, 
                                                    stratify=df[labels_column], 
                                                    random_state=42)

# Create a TFIDF vectorizer
vectorizer = TfidfVectorizer(stop_words=xho_stop_words, 
                             lowercase=True,
                             strip_accents='unicode',
                             max_features=5000)

# Fit and transform the training data
X_train_tfidf = vectorizer.fit_transform(X_train)

# Transform the testing data
X_test_tfidf = vectorizer.transform(X_test)

# Initialize and train the Logistic Regression model for News categorization
model = LogisticRegression(verbose=1)
model.fit(X_train_tfidf, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test_tfidf)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f'Test Accuracy: {accuracy * 100:.2f}%')
