"""FastAPI inference server for churn prediction"""
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

# Load model
with open('models/churn_model.pkl', 'rb') as f:
    model = pickle.load(f)

class CustomerData(BaseModel):
    age: int
    tenure_months: int
    monthly_charges: float
    total_charges: float
    num_support_calls: int

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict")
def predict(data: CustomerData):
    features = np.array([[
        data.age,
        data.tenure_months,
        data.monthly_charges,
        data.total_charges,
        data.num_support_calls
    ]])
    
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]
    
    return {
        "churn": int(prediction),
        "churn_probability": float(probability)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)