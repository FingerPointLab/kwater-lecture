import streamlit as st
import pandas as pd
import plotly.express as px

# Set page title
st.set_page_config(page_title='CO₂ Emissions Dashboard', page_icon=':chart_with_upwards_trend:')

# Set app header
st.header('CO₂ Emissions Dashboard')

# Load data from GitHub
file = 'data/co2.csv'
df = pd.read_csv(file, usecols=['Entity', 'Year', 'Code', 'Annual CO₂ emissions'])

# 연도 데이터를 정수형으로 변경
df['Year'] = df['Year'].astype(int)

# Slider에서 연도 선택하기
selected_year = st.select_slider('연도를 선택하세요', options=df['Year'])

# 연도별 데이터셋 필터링
data = df[df['Year'] == selected_year]

# Create a choropleth map using Plotly Express
fig = px.choropleth(data_frame=data,
                    locations='Code',
                    color='Annual CO₂ emissions',
                    hover_name='Entity',
                    title=f'CO₂ Emissions Map ({selected_year})')
st.plotly_chart(fig)

# 국가선택(복수선택)
countries = st.multiselect('국가명 선택(복수선택)', options=data['Entity'].unique())

# 선택한 국가명으로 데이터셋 필터링
data = data[data['Entity'].isin(countries)]

# bar chart를 이용하여 선택한 연도와 국가들의 이산화탄소 배출량 비교
fig = px.bar(data_frame=data,
             x='Entity',
             y='Annual CO₂ emissions',
             color='Entity',
             title=f'국가별 CO₂ 배출량 비교 ({selected_year})')
st.plotly_chart(fig)