# 5_chart_1.py
import streamlit as st
import pandas as pd
import plotly.express as px

# 데이터 불러오기
data = 'data/gdp_by_country.csv'
df = pd.read_csv(data)

# 원본 데이터에서 국가명 리스트 가져오기
clist = df['country'].unique()

# 사이드바에서 국가명 선택
country = st.sidebar.selectbox("국가를 선택하세요:",clist)

# 메인화면
st.subheader('GDP per Capita over time')

# 선택한 국가명에 따라 연도별 gdp 추이를 라인 그래프 설정하기
fig = px.line(df[df['country'] == country], 
    x = "year", y = "gdpPercap", title = country)

# plotly 그래프 출력하기
st.plotly_chart(fig)


# 원본 데이터에서 선택한 국가의 rawdata 확인하기
st.subheader('data')
st.write(df[df['country'] == country])