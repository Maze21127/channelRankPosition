from aiogram import executor, Dispatcher, types

from bot.loader import dp, scheduler, app, bot
from bot.schedule import send_stats, send_stats_additional


async def on_startup(dispatcher: Dispatcher):
    await app.start()
    await dispatcher.bot.set_my_commands([
        types.BotCommand('start', 'Запустить бота'),
        types.BotCommand('search', 'Просмотр статистики'),
    ])
    print("set commands")

    times = ("10", "14", "18", "21")
    for time in times:
        scheduler.add_job(send_stats, args=[bot], trigger='cron', hour=time)

    additional_times = ("9", "14", "19", "21")
    for time in additional_times:
        scheduler.add_job(
            send_stats_additional, args=[bot], trigger='cron', hour=time
        )

    scheduler.start()
    print("Jobs added")


async def on_shutdown(dispatcher: Dispatcher):
    await app.stop()
    print("Disconnected")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
