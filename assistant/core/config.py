from pydantic import BaseModel
from dotenv import load_dotenv
import os, json


load_dotenv()


def _json_or_none(text: str | None):
    if not text:
    return None
try:
    return json.loads(text)
except Exception:
return None

class Settings(BaseModel):
    email_smtp: os.getenv('EMAIL_SMTP', 'stmp.gmail.com')
    email_port: int = int(os.getenv('EMAIL_PORT', 587))
    email_use_tls: bool = os.getenv('EMAIL_USE_TLS', 'true').lower() == 'true'
    email_user: str | None = os.getenv('EMAIL_USER')
    email_password: str | None = os.getenv('EMAIL_PASSWORD')

    news_api_key: str | None = os.getenv('NEWS_API_KEY')
    news_sources: str | None = os.getenv('NEWS_SOURCES') # comma-sep

    stt_engine: str = os.getenv('STT_ENGINE', 'google') #google|vosk|whisper
    wakw_word: str = os.getenv('WAKE_WORD', 'computer')

    llm_provider: str = os.getenv('LLM_PROVIDER', 'none') # ollama|openAi|none
    ollama_host: str = os.getenv('OLLAMA_HOST', 'http://localhost:11434')
    ollam_host: str = os.getenv('OLLAMA_MODEL', 'llama3')
    openai_key: str | None - os.getenv('OPENAI_API_KEY')

settings = Settings()