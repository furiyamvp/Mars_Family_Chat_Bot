from aiogram import types
from loader import dp
from utils.db_commands.forbidden_words import get_all_forbidden_words


@dp.message_handler(content_types=types.ContentType.TEXT, chat_type=types.ChatType.GROUP)
async def filter_bad_words(message: types.Message):
    user_text = message.text.lower()
    forbidden_words = await get_all_forbidden_words()

    if any(link in user_text for link in ["http://", "https://", "www.", "t.me/"]) and not user_text.startswith("@"):
        await message.delete()

        user_identity = f"@{message.from_user.username}" if message.from_user.username else \
            f"{message.from_user.full_name}"

        await message.answer(f"{user_identity} havola yuborish mumkin emas ❗️")
        return

    if user_text.startswith("@") and " " not in user_text:
        if user_text.startswith("@") and user_text.endswith("_bot"):
            pass
        elif user_text.startswith("@"):
            await message.delete()

            user_identity = f"@{message.from_user.username}" if message.from_user.username else \
                f"{message.from_user.full_name}"

            await message.answer(f"{user_identity} kanallarni tashlash mumkin emas ❗️")
            return

    for word in forbidden_words:
        if word in user_text:
            await message.delete()

            user_identity = f"@{message.from_user.username}" if message.from_user.username else \
                f"{message.from_user.full_name}"

            await message.answer(f"{user_identity} bu so'zni ishlatish mumkin emas ❗️")
            return
