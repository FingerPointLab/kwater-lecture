# 5_chart_3.py
import streamlit as st
import numpy as np
import plotly.figure_factory as ff

# 임의의 histogram data 생성
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# 데이터를 하나의 리스트로 묶기
hist_data = [x1, x2, x3]
group_labels = ['Group 1', 'Group 2', 'Group 3']

# 데이터의 빈도를 나타내는 히스토그램 차트 생성하기
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# 차트 출력
st.plotly_chart(fig, use_container_width=True)