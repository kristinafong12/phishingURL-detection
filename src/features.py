
---

# 🧠 3. `src/features.py`

```python
import re
import tldextract

def extract_features(url):
    features = {}

    # URL length
    features['url_length'] = len(url)

    # IP address in URL
    features['has_ip'] = int(bool(re.search(r'\d+\.\d+\.\d+\.\d+', url)))

    # Suspicious keywords
    suspicious_words = ['login', 'verify', 'secure', 'account', 'update']
    features['suspicious_words'] = sum(word in url.lower() for word in suspicious_words)

    # Dot count
    features['dot_count'] = url.count('.')

    # Hyphen in domain
    ext = tldextract.extract(url)
    features['has_hyphen'] = int('-' in ext.domain)

    return features
