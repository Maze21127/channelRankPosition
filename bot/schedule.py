from aiogram import Bot, types

from bot.service.search import get_stats
from settings import RESULT_CHAT_ID, ADDITIONAL_RESULT_CHAT_ID


async def send_stats(bot: Bot):
    messages = await get_stats()
    for message in messages:
        await bot.send_message(text=message, parse_mode=types.ParseMode.HTML, chat_id=RESULT_CHAT_ID)


async def send_stats_additional(bot: Bot):
    messages = await get_stats(with_additional_signs=True)
    for message in messages:
        await bot.send_message(
            text=message, parse_mode=types.ParseMode.HTML, chat_id=ADDITIONAL_RESULT_CHAT_ID
        )