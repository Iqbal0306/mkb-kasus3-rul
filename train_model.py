import joblib
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from xgboost import XGBRegressor

# 1. Siapkan Data (Ganti dengan URL/File CSV praktikum yang asli)
# Ini adalah data dummy sintetis agar skrip langsung bisa dicoba
data = {
    "arus_ampere": [12.5, 13.0, 18.2, 14.1, 19.5, 12.8, 20.1],
    "getaran_mm_s": [2.1, 2.3, 5.8, 2.9, 6.2, 2.2, 7.1],
    "suhu_body_c": [45.0, 46.5, 75.2, 50.1, 80.0, 44.5, 85.5],
    "sisa_umur_jam": [200.5, 195.0, 20.5, 150.0, 10.2, 210.0, 2.5] # Target (RUL)
}
df = pd.DataFrame(data)

X = df[["arus_ampere", "getaran_mm_s", "suhu_body_c"]]
y = df["sisa_umur_jam"]

# 2. Bangun Pipeline Regresi
pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("model", XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42))
])

# 3. Latih dan Simpan
print("Melatih model regresi RUL Motor Induksi...")
pipeline.fit(X, y)

joblib.dump(pipeline, "artifacts/model_rul.joblib")
print("✅ Selesai! Model tersimpan di artifacts/model_rul.joblib")