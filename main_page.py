import streamlit as st

st.title('실습 페이지')
st.subheader('2024-12-27 전성원 SKN AI 부트캠프 9기 실습')

st.page_link("pages/1_input_page.py", label="input 실습", icon="🌎")
st.page_link("pages/2_data_page.py", label="data 실습", icon="🌎")
st.page_link("pages/3_session_state_page.py", label="session 실습", icon="🌎")

# 상태 초기화
if 'cat_img_root' not in st.session_state:
    st.session_state.cat_img_root = "img/cat.png"
if 'captions' not in st.session_state:
    st.session_state.captions = "식빵에 낀 고양이"

def change_img(cat_img_root, captions):
    st.session_state.cat_img_root = cat_img_root
    st.session_state.captions = captions

# 현재 이미지 표시
st.image(st.session_state.cat_img_root, caption=st.session_state.captions)

my_cat = st.text_input('고양이의 이름을 지어주세요')
st.write(my_cat)

if st.button(f'{my_cat} 환영하기'):
    st.success(f"{my_cat} 쓰다듬는중...:rocket::rocket::rocket:", icon="✅")
    change_img("img/yawnCat.jpg", "하품하는 고양이")
    st.write("브레드가 기뻐합니다.")
    st.write("브레드: 이야옹!!!!! :cat:")



