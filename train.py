import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

data = pd.read_csv("transactions.csv")

features = [
    "transaction_amount",
    "hour",
    "account_age_days",
    "transactions_last_24h",
    "device_changes",
    "country_mismatch",
    "failed_attempts"
]

X = data[features]
y = data["is_risky"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=150,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Model Accuracy:", accuracy_score(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions))

joblib.dump(model, "risk_model.pkl")

print("\nModel saved successfully!")