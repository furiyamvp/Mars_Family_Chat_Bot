from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.admin import admin_main_menu
from loader import dp


@dp.message_handler(text="Orqaga ⬅️", role="admin")
async def go_back_to_main_menu(message: types.Message, state: FSMContext):
    text = "Bosh sahifaga qaytdingiz."
    await message.answer(text=text, reply_markup=admin_main_menu)
    await state.finish()
