# 🚗 Vehicle Count Prediction using Random Forest

This project predicts the number of vehicles from timestamp-based sensor data using **Python** and **Machine Learning (Random Forest Regressor)**.

---

## 📌 Project Overview
- Extracts features such as **day, weekday, hour, month, year, etc.** from the DateTime column.
- Trains a **RandomForestRegressor** model from `scikit-learn`.
- Makes predictions based on time-related features.

---

## 📂 Dataset
- File: `vehicles.csv`
- Columns:
  - `DateTime` → Original timestamp
  - `Vehicles` → Target label (number of vehicles)

---

## ⚙️ Steps in the Code
1. Import necessary libraries (`pandas`, `sklearn`).
2. Load dataset using pandas.
3. Convert `DateTime` into multiple features:
   - Day, Weekday, Hour, Month, Year, Day of Year, Week of Year
4. Drop `DateTime` column after feature extraction.
5. Separate features (`train1`) and target (`Vehicles`).
6. Train a **RandomForestRegressor** model.
7. Test the model with sample inputs.

---

## 🧑‍💻 Example Code
```python
from sklearn.ensemble import RandomForestRegressor

# Define the model
m1 = RandomForestRegressor()

# Train the model
m1.fit(train1, target)

# Make a prediction
print(m1.predict([[11,6,0,1,2015,11,2]]))
