from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram import Client

from settings import BOT_TOKEN, API_ID, API_HASH

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)
scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
app = Client("Rank Checking", api_id=API_ID, api_hash=API_HASH)
