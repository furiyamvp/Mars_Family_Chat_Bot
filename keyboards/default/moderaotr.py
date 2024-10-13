from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


moderator_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Taqiqlangan so'z qo'shish ➕")
        ],
        [
            KeyboardButton("Taqiqlangan so'zni o'chirish 🗑")
        ],
    ], resize_keyboard=True
)
