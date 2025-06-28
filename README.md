# 🚖 Taxi Fare Prediction

This project predicts the **fare amount** for NYC taxi rides using historical trip data. It includes full data preprocessing, feature engineering, model training, and deployment via both **Streamlit** (frontend) and **FastAPI** (backend).

🔗 **Live App**: [https://taxi-fare-predictor.streamlit.app](https://taxi-fare-predictor.streamlit.app)  
🔧 **API Endpoint**: [https://taxi-fare-predictor.onrender.com/docs](https://taxi-fare-predictor.onrender.com/docs)

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
- Scikit-learn (Model & Pipeline)  
- Matplotlib, Seaborn (EDA)  
- Streamlit (frontend/UI)  
- FastAPI (model backend)  
- Render (backend deployment)  

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

## 📈 Model Evaluation (on unseen February data)

| Metric        | Linear Regression |
|---------------|-------------------|
| RMSE          | `4.91`            |
| MAE           | `2.91`            |
| R² Score      | `0.9425`          |

✅ The model explains ~94% of the fare variance.

---

## 🔁 Full-Stack Architecture

This project follows a **modular, real-world architecture**:


- 🖥️ **Frontend**: Streamlit (collects input & displays fare)  
- ⚙️ **Backend**: FastAPI (runs prediction logic via `/predict`)  
- ☁️ **Deployment**: Streamlit Cloud (UI) + Render (API)

---

## 💻 How to Run Locally

1. Clone the repo  
2. Install dependencies:

```bash
pip install -r requirements.txt
```
3. Run Streamlit frontend

```bash
streamlit run app.py
```
4. Run FastAPI backend

```bash
uvicorn api:app --reload
```
5. Render start command (for deployment)

```yaml
startCommand: uvicorn api:app --host 0.0.0.0 --port 10000
```
