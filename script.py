from src.model import train_model
from src.predictor import predict_url

# Sample dataset
data = [
    ("http://secure-login-paypal.com", 1),
    ("https://google.com", 0),
    ("http://192.168.0.1/login", 1),
    ("https://github.com", 0),
    ("http://verify-account-bank.com", 1)
]

# Train model
model = train_model(data)

# Test URLs
test_urls = [
    "http://paypal-login-security.com",
    "https://openai.com",
    "http://192.168.1.1/verify"
]

print("\n=== Phishing Detection Results ===")
for url in test_urls:
    result = predict_url(model, url)
    print(f"{url} -> {result}")
