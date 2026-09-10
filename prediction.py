from sklearn.linear_model import LinearRegression
import numpy as np
X = np.array([[1],[2],[3],[4]])
Y = np.array([20,40,60,80])
model = LinearRegression()
model.fit(X,Y)
prediction = model.predict([[5]])
print("predict marks for 5 hours study =",prediction[0])
