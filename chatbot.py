from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config import OPENAI_API_KEY

# 🔹 프롬프트 템플릿 설정
TEMPLATE = """ 
성경 지식을 알려주는 챗봇입니다. 질문자의 문의에 친절하고 상세하게 답변해주세요.
성경 지식에서 벗어나는 내용은 답변해주지 마세요.

{history}
user: {user_input}
"""


def get_response_stream(user_input, history, api_key):
    """스트리밍 방식으로 챗봇 응답 생성"""
    # 🔹 프롬프트 & LLM 설정
    prompt = PromptTemplate.from_template(TEMPLATE)
    llm = ChatOpenAI(model_name="gpt-4o", temperature=0, openai_api_key=api_key)
    parser = StrOutputParser()

    # 🔹 체인 생성 (프롬프트 → LLM → 파서)
    chain = (prompt | llm | parser)

    # 🔹 대화 이력 가공
    history_text = '\n'.join([':'.join(entry.values()) for entry in history])

    # 🔹 OpenAI API 스트리밍 호출
    return chain.stream({"user_input": user_input, "history": history_text})
