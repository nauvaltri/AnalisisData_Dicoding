import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
day_df = pd.read_csv('Bike Sharing Dataset/day.csv')  
hour_df = pd.read_csv('Bike Sharing Dataset/hour.csv')  
bike_sharing_df = day_df.merge(hour_df, on='dteday', how='inner', suffixes=('_day', '_hour'))

# Dashboard title
st.title("🚴 Dashboard Penyewaan Sepeda")
st.markdown("Analisis interaktif data penyewaan sepeda berdasarkan musim, hari, dan suhu.")

# Sidebar for user input
st.sidebar.title("Pilih Parameter Analisis")
season_choice = st.sidebar.selectbox("Pilih Musim", bike_sharing_df['season_day'].unique())
weekday_choice = st.sidebar.selectbox("Pilih Hari dalam Seminggu", bike_sharing_df['weekday_hour'].unique())

# Function to plot seasonal trend
def plot_seasonal_trend():
    seasonal_data = bike_sharing_df.groupby('season_day')['cnt_hour'].sum().reset_index()
    plt.figure(figsize=(10, 5))
    sns.barplot(data=seasonal_data, x='season_day', y='cnt_hour', palette='coolwarm')
    plt.title("🌼 Jumlah Penyewaan Sepeda per Musim", fontsize=16)
    plt.xlabel("Musim", fontsize=14)
    plt.ylabel("Jumlah Penyewaan", fontsize=14)
    st.pyplot(plt)

# Function to plot weekday trend
def plot_weekday_trend():
    weekday_data = bike_sharing_df.groupby('weekday_hour')['cnt_hour'].sum().reset_index()
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=weekday_data, x='weekday_hour', y='cnt_hour', marker='o', color='orange', linewidth=2)
    plt.title("📅 Jumlah Penyewaan Sepeda per Hari dalam Seminggu", fontsize=16)
    plt.xlabel("Hari dalam Seminggu", fontsize=14)
    plt.ylabel("Jumlah Penyewaan", fontsize=14)
    st.pyplot(plt)

# Function to plot temperature effect
def plot_temperature_effect():
    plt.figure(figsize=(10, 5))
    sns.scatterplot(data=bike_sharing_df, x='temp_hour', y='cnt_hour', alpha=0.6, color='purple')
    plt.title("🌡️ Pengaruh Suhu Terhadap Jumlah Penyewaan Sepeda", fontsize=16)
    plt.xlabel("Suhu", fontsize=14)
    plt.ylabel("Jumlah Penyewaan", fontsize=14)
    st.pyplot(plt)

# Buttons to trigger plots
if st.sidebar.button("Tampilkan Tren Musim"):
    plot_seasonal_trend()

if st.sidebar.button("Tampilkan Tren Hari dalam Seminggu"):
    plot_weekday_trend()

if st.sidebar.button("Tampilkan Pengaruh Suhu"):
    plot_temperature_effect()

# Data overview
st.subheader("📊 Data Penyewaan Sepeda")
st.dataframe(bike_sharing_df)

st.subheader("📈 Statistik Deskriptif")
st.write(bike_sharing_df.describe())

# Add a footer
st.markdown("___")
st.markdown("Data diambil dari [Bike Sharing Dataset](https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset)")
