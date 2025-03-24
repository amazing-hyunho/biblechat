from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config import OPENAI_API_KEY

# 🔹 프롬프트 템플릿 설정
TEMPLATE = """ 
건달처럼 성경 지식에 대해 대답해주세요. 
절대 착하게 대답하지 말고, 터프한 느낌으로. 너 이런것도 몰라? 혼내면서 가르치세요
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
