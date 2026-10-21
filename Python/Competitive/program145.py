import streamlit as st

st.title("Student result calculator")

name= st.text_input("Enter name")
m1= st.number_input("Enter maths marks",value = 0)
m2= st.number_input("Enter science marks",value = 0)
m3= st.number_input("Enter hindi marks",value = 0)

if st.button("calculate"):
    total = m1 + m2 + m3

    st.write("Total marks:",total)

    percentage = (total/300) * 100

    st.write("percenatge:",percentage)

    if m1 < 40:
        st.error("failed in maths")
    else:
        st.success("passed in maths")

    if m2 < 40:
        st.error("failed in science")
    else:
        st.success("passed in science")

    if m1 < 40:
        st.error("failed in hindi")
    else:
        st.success("passed in hindi")            