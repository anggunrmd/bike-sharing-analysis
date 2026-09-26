import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dashboard/hour.csv")

# Judul dashboard
st.title("Dashboard Analisis Bike Sharing")

st.write(
    "Dashboard ini menampilkan analisis jumlah penyewaan sepeda "
    "berdasarkan jam dan musim selama periode 2011–2012."
)

# =====================================
# PERTANYAAN 1
# =====================================

st.header("1. Jumlah Penyewaan Berdasarkan Jam")

rental_by_hour = df.groupby("hr")["cnt"].sum().reset_index()

max_hour = rental_by_hour.loc[
    rental_by_hour["cnt"].idxmax()
]

st.write(
    f"Jumlah penyewaan tertinggi terjadi pada pukul "
    f"{int(max_hour['hr'])}.00 dengan total "
    f"{int(max_hour['cnt']):,} penyewaan."
)

fig1, ax1 = plt.subplots(figsize=(10, 5))

ax1.bar(
    rental_by_hour["hr"],
    rental_by_hour["cnt"]
)

ax1.set_title("Total Penyewaan Sepeda Berdasarkan Jam")
ax1.set_xlabel("Jam")
ax1.set_ylabel("Total Penyewaan")
ax1.set_xticks(range(24))

st.pyplot(fig1)


# =====================================
# PERTANYAAN 2
# =====================================

st.header("2. Rata-rata Penyewaan Berdasarkan Musim")

rental_by_season = df.groupby("season")["cnt"].mean().reset_index()

season_names = {
    1: "Winter",
    2: "Spring",
    3: "Summer",
    4: "Fall"
}

rental_by_season["season_name"] = (
    rental_by_season["season"].map(season_names)
)

max_season = rental_by_season.loc[
    rental_by_season["cnt"].idxmax()
]

st.write(
    f"Rata-rata penyewaan tertinggi terjadi pada musim "
    f"{max_season['season_name']} dengan rata-rata "
    f"{max_season['cnt']:.2f} penyewaan."
)

fig2, ax2 = plt.subplots(figsize=(8, 5))

ax2.bar(
    rental_by_season["season_name"],
    rental_by_season["cnt"]
)

ax2.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Musim")
ax2.set_xlabel("Musim")
ax2.set_ylabel("Rata-rata Penyewaan")

st.pyplot(fig2)