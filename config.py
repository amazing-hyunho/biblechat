from pyngrok import ngrok
import os
from dotenv import load_dotenv


#PYNGROK_API_KEY = '2rN06yr538OB5MV6zru6pZhszsp_3qpEMf8MCJvstrysKVSDx'
# ngrok 서비스 인증
#ngrok.set_auth_token(PYNGROK_API_KEY)
#ngrok_tunnel = ngrok.connect(addr='5011', proto='http', bind_tls=True)
#print(' * Tunnel URL:', ngrok_tunnel.public_url)


# .env 파일 로드
load_dotenv()

# OpenAI API 키 설정
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "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")