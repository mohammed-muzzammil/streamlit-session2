import streamlit as st
import pandas as pd
import os
import streamlit_authenticator as stauth

# Enter the path here where all the temporary files will be stored
# For windows, use '\\' instead of '/'
# For linux or macOS, use '/'
temp = '/temp.csv'

path = os.getcwd()
path = path + temp

# Data Preprocessing Application

st.title("Data Preprocessing")


# File uploader

def file_uploader_csv():
    file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])
    if file is not None:
        if st.sidebar.button("Upload"):
            df = pd.read_csv(file)
            df.to_csv(path)
            st.write(df)


def file_uploader_xlsx():
    file = st.sidebar.file_uploader("Upload an XLSX file", type=["xlsx"])
    if file is not None:
        if st.sidebar.button("Upload"):
            df = pd.read_excel(file)
            df.to_csv(path)
            st.write(df)


def file_upload_options():
    st.sidebar.header("File Uploader")
    choice = st.sidebar.radio("File Upload Options", ("CSV", "XLSX"))
    if choice == "CSV":
        file_uploader_csv()
    elif choice == "XLSX":
        file_uploader_xlsx()


# Missing value treatment

def missing_value_options():
    st.sidebar.header("Missing Value Treatment")
    choice = st.sidebar.radio("Missing Value Options", ("Mean Method", "Median Method"))
    if choice == "Mean Method":
        if st.sidebar.button("Process"):
            mean_method()
    elif choice == "Median Method":
        if st.sidebar.button("Process"):
            median_method()


def mean_method():
    df = pd.read_csv(path)
    df.fillna(df.mean(), inplace=True)
    st.dataframe(df)
    df.to_csv(path)
    return


def median_method():
    df = pd.read_csv(path)
    df.fillna(df.median(), inplace=True)
    st.dataframe(df)
    df.to_csv(path)
    return


# Feature Scaling

def feature_scaling_options():
    st.sidebar.header("Feature Scaling")
    choice = st.sidebar.radio("Feature Scaling Options", ("None", "Standardization"))
    if choice == "None":
        pass
    elif choice == "Standardization":
        if st.sidebar.button("Process Standardization"):
            standardization()


def standardization():
    df = pd.read_csv(path)
    df = (df - df.mean()) / df.std()
    st.dataframe(df)
    df.to_csv(path)


# Download CSV
def download_file():
    st.sidebar.title("Data Export")
    if st.sidebar.checkbox("Download CSV"):
        st.write("Export data will be")
        df = pd.read_csv(path)
        st.dataframe(df)
        if st.sidebar.button("Export data"):
            download_csv()


def download_csv():
    st.download_button(
        "Download CSV",
        file_name="data.csv",
        data=path,
        mime="text/csv"
    )


def auth():
    names = ['Mohammed Muzzammil']
    usernames = ['mmuzz', 'thescholar']
    passwords = ['123', '234']
    hashed_passwords = stauth.hasher(passwords).generate()

    authenticator = stauth.authenticate(names, usernames, hashed_passwords,
                                        'some_cookie_name', 'some_signature_key', cookie_expiry_days=30)

    name, authentication_status = authenticator.login('Login', 'main')
    return authentication_status


def main():
    file_upload_options()
    missing_value_options()
    feature_scaling_options()
    download_file()


authentication_status = auth()

if authentication_status:
    main()
if authentication_status is None:
    st.info('Please login to use the application')
elif not authentication_status:
    st.info('Your username or password is incorrect')
