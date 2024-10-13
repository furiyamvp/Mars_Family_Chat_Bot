from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from keyboards.default.moderaotr import moderator_main_menu
from loader import dp


@dp.message_handler(CommandStart(), role="moderator")
async def start_for_moderator_handler(message: types.Message):
    text = "Salom admin 👋"
    await message.answer(text=text, reply_markup=moderator_main_menu)