import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Streamlit 요소 예시")  # 페이지 제목

st.header("텍스트 요소")  # 텍스트 관련 요소
st.write("이것은 일반 텍스트입니다.")  # 일반 텍스트
st.markdown("**마크다운** _지원_")  # 마크다운 지원
st.code("print('Hello Streamlit!')", language='python')  # 코드 블록

st.header("데이터 표시")  # 데이터프레임, 테이블 등
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})
st.dataframe(df)  # 동적 데이터프레임
st.table(df)      # 정적 테이블

st.header("차트 및 시각화")  # 차트 예시
st.line_chart(df)  # 라인 차트
st.bar_chart(df)   # 바 차트
st.area_chart(df)  # 영역 차트

fig, ax = plt.subplots()
ax.plot(df['A'], df['B'])
st.pyplot(fig)  # Matplotlib 차트

st.header("미디어 요소")  # 이미지, 오디오, 비디오
st.image("https://static.streamlit.io/examples/dog.jpg", caption="강아지 이미지")  # 이미지
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")  # 오디오
st.video("https://www.w3schools.com/html/mov_bbb.mp4")  # 비디오

st.header("입력 위젯")  # 사용자 입력 위젯
name = st.text_input("이름을 입력하세요")  # 텍스트 입력
age = st.number_input("나이", min_value=0, max_value=120)  # 숫자 입력
agree = st.checkbox("동의하십니까?")  # 체크박스
color = st.radio("좋아하는 색상은?", ["빨강", "파랑", "초록"])  # 라디오 버튼
hobby = st.selectbox("취미를 선택하세요", ["독서", "운동", "게임"])  # 셀렉트박스
hobbies = st.multiselect("여러 취미를 선택하세요", ["독서", "운동", "게임"])  # 멀티셀렉트
date = st.date_input("날짜를 선택하세요")  # 날짜 입력
time = st.time_input("시간을 선택하세요")  # 시간 입력
file = st.file_uploader("파일을 업로드하세요")  # 파일 업로더
st.button("버튼 클릭")  # 버튼

st.header("슬라이더")  # 슬라이더 예시
value = st.slider("값을 선택하세요", 0, 100, 50)  # 슬라이더

st.header("레이아웃")  # 컬럼, 탭, 익스팬더 등
col1, col2 = st.columns(2)
col1.write("왼쪽 컬럼")
col2.write("오른쪽 컬럼")

with st.expander("더보기"):
    st.write("익스팬더 안의 내용입니다.")

tab1, tab2 = st.tabs(["탭 1", "탭 2"])
tab1.write("첫 번째 탭 내용")
tab2.write("두 번째 탭 내용")

st.header("상태 표시")  # 진행바, 스피너 등
st.progress(70)  # 진행바
with st.spinner("로딩 중..."):
    st.write("잠시 기다려주세요.")

st.success("성공 메시지")  # 성공 메시지
st.error("에러 메시지")    # 에러 메시지
st.warning("경고 메시지")  # 경고 메시지
st.info("정보 메시지")     # 정보 메시지

# 각 요소마다 주석으로 설명을 달았습니다.import streamlit as st
import pandas as pd
import math
from pathlib import Path

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='GDP dashboard',
    page_icon=':earth_americas:', # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------
# Declare some useful functions.

@st.cache_data
def get_gdp_data():
    """Grab GDP data from a CSV file.

    This uses caching to avoid having to read the file every time. If we were
    reading from an HTTP endpoint instead of a file, it's a good idea to set
    a maximum age to the cache with the TTL argument: @st.cache_data(ttl='1d')
    """

    # Instead of a CSV on disk, you could read from an HTTP endpoint here too.
    DATA_FILENAME = Path(__file__).parent/'data/gdp_data.csv'
    raw_gdp_df = pd.read_csv(DATA_FILENAME)

    MIN_YEAR = 1960
    MAX_YEAR = 2022

    # The data above has columns like:
    # - Country Name
    # - Country Code
    # - [Stuff I don't care about]
    # - GDP for 1960
    # - GDP for 1961
    # - GDP for 1962
    # - ...
    # - GDP for 2022
    #
    # ...but I want this instead:
    # - Country Name
    # - Country Code
    # - Year
    # - GDP
    #
    # So let's pivot all those year-columns into two: Year and GDP
    gdp_df = raw_gdp_df.melt(
        ['Country Code'],
        [str(x) for x in range(MIN_YEAR, MAX_YEAR + 1)],
        'Year',
        'GDP',
    )

    # Convert years from string to integers
    gdp_df['Year'] = pd.to_numeric(gdp_df['Year'])

    return gdp_df

gdp_df = get_gdp_data()

# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
'''
# :earth_americas: GDP dashboard

Browse GDP data from the [World Bank Open Data](https://data.worldbank.org/) website. As you'll
notice, the data only goes to 2022 right now, and datapoints for certain years are often missing.
But it's otherwise a great (and did I mention _free_?) source of data.
'''

# Add some spacing
''
''

min_value = gdp_df['Year'].min()
max_value = gdp_df['Year'].max()

from_year, to_year = st.slider(
    'Which years are you interested in?',
    min_value=min_value,
    max_value=max_value,
    value=[min_value, max_value])

countries = gdp_df['Country Code'].unique()

if not len(countries):
    st.warning("Select at least one country")

selected_countries = st.multiselect(
    'Which countries would you like to view?',
    countries,
    ['DEU', 'FRA', 'GBR', 'BRA', 'MEX', 'JPN'])

''
''
''

# Filter the data
filtered_gdp_df = gdp_df[
    (gdp_df['Country Code'].isin(selected_countries))
    & (gdp_df['Year'] <= to_year)
    & (from_year <= gdp_df['Year'])
]

st.header('GDP over time', divider='gray')

''

st.line_chart(
    filtered_gdp_df,
    x='Year',
    y='GDP',
    color='Country Code',
)

''
''


first_year = gdp_df[gdp_df['Year'] == from_year]
last_year = gdp_df[gdp_df['Year'] == to_year]

st.header(f'GDP in {to_year}', divider='gray')

''

cols = st.columns(4)

for i, country in enumerate(selected_countries):
    col = cols[i % len(cols)]

    with col:
        first_gdp = first_year[first_year['Country Code'] == country]['GDP'].iat[0] / 1000000000
        last_gdp = last_year[last_year['Country Code'] == country]['GDP'].iat[0] / 1000000000

        if math.isnan(first_gdp):
            growth = 'n/a'
            delta_color = 'off'
        else:
            growth = f'{last_gdp / first_gdp:,.2f}x'
            delta_color = 'normal'

        st.metric(
            label=f'{country} GDP',
            value=f'{last_gdp:,.0f}B',
            delta=growth,
            delta_color=delta_color
        )
        
# -----------------------------------------------------------------------------
# Streamlit 주요 요소 예시 (각주 포함)

st.divider()
st.header('Streamlit 주요 요소 예시', divider='rainbow')

# 텍스트 요소
st.subheader('텍스트 요소')  # 텍스트 관련 요소
st.write('이것은 일반 텍스트입니다.')  # 일반 텍스트
st.markdown('**마크다운** _지원_')  # 마크다운 지원
st.code("print('Hello Streamlit!')", language='python')  # 코드 블록

# 데이터 표시
st.subheader('데이터 표시')  # 데이터프레임, 테이블 등
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
st.dataframe(df)  # 동적 데이터프레임
st.table(df)      # 정적 테이블



# 미디어 요소
st.subheader('미디어 요소')  # 이미지, 오디오, 비디오
st.image('https://static.streamlit.io/examples/dog.jpg', caption='강아지 이미지')  # 이미지
st.audio('https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3')  # 오디오
st.video('https://www.w3schools.com/html/mov_bbb.mp4')  # 비디오

# 입력 위젯
st.subheader('입력 위젯')  # 사용자 입력 위젯
name = st.text_input('이름을 입력하세요')  # 텍스트 입력
age = st.number_input('나이', min_value=0, max_value=120)  # 숫자 입력
agree = st.checkbox('동의하십니까?')  # 체크박스
color = st.radio('좋아하는 색상은?', ['빨강', '파랑', '초록'])  # 라디오 버튼
hobby = st.selectbox('취미를 선택하세요', ['독서', '운동', '게임'])  # 셀렉트박스
hobbies = st.multiselect('여러 취미를 선택하세요', ['독서', '운동', '게임'])  # 멀티셀렉트
date = st.date_input('날짜를 선택하세요')  # 날짜 입력
time = st.time_input('시간을 선택하세요')  # 시간 입력
file = st.file_uploader('파일을 업로드하세요')  # 파일 업로더
st.button('버튼 클릭')  # 버튼

# 슬라이더
st.subheader('슬라이더')  # 슬라이더 예시
value = st.slider('값을 선택하세요', 0, 100, 50)  # 슬라이더

# 레이아웃
st.subheader('레이아웃')  # 컬럼, 탭, 익스팬더 등
col1, col2 = st.columns(2)
col1.write('왼쪽 컬럼')
col2.write('오른쪽 컬럼')

with st.expander('더보기'):
    st.write('익스팬더 안의 내용입니다.')

tab1, tab2 = st.tabs(['탭 1', '탭 2'])
tab1.write('첫 번째 탭 내용')
tab2.write('두 번째 탭 내용')

# 상태 표시
st.subheader('상태 표시')  # 진행바, 스피너 등
st.progress(70)  # 진행바
with st.spinner('로딩 중...'):
    st.write('잠시 기다려주세요.')

st.success('성공 메시지')  # 성공 메시지
st.error('에러 메시지')    # 에러 메시지
st.warning('경고 메시지')  # 경고 메시지
st.info('정보 메시지')     # 정보 메시지

# 각 요소마다 주석으로 설명을 달았습니다.
