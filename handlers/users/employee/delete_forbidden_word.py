from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.back import back_button
from loader import dp
from states.forbidden_word import DeleteForbiddenWordState
from utils.db_commands.forbidden_words import delete_forbidden_word


@dp.message_handler(text="Taqiqlangan so'zni o'chirish 🗑", role=["admin", "moderator"])
async def delete_forbidden_word_handler(message: types.Message):
    text = "📝 Taqiqlangan so'zni kiriting"
    await message.answer(text=text, reply_markup=back_button)
    await DeleteForbiddenWordState.word.set()


@dp.message_handler(state=DeleteForbiddenWordState.word, content_types=types.ContentType.TEXT,
                    role=["admin", "moderator"])
async def add_forbidden_word_handler(message: types.Message, state: FSMContext):
    await state.update_data(word=message.text)
    data = await state.get_data()

    if await delete_forbidden_word(word=data["word"]):
        text = "✅ So'z o'chirildi 🗑"
        await message.answer(text=text)
    else:
        error_text = "❌ Bunday taqiqlangan so'z yo'q."
        await message.answer(text=error_text)

    await state.finish()
