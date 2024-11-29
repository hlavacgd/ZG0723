
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# FastAPI alkalmazás inicializálása
app = FastAPI()

# Modell betöltése
model = joblib.load("decision_tree_model.pkl")

# Adatmodell a kérésekhez
class PredictionRequest(BaseModel):
    features: list  # A bemeneti jellemzők listája

# Predikciós endpoint
@app.post("/predict")
def predict(data: PredictionRequest):
    # A bemeneti adatot numpy array-é alakítjuk
    input_features = np.array(data.features).reshape(1, -1)
    prediction = model.predict(input_features)
    return {"prediction": int(prediction[0])}
    