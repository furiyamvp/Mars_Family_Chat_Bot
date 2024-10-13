from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart

from keyboards.default.admin import admin_main_menu
from keyboards.default.back import back_button

from states.admin import AddModeratorState

from loader import dp
from utils.db_commands.employee import add_moderator


@dp.message_handler(CommandStart(), role="admin")
async def start_for_moderator_handler(message: types.Message):
    text = "Salom admin 👋"
    await message.answer(text=text, reply_markup=admin_main_menu)


@dp.message_handler(text="Moderator qo'shish 👤", role="admin")
async def add_moderator_button_handler(message: types.Message):
    text = "📝 Moderatorni ismini kiriting"
    await message.answer(text=text, reply_markup=back_button)
    await AddModeratorState.first_name.set()


@dp.message_handler(state=AddModeratorState.first_name, content_types=types.ContentType.ANY)
async def add_moderator_first_name_handler(message: types.Message, state: FSMContext):
    if message.content_type != types.ContentType.TEXT:
        await message.answer("❌ Iltimos, faqat matn kiriting.")
        return

    await state.update_data(first_name=message.text)
    text = "📝 Moderatorning familiyasini kiriting"
    await message.answer(text=text)
    await AddModeratorState.last_name.set()


@dp.message_handler(state=AddModeratorState.last_name, content_types=types.ContentType.ANY)
async def add_moderator_last_name_handler(message: types.Message, state: FSMContext):
    if message.content_type != types.ContentType.TEXT:
        await message.answer("❌ Iltimos, faqat matn kiriting.")
        return

    await state.update_data(last_name=message.text)
    text = "📥 Moderatorning chat ID sini kiriting yoki foydalanuvchidan xabar yuboring"
    await message.answer(text=text)
    await AddModeratorState.chat_id.set()


@dp.message_handler(state=AddModeratorState.chat_id, content_types=types.ContentType.ANY)
async def add_moderator_chat_id_handler(message: types.Message, state: FSMContext):
    chat_id = None

    if message.forward_from:
        chat_id = message.forward_from.id

    elif message.content_type == types.ContentType.TEXT:
        try:
            chat_id = int(message.text)
        except ValueError:
            await message.answer("❌ Iltimos, to'g'ri chat ID kiriting yoki foydalanuvchidan xabar yuboring.")
            return

    else:
        await message.answer("❌ Iltimos, chat ID yoki foydalanuvchidan xabar yuboring.")
        return

    await state.update_data(chat_id=chat_id)
    text = "📞 Moderatorning telefon raqamini kiriting (+998 bilan boshlansin)"
    await message.answer(text=text)
    await AddModeratorState.phone_number.set()


@dp.message_handler(state=AddModeratorState.phone_number, content_types=types.ContentType.TEXT)
async def add_moderator_phone_number_handler(message: types.Message, state: FSMContext):
    phone_number = message.text

    if not phone_number.startswith("+998") or not phone_number[1:].isdigit() or len(phone_number) != 13:
        await message.answer(
            "❌ Telefon raqami noto'g'ri. 📱 Raqam +998 bilan boshlanishi va 12 ta raqamdan iborat bo'lishi kerak.")
        return

    await state.update_data(phone_number=phone_number)

    data = await state.get_data()
    if await add_moderator(data=data):
        text = (
            f"✅ Moderator qo'shildi!\n\n"
            f"👤 Ismi: {data['first_name']}\n"
            f"👤 Familiyasi: {data['last_name']}\n"
            f"🆔 Chat ID: {data['chat_id']}\n"
            f"📞 Telefon raqami: {data['phone_number']}"
        )
        await message.answer(text=text)
    else:
        error_text = "❌ Moderator qo'shishda xatolik yuz berdi."
        await message.answer(text=error_text, reply_markup=admin_main_menu)

    await state.finish()
