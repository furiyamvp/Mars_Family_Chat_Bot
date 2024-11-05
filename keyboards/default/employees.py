from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from main.models import ForbiddenWordModel

async def forbidden_word_menu_def():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="So'z qo'shish ➕"),
                KeyboardButton(text="O'chirish 🗑")
            ],
            [
                KeyboardButton(text="Orqaga 🔙")
            ],
        ], resize_keyboard=True
    )
    return markup
