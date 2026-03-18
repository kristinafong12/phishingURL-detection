import pandas as pd
from sklearn.linear_model import LogisticRegression
from src.feature_extraction import extract_features

def train_model(data):
    rows = []

    for url, label in data:
        features = extract_features(url)
        features['label'] = label
        rows.append(features)

    df = pd.DataFrame(rows)

    X = df.drop(columns=['label'])
    y = df['label']

    model = LogisticRegression()
    model.fit(X, y)

    return model
