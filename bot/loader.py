from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from settings import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)
scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
