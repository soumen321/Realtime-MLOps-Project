"""Generate synthetic churn dataset"""
import pandas as pd
import numpy as np

np.random.seed(42)

# Generate 1000 samples
n_samples = 1000

data = {
    'customer_id': range(1, n_samples + 1),
    'age': np.random.randint(18, 70, n_samples),
    'tenure_months': np.random.randint(1, 72, n_samples),
    'monthly_charges': np.random.uniform(20, 120, n_samples),
    'total_charges': np.random.uniform(100, 8000, n_samples),
    'num_support_calls': np.random.randint(0, 10, n_samples),
}

# Simple churn logic: higher charges + more support calls = more churn
churn_prob = (
    (data['monthly_charges'] / 120) * 0.3 +
    (data['num_support_calls'] / 10) * 0.4 +
    (1 - data['tenure_months'] / 72) * 0.3
)
data['churn'] = (np.random.random(n_samples) < churn_prob).astype(int)

df = pd.DataFrame(data)
df.to_csv('data/churn_data.csv', index=False)
print(f"Generated {len(df)} samples")
print(f"Churn rate: {df['churn'].mean():.2%}")