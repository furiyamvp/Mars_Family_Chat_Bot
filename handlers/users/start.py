from aiogram import types
from loader import dp


@dp.message_handler(content_types=types.ContentType.ANY, chat_type=types.ChatType.PRIVATE)
async def admin_start_handler(message: types.Message):
    text = ("Bu bot faqat gruppada suhbatda ishlaydi.\n"
            "Gruppada foydalanuvchilar bot qo'shmasligi\n"
            "va so'kinmasligini ta'minlaydi.")
    await message.answer(text=text)
