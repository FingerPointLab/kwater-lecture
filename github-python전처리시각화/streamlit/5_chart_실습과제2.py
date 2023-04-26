# 5_chart_실습과제2.py
import streamlit as st
import pandas as pd
import plotly.express as px

# 데이터 불러오기
data = 'data/gdp_by_country.csv'
df = pd.read_csv(data)

# 연도 리스트
yearlist = df['year'].unique()

# 연도 선택
input_year = st.select_slider('연도를 선택하세요', options=yearlist)

# dataset 필터링
dataset = df.query(f"year=={input_year}")

# chart 설정
fig = px.scatter(
    dataset,
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

tab1, tab2 = st.tabs(["chart", "Data"])
with tab1:
    st.subheader(f"{input_year}년도 대륙별 gdp와 기대수명 상관관계")
    # chart 출력
    st.plotly_chart(fig, use_container_width=True)
with tab2:
    st.subheader(f"{input_year}")
    # dataset 출력
    st.write(dataset)