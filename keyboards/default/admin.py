from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


admin_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Moderator qo'shish 👤")
        ],
        [
            KeyboardButton("Taqiqlangan so'z qo'shish ➕"),
            KeyboardButton("Taqiqlangan so'zni o'chirish 🗑")
        ],
    ], resize_keyboard=True
)
