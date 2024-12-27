import streamlit as st

st.title("사용자 입력 받기")

st.page_link("main_page.py", label="Main으로..", icon="🏠")

col1, _, col2 = st.columns(3)
#col1, col2 = st.columns(2)

with col1:
    nickname = st.text_input("닉네임 입력")
    age = st.number_input("나이 입력", min_value=13, max_value=80)

    options = ["대학생", '고등학생', "중학생", "초등학생", "해당사항 없어"]
    selected = st.selectbox("학교 입력", options)

    if selected == "해당사항 없어":
        selected = "직장 다녀"

    r_options = ["맛집 탐방", "영화 감상", "음악 감상", "사진찍기"]
    choice = st.radio("취미 입력", r_options)
    selected_many = st.multiselect('취미가 여러 개라면', r_options)

    selected_text = "내 취미는 이외에 "
    for sm in range(0, len(selected_many)):
        if sm < len(selected_many)-1:
            tmp = ":red["+selected_many[sm]+"]" + ","
            selected_text += tmp
        else:
            tmp = ":red["+selected_many[sm]+"]"
            selected_text += tmp
        
    selected_text += " 등 이 있어."

    checked = st.checkbox("개인정보 제공 동의")
    checked_answer = ''

    if checked:
        checked_answer = "응. 동의해."
    else:
        checked_answer = "아니. 동의하지 않아."


def stream_data():
    st.write(f"이름이 뭐야? {nickname}")
    st.write(f"몇 살이야? {age}")
    st.write(f"어디 다녀? {selected}")
    st.write(f"취미가 뭐야? {choice}")
    st.write(f"취미가 여러개야? {selected_text}")
    st.write(f"개인정보 제공 동의해? {checked_answer}")

with col2:
    if st.button('입력 완료!'):
        code = f'''
            이름이 뭐야? **:blue[{nickname}]** \n
            몇 살이야? **:blue[{int(age)}세]**\n
            어디 다녀? **:blue[{selected}]**\n
            취미가 뭐야? **:blue[{choice}]**\n
            취미가 여러개야? **:blue[{selected_text}]**\n
            개인정보 제공 동의해? **:blue[{checked_answer}]**
        '''
        # st.write(f"이름이 뭐야? {nickname}")
        # st.write(f"몇 살이야? {age}")
        # st.write(f"어디 다녀? {selected}")
        # st.write(f"취미가 뭐야? {choice}")
        # st.write(f"취미가 여러개야? {selected_text}")
        # st.write(f"개인정보 제공 동의해? {checked_answer}")

        st.markdown(code)
        #st.write_stream(stream_data)

