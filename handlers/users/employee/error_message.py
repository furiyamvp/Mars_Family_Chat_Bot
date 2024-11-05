from aiogram import types

from loader import dp


@dp.message_handler(content_types=types.ContentType.ANY, chat_type=types.ChatType.PRIVATE, role=["admin", "moderator"])
async def employee_message_error_handler():
    return
