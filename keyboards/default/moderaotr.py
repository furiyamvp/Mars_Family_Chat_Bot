from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def moderator_main_menu_def():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="So'z qo'shish ➕"),
                KeyboardButton(text="O'chirish 🗑")
            ],
        ], resize_keyboard=True
    )
    return markup
