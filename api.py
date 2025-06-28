from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("fare_predictor.pkl")

# Initialize FastAPI app
app = FastAPI()

# Define input schema using Pydantic
class RideInput(BaseModel):
    VendorID: int
    passenger_count: int
    RatecodeID: int
    payment_type: int
    extra: float
    tip_amount: float
    tolls_amount: float
    Airport_fee: float
    cbd_congestion_fee: float
    date: int
    hour: int
    day: str
    mean_distance: float
    PUborough: str
    DOborough: str

# Define the /predict endpoint
@app.post("/predict")
def predict_fare(ride: RideInput):
    # Convert input to DataFrame
    input_df = pd.DataFrame([ride.dict()])
    
    # Make prediction
    prediction = model.predict(input_df)[0]
    
    # Return result
    return {"predicted_fare": round(prediction, 2)}
