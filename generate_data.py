import pandas as pd
import numpy as np

np.random.seed(42)

n = 3000

data = pd.DataFrame({
    "transaction_amount": np.random.exponential(3000, n).round(2),
    "hour": np.random.randint(0, 24, n),
    "account_age_days": np.random.randint(10, 2000, n),
    "transactions_last_24h": np.random.randint(1, 30, n),
    "device_changes": np.random.randint(0, 5, n),
    "country_mismatch": np.random.randint(0, 2, n),
    "failed_attempts": np.random.randint(0, 6, n)
})

risk_score = (
    (data["transaction_amount"] > 10000) * 2 +
    (data["hour"].isin([0, 1, 2, 3, 4])) * 2 +
    (data["transactions_last_24h"] > 15) * 2 +
    (data["device_changes"] >= 2) * 2 +
    (data["country_mismatch"] == 1) * 2 +
    (data["failed_attempts"] >= 3) * 2
)

data["is_risky"] = (risk_score >= 4).astype(int)

data.to_csv("transactions.csv", index=False)

print("Dataset created successfully!")
print("Rows:", len(data))
print(data.head())