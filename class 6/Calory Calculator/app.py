import streamlit as st

st.set_page_config(
    page_title="Calorie Calculator",
    page_icon="🔥"
)

st.title("🔥 Calorie Calculator")
st.write("Enter your details to get a simple calorie estimate.")

# User details
name = st.text_input("Enter your name:")

age = st.number_input(
    "Enter your age:",
    min_value=1,
    max_value=100,
    step=1
)

weight = st.number_input(
    "Enter your weight (kg):",
    min_value=1.0,
    max_value=200.0,
    step=0.1
)

height = st.number_input(
    "Enter your height (cm):",
    min_value=50.0,
    max_value=250.0,
    step=0.1
)

# Calculate button
if st.button("🔥 Calculate Calories"):

    if name == "":
        st.warning("Please enter your name.")

    else:
        # Simple calorie estimation
        calories = 10 * weight + 6.25 * height - 5 * age

        st.success(f"Hello, {name}! 👋")

        st.metric(
            "Estimated Daily Energy",
            f"{round(calories, 2)} calories"
        )

        st.info(
            f"Your body may need roughly {round(calories)} calories "
            "of energy per day according to this simple estimate."
        )

        # Activity
        activity = st.radio(
            "Are you active today?",
            ["Yes", "No"]
        )

        if activity == "Yes":
            st.write("🏃 You are active today!")
        else:
            st.write("🚶 Try to stay active with normal daily movement.")

        st.caption(
            "Note: This is a simple educational estimate, not a medical or diet recommendation."
        )
