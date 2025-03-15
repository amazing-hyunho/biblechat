from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config import OPENAI_API_KEY


def get_response(user_input, history):
    """챗봇 응답 생성 함수"""
    prompt_template = """📖 성경 지식을 알려주는 챗봇입니다. 
    질문자의 문의에 친절하고 상세하게 답변해주세요. 성경 지식에서 벗어나는 내용은 답변해주지 마세요.

    {history}
    user: {user_input}
    """

    # LangChain Prompt 설정
    prompt = PromptTemplate.from_template(prompt_template)

    # LangChain LLM 설정
    llm = ChatOpenAI(model_name="gpt-4o", temperature=0, openai_api_key=OPENAI_API_KEY)
    parser = StrOutputParser()
    chain = (prompt | llm | parser)

    # 대화 이력 정리
    history_text = '\n'.join([':'.join(entry.values()) for entry in history])

    # 응답 생성
    response = chain.invoke({"user_input": user_input, "history": history_text})
    return response