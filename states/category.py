from aiogram.dispatcher.filters.state import State, StatesGroup


class AddCategoryState(StatesGroup):
    name = State()
    description = State()


class DeleteCategoryState(StatesGroup):
    name = State()

