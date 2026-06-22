import streamlit as st

# ----------------------------
# Title
# ----------------------------
st.set_page_config(page_title="BMI AI Assistant", page_icon="🏋️")

st.title("🏋️ BMI AI Assistant")
st.write("Know your Body Mass Index and receive basic health recommendations.")

# ----------------------------
# User Details
# ----------------------------

name = st.text_input("👤 Enter Your Name")

age = st.number_input("🎂 Enter Your Age", min_value=1, max_value=120)

gender = st.selectbox(
    "🚻 Select Your Gender",
    ["Male", "Female"]
)

weight = st.number_input(
    "⚖️ Enter Your Weight (kg)",
    min_value=1.0
)

height = st.number_input(
    "📏 Enter Your Height (metres)",
    min_value=0.5
)

activity = st.selectbox(
    "🏃 Activity Level",
    [
        "Sedentary",
        "Lightly Active",
        "Moderately Active",
        "Very Active"
    ]
)

goal = st.selectbox(
    "🎯 Fitness Goal",
    [
        "Lose Weight",
        "Maintain Weight",
        "Gain Muscle"
    ]
)

# ----------------------------
# BMI Calculation
# ----------------------------

if st.button("🚀 Calculate BMI"):

    bmi = weight / (height ** 2)

    st.subheader(f"Hello {name} 👋")

    st.write(f"### Your BMI is **{bmi:.2f}**")

    # BMI Category

    if bmi < 18.5:
        st.warning("🟡 You are Underweight")

    elif bmi < 25:
        st.success("🟢 You are in the Healthy Range")
        st.balloons()

    elif bmi < 30:
        st.warning("🟠 You are Overweight")

    else:
        st.error("🔴 You are Obese")

    # ----------------------------
    # Extra Information
    # ----------------------------

    water = weight * 0.035
    protein = weight * 1.2

    st.divider()

    st.subheader("📋 Health Summary")

    st.write(f"💧 Recommended Water Intake: **{water:.1f} litres/day**")

    st.write(f"💪 Recommended Protein Intake: **{protein:.0f} g/day**")

    st.write(f"🏃 Activity Level: **{activity}**")

    st.write(f"🎯 Goal: **{goal}**")

    st.divider()

    st.info(
        "💡 Health Tip: Consistency beats perfection. "
        "Exercise regularly, stay hydrated, sleep well, and eat a balanced diet."
    )