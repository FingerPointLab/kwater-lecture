# 3_wigets_2.py
import streamlit as st
import pandas as pd

# file uploader - 하나의 파일을 업로드
uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'])

if uploaded_file is not None:
    st.write("filename:", uploaded_file.name)
    df = pd.read_csv(uploaded_file)
    st.write(df)


# file uploader - 여러 파일을 업로드
# uploaded_files = st.file_uploader("Choose CSV files", accept_multiple_files=True)

# 반복문을 이용하여 파일을 읽고 출력하기
# if uploaded_files is not None:
#     for uploaded_file in uploaded_files:
#         st.write("filename:", uploaded_file.name)
#         df = pd.read_csv(uploaded_file)
#         st.write(df)