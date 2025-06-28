import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# Page settings
st.set_page_config(page_title="Taxi Fare Predictor", page_icon="🚖", layout="centered")
st.markdown("""
    <h1 style='text-align: center; color: green;'>🚕 Yellow Cab Fare Predictor (NYC)</h1>
    <p style='text-align: center;'>Enter ride details to estimate the fare.</p>
    <hr>
""", unsafe_allow_html=True)

# Inputs
col1, col2 = st.columns(2)

with col1:
    VendorID = st.selectbox("🏢 Vendor", [1, 2, 6, 7],
        format_func=lambda x: ["Creative Mobile Technologies, LLC",
                               "Curb Mobility, LLC", "Myle Technologies Inc", "Helix"][[1, 2, 6, 7].index(x)])

    RatecodeID = st.selectbox("💳 Ratecode", [1, 2, 3, 4, 5, 6, 99],
        format_func=lambda x: ['Standard rate', 'JFK', 'Newark',
                               'Nassau or Westchester', 'Negotiated fare',
                               'Group ride', 'Null/unknown'][[1, 2, 3, 4, 5, 6, 99].index(x)])

    payment_type = st.selectbox("💸 Payment Type", [1, 2],
        format_func=lambda x: ['Credit card', 'Cash'][[1, 2].index(x)])

    passenger_count = st.number_input("👥 Passenger Count", min_value=1, max_value=6, value=1)

with col2:
    PUborough = st.selectbox("📍 Pickup Borough", ['Manhattan', 'Brooklyn', 'Queens', 'Bronx', 'Staten Island', 'EWR'])
    DOborough = st.selectbox("📍 Dropoff Borough", ['Manhattan', 'Brooklyn', 'Queens', 'Bronx', 'Staten Island', 'EWR'])
    trip_distance = st.number_input("🌍 Trip Distance (miles)", min_value=0.1, max_value=100.0, value=1.5)
    pickup_hour = st.slider("🕒 Pickup Hour", 0, 23, 12)

mean_distance = trip_distance

# Date-based features
date = st.date_input("Ride Date", value=datetime.today())
date = datetime.today()
day = date.strftime("%A")
day_number = date.day

# Tip
tip_amount = st.number_input("🌟 Tip Amount", min_value=0.0, max_value=100.0, value=1.0) if st.checkbox("Add tip?") else 0.0

# Auto-computed hidden fields
extra = 0.0
extra += 0.5 if pickup_hour >= 20 or pickup_hour < 6 else 0
extra += 1.0 if 7 <= pickup_hour <= 9 or 17 <= pickup_hour <= 19 else 0
extra += 1.5 if passenger_count >= 5 else 0
extra += 5.0 if PUborough == 'Queens' else 0
extra += 1.3
extra += 2.5 if PUborough == 'Manhattan' else 0
extra = min(extra, 15.0)

tolls_amount = 0.0
tolls_amount += 6.12 if 'Bronx' in [PUborough, DOborough] else 0
tolls_amount += 5.76 if 'Queens' in [PUborough, DOborough] else 0
tolls_amount += 17.0 if 'Staten Island' in [PUborough, DOborough] else 0
tolls_amount += 10.0 if PUborough != DOborough else 0
tolls_amount = min(tolls_amount, 130.0)

Airport_fee = 1.25 if 'JFK' in [PUborough, DOborough] else 1.75 if 'EWR' in [PUborough, DOborough] else 0.0
cbd_congestion_fee = 0.75 if PUborough == 'Manhattan' and 7 <= pickup_hour <= 19 else 0.0

# Create DataFrame
input_dict = {
    'VendorID': [VendorID],
    'passenger_count': [passenger_count],
    'RatecodeID': [RatecodeID],
    'payment_type': [payment_type],
    'extra': [extra],
    'tip_amount': [tip_amount],
    'tolls_amount': [tolls_amount],
    'Airport_fee': [Airport_fee],
    'cbd_congestion_fee': [cbd_congestion_fee],
    'date': [day_number],
    'hour': [pickup_hour],
    'day': [day],
    'mean_distance': [mean_distance],
    'PUborough': [PUborough],
    'DOborough': [DOborough]
}

input_df = pd.DataFrame(input_dict)

# Prediction
st.markdown("---")
if st.button("🔍 Predict Fare"):
    try:
        # Send POST request to FastAPI
        API_URL = "https://taxi-fare-predictor.onrender.com/predict"
        response = requests.post(API_URL, json=input_df.iloc[0].to_dict())

        if response.status_code == 200:
            prediction = response.json()["predicted_fare"]
            if prediction < 0 or prediction > 500:
                st.warning("⚠️ Predicted fare seems unusual. Please review the inputs.")
            else:
                st.success(f"💰 Estimated Fare: ${round(prediction, 2)}")
        else:
            st.error(f"❌ API Error: {response.status_code} - {response.text}")

    except Exception as e:
        st.error(f"❌ Request failed: {e}")

