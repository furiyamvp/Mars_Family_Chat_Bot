from aiogram import types
from loader import dp
from keyboards.default.employees import forbidden_word_menu_def
from utils.db_commands.category import view_all_categories

@dp.message_handler(text="Kategoriyalarni ko'rish 📜", role=["admin", "moderator"])
async def view_categories_handler(message: types.Message):
    categories = await view_all_categories()

    if categories:
        text = "📜 Barcha kategoriyalar:\n\n"
        for category in categories:
            text += f"📛 Nomi: {category['name']}\n"
            text += f"📝 Tavsifi: {category['description']}\n\n"
    else:
        text = "❌ Kategoriyalarni olishda muammo bor."

    await message.answer(text=text, reply_markup=await forbidden_word_menu_def())
