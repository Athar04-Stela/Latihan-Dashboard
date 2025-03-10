import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
@st.cache_data
def load_dataHarian():
    df = pd.read_csv("\Dashboard\data_harian.csv")  # Pastikan file main_data.csv sudah tersedia
    df['dteday'] = pd.to_datetime(df['dteday'])  # Konversi tanggal
    return df

def load_dataJam():
    df = pd.read_csv("\Dashboard\data_jam.csv")  # Pastikan file main_data.csv sudah tersedia
    df['dteday'] = pd.to_datetime(df['dteday'])  # Konversi tanggal
    return df

df_harian = load_dataHarian()
df_jam = load_dataJam()

# Dashboard Title
st.title("Dashboard Analisis Peminjaman Sepeda")

# Tren Peminjaman Harian
st.subheader("Tren Peminjaman Sepeda Harian (2011-2012)")
fig, ax = plt.subplots(figsize=(12, 5))
sns.lineplot(x=df_harian['dteday'], y=df_harian['cnt'], ax=ax, color='blue', linewidth=1)
ax.set_xlabel("Tanggal")
ax.set_ylabel("Jumlah Peminjaman")
ax.set_title("Tren Peminjaman Sepeda Harian")
st.pyplot(fig)

# Pengaruh Cuaca terhadap Peminjaman
st.subheader("Pengaruh Cuaca terhadap Peminjaman Sepeda")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=df_harian['weathersit'], y=df_harian['cnt'], estimator="mean", ax=ax)
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Rata-rata Peminjaman")
ax.set_title("Rata-rata Peminjaman Sepeda Berdasarkan Cuaca")
st.pyplot(fig)

# Peminjaman Berdasarkan Musim
st.subheader("Perbedaan Peminjaman di Berbagai Musim")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=df_harian['season'], y=df_harian['cnt'], estimator="mean", ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Rata-rata Peminjaman")
ax.set_title("Rata-rata Peminjaman Sepeda Berdasarkan Musim")
st.pyplot(fig)

# Perbandingan Pengguna Kasual vs Terdaftar
st.subheader("Perbandingan Pengguna Kasual vs Terdaftar")
fig, ax = plt.subplots(figsize=(6, 5))
sns.barplot(x=["Casual", "Registered"], y=[df_jam['casual'].sum(), df_jam['registered'].sum()], ax=ax)
ax.set_xlabel("Tipe Pengguna")
ax.set_ylabel("Total Peminjaman")
ax.set_title("Total Peminjaman Sepeda: Kasual vs Terdaftar")
st.pyplot(fig)

# Pola Peminjaman Per Jam
st.subheader("Pola Peminjaman Sepeda Per Jam")
hourly_avg = df_jam.groupby("hr")["cnt"].mean()
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=hourly_avg.index, y=hourly_avg.values, marker="o", color="blue", linewidth=2, ax=ax)
ax.set_xlabel("Jam dalam Sehari")
ax.set_ylabel("Rata-rata Peminjaman")
ax.set_title("Rata-rata Peminjaman Sepeda Per Jam")
st.pyplot(fig)

st.caption('Copyright © Dicoding 2023')
