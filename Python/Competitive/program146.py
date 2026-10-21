import streamlit as st

st.title("celsius to fahreinhet conversion")

temp= st.number_input("Enter temperature in celsius",value = 0)

if st.button("convert"):
    fah = (temp * 1.8) + 32

    st.write("temperature in fahreinheit is:",fah)