import streamlit as st
import pandas as pd
import numpy as np
import pickle

from xgboost import XGBRegressor

# Load model dari file pickle
with open('XGBoostModel_CaliforniaHouse.sav', 'rb') as file:
    model = pickle.load(file)

# Custom CSS style
st.markdown("""
    <style>
    .main {
        background-color: #ffffff;
    }
    .custom-header {
        background: linear-gradient(90deg, #e9dc3c, #F0FF00);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 30px;
    }
    .custom-header h1 {
        font-size: 45px;
        color: #000000;
        margin: 0;
    }
    .custom-header p {
        margin: 5px 0 0;
        font-size: 18px;
        color: #000000;
    }
    .stButton>button {
        margin-top: 20px;
        background-color: #F0FF00;
        color: black;
        border-radius: 10px;
        padding: 14px 32px;
        border: none;
        font-size: 22px;
        display: inline-block;
    }
    .stButton {
        text-align: center;
    }
    .stButton>button:hover {
        background-color: #e9dc3c;
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

# Header dengan icon dan custom style
st.markdown("""
    <div class="custom-header">
        <h1>Say White Machine Learning for California Housing Price</h1>
        <p>🏡 Machine Learning untuk Memprediksi Harga Properti di Wilayah California 🏡</p>
    </div>
""", unsafe_allow_html=True)

# Form input data dari user
st.write("Masukkan data berikut untuk memprediksi harga properti:")

# 1. median_income
st.markdown("**Pendapatan Rata-rata (dalam puluhan ribu USD)**")
st.caption("Minimum Input: 0.5 | Maximum Input: 15.0")
median_income = st.number_input('Pendapatan Rata-rata', min_value=0.5, max_value=15.0, value=3.8, label_visibility='collapsed'
)
# 2. housing_median_age
st.markdown("**Usia Bangunan (tahun)**")
st.caption("Minimum Input: 1 | Maximum Input: 52")
housing_median_age = st.number_input('Usia Median Bangunan', min_value=1, max_value=52, value=29, label_visibility='collapsed'
)
# 3. total_rooms
st.markdown("**Jumlah Ruangan di Blok Hunian**")
st.caption("Minimum Input: 2 | Maximum Input: 32627")
total_rooms = st.number_input('Jumlah Ruangan', min_value=2, max_value=32627, value=2640, label_visibility='collapsed'
)
# 4. total_bedrooms
st.markdown("**Jumlah Kamar Tidur di Blok Hunian**")
st.caption("Minimum Input: 1 | Maximum Input: 6445")
total_bedrooms = st.number_input('Jumlah Kamar Tidur', min_value=1, max_value=6445, value=538, label_visibility='collapsed'
)
# 5. population
st.markdown("**Populasi Penduduk di Blok Hunian**")
st.caption("Minimum Input: 3 | Maximum Input: 35682")
population = st.number_input('Jumlah Penduduk', min_value=3, max_value=35682, value=1425, label_visibility='collapsed'
)
# 6. households
st.markdown("**Jumlah Rumah Tangga di Blok Hunian**")
st.caption("Minimum Input: 1 | Maximum Input: 6082")
households = st.number_input('Jumlah Rumah Tangga', min_value=1, max_value=6082, value=499, label_visibility='collapsed'
)
# 7. latitude
st.markdown("**Latitude Lokasi Properti**")
st.caption("Minimum Input: 32.54 | Maximum Input: 41.95")
latitude = st.number_input('Latitude', min_value=32.54, max_value=41.95, value=35.63, label_visibility='collapsed'
)
# 8. longtitude 
st.markdown("**Longitude Lokasi Properti**")
st.caption("Minimum Input: -124.35 | Maximum Input: -114.31")
longitude = st.number_input('Longitude', min_value=-124.35, max_value=-114.31, value=-119.57, label_visibility='collapsed'
)
# 9. ocean_proximity
st.markdown("**Jarak ke Laut (Ocean Proximity)**")
ocean_proximity = st.selectbox(
    'Ocean Proximity',
    ['INLAND', 'NEAR OCEAN', 'NEAR BAY', '<1H OCEAN']
)

# Buat dataframe dari input user
input_data = pd.DataFrame([{
    'median_income': median_income,
    'housing_median_age': housing_median_age,
    'total_rooms': total_rooms,
    'total_bedrooms': total_bedrooms,
    'population': population,
    'households': households,
    'latitude': latitude,
    'longitude': longitude,
    'ocean_proximity': ocean_proximity
}])

# Tombol Prediksi
if st.button('🔍 Prediksi Harga Properti'):
    result = model.predict(input_data)
    st.success(f"Harga properti diprediksi sekitar **${result[0]:,.2f}**")

# Footer
st.markdown("---")
st.caption("Created by M Narendra Atma Ghifari | 2025")
