from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from keyboards.default.moderaotr import moderator_main_menu_def
from keyboards.default.admin import admin_main_menu_def
from loader import dp

@dp.message_handler(CommandStart(), role="admin")
async def start_for_admin_handler(message: types.Message):
    text = "👋 Salom admin"
    await message.answer(text=text, reply_markup=await admin_main_menu_def())

@dp.message_handler(CommandStart(), role="moderator")
async def start_for_moderator_handler(message: types.Message):
    text = "👋 Salom moderator"
    await message.answer(text=text, reply_markup=await moderator_main_menu_def())
