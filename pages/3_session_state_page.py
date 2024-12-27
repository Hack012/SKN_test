import streamlit as st

st.title('Counter')

st.page_link("main_page.py", label="Main으로..", icon="🏠")

if "customer_count" not in st.session_state:
    st.session_state.customer_count = 0

customer_count = 0

if st.button('손님 한 명 추가요~!'):
    st.session_state.customer_count += 1

if st.button('오늘 장사 끝! 손님 수 초기화!'):
    st.session_state.customer_count = 0

st.write(f"지금까지 온 손님 수 : {st.session_state.customer_count}")