# Bike Sharing Data Analysis

## Deskripsi
Proyek ini merupakan analisis data penyewaan sepeda menggunakan Bike Sharing Dataset Analisis dilakukan untuk mengetahui pola jumlah sepeda berdasarkan jam dan musim selama periode 2011-2012.

## Pertanyaan Bisnis
1. Pada ja berapa jumlah penyewaan sepeda paling tinggi selama periode 2011-2012?
2. Bagaimana perbedaan rata-rata jumlah penyewaan sepeda pada setiap musim selama periode 2011-2012?

## Dataset
Dataset yang digunakan adalah 'hour.csv' yang berisi data penyewaan sepeda berdasarkan jam selama periode 2011-2012.

## Dashboard 
Dashboard dibuat menggunakan Streamlit dan menampilkan:
- Total penyewaan sepeda berdasarkan jam.
- Rata-rata penyewaan sepeda berdasarkan musim.

## Cara Menjalankan Dashboard

### 1. Install library
Buka terminal pada folder project, kemudian jalankan:

```bash
pip install -r requirements.txt

### 2. Jalankan perintah
python -m streamlit run dashboard/dashboard.py

### 3. Buka Dashboard
Setelah Streamlit berjalan, buka alamat yang ditampilkan pada terminal, biasanya: http://localhost:8501 