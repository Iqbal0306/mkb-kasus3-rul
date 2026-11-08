import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Prediksi RUL Motor", page_icon="⚙️")

st.title("⚙️ Prediksi Sisa Umur Pakai Motor Induksi")
st.write("Masukkan nilai sensor saat ini untuk memperkirakan berapa jam lagi motor akan bertahan sebelum rusak.")

# Load model
try:
    model = joblib.load("artifacts/model_rul.joblib")
except FileNotFoundError:
    st.error("Model tidak ditemukan! Pastikan file artifacts/model_rul.joblib ada di repositori.")
    st.stop()

with st.form("form_sensor"):
    st.subheader("Data Sensor Real-Time")
    arus = st.number_input("Arus (Ampere)", min_value=0.0, value=12.5)
    getaran = st.number_input("Getaran (mm/s)", min_value=0.0, value=2.1)
    suhu = st.number_input("Suhu Body (°C)", min_value=0.0, value=45.0)
    tegangan = st.number_input("Tegangan (Volt)", min_value=0.0, value=220.0)
    
    submitted = st.form_submit_button("Prediksi Sisa Umur")

if submitted:
    # Key harus sama persis dengan FITUR saat melatih model di Colab
    input_data = pd.DataFrame([{
        "arus_ampere": arus,
        "getaran_mm_s": getaran,
        "suhu_body_c": suhu,
        "tegangan_volt": tegangan
    }])
    
    # Lakukan prediksi
    prediksi_rul = model.predict(input_data)[0]
    
    # Mencegah nilai minus jika mesin sudah di ambang batas rusak parah
    rul = round(max(0.0, float(prediksi_rul)), 2)
    
    st.divider()
    if rul > 500:
        st.success(f"✅ **Kondisi Prima!** Motor diperkirakan dapat beroperasi selama **{rul} jam** lagi.")
    elif rul > 100:
        st.info(f"🆗 **Kondisi Normal.** Sisa umur operasional motor: **{rul} jam**.")
    elif rul > 24:
        st.warning(f"⚠️ **Perhatian.** Sisa umur operasional motor: **{rul} jam**. Segera siapkan jadwal servis rutin.")
    else:
        st.error(f"🚨 **KRITIS!** Hentikan operasi. Motor akan gagal dalam **{rul} jam**.")