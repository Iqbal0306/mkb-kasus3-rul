import streamlit as st
import requests

st.set_page_config(page_title="Prediksi RUL Motor", page_icon="⚙️")
st.title("⚙️ Prediksi Sisa Umur Pakai Motor Induksi")
st.write("Sistem Arsitektur Terpisah: UI (Streamlit) -> API (FastAPI) -> Model (XGBoost)")

with st.form("form_sensor"):
    st.subheader("Data Sensor Real-Time")
    arus = st.number_input("Arus (Ampere)", min_value=0.0, value=12.5)
    getaran = st.number_input("Getaran (mm/s)", min_value=0.0, value=2.1)
    suhu = st.number_input("Suhu Body (°C)", min_value=0.0, value=45.0)
    tegangan = st.number_input("Tegangan (Volt)", min_value=0.0, value=220.0)
    
    submitted = st.form_submit_button("Prediksi Sisa Umur")

if submitted:
    # Format JSON yang akan dikirim ke FastAPI
    payload = {
        "arus_ampere": arus,
        "getaran_mm_s": getaran,
        "suhu_body_c": suhu,
        "tegangan_volt": tegangan
    }
    
    try:
        # Menembak endpoint FastAPI secara lokal
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        hasil = response.json()
        
        rul = hasil["remaining_useful_life_hours"]
        
        st.divider()
        if rul > 500:
            st.success(f"✅ **Kondisi Prima!** Motor diperkirakan beroperasi **{rul} jam** lagi.")
        elif rul > 100:
            st.info(f"🆗 **Kondisi Normal.** Sisa umur operasional: **{rul} jam**.")
        elif rul > 24:
            st.warning(f"⚠️ **Perhatian.** Sisa umur operasional: **{rul} jam**. Siapkan servis.")
        else:
            st.error(f"🚨 **KRITIS!** Hentikan operasi. Motor gagal dalam **{rul} jam**.")
            
    except requests.exceptions.ConnectionError:
        st.error("Server API belum berjalan. Pastikan FastAPI (uvicorn) sudah dihidupkan di terminal terpisah.")