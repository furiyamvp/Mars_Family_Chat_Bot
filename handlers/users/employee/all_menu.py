from aiogram import types
from loader import dp
from keyboards.default.admin import admin_moderator_menu_def, admin_category_menu_def
from keyboards.default.moderaotr import moderator_main_menu_def

@dp.message_handler(text="Moderatorlar 👤", role="admin")
async def moderator_menu_handler(message: types.Message):
    text = "👋 Moderatorlarni boshqarish qismga xush kelibsiz!"
    await message.answer(text=text, reply_markup=await admin_moderator_menu_def())

@dp.message_handler(text="Taqiqlangan so'zlar 🔒", role=["admin", "moderator"])
async def forbidden_word_menu_handler(message: types.Message):
    text = "👋 So'zlarni boshqarish qismga xush kelibsiz!"
    await message.answer(text=text, reply_markup=await moderator_main_menu_def())

@dp.message_handler(text="Kategoriyalar 🔗", role="admin")
async def category_menu_handler(message: types.Message):
    text = "👋 Kategoriyalarni boshqarish qismga xush kelibsiz!"
    await message.answer(text=text, reply_markup=await admin_category_menu_def())
