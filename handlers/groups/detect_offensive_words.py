from aiogram import types
from loader import dp

FORBIDDEN_WORDS = ["messi or ronaldo", "messi yoki ronaldo", "messi", "ronaldo", "kot", "ko't", "🖕", "👌👈", "👊🫷"]


@dp.message_handler(content_types=types.ContentType.TEXT, chat_type=types.ChatType.GROUP)
async def filter_bad_words(message: types.Message):
    text = message.text.lower()

    for word in FORBIDDEN_WORDS:
        if word in text:
            await message.delete()
            await message.answer(f"@{message.from_user.username} bu so'zni ishlatish mumkin emas !")
            return
