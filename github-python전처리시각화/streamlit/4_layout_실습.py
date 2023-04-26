# layout
import streamlit as st

st.header('columns')


# sidebar
input1 = st.sidebar.selectbox('이미지를 선택하세요', ['클릭','cat','dog'])

# column layout
col1, col2 = st.columns(2)

with col1:
    st.header('이미지')
    if input1 == 'cat':
        st.image("images/cat.jpg", use_column_width=True)
    elif input1 == 'dog':
        st.image("images/dog.jpg", use_column_width=True)
    else:
        st.write('sidebar에서 cat / dog 중에서 선택하세요.')
with col2:
    if st.button('울음소리'):
        if input1 == 'cat':
            st.write('야옹')
        elif input1 == 'dog':
            st.write('멍멍')    
        else:
            st.write('sidebar에서 cat / dog 중에서 선택하세요.')