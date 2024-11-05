from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.admin import admin_main_menu_def
from keyboards.default.moderaotr import moderator_main_menu_def
from loader import dp


@dp.message_handler(text="Orqaga 🔙", role="admin", state="*")
async def admin_back_to_main_menu(message: types.Message, state: FSMContext):
    text = "Bosh sahifaga qaytdingiz."
    await message.answer(text=text, reply_markup=await admin_main_menu_def())
    await state.finish()


@dp.message_handler(text="Orqaga 🔙", role="moderator", state="*")
async def moderator_back_to_main_menu(message: types.Message, state: FSMContext):
    text = "Bosh sahifaga qaytdingiz."
    await message.answer(text=text, reply_markup=await moderator_main_menu_def())
    await state.finish()
