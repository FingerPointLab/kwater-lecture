# 5_chart_실습과제.py
import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(layout = "wide")

# 데이터 불러오기
data = 'data/gdp_by_country.csv'
df = pd.read_csv(data)

# 사이드바
page = st.sidebar.radio("페이지를 선택하세요", ('국가별','대륙별'))

# 메인페이지
st.header("National Statistics")
if page == '국가별':
    ## Countries
    clist = df['country'].unique()
    country = st.selectbox("Select a country:",clist)
    col1, col2 = st.columns(2)
    fig = px.line(df[df['country'] == country], 
                  x = "year", y = "gdpPercap",title = "GDP per Capita")

    col1.plotly_chart(fig,use_container_width = True)
    fig = px.line(df[df['country'] == country], 
                  x = "year", y = "pop",title = "Population Growth")

    col2.plotly_chart(fig,use_container_width = True)
else:
    ## Continents
    contlist = df['continent'].unique()

    continent = st.selectbox("Select a continent:",contlist)
    col1,col2 = st.columns(2)
    fig = px.line(df[df['continent'] == continent], 
                  x = "year", y = "gdpPercap",
    title = "GDP per Capita",color = 'country')

    col1.plotly_chart(fig)
    fig = px.line(df[df['continent'] == continent], 
                  x = "year", y = "pop",
    title = "Population",color = 'country')

    col2.plotly_chart(fig, use_container_width = True)