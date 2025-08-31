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