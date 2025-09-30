import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.divider()
st.header('Streamlit 주요 요소 예시', divider='rainbow')
st.write("아래는 Streamlit에서 사용할 수 있는 다양한 UI 요소들의 예시입니다.")

with st.expander("예시 펼쳐보기"):
    # 텍스트 요소
    st.subheader('텍스트 요소')
    st.write('일반 텍스트(write)')
    st.markdown('**마크다운**을 이용한 _텍스트_')
    st.code("print('Hello Streamlit!')", language='python')

    # 데이터 표시
    st.subheader('데이터 표시')
    df_example = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    st.dataframe(df_example)
    st.table(df_example)

    # Matplotlib 차트 표시
    st.subheader('Matplotlib 차트')
    fig, ax = plt.subplots()
    ax.plot(df_example['A'], df_example['B'])
    ax.set_title("Matplotlib Chart Example")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    st.pyplot(fig)

    # 미디어 요소
    st.subheader('미디어 요소')
    st.image('https://static.streamlit.io/examples/dog.jpg', caption='강아지 이미지', width=300)

    # 입력 위젯
    st.subheader('입력 위젯')
    st.text_input('이름을 입력하세요')
    st.number_input('나이', min_value=0, max_value=120, value=25)
    st.checkbox('동의하십니까?')
    st.radio('좋아하는 색상은?', ['빨강', '파랑', '초록'])
    st.selectbox('취미를 선택하세요', ['독서', '운동', '게임'])
    st.multiselect('여러 취미를 선택하세요', ['독서', '운동', '게임'])
    st.date_input('날짜를 선택하세요')
    st.time_input('시간을 선택하세요')
    st.file_uploader('파일을 업로드하세요')
    st.button('클릭 버튼')

    # 슬라이더
    st.subheader('슬라이더')
    st.slider('값을 선택하세요', 0, 100, 50)

    # 레이아웃
    st.subheader('레이아웃')
    col1, col2 = st.columns(2)
    col1.write('왼쪽 컬럼')
    col2.write('오른쪽 컬럼')

    tab1, tab2 = st.tabs(['탭 1', '탭 2'])
    tab1.write('첫 번째 탭 내용')
    tab2.write('두 번째 탭 내용')

    # 상태 표시
    st.subheader('상태 표시')
    st.progress(70)
    with st.spinner('로딩 중...'):
        st.write("처리 완료!")

    st.success('성공 메시지')
    st.error('에러 메시지')
    st.warning('경고 메시지')
    st.info('정보 메시지')