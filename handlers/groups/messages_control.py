from aiogram import types
from loader import dp
from utils.db_commands.forbidden_word import get_all_forbidden_words
from utils.db_commands.employee import get_all_employees_chat_id


@dp.message_handler(content_types=types.ContentType.TEXT)
async def filter_bad_words(message: types.Message):
    if message.chat.type == types.ChatType.PRIVATE:
        return

    employee_ids = await get_all_employees_chat_id()

    if message.from_user.id in employee_ids:
        return

    user_text = message.text.lower()
    forbidden_words = await get_all_forbidden_words()

    user_identity = f"@{message.from_user.username}" if message.from_user.username else f"{message.from_user.full_name}"

    for forbidden_word in forbidden_words:
        word = forbidden_word['word']
        answer = forbidden_word['answer']

        if word in user_text:
            await message.delete()
            await message.answer(f"{user_identity} {answer}")
            return

    if any(link in user_text for link in ["http://", "https://", "www.", "t.me/"]) and not user_text.startswith("@"):
        await message.delete()
        await message.answer(f"{user_identity} havola yuborish mumkin emas ❗️")
        return

    if user_text.startswith("@") and " " not in user_text:
        if user_text.startswith("@") and user_text.endswith("_bot"):
            pass
        elif user_text.startswith("@"):
            await message.delete()
            await message.answer(f"{user_identity} havola yuborish mumkin emas ❗️")
            return
