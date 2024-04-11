from dotenv import load_dotenv
from envparse import env

load_dotenv('.env')


API_ID = env.int('API_ID')
API_HASH = env('API_HASH')
BOT_TOKEN = env("BOT_TOKEN")
RESULT_CHAT_ID = env.int('RESULT_CHAT_ID')
ADDITIONAL_RESULT_CHAT_ID = env.int('ADDITIONAL_RESULT_CHAT_ID')
LAST_MESSAGE_CONTAINS = env("LAST_MESSAGE_CONTAINS")