[15:05, 4/5/2026] Abhishek Jagdale: import streamlit as st

Title and header

st.title("Simple Streamlit Application")

st header User Input and Display Demo")

User input widgets

namest text input("Enter your name:"

agest number input("Enter your age", min value=1, max value=100)

color st.selectbox("Choose your favorite color", ["Red", "Blue", "Green"])

Button

if st.button("Submit"):

st.success("Data submitted successfully!")
[15:05, 4/5/2026] Abhishek Jagdale: st.write("Name:", name)

st.write("Age:", age)

st.write("Favorite Color:", color)

# Display text and markdown

st.markdown("### This is a Markdown heading")

st.text("This is plain text output")
