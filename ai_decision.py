import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
import os

MODEL_PATH = "data/saved_models.pkl"

def train_model():
    X, y = [], []
    np.random.seed(42)

    for _ in range(1000):
        distance = np.random.uniform(1, 200)
        speed = np.random.uniform(0, 10)
        risk = 1 if (distance < 20 and speed > 2) else 0
        X.append([distance, speed])
        y.append(risk)

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)
    return model

# Load model if exists, else train & save
if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
else:
    model = train_model()
    os.makedirs("data", exist_ok=True)
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)

def ai_decision(distance, closing_speed):
    prob = model.predict_proba([[distance, closing_speed]])[0][1]
    return prob