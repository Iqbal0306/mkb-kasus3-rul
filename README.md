# ⚙️ Predictive Maintenance: RUL Induction Motor

Sistem cerdas berbasis *Machine Learning* untuk memprediksi Sisa Umur Pakai (*Remaining Useful Life* / RUL) dari motor induksi industri berdasarkan data sensor operasional. Proyek ini merupakan implementasi Praktikum **Studi Kasus 03**.

## 🚀 Fitur Utama
* **Algoritma Model:** XGBoost Regressor
* **Antarmuka Pengguna:** Streamlit
* **Parameter Input:** Arus (Ampere), Getaran (mm/s), Suhu Body (°C), dan Tegangan (Volt).
* **Output Sistem:** Estimasi sisa umur operasional mesin (dalam jam) beserta indikator peringatan visual (Kondisi Prima / Normal / Perhatian / Kritis).

## 🛠️ Teknologi yang Digunakan
* `scikit-learn` & `xgboost` untuk regresi dan imputasi data.
* `pandas` & `numpy` untuk manipulasi data tabular.
* `joblib` untuk serialisasi model.
* `streamlit` untuk peluncuran antarmuka web (*deployment*).

## 💻 Cara Menjalankan Secara Lokal
1. Buat lingkungan virtual dan instal pustaka:
   `python -m pip install -r requirements.txt`
2. Jalankan aplikasi web:
   `python -m streamlit run app/ui/streamlit_app.py`

## 👨‍💻 Pengembang
* **Nama:** Iqbal Ianudin
* **NIM:** [Isi NIM Kamu]
* **Mata Kuliah:** Mekatronika dan Kecerdasan Buatan (MKB)