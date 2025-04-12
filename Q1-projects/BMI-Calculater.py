import streamlit as st
import pandas as pd

# set up our App
st.set_page_config(page_title="BMI Calculater",layout='centered')

# Title
st.title("**BMI Calculater**")

# Header
st.header("Welcome To BMI Calculater :sunglasses:")

# SubHeader
st.subheader("*Height*")

# Slider bar
height =st.slider("Enter your hight (in cm):",100,250,175)

# SubHeader
st.subheader("*weight*")

# Slider bar
weight =st.slider("Enter your weight (in kg):",40,200,70)


# Reuslt
bmi = (weight/(height/100)**2)
# show  user result
st.write(f" your bmi is {bmi:.2f}")

# difaine  user BMI Catagories.

st.write("###BMI CATAGORIES")

st.write("-Under Weight: BMI less then 18.5")

st.write("-Normal Weight: BMI b/w 18.5Kg & 24.9Kg")

st.write("-Over Weight: BMI b/w 25Kg & 29.9Kg")

st.write("-Obesity: BMI 30 or Greater")

