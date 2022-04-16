import streamlit as st
import pandas as pd

# Title
st.title("Streamlit App")

# Inputs

# Text Input
name = st.text_input("Name", "Type your name here")
st.write("Hello, ", name)

# Number Input
age = st.number_input("Age")
st.write(age)

# Checkbox
if st.checkbox("Show Age"):
    st.write(age)

# Radio Button
status = st.radio("Status", ("Single", "Married", "Divorced"))

if status == "Single":
    st.write("You are single")

# Selectbox
occupation = st.selectbox("Occupation", ("Student", "Teacher", "Doctor"))

# Multi-Selectbox
skills = st.multiselect("Skills", ("Python", "Java", "C++", "C#", "JavaScript"))

for skill in skills:
    if skill == "Python":
        st.write("You are a Python programmer cool")

# Slider
age = st.slider("Age", 0, 100)

# Range Slider
age1 = st.slider("Age", 0, 100, (25, 35))
st.write(age1)

# Button
button = st.button("Click Me")
if button:
    st.write("You clicked the button")

# Date Input
date = st.date_input("Date")

# Text Area
text = st.text_area("Text Area")

# sidebar
st.sidebar.header("Sidebar")
st.sidebar.text_input("Text Input")

# File Upload

file_type = st.radio("File Type", ("CSV", "XLSX"))
if file_type == "CSV":
    file = st.file_uploader("Upload CSV File", type="csv")
    if file is not None:
        df = pd.read_csv(file)
        st.dataframe(df)

        st.download_button(
            label="Download data as CSV",
            data=file,
            file_name='large_df.csv',
            mime='text/csv',
        )


elif file_type == "XLSX":
    file = st.file_uploader("Upload XLSX File", type="xlsx")
    if file is not None:
        df = pd.read_excel(file)
        st.dataframe(df)

# Upload jpg image
image = st.file_uploader("Upload an image", type="jpg")
if image is not None:
    st.image(image)
