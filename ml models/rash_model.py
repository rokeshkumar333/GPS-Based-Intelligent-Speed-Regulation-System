from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Data: [speed change, acceleration]
X = np.array([
    [5,2],
    [20,10],
    [2,1],
    [30,15]
])

# 0 = normal, 1 = rash
y = [0,1,0,1]

model = DecisionTreeClassifier()
model.fit(X,y)

# Test
test = [[25,12]]

result = model.predict(test)

if result == 1:
    print("Rash Driving Detected")
else:
    print("Normal Driving")