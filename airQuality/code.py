import pandas as pd
import numpy as np

# Read datasets
air = pd.read_csv("air.csv", encoding='latin1')
heart = pd.read_csv("heart.csv")

print(air.head())
print(heart.head())

# Data Cleaning
print(air.isnull().sum())
print(heart.isnull().sum())

air.fillna(air.mean(numeric_only=True), inplace=True)
heart.fillna(heart.mean(numeric_only=True), inplace=True)

# Data Integration
air['id'] = range(len(air))
heart['id'] = range(len(heart))

data = pd.merge(air, heart, on='id')

print(data.head())

# Data Transformation
data['age'] = (data['age'] - data['age'].min()) / (data['age'].max() - data['age'].min())

data = pd.get_dummies(data, drop_first=True)

print(data.head())

# Error Correction
data.drop_duplicates(inplace=True)
data[data < 0] = 0

# Model Building
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X = heart.drop('output', axis=1)
y = heart['output']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

score = model.score(X_test, y_test)

print("Model Accuracy:", score)