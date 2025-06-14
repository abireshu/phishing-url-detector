from feature_extraction import extract_features
import pandas as pd
import joblib


# List of URLs to predict
urls = [
    # Legitimate URLs
    'https://www.google.com',
    'https://www.amazon.com',
    'https://www.microsoft.com',
    'https://www.linkedin.com',
    'https://www.github.com',

    # Phishing or suspicious URLs (examples based on common phishing patterns)
   'http://netflix.verify-account-membership.com',   
   'http://facebook-login.secure-auth.info',
   'http://paypal.verify-account-login.com/login.html',
   'http://sbi-bank-secure-login.com/update',       
   'http://googl.e-login.securepage123.com' 

]

# Extracting features for each URL
feature_list = [extract_features(url) for url in urls]

# Converting list of dicts to DataFrame
new_X = pd.DataFrame(feature_list)

# Loading trained model
model = joblib.load('Trained_model.pkl')

# Prediction
predictions = model.predict(new_X)

for url, pred in zip(urls, predictions):
    print(f"URL: {url} -> Prediction: {'Phishing' if pred == 0 else 'Legitimate'}")
