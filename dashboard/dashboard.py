import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("data/hour.csv")

# Ubah tanggal
df["dteday"] = pd.to_datetime(df["dteday"])

# Nama musim
season_names = {
    1: "Winter",
    2: "Spring",
    3: "Summer",
    4: "Fall"
}

df["season_name"] = df["season"].map(season_names)


# =========================
# TITLE
# =========================
st.title("🚲 Bike Sharing Dashboard")

st.write(
    "Dashboard interaktif untuk menganalisis pola penyewaan sepeda "
    "berdasarkan jam dan musim selama periode 2011–2012."
)


# =========================
# SIDEBAR FILTER
# =========================
st.sidebar.header("Filter Data")

# Filter tanggal
min_date = df["dteday"].min().date()
max_date = df["dteday"].max().date()

date_range = st.sidebar.date_input(
    "Pilih Rentang Tanggal",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Filter musim
selected_seasons = st.sidebar.multiselect(
    "Pilih Musim",
    options=["Winter", "Spring", "Summer", "Fall"],
    default=["Winter", "Spring", "Summer", "Fall"]
)

# Filter jam
hour_range = st.sidebar.slider(
    "Pilih Rentang Jam",
    min_value=0,
    max_value=23,
    value=(0, 23)
)


# =========================
# APPLY FILTER
# =========================

filtered_df = df.copy()

# Filter tanggal
if len(date_range) == 2:
    start_date, end_date = date_range

    filtered_df = filtered_df[
        (filtered_df["dteday"].dt.date >= start_date)
        & (filtered_df["dteday"].dt.date <= end_date)
    ]

# Filter musim
filtered_df = filtered_df[
    filtered_df["season_name"].isin(selected_seasons)
]

# Filter jam
filtered_df = filtered_df[
    (filtered_df["hr"] >= hour_range[0])
    & (filtered_df["hr"] <= hour_range[1])
]


# =========================
# SUMMARY
# =========================
st.subheader("Ringkasan Data")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Penyewaan",
        f"{filtered_df['cnt'].sum():,}"
    )

with col2:
    if len(filtered_df) > 0:
        st.metric(
            "Rata-rata Penyewaan",
            f"{filtered_df['cnt'].mean():.2f}"
        )
    else:
        st.metric("Rata-rata Penyewaan", "0")

with col3:
    st.metric(
        "Jumlah Data",
        f"{len(filtered_df):,}"
    )


# =========================
# PERTANYAAN 1
# =========================
st.subheader(
    "Pertanyaan 1: Pada jam berapa jumlah penyewaan sepeda paling tinggi?"
)

rental_by_hour = (
    filtered_df
    .groupby("hr")["cnt"]
    .sum()
    .reset_index()
)

if len(rental_by_hour) > 0:

    max_hour = rental_by_hour.loc[
        rental_by_hour["cnt"].idxmax()
    ]

    st.write(
        f"Pada data yang dipilih, jumlah penyewaan tertinggi terjadi "
        f"pada pukul **{int(max_hour['hr']):02d}.00** "
        f"dengan total **{int(max_hour['cnt']):,} penyewaan**."
    )

    fig1, ax1 = plt.subplots(figsize=(10, 5))

    ax1.bar(
        rental_by_hour["hr"],
        rental_by_hour["cnt"]
    )

    ax1.set_title("Total Penyewaan Sepeda Berdasarkan Jam")
    ax1.set_xlabel("Jam")
    ax1.set_ylabel("Total Penyewaan")

    st.pyplot(fig1)


# =========================
# PERTANYAAN 2
# =========================
st.subheader(
    "Pertanyaan 2: Bagaimana perbedaan rata-rata penyewaan pada setiap musim?"
)

rental_by_season = (
    filtered_df
    .groupby("season_name")["cnt"]
    .mean()
    .reindex(["Winter", "Spring", "Summer", "Fall"])
    .dropna()
    .reset_index()
)

if len(rental_by_season) > 0:

    max_season = rental_by_season.loc[
        rental_by_season["cnt"].idxmax()
    ]

    st.write(
        f"Pada data yang dipilih, **{max_season['season_name']}** "
        f"memiliki rata-rata penyewaan tertinggi, yaitu "
        f"**{max_season['cnt']:.2f} penyewaan**."
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

else:
    st.warning("Tidak ada data yang sesuai dengan filter yang dipilih.")