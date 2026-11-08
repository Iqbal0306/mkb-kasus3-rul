import streamlit as st
import requests

st.set_page_config(page_title="Prediksi RUL Motor", page_icon="⚙️")

st.title("⚙️ Prediksi Sisa Umur Pakai Motor Induksi")
st.write("Masukkan nilai sensor saat ini untuk memperkirakan berapa jam lagi motor akan bertahan sebelum rusak.")

with st.form("form_sensor"):
    arus = st.number_input("Arus (Ampere)", min_value=0.0, value=12.0)
    getaran = st.number_input("Getaran (mm/s)", min_value=0.0, value=2.0)
    suhu = st.number_input("Suhu Body (°C)", min_value=0.0, value=45.0)
    
    submitted = st.form_submit_button("Prediksi Sisa Umur")

if submitted:
    payload = {
        "arus_ampere": arus,
        "getaran_mm_s": getaran,
        "suhu_body_c": suhu
    }
    
    try:
        # Kirim data ke backend FastAPI
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        hasil = response.json()
        
        rul = hasil["remaining_useful_life_hours"]
        
        if rul > 100:
            st.success(f"✅ **Aman!** Perkiraan sisa umur motor: **{rul} jam**")
        elif rul > 24:
            st.warning(f"⚠️ **Perhatian.** Perkiraan sisa umur motor: **{rul} jam**")
        else:
            st.error(f"🚨 **KRITIS!** Motor harus segera diservis. Sisa umur: **{rul} jam**")
            
    except requests.exceptions.ConnectionError:
        st.error("Server API belum berjalan. Pastikan FastAPI (uvicorn) sudah dihidupkan.")