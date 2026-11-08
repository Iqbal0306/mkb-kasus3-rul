from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="API RUL Motor Induksi")

# Load model saat API menyala
model = joblib.load("artifacts/model_rul.joblib")

# Skema Input Sensor
class SensorMotor(BaseModel):
    arus_ampere: float
    getaran_mm_s: float
    suhu_body_c: float

@app.post("/predict")
def predict_rul(data: SensorMotor):
    # Ubah input menjadi DataFrame
    input_df = pd.DataFrame([data.model_dump()])
    
    # Lakukan prediksi
    prediksi_rul = model.predict(input_df)[0]
    
    # Filter agar sisa umur tidak minus (jika model menebak angka negatif)
    sisa_umur = max(0.0, float(prediksi_rul))
    
    return {
        "status": "success",
        "remaining_useful_life_hours": round(sisa_umur, 2)
    }