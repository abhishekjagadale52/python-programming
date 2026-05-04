import streamlit as st
def main():
    st.set_page_config(page_title="BMI Health Checker", page_icon="⚖️")
    
    st.title("⚖️ BMI Health Checker")
    st.write("Calculate your Body Mass Index (BMI) to check your health status.")
    # Input Section
    col1, col2 = st.columns(2)
    
    with col1:
        weight = st.number_input("Enter your weight (in kg)", min_value=1.0, value=70.0, step=0.1)
    
    with col2:
        # User can choose height input method
        height_unit = st.radio("Height unit:", ["Meters", "Centimeters"])
        if height_unit == "Meters":
            height = st.number_input("Enter your height (in m)", min_value=0.5, max_value=2.5, value=1.7, step=0.01)
        else:
            height_cm = st.number_input("Enter your height (in cm)", min_value=50.0, max_value=250.0, value=170.0, step=1.0)
            height = height_cm / 100
    if st.button("Calculate BMI"):
        if height > 0:
            # BMI Formula: weight (kg) / [height (m)]^2
            bmi = weight / (height ** 2)
            
            st.divider()
            st.header(f"Your BMI: {bmi:.2f}")
            # Health Categories
            if bmi < 18.5:
                st.warning("Category: Underweight")
                st.info("💡 Recommendation: Consult a healthcare provider about reaching a healthy weight.")
            elif 18.5 <= bmi < 24.9:
                st.success("Category: Normal weight")
                st.info("✨ Great job! Maintaining a healthy weight reduces health risks.")
            elif 25 <= bmi < 29.9:
                st.warning("Category: Overweight")
                st.info("💡 Recommendation: Consider a balanced diet and regular physical activity.")
            else:
                st.error("Category: Obesity")
                st.info("💡 Recommendation: Speak with a doctor regarding weight management and health risks.")
            
            # Show BMI Reference Table
            with st.expander("See BMI Categories Reference"):
                st.write("""

| BMI Range | Category |
| :--- | :--- |
| Below 18.5 | Underweight |
| 18.5 – 24.9 | Normal Weight |
| 25.0 – 29.9 | Overweight |
| 30.0 and Above | Obesity |

                """)
        else:
            st.error("Height must be greater than zero.")
if _name_ == "_main_":
    main()
