from sklearn.linear_model import LinearRegression
import numpy as np

class DummyModel:
    def __init__(self):
        X = np.array([[1], [2], [3], [4]])
        y = np.array([10, 20, 30, 40])
        self.model = LinearRegression().fit(X, y)

    def predict(self, value: float) -> float:
        return float(self.model.predict([[value]])[0])
