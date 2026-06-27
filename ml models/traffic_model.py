import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample dataset
data = {
    "traffic": [10, 20, 30, 40, 50],
    "speed": [60, 50, 40, 30, 20]
}

df = pd.DataFrame(data)

X = df[["traffic"]]
y = df["speed"]

model = LinearRegression()
model.fit(X, y)

# Predict
traffic_input = [[35]]
predicted_speed = model.predict(traffic_input)

print("Predicted Safe Speed:", predicted_speed[0])