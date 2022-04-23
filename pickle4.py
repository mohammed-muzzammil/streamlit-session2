import pickle
import streamlit as st
import os

# Header
st.title("Salary prediction model with pickle")

# Import the machine learning model using pickle
with open('/Users/macbook/Downloads/Model.pkl', 'rb') as f:
    regressor = pickle.load(f)


# Function to predict salary based on experience

yoe = st.slider('Years of Experience', 0, 10)
if st.button('Predict'):
    salary = regressor.predict([[yoe]])

    st.success('Salary is $ {}'.format(salary))


