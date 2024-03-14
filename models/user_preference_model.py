# user_preference_model.py

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report
from sklearn.externals import joblib
import numpy as np

class UserPreferenceModel:
    def __init__(self):
        self.model = RandomForestClassifier()

    def train(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        scores = cross_val_score(self.model, X, y, cv=5)
        print(f"Cross-Validation Scores: {scores}")
        print(f"Average Score: {np.mean(scores)}")

    def predict(self, X):
        try:
            return self.model.predict(X)
        except Exception as e:
            print(f"Error during prediction: {e}")
            return None

    def save_model(self, path):
        joblib.dump(self.model, path)

    def load_model(self, path):
        self.model = joblib.load(path)
