import streamlit as st
import pandas as pd

# 제목 및 부제목
st.title("제목")
st.header("헤더")
st.subheader("서브헤더")


# 텍스트
st.write("텍스트")

# 데이터프레임 표현
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)