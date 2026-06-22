import streamlit as st

# -------------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------------

st.set_page_config(
    page_title="FitSense AI",
    page_icon="🏋️",
    layout="wide"
)

# -------------------------------------------------------
# TITLE
# -------------------------------------------------------

st.title("🏋️ FitSense AI")
st.caption("Your Personal Health Companion")

st.write(
    "Calculate your BMI, estimate your daily calorie needs, "
    "and receive personalized health recommendations."
)

# -------------------------------------------------------
# SIDEBAR
# -------------------------------------------------------

st.sidebar.header("👤 Enter Your Details")

name = st.sidebar.text_input("Name")

age = st.sidebar.number_input(
    "Age",
    min_value=1,
    max_value=120,
    value=21
)

gender = st.sidebar.selectbox(
    "Gender",
    ["Male", "Female"]
)

height = st.sidebar.number_input(
    "Height (metres)",
    min_value=0.50,
    max_value=2.50,
    value=1.70
)

weight = st.sidebar.number_input(
    "Weight (kg)",
    min_value=10.0,
    max_value=250.0,
    value=70.0
)

activity = st.sidebar.selectbox(
    "Activity Level",
    [
        "Sedentary",
        "Lightly Active",
        "Moderately Active",
        "Very Active",
        "Extremely Active"
    ]
)

goal = st.sidebar.selectbox(
    "Fitness Goal",
    [
        "Lose Weight",
        "Maintain Weight",
        "Gain Muscle"
    ]
)

calculate = st.sidebar.button("🚀 Calculate")

# -------------------------------------------------------
# MAIN PROGRAM
# -------------------------------------------------------

if calculate:

    bmi = weight / (height ** 2)

    # BMI Category
    if bmi < 18.5:
        category = "Underweight"
        color = "warning"

    elif bmi < 25:
        category = "Healthy"
        color = "success"

    elif bmi < 30:
        category = "Overweight"
        color = "warning"

    else:
        category = "Obese"
        color = "error"

    # ---------------------------------------------------
    # BMR
    # ---------------------------------------------------

    height_cm = height * 100

    if gender == "Male":
        bmr = (10 * weight) + (6.25 * height_cm) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height_cm) - (5 * age) - 161

    # ---------------------------------------------------
    # Activity Multipliers
    # ---------------------------------------------------

    activity_factor = {
        "Sedentary": 1.2,
        "Lightly Active": 1.375,
        "Moderately Active": 1.55,
        "Very Active": 1.725,
        "Extremely Active": 1.9
    }

    maintenance = bmr * activity_factor[activity]

    if goal == "Lose Weight":
        target = maintenance - 500

    elif goal == "Gain Muscle":
        target = maintenance + 300

    else:
        target = maintenance

    # ---------------------------------------------------
    # EXTRA CALCULATIONS
    # ---------------------------------------------------

    water = weight * 0.035

    protein = weight * 1.2

    ideal_min = 18.5 * (height ** 2)

    ideal_max = 24.9 * (height ** 2)

    # ---------------------------------------------------
    # HEADER
    # ---------------------------------------------------

    st.success(f"Welcome, {name}! 👋")

    # ---------------------------------------------------
    # TWO COLUMN LAYOUT
    # ---------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📊 BMI Result")

        st.metric("BMI", f"{bmi:.2f}")

        if color == "success":
            st.success(f"🟢 {category}")
            st.balloons()

        elif color == "warning":
            st.warning(f"🟠 {category}")

        else:
            st.error(f"🔴 {category}")

        # BMI Progress

        bmi_progress = min(bmi / 40, 1.0)

        st.write("BMI Scale")

        st.progress(bmi_progress)

        st.write(f"Healthy BMI Range: **18.5 - 24.9**")

    with col2:

        st.subheader("❤️ Health Summary")

        st.metric("🔥 BMR", f"{bmr:.0f} kcal/day")

        st.metric(
            "🍽 Daily Calories",
            f"{target:.0f} kcal/day"
        )

        st.metric(
            "💧 Water Intake",
            f"{water:.1f} L/day"
        )

        st.metric(
            "💪 Protein",
            f"{protein:.0f} g/day"
        )

    st.divider()

    st.subheader("🎯 Ideal Weight Range")

    st.write(
        f"Your healthy weight range is **{ideal_min:.1f} kg - {ideal_max:.1f} kg**."
    )

    st.divider()

    st.subheader("💡 Health Advice")

    if category == "Underweight":

        st.info(
            """
• Eat protein-rich meals.

• Include healthy fats.

• Begin light strength training.

• Sleep at least 8 hours.
"""
        )

    elif category == "Healthy":

        st.success(
            """
🎉 Excellent!

Keep exercising regularly.

Stay hydrated.

Maintain a balanced diet.

Keep up the great work!
"""
        )

    elif category == "Overweight":

        st.warning(
            """
• Walk at least 8,000 steps daily.

• Reduce sugary foods.

• Increase protein intake.

• Exercise 4-5 times a week.
"""
        )

    else:

        st.error(
            """
• Consult a healthcare professional if needed.

• Start with light physical activity.

• Avoid processed foods.

• Stay consistent—small changes matter.
"""
        )

    st.divider()

    st.caption(
        "⚠ This calculator provides general wellness guidance and is not a substitute for professional medical advice."
    )