from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



async def back_button_def():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton("Orqaga 🔙")
            ],
        ], resize_keyboard=True
    )
    return markup
