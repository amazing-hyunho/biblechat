import streamlit as st
from chatbot import get_response
from utils import check_openai_api_key
from config import OPENAI_API_KEY

# 🔹 API 키 입력 받기
key = st.sidebar.text_input('OPENAI API KEY', type='password', value=OPENAI_API_KEY)

# 🔹 API 키 유효성 확인
if key and check_openai_api_key(key):
    st.title("📖 성경읽자 챗봇")

    # 세션 상태 초기화
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # 이전 메시지 표시
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # 사용자 입력 처리
    if question := st.chat_input("궁금한 성경 지식을 입력하세요:"):
        with st.chat_message("user"):
            st.write(question)
        with st.chat_message("assistant"):
            response = get_response(question, st.session_state.messages)
            st.write(response)

        # 세션 상태 업데이트
        st.session_state.messages.append({"role": "user", "content": question})
        st.session_state.messages.append({"role": "assistant", "content": response})

# 🔹 자동 스크롤 스크립트
js = '''
<script>
    var body = window.parent.document.querySelector(".main");
    body.scrollTop = 0;
</script>
'''
st.components.v1.html(js)