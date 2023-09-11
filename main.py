from aiogram import executor, Dispatcher, types

from bot.loader import dp, scheduler
from bot.service.search import get_stats


async def on_startup(dispatcher: Dispatcher):
    await dispatcher.bot.set_my_commands([
        types.BotCommand('start', 'Запустить бота'),
        types.BotCommand('search', 'Просмотр статистики'),
    ])
    print("set commands")

    times = ("10", "14", "18", "21")
    for time in times:
        scheduler.add_job(get_stats, trigger='cron', hour=time)

    scheduler.start()
    print("Jobs added")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
