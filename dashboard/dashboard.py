import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('dashboard/day.csv')
    return df

# Load the data
df = load_data()

# Sidebar
st.sidebar.title("Informasi Pengguna")
st.sidebar.subheader("Data Diri")
st.sidebar.write("- **Nama:** Akhtar Ramadhan Putra")
st.sidebar.write("- **Email:** m295d4ky1879@bangkit.academy")
st.sidebar.write("- **ID Dicoding:** [akhtar_ramadhan](https://www.dicoding.com/users/akhtar_ramadhan/)")

# Main Content
st.title("Dashboard Analisis Data Bike Sharing")

# Data Wrangling
df['dteday'] = pd.to_datetime(df['dteday'])
df['mnth'] = df['mnth'].map({1:"Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"May", 6:"Jun", 7:"Jul", 8:"Aug",
                              9:"Sep", 10:"Oct", 11:"Nov", 12:"Dec"})
df['season'] = df['season'].map({1:"semi", 2:"panas", 3:"gugur", 4:"salju"})
df['weathersit'] = df['weathersit'].map({1:"cerah", 2:"berawan", 3:"hujan ringan", 4:"hujan deras"})

# Main Function
def main():
    data_summary_option = st.checkbox("Tampilkan Data Summary", True)
    if data_summary_option:
        st.header("Data Summary")
        st.write(df.head())
        st.markdown("---")  # Garis horizontal

        st.header("Informasi Statistik Data")
        st.write(df.describe())
        st.markdown("---")  # Garis horizontal

    visualization_option = st.checkbox("Tampilkan Visualisasi Data", True)
    if visualization_option:
        st.header("Visualisasi Data")
        # Visualisasi: Distribusi Jumlah Sepeda yang Disewakan Berdasarkan Musim
        st.subheader("Distribusi Jumlah Sepeda yang Disewakan Berdasarkan Musim")
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        sns.boxplot(data=df, x='season', y='cnt', ax=ax1)
        plt.xlabel('Musim')
        plt.ylabel('Jumlah Sepeda')
        plt.title('Distribusi Jumlah Sepeda yang Disewakan Berdasarkan Musim')
        plt.xticks([0, 1, 2, 3], ['Semi', 'Panas', 'Gugur', 'Salju'])
        st.pyplot(fig1)
        st.markdown("---")  # Garis horizontal

        # Visualisasi: Jumlah Sepeda yang Disewakan Berdasarkan Hari dalam Seminggu
        st.subheader("Jumlah Sepeda yang Disewakan Berdasarkan Hari dalam Seminggu")
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        sns.barplot(data=df, x='weekday', y='cnt', ax=ax2)
        plt.xlabel('Hari dalam Seminggu')
        plt.ylabel('Jumlah Sepeda')
        plt.title('Jumlah Sepeda yang Disewakan Berdasarkan Hari dalam Seminggu')
        plt.xticks([0, 1, 2, 3, 4, 5, 6], ['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu'])
        st.pyplot(fig2)

if __name__ == '__main__':
    main()
