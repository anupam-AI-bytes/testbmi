import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import random

st.set_page_config(page_title="FitSense AI v1.2", page_icon="🏋️", layout="wide")

st.title("🏋️ FitSense AI")
st.caption("Version 1.2 • Professional Dashboard")

st.sidebar.header("👤 Enter Your Details")
name=st.sidebar.text_input("Name")
age=st.sidebar.number_input("Age",1,120,21)
gender=st.sidebar.selectbox("Gender",["Male","Female"])
height=st.sidebar.number_input("Height (m)",0.5,2.5,1.70)
weight=st.sidebar.number_input("Weight (kg)",10.0,250.0,70.0)
activity=st.sidebar.selectbox("Activity",["Sedentary","Lightly Active","Moderately Active","Very Active","Extremely Active"])
goal=st.sidebar.selectbox("Goal",["Lose Weight","Maintain Weight","Gain Muscle"])

if st.sidebar.button("🚀 Calculate"):
    bmi=weight/(height**2)
    if bmi<18.5:
        category="Underweight"; msg=st.warning
    elif bmi<25:
        category="Healthy"; msg=st.success
    elif bmi<30:
        category="Overweight"; msg=st.warning
    else:
        category="Obese"; msg=st.error

    hcm=height*100
    bmr=(10*weight)+(6.25*hcm)-(5*age)+(5 if gender=="Male" else -161)
    factors={"Sedentary":1.2,"Lightly Active":1.375,"Moderately Active":1.55,"Very Active":1.725,"Extremely Active":1.9}
    maintenance=bmr*factors[activity]
    target=maintenance-500 if goal=="Lose Weight" else maintenance+300 if goal=="Gain Muscle" else maintenance
    water=weight*0.035
    protein=weight*1.2
    ideal_min=18.5*height**2
    ideal_max=24.9*height**2

    score=100
    if bmi<18.5: score-=20
    elif bmi>=25 and bmi<30: score-=15
    elif bmi>=30: score-=30
    if activity=="Sedentary": score-=15
    elif activity=="Lightly Active": score-=10
    elif activity=="Moderately Active": score-=5
    score=max(score,0)

    st.success(f"Welcome, {name}!")

    c1,c2=st.columns(2)
    with c1:
        st.metric("BMI",f"{bmi:.2f}")
        msg(category)
        if category=="Healthy": st.balloons()
        st.progress(min(bmi/40,1.0))
        fig=go.Figure(go.Indicator(mode="gauge+number",value=bmi,title={"text":"BMI Gauge"},
            gauge={"axis":{"range":[10,40]},
            "steps":[
                {"range":[10,18.5],"color":"lightblue"},
                {"range":[18.5,25],"color":"lightgreen"},
                {"range":[25,30],"color":"orange"},
                {"range":[30,40],"color":"red"}]}))
        st.plotly_chart(fig,use_container_width=True)

    with c2:
        st.metric("Health Score",f"{score}/100")
        st.progress(score/100)
        st.metric("BMR",f"{bmr:.0f} kcal")
        st.metric("Daily Calories",f"{target:.0f} kcal")
        st.metric("Water",f"{water:.1f} L")
        st.metric("Protein",f"{protein:.0f} g")

    st.subheader("🎯 Ideal Weight")
    st.write(f"**{ideal_min:.1f} kg – {ideal_max:.1f} kg**")

    chart=pd.DataFrame({"Metric":["Calories","Protein","Water (ml)"],
                        "Value":[target,protein,water*1000]})
    st.subheader("📈 Nutrition Summary")
    st.bar_chart(chart.set_index("Metric"))

    with st.expander("📚 Learn About BMI"):
        st.markdown("""
- **Underweight:** BMI < 18.5
- **Healthy:** BMI 18.5–24.9
- **Overweight:** BMI 25–29.9
- **Obese:** BMI ≥ 30
""")

    tips={
        "Underweight":"Increase nutritious calories and strength training.",
        "Healthy":"Maintain your healthy lifestyle and stay active.",
        "Overweight":"Aim for regular exercise and reduce sugary foods.",
        "Obese":"Start with small sustainable lifestyle changes and consult a healthcare professional if needed."
    }
    st.info("💡 "+tips[category])

    report=f"""FitSense AI Report

Name: {name}
Age: {age}
Gender: {gender}
BMI: {bmi:.2f}
Category: {category}
BMR: {bmr:.0f}
Daily Calories: {target:.0f}
Water: {water:.1f} L
Protein: {protein:.0f} g
Ideal Weight: {ideal_min:.1f}-{ideal_max:.1f} kg
Health Score: {score}/100
"""
    st.download_button("📄 Download Report",report,file_name="FitSense_Report.txt")

    quotes=[
        "Small progress is still progress. 💪",
        "Consistency beats intensity. 🌱",
        "Health is your greatest investment. ❤️",
        "Stay hydrated and keep moving! 🚶",
        "Every healthy choice counts. ⭐"
    ]
    st.success(random.choice(quotes))
else:
    st.info("Fill in your details from the sidebar and click 'Calculate'.")
