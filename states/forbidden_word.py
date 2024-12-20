from aiogram.dispatcher.filters.state import StatesGroup, State


class AddForbiddenWordState(StatesGroup):
    word = State()
    answer = State()
    category = State()



class DeleteForbiddenWordState(StatesGroup):
    word = State()
