# 4_layout_1.py
import streamlit as st

st.header('columns')

# column layout
col1, col2, col3 = st.columns(3)

with col1:
    st.header('col1')
    
with col2:
    st.header('col2')
    
with col3:
    st.header('col3')
    

# sidebar
st.sidebar.header('sidebar')

st.sidebar.date_input('날짜를 선택하세요.')