import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Prediksi RUL Motor", page_icon="⚙️")

st.title("⚙️ Prediksi Sisa Umur Pakai Motor Induksi")
st.write("Masukkan nilai sensor saat ini untuk memperkirakan berapa jam lagi motor akan bertahan sebelum rusak.")

# Load model secara langsung
try:
    model = joblib.load("artifacts/model_rul.joblib")
except FileNotFoundError:
    st.error("Model tidak ditemukan! Pastikan file artifacts/model_rul.joblib ada di repositori.")
    st.stop()

with st.form("form_sensor"):
    arus = st.number_input("Arus (Ampere)", min_value=0.0, value=12.0)
    getaran = st.number_input("Getaran (mm/s)", min_value=0.0, value=2.0)
    suhu = st.number_input("Suhu Body (°C)", min_value=0.0, value=45.0)
    
    submitted = st.form_submit_button("Prediksi Sisa Umur")

if submitted:
    # Buat DataFrame dari input
    input_data = pd.DataFrame([{
        "arus_ampere": arus,
        "getaran_mm_s": getaran,
        "suhu_body_c": suhu
    }])
    
    # Lakukan prediksi langsung
    prediksi_rul = model.predict(input_data)[0]
    
    # Cegah angka minus
    rul = round(max(0.0, float(prediksi_rul)), 2)
    
    if rul > 100:
        st.success(f"✅ **Aman!** Perkiraan sisa umur motor: **{rul} jam**")
    elif rul > 24:
        st.warning(f"⚠️ **Perhatian.** Perkiraan sisa umur motor: **{rul} jam**")
    else:
        st.error(f"🚨 **KRITIS!** Motor harus segera diservis. Sisa umur: **{rul} jam**")
