from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
import joblib

app = FastAPI(title="API RUL Motor Induksi")

# Wajib didefinisikan agar joblib bisa membaca Pipeline yang dibuat di Colab
def bersihkan_data(df):
    df_bersih = df.copy()
    df_bersih.loc[df_bersih["getaran_mm_s"] < 0, "getaran_mm_s"] = np.nan
    df_bersih.loc[df_bersih["arus_ampere"] < 0, "arus_ampere"] = np.nan
    return df_bersih

# Load model saat API menyala
model = joblib.load("artifacts/model_rul.joblib")

# Skema Input (Sekarang 4 Sensor)
class SensorMotor(BaseModel):
    arus_ampere: float
    getaran_mm_s: float
    suhu_body_c: float
    tegangan_volt: float

@app.post("/predict")
def predict_rul(data: SensorMotor):
    input_df = pd.DataFrame([data.model_dump()])
    
    prediksi_rul = model.predict(input_df)[0]
    sisa_umur = max(0.0, float(prediksi_rul))
    
    return {
        "status": "success",
        "remaining_useful_life_hours": round(sisa_umur, 2)
    }