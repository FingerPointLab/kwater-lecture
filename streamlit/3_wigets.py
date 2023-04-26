import streamlit as st

st.subheader('버튼')
# 버튼
if st.button("버튼 클릭"):
    st.write("버튼을 클릭하셨습니다..")

    
st.subheader('체크박스')
# 체크박스
checkbox_btn = st.checkbox('Checktbox Button')
# 체크박스 선택 시
if checkbox_btn:
    st.write('체크박스를 클릭하셨습니다..')
    
    
st.subheader('라디오버튼')
# 라디오버튼
selected_item = st.radio("음료 선택", ("아메리카노", "녹차", "물"))

if selected_item == "아메리카노":
  st.write("☕")
elif selected_item == "녹차":
  st.write("🍵")
elif selected_item == "물":
  st.write("💧")


st.subheader('선택 박스(단일)')
# 선택 박스 (단일 선택)
option = st.selectbox('가장 좋아하는 계절은?',
                   ('봄', '여름', '가을', '겨울'))
st.write('가장 좋아하는 계절은:', option)


st.subheader('선택 박스(다중)')
# 선택 박스 (다중 선택)
multi_select = st.multiselect('좋아하는 요일을 모두 선택하세요.',
                            ['월', '화', '수', '목', '금', '토', '일'])
st.write('좋아하는 요일은:', multi_select)


st.subheader('슬라이더')
# 수치 데이터 입력을 위한 슬라이더
# 범위 선택 슬라이더
# st.slider('라벨명', 시작값, 끝값, (default선택범위))
values = st.slider('범위를 설정하세요', 0.0, 100.0, (25.0, 75.0))
st.write('Range:', values)

# 단일 수치 선택 슬라이더
# st.slider('라벨명', 시작값, 끝값
value = st.slider('값을 선택하세요.', 0.0, 100.0)
st.write('Slider number', value)


st.subheader('다양한 형식의 데이터 입력')
# 단순 텍스트 데이터 입력
txt_input = st.text_input('텍스트를 입력하세요.')

# 여러 줄의 텍스트 입력
txt_input_multi = st.text_area('여러 줄의 텍스트를 입력하세요')

# 수치 데이터 입력
txt_input_number = st.text_input('숫자를 입력하세요')

# 날짜 입력
input_date = st.date_input('날짜를 선택하세요')

# 시간 입력
input_time = st.time_input('시간을 선택하세요')