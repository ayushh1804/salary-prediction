import streamlit as st
from predict import show_prediction
from explore import show_explore
page = st.sidebar.selectbox("Explore or Predict",("Predict","Explore"))

if page == "Predict":
    show_prediction()
else:
    show_explore()