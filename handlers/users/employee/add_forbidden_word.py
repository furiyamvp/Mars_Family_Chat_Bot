from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.back import back_button
from loader import dp
from states.forbidden_word import AddForbiddenWordState
from utils.db_commands.employee import get_employee_data
from utils.db_commands.forbidden_words import add_forbidden_word


@dp.message_handler(text="Taqiqlangan so'z qo'shish ➕", role=["admin", "moderator"])
async def add_forbidden_word_button_handler(message: types.Message):
    text = "📝 Taqiqlamoqchi bo'lgan so'zingizni kiriting"
    await message.answer(text=text, reply_markup=back_button)
    await AddForbiddenWordState.word.set()


@dp.message_handler(state=AddForbiddenWordState.word, content_types=types.ContentType.TEXT, role=["admin", "moderator"])
async def add_forbidden_word_handler(message: types.Message, state: FSMContext):
    employee_data = await get_employee_data(int(message.chat.id))
    await state.update_data(word=message.text)
    data = await state.get_data()

    if await add_forbidden_word(data=data, employee_id=employee_data["id"]):
        text = "✅ So'z taqiqlandi"
        await message.answer(text=text)
        await state.finish()
    else:
        error_text = "❌ Bu so'z allaqachon taqiqlangan."
        await message.answer(text=error_text)

    await state.finish()