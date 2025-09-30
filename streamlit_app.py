import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from pathlib import Path

# 페이지 기본 설정 (가장 처음에 한 번만 호출해야 합니다)
st.set_page_config(
    page_title='종합 대시보드',
    page_icon=':chart_with_upwards_trend:',
    layout='wide'
)

# -----------------------------------------------------------------------------
# 1. GDP 대시보드 섹션
# -----------------------------------------------------------------------------

st.title(':earth_americas: GDP 대시보드')
st.markdown("""
[World Bank Open Data](https://data.worldbank.org/)의 GDP 데이터를 살펴보세요.
데이터는 2022년까지이며, 일부 연도의 데이터는 누락될 수 있습니다.
""")

# 데이터 로딩 함수 (캐싱 기능으로 성능 향상)
@st.cache_data
def get_gdp_data():
    """CSV 파일에서 GDP 데이터를 가져옵니다."""
    # 데이터 파일 경로 설정 (데이터 파일은 코드 파일과 같은 폴더 내 'data' 폴더에 있다고 가정)
    # 만약 data 폴더가 없다면 이 부분은 실제 파일 위치에 맞게 수정해야 합니다.
    try:
        DATA_FILENAME = Path(__file__).parent / 'data/gdp_data.csv'
        raw_gdp_df = pd.read_csv(DATA_FILENAME)
    except FileNotFoundError:
        st.error("'data/gdp_data.csv' 파일을 찾을 수 없습니다. 파일 경로를 확인해주세요.")
        return pd.DataFrame() # 파일이 없으면 빈 데이터프레임 반환

    MIN_YEAR = 1960
    MAX_YEAR = 2022

    # 데이터 구조를 (Country, Year, GDP) 형태로 변환 (Melt)
    gdp_df = raw_gdp_df.melt(
        ['Country Code'],
        [str(x) for x in range(MIN_YEAR, MAX_YEAR + 1)],
        'Year',
        'GDP',
    )