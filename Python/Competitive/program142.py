import streamlit as st

st.title("Addition")

no1 = st.number_input("Enter first number",value = 0)
no2 = st.number_input("Enter second number",value = 0)

if st.button("Addition"):
    Ans = no1 + no2
    st.success("Addition is:"+str(Ans))
