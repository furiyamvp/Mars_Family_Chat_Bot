from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.admin import all_category_menu_def
from loader import dp
from utils.db_commands.category import delete_category_def
from states.category import DeleteCategoryState

@dp.message_handler(text="O'chirish 🔗🗑", role="admin")
async def delete_forbidden_word_handler(message: types.Message):
    text = ("📝 O'chirmoqchi bo'lgan taqiqlangan so'zni kiriting.\n\n"
            "❗️ Eslatma: Agar category ni ochirsangiz, unga tegishli hammma categorylar ham ochib ketadi.")
    await message.answer(text=text, reply_markup=await all_category_menu_def())
    await DeleteCategoryState.name.set()

@dp.message_handler(state=DeleteCategoryState.name, role="admin")
async def process_delete_forbidden_word(message: types.Message, state: FSMContext):
    if await delete_category_def(message.text):
        text = "✅ Kategoriya muvaffaqiyatli o'chirildi."
        await message.answer(text=text, )
        await state.finish()
    else:
        error_text = "❌ Bunday kategoriya mavjud emas."
        await message.answer(text=error_text)
        await state.finish()
