# Simple Linear Regression Example
# Predict marks based on study hours

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    'Hours': [1, 2, 3, 4, 5, 6],
    'Marks': [20, 40, 50, 60, 70, 80]
}

df = pd.DataFrame(data)

# Features (X) and Target (y)
X = df[['Hours']]   # 2D
y = df['Marks']     # 1D

# Train the model
model = LinearRegression()
model.fit(X, y)

# Predict for new value
hours = 7
predicted_marks = model.predict(np.array([[hours]]))

print(f"If a student studies for {hours} hours, predicted marks = {predicted_marks[0]:.2f}")