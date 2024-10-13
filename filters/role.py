from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from utils.db_commands.employee import get_employee_role


class EmployeeRoleFilter(BoundFilter):
    key = 'role'

    def __init__(self, role):
        if isinstance(role, str):
            self.role = [role]
        else:
            self.role = role

    async def check(self, message: types.Message):
        user_role = await get_employee_role(message.chat.id)
        return user_role in self.role
