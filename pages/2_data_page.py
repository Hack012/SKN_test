import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import os
import matplotlib.font_manager as fm

st.title("게임 캐릭터의 인지도")

st.page_link("main_page.py", label="Main으로..", icon="🏠")

@st.cache_data
def fontRegistered():
    font_dirs = [os.getcwd() + '\customFonts']
    print("위치",os.getcwd())
    font_files = fm.findSystemFonts(fontpaths=font_dirs)

    for font_file in font_files:
        fm.fontManager.addfont(font_file)
    fm._load_fontmanager(try_read_cache=False)

data = pd.DataFrame({
    "캐릭터": ["전사", "법사", "힐러", "탱커", "랜덤"],
    "선택횟수": [120, 95, 150, 80, 111],
    "승률 (%)": [52, 48, 56, 60, 49],
    "인지도 (%)": [25, 20, 30, 15, 22]
})

st.dataframe(data, use_container_width=True)

# edited_data = st.data_editor(data)
# st.write(edited_data)

st.bar_chart(data.set_index('캐릭터')['선택횟수'])
st.line_chart(data.set_index('캐릭터')['승률 (%)'])

fontRegistered()
fontNames = [f.name for f in fm.fontManager.ttflist]
#fontname = st.selectbox("폰트 선택", pd.unique(fontNames))
plt.rc('font', family="NanumGothic")
fig = data.plot.pie(
    y="인지도 (%)",
    labels=data["캐릭터"],
    autopct="%1.1f%%",
    figsize=(6,6),
    legend=False,
    title="캐릭터 별 인지도"
).get_figure()
st.pyplot(fig)