import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
import pickle

# Header aplikasi
st.title("Aplikasi perceptron dengan Streamlit")
st.write("Aplikasi ini menggunakan algoritma perceptron untuk klasifikasi data pumpkin seeds.")

# Muat model yang sudah disimpan
with open ('pumpin-perceptron.pkl', 'rb') as file:
    model = pickle.load(file)

 # Input fitur
area = st.number_input("Area", min_value=0.0, step=0.1)
perimeter = st.number_input("Perimeter", min_value=0.0, step=0.1)
major_axis_length = st.number_input("Major Axis Length", min_value=0.0, step=0.1)
minor_axis_length = st.number_input("Minor Axis Length", min_value=0.0, step=0.1)
convex_area = st.number_input("Convex Area", min_value=0.0, step=0.1)
equiv_diameter = st.number_input("Equivalent Diameter", min_value=0.0, step=0.1)
eccentricity = st.number_input("Eccentricity", min_value=0.0, step=0.01)
solidity = st.number_input("Solidity", min_value=0.0, step=0.01)
extent = st.number_input("Extent", min_value=0.0, step=0.01)
roundness = st.number_input("Roundness", min_value=0.0, step=0.01)
aspect_ratio = st.number_input("Aspect Ratio", min_value=0.0, step=0.01)
compactness = st.number_input("Compactness", min_value=0.0, step=0.01)
    # Prediksi berdasarkan input

if st.button("Prediksi"):
    if area > 0 and perimeter > 0 and major_axis_length > 0 and minor_axis_length > 0 and convex_area > 0 and equiv_diameter > 0 and eccentricity > 0 and solidity > 0 and extent > 0 and roundness > 0 and aspect_ratio > 0 and compactness > 0:
        prediction = model.predict([[area, perimeter, major_axis_length, minor_axis_length, convex_area, equiv_diameter, eccentricity, solidity, extent, roundness, aspect_ratio, compactness]])
        st.success(f'Prediksi biji labu: {prediction[0]}')


