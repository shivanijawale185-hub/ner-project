import streamlit as st
import pandas as pd
import numpy as np

# Page config
st.set_page_config(
    page_title="My Streamlit App",
    page_icon="📊",
    layout="centered"
)

# Title
st.title("📊 Streamlit Demo App")
st.write("This is a simple Streamlit app for deployment.")

# Sidebar
st.sidebar.header("User Input")

number = st.sidebar.number_input("Enter a number", value=5)

# Main logic
st.subheader("Square of the number")
st.write(f"Square of {number} is **{number ** 2}**")

# Sample DataFrame
st.subheader("Sample Data")
df = pd.DataFrame({
    "A": np.random.randint(1, 100, 5),
    "B": np.random.randint(1, 100, 5)
})

st.dataframe(df)

# Chart
st.subheader("Line Chart")
st.line_chart(df)

st.success("App is running successfully 🚀")
