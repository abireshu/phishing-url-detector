import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Loading  dataset
data = pd.read_csv('Datasets\Dataset.csv')

# List of numeric/categorical columns to use as features

numeric_features = [
    'URLLength',
    'NoOfSubDomain',
    'IsDomainIP',
    'IsHTTPS',
    'NoOfOtherSpecialCharsInURL',
    'NoOfQMarkInURL',
    'ObfuscationRatio'

]

X = data[numeric_features]
y = data['label']

# Checking for missing values and fill if needed
print(X.isnull().sum())
X = X.fillna(0)

# Spliting data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training model
model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, 'Trained_model.pkl')  

# Optional: Save meta data for test set
'''meta_cols = data[['FILENAME', 'URL']]
_, meta_test, _, _ = train_test_split(meta_cols, y, test_size=0.2, random_state=42)
results = pd.DataFrame({
    'FILENAME': meta_test['FILENAME'],
    'URL': meta_test['URL'],
    'Prediction': y_pred
})
results.to_csv('prediction.csv', index=False)'''