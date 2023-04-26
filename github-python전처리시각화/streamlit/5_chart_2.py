# 5_chart_2.py
import streamlit as st
import pandas as pd
import plotly.express as px

# 데이터 불러오기
data = 'data/gdp_by_country.csv'
df = pd.read_csv(data)

# 원본 데이터에서 대륙명 리스트 가져오기
ctnlist = df['continent'].unique()

# 사이드바에서 대륙 선택
ctn_selected = st.sidebar.selectbox("대륙을 선택하세요:",ctnlist)

# 원본 데이터셋에서 필터링하기
df_filtered = df[df['continent'] == ctn_selected]

# 막대그래프 그리기
st.header('대륙별 인구변화 추이')
fig = px.bar(df_filtered, x='year', y='pop', color='country')
st.plotly_chart(fig)