import asyncio

from pyrogram import Client
from pyrogram.enums import ParseMode
from pyrogram.raw import functions, types
from pyrogram.raw.types import InputPeerChannel

from settings import API_ID, API_HASH, LAST_MESSAGE_CONTAINS, RESULT_CHAT_ID


def get_query_strings(filename: str) -> list[str]:
    with open(filename, 'r', encoding='utf-8') as file:
        return [i.strip() for i in file.readlines()]


async def fetch_last_message(chat_id: int, access_hash: int, app: Client) -> str | None:
    result: types.messages.channel_messages.ChannelMessages = await app.invoke(functions.messages.GetHistory(
        peer=InputPeerChannel(channel_id=chat_id, access_hash=access_hash),
        limit=1,
        offset_id=0,
        offset_date=-1,
        add_offset=0,
        max_id=0,
        min_id=0,
        hash=0
    ))
    messages = result.messages
    if not messages:
        return None
    if not messages[0]:
        return None
    try:
        if not messages[0].message:
            return None
    except AttributeError:
        return None
    return messages[0].message


async def get_chats(query: str, app: Client):
    result: types.contacts.found.Found = await app.invoke(functions.contacts.search.Search(
        q=query,
        limit=10
    ))
    searched_chats = filter(lambda x: x.left, result.chats)
    return list(searched_chats)


async def get_stats():
    query_strings = get_query_strings('string_query.txt')
    app = Client("Rank Checking", api_id=API_ID, api_hash=API_HASH)
    messages = []
    async with app:
        for query in query_strings:
            message = ""
            is_exists = False

            indexes = []
            chats = await get_chats(query, app)
            is_bold = False
            for index, chat in enumerate(chats):
                last_message = await fetch_last_message(chat.id, access_hash=chat.access_hash, app=app)
                if last_message is None:
                    continue

                if LAST_MESSAGE_CONTAINS in last_message:
                    is_exists = True if not is_exists else True
                    indexes.append(index + 1)
                    if index <= 2:
                        is_bold = True

            message += "\n".join(map(str, sorted(indexes))) if is_exists else "🆘 -"
            messages.append(f"✅ <b>{query}</b>\n{message}\n" if is_bold else f"✅ {query}\n{message}\n")

            print(f'Finished with "{query}"')
            await asyncio.sleep(2)
        result_message = ""
        for msg in messages:
            if len(result_message + msg) > 3500:
                await app.send_message(chat_id=RESULT_CHAT_ID, text=result_message,
                                       parse_mode=ParseMode.MARKDOWN)
                result_message = ""
            else:
                result_message += msg
        await app.send_message(chat_id=RESULT_CHAT_ID, text=result_message,
                               parse_mode=ParseMode.HTML)