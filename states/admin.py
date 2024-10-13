from aiogram.dispatcher.filters.state import StatesGroup, State


class AddModeratorState(StatesGroup):
    first_name = State()
    last_name = State()
    chat_id = State()
    phone_number = State()
