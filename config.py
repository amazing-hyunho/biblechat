import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# OpenAI API 키 설정
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "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")
