import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
 
st.write(
    """
    # Project Finalku
    Selamat datang di web visualisasi ini
    """
)

df = pd.read_csv("day.csv", delimiter=",")

st.dataframe(data=df, width=500, height=150)

# Menghitung total untuk setiap kategori hari
total_weekday = sum(df['weekday'])
total_workingday = sum(df['workingday'])

# Menyiapkan kategori dan nilai total
categories = ['Weekday', 'Workingday']
total_values = [total_weekday, total_workingday]

# Membuat aplikasi Streamlit
st.title('Total Peminjaman Sepeda Berdasarkan Kategori Hari')
st.bar_chart(dict(zip(categories, total_values)))

# Menampilkan diagram batang dengan judul
st.pyplot(plt)


# Analisis pengaruh cuaca terhadap jumlah peminjaman sepeda
cuaca_analisis = df.groupby('weathersit')['cnt'].mean()

# Menampilkan statistik deskriptif untuk variabel-variabel terkait cuaca
deskriptif_cuaca = df.groupby('weathersit')[['temp', 'atemp', 'hum', 'windspeed']].describe()

# Membuat aplikasi Streamlit
st.title('Analisis Pengaruh Cuaca Terhadap Jumlah Peminjaman Sepeda')

# Menggunakan kolom untuk menyusun tata letak
col1, col2 = st.columns(2)

# Visualisasi pengaruh cuaca - Kolom pertama
col1.subheader('Rata-rata Jumlah Peminjaman Sepeda Berdasarkan Cuaca')
col1.bar_chart(cuaca_analisis)

# Visualisasi pengaruh cuaca - Kolom kedua
col2.subheader('Box Plot Variabel Terkait Cuaca')
col2.pyplot(plt.boxplot([df[df['weathersit'] == i]['temp'] for i in df['weathersit']]))
plt.title('Box Plot Variabel Terkait Cuaca')

# Menampilkan statistik deskriptif untuk variabel-variabel terkait cuaca
st.subheader('Statistik Deskriptif untuk Variabel Terkait Cuaca')
st.table(deskriptif_cuaca)

# Menampilkan plot
st.pyplot()
