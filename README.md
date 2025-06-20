# Taxi Fare Prediction

This project predicts the **fare amount** for Taxi rides using historical trip data. It includes full data preprocessing, feature engineering, model training, and evaluation.

---

##  Objective

To build a regression model that can accurately estimate taxi fares based on:

- Trip distance & duration
- Pickup hour and day
- Borough-level pickup/dropoff zones
- Surcharges (tolls, congestion fees, etc.)
- Vendor and payment details

---

##  Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn (Model)
- Matplotlib & Seaborn (for EDA)
- Streamlit (for deployment)

---

##  Dataset Features

| Column               | Description                                |
|----------------------|--------------------------------------------|
| `trip_distance`      | Distance of the trip in miles              |
| `passenger_count`    | Number of passengers                       |
| `hour`, `day`, `date`| Extracted from pickup datetime             |
| `PULocationID`, `DOLocationID` | Pickup and dropoff zones        |
| `PUborough`, `DOborough` | Mapped boroughs using location zones   |
| `tolls_amount`, `Airport_fee`, `cbd_congestion_fee` | Surcharges |
| `total_amount`       |  Target variable                         |

---

##  Model Used

A `LinearRegression` model wrapped in a Scikit-learn `Pipeline` with:

- **Numeric preprocessing**: imputation + scaling  
- **Categorical preprocessing**: imputation + one-hot encoding  
- **Feature selection**: only relevant columns used after cleaning

---

##  Model Evaluation (on unseen February data)

| Metric     | Logistic Regression |
|------------|------------|
| **RMSE**   | `4.91`     |
| **MAE**    | `2.91`     |
| **R² Score** | `0.9425` |

 The model explains ~94% of the variance in fare and generalizes well to new data.

---

##  Deployment 

The model is deployed using **Streamlit** with a simple web UI that allows users to:

- Input trip details (hour, distance, boroughs, surcharges)
- Get an instant fare estimate

Run locally:

```bash
streamlit run app.py
