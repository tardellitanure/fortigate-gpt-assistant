import os
from dotenv import load_dotenv

load_dotenv()

FORTIGATE_HOST = os.getenv("FORTIGATE_HOST")
FORTIGATE_TOKEN = os.getenv("FORTIGATE_TOKEN")
GPT_API_KEY = os.getenv("GPT_API_KEY")
GPT_MODEL = os.getenv("GPT_MODEL", "gpt-4")
