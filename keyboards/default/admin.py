from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from utils.db_commands.category import get_all_category_names


async def admin_main_menu_def():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Moderatorlar 👤")
            ],
            [
                KeyboardButton(text="Taqiqlangan so'zlar 🔒"),
                KeyboardButton(text="Kategoriyalar 🔗")
            ],
        ], resize_keyboard=True
    )
    return markup


async def admin_moderator_menu_def():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Moderator Qo'shish 👤➕"),
                KeyboardButton(text="O'chirish 👤🗑")
            ],
            [
                KeyboardButton(text="Orqaga 🔙")
            ],
        ], resize_keyboard=True
    )
    return markup


async def admin_category_menu_def():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Kategoriyalarni ko'rish 📜")
            ],
            [
                KeyboardButton(text="Kategoriya Qo'shish 🔗➕"),
                KeyboardButton(text="O'chirish 🔗🗑")
            ],
            [
                KeyboardButton(text="Orqaga 🔙")
            ],
        ], resize_keyboard=True
    )
    return markup


async def all_category_menu_def():
    categories = await get_all_category_names()
    category_menu = ReplyKeyboardMarkup(resize_keyboard=True)
    back = KeyboardButton(text="Orqaga 🔙")
    category_menu.row(back)

    category_buttons = []
    for category in categories:
        keyboard = KeyboardButton(text=category)
        category_buttons.append(keyboard)

        if len(category_buttons) == 2:
            category_menu.row(*category_buttons)
            category_buttons = []

    if category_buttons:
        category_menu.row(*category_buttons)

    return category_menu
