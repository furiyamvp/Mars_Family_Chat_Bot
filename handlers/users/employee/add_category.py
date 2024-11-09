from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.back import back_button_def
from loader import dp
from states.category import AddCategoryState
from utils.db_commands.category import add_category_def
from utils.db_commands.employee import get_employee_data


@dp.message_handler(text="Kategoriya Qo'shish 🔗➕", role="admin")
async def add_category_button_handler(message: types.Message):
    text = "📝 Qo'shmoqchi bo'lgan kategoryangiz nomini kiriting"
    await message.answer(text=text, reply_markup=await back_button_def())
    await AddCategoryState.name.set()


@dp.message_handler(state=AddCategoryState.name, role="admin")
async def add_category_name_handler(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text.lower())
    text = "♻️ Kategoriyani tavsif kiriting."
    await message.answer(text=text)
    await AddCategoryState.description.set()


@dp.message_handler(state=AddCategoryState.description, role="admin")
async def add_category_description_handler(message: types.Message, state: FSMContext):
    employee_data = await get_employee_data(int(message.chat.id))
    await state.update_data(description=message.text)
    data = await state.get_data()

    if await add_category_def(data=data, employee_id=employee_data["id"]):
        text = "✅ Kategoriya muvaffaqiyatli qo'shildi."
        await message.answer(text)
    else:
        error_text = "❌ Bunday kategoriya allaqachon mavjud."
        await message.answer(error_text)

    await state.finish()
