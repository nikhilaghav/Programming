import streamlit as st

st.title("Even or Odd")

no = st.number_input("Enter number",value = 0)

if st.button("check"):
    if no % 2 ==0:
        st.write("Number is Even")
    else:
        st.write("Number is odd")    
    