import asyncio

from pyrogram import Client

from settings import API_ID, API_HASH

app = Client("Rank Checking", api_id=API_ID, api_hash=API_HASH)


async def main():
    async with app:
        async for chat in app.get_dialogs():
            print(chat.chat.title, chat.chat.id)


if __name__ == '__main__':
    asyncio.run(main())