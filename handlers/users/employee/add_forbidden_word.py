from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.back import back_button_def
from keyboards.default.admin import all_category_menu_def
from keyboards.default.employees import forbidden_word_menu_def
from loader import dp
from states.forbidden_word import AddForbiddenWordState
from utils.db_commands.category import get_category_id_by_name
from utils.db_commands.employee import get_employee_data
from utils.db_commands.forbidden_word import add_forbidden_word

@dp.message_handler(text="So'z qo'shish ➕", role=["admin", "moderator"])
async def add_forbidden_word_button_handler(message: types.Message):
    text = "📝 Taqiqlamoqchi bo'lgan so'zingizni kiriting"
    await message.answer(text=text, reply_markup=await back_button_def())
    await AddForbiddenWordState.word.set()

@dp.message_handler(state=AddForbiddenWordState.word, content_types=types.ContentType.TEXT, role=["admin", "moderator"])
async def add_forbidden_word_word_handler(message: types.Message, state: FSMContext):
    await state.update_data(word=message.text.lower())
    text = "⭕️ Shu taqiqlamoqchi bo'lgan so'zingizni ishlatishsa nima deb javob berilsin ?"
    await message.answer(text=text, reply_markup=await back_button_def())
    await AddForbiddenWordState.answer.set()

@dp.message_handler(state=AddForbiddenWordState.answer, content_types=types.ContentType.TEXT, role=["admin", "moderator"])
async def add_forbidden_word_answer_handler(message: types.Message, state: FSMContext):
    await state.update_data(answer=message.text)
    text = "⛓️ Sizning so'zingiz qaysi kategoryga kiradi?"
    await message.answer(text=text, reply_markup=await all_category_menu_def())
    await AddForbiddenWordState.category.set()

@dp.message_handler(state=AddForbiddenWordState.category, content_types=types.ContentType.TEXT, role=["admin", "moderator"])
async def add_forbidden_word_category_handler(message: types.Message, state: FSMContext):
    employee_data = await get_employee_data(int(message.chat.id))
    category_data = await get_category_id_by_name(message.text)
    if category_data != "False":
        await state.update_data(category_id=category_data)
        data = await state.get_data()
        if await add_forbidden_word(data=data, employee_id=employee_data["id"]):
            text = "✅ So'z taqiqlandi."
            await message.answer(text=text, reply_markup=await forbidden_word_menu_def())
            await state.finish()
        else:
            error_text = "❌ Bu so'z allaqachon taqiqlangan."
            await message.answer(text=error_text, reply_markup=await forbidden_word_menu_def())
            await state.finish()
    else:
        await message.answer("⛓️ Bizda bunday kategoriya yo'q, shuning uchun iloji bo'lsa tugma orqali tanlang.",
                             reply_markup=await all_category_menu_def())
        await AddForbiddenWordState.category.set()
