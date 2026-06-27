from sklearn.ensemble import IsolationForest
import numpy as np

# Normal data
data = np.array([[10],[12],[11],[13],[14]])

model = IsolationForest()
model.fit(data)

# New values
test = np.array([[12],[200]])  # 200 is abnormal

result = model.predict(test)

for i in range(len(test)):
    if result[i] == -1:
        print("Anomaly detected:", test[i])
    else:
        print("Normal:", test[i])