# 🚖 Taxi Fare Prediction

This project predicts the **fare amount** for NYC taxi rides using historical trip data. It includes full data preprocessing, feature engineering, model training, and deployment via Streamlit.

🔗 **[Try the Live App](https://taxi-fare-prediction-kgyrhmvegjcjanwgfzydtb.streamlit.app/)**

---

## 🎯 Objective

To build a regression model that can accurately estimate taxi fares based on:

- Trip distance & duration
- Pickup hour and day
- Borough-level pickup/dropoff zones
- Surcharges (tolls, congestion fees, etc.)
- Vendor and payment details

---

## 🛠 Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn (Model)
- Matplotlib & Seaborn (for EDA)
- Streamlit (for deployment)

---

## 📊 Dataset Features

| Column               | Description                                |
|----------------------|--------------------------------------------|
| `trip_distance`      | Distance of the trip in miles              |
| `passenger_count`    | Number of passengers                       |
| `hour`, `day`, `date`| Extracted from pickup datetime             |
| `PUborough`, `DOborough` | Pickup and dropoff boroughs            |
| `tolls_amount`, `Airport_fee`, `cbd_congestion_fee` | Surcharges |
| `total_amount`       | Target variable (fare)                     |

---

## 🔍 Model

A `LinearRegression` model wrapped in a Scikit-learn `Pipeline`:

- **Numerical features**: imputation + scaling  
- **Categorical features**: imputation + one-hot encoding  

---

## 📈 Model Evaluation (on unseen Feb data)

| Metric        | Linear Regression |
|---------------|-------------------|
| RMSE          | `4.91`            |
| MAE           | `2.91`            |
| R² Score      | `0.9425`          |

✅ The model explains ~94% of the fare variance.

---

## 🌐 Deployment

Deployed with **Streamlit**. Users can:

- Input trip details (time, passengers, boroughs, etc.)
- Get instant fare predictions based on real model logic

To run locally:

```bash
streamlit run app.py
