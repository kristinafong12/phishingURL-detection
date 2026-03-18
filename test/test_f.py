from src.feature_extraction import extract_features

def test_feature_extraction():
    url = "http://example-login.com"
    features = extract_features(url)

    assert features['url_length'] > 0
    assert isinstance(features['has_ip'], int)
