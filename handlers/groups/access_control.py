from aiogram import types
from loader import dp


@dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS, chat_type=types.ChatType.GROUP)
async def check_new_members(message: types.Message):
    new_members = message.new_chat_members
    for member in new_members:
        if member.is_bot:
            if member.username not in ["mars_family_chat_bot", "mars_family_chat_test_bot"]:
                await message.answer(f"{message.from_user.full_name} - bot qo'shish mumkin emas !")
                await message.chat.kick(member.id)
    await message.delete()


@dp.message_handler(content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def delete_left_message(message: types.Message):
    await message.delete()
