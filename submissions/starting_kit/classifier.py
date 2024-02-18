from sklearn.base import BaseEstimator
import numpy as np


class Classifier(BaseEstimator):
    def __init__(self):
        return

    def fit(self, X, y):
        return

    def predict_proba(self, X):
        y = np.zeros((X.shape[0],2))
        y[:, 0] = 1.
        return y
