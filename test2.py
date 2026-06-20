import streamlit as st
st.header("Sanyam BMI Calculator")
name = st.text_input("Enter Name")
weight = st.number_input("Enter your Weight in kg")
height = st.number_input("Enter your Height in metres")
st.selectbox("Select Your Gender", ["Male", "Female"])
if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)
    st.write ("Your BMI is: ", bmi)
    if bmi<19:
        st.write("You are Underweight")
    elif bmi>=19 and bmi<25:
        st.write("You are Normal")
    elif bmi>=25 and bmi<30:
        st.write("You are Overweight")
    else:        st.write("You are Obese")

