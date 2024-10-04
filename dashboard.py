import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

day_df = pd.read_csv('Bike Sharing Dataset\day.csv')  
hour_df = pd.read_csv('Bike Sharing Dataset\hour.csv')  

bike_sharing_df = day_df.merge(hour_df, on='dteday', how='inner', suffixes=('_day', '_hour'))

st.title("Dashboard Penyewaan Sepeda")

st.sidebar.title("Pilih Parameter Analisis")
season_choice = st.sidebar.selectbox("Pilih Musim", bike_sharing_df['season_day'].unique())
weekday_choice = st.sidebar.selectbox("Pilih Hari dalam Seminggu", bike_sharing_df['weekday_hour'].unique())

def plot_seasonal_trend():
    seasonal_data = bike_sharing_df.groupby('season_day')['cnt_hour'].sum().reset_index()
    plt.figure(figsize=(10, 5))
    sns.barplot(data=seasonal_data, x='season_day', y='cnt_hour', palette='viridis')
    plt.title("Jumlah Penyewaan Sepeda per Musim")
    plt.xlabel("Musim")
    plt.ylabel("Jumlah Penyewaan")
    st.pyplot(plt)

def plot_weekday_trend():
    weekday_data = bike_sharing_df.groupby('weekday_hour')['cnt_hour'].sum().reset_index()
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=weekday_data, x='weekday_hour', y='cnt_hour', marker='o')
    plt.title("Jumlah Penyewaan Sepeda per Hari dalam Seminggu")
    plt.xlabel("Hari dalam Seminggu")
    plt.ylabel("Jumlah Penyewaan")
    st.pyplot(plt)

def plot_temperature_effect():
    plt.figure(figsize=(10, 5))
    sns.scatterplot(data=bike_sharing_df, x='temp_hour', y='cnt_hour', alpha=0.6)
    plt.title("Pengaruh Suhu Terhadap Jumlah Penyewaan Sepeda")
    plt.xlabel("Suhu")
    plt.ylabel("Jumlah Penyewaan")
    st.pyplot(plt)

if st.sidebar.button("Tampilkan Tren Musim"):
    plot_seasonal_trend()

if st.sidebar.button("Tampilkan Tren Hari dalam Seminggu"):
    plot_weekday_trend()

if st.sidebar.button("Tampilkan Pengaruh Suhu"):
    plot_temperature_effect()

st.subheader("Data Penyewaan Sepeda")
st.dataframe(bike_sharing_df)

st.subheader("Statistik Deskriptif")
st.write(bike_sharing_df.describe())
