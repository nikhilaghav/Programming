import streamlit as st

st.title("Interest calculator")

amount = st.number_input("Enter amount",value = 0)
ROI= st.number_input("Enter Rate of interest",value = 0)
time= st.number_input("Enter time period",value = 0)

if st.button("calculate"):
    SI = (amount * ROI * time)/100

    st.write("Simple interest will be:",SI)    