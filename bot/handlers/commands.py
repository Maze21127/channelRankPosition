from aiogram import types
from aiogram.dispatcher.filters import CommandStart, Command

from bot.loader import dp
from bot.service.search import get_stats
from settings import RESULT_CHAT_ID


@dp.message_handler(CommandStart(), chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def start_user(message: types.Message):
    if message.chat.id != RESULT_CHAT_ID:
        return
    await message.answer("Статистика по местам в поиске доступна по команде /search")


@dp.message_handler(Command("search"), chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def search(message: types.Message):
    if message.chat.id != RESULT_CHAT_ID:
        return
    await message.answer("Запущено сканирование, вы получите отчет в течении нескольких минут.")
    messages = await get_stats()
    for msg in messages:
        await message.answer(text=msg, parse_mode=types.ParseMode.HTML)
