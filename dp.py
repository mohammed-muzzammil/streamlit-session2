import streamlit as st
import pandas as pd
import os

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


def main():
    file_upload_options()
    missing_value_options()
    download_file()


main()
