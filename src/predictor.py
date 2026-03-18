import pandas as pd
from src.feature_extraction import extract_features

def predict_url(model, url):
    features = extract_features(url)
    df = pd.DataFrame([features])

    prediction = model.predict(df)[0]
    return "⚠️ Phishing" if prediction == 1 else "✅ Safe"
