# Vehicle Count Prediction using Random Forest

import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load dataset
train = pd.read_csv("vehicles.csv")

# Convert DateTime column
train['DateTime'] = pd.to_datetime(train['DateTime'])

# Feature engineering
train['date'] = train['DateTime'].dt.day
train['weekday'] = train['DateTime'].dt.weekday
train['hour'] = train['DateTime'].dt.hour
train['month'] = train['DateTime'].dt.month
train['year'] = train['DateTime'].dt.year
train['dayofyear'] = train['DateTime'].dt.dayofyear
train['weekofyear'] = train['DateTime'].dt.isocalendar().week

# Drop original DateTime
train = train.drop(['DateTime'], axis=1)

# Features & Target
train1 = train.drop(['Vehicles'], axis=1)
target = train['Vehicles']

# Train RandomForest model
model = RandomForestRegressor()
model.fit(train1, target)

# Test prediction
print("Sample Prediction:", model.predict([[11, 6, 0, 1, 2015, 11, 2]]))
