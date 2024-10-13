from sqlalchemy.exc import NoResultFound

from main.models import EmployeeTable
from main.database import database

from sqlalchemy import select
from main.constants import EmployeeRole


async def get_all_moderators_chat_id() -> list[int]:
    try:
        query = select(EmployeeTable)
        row = await database.fetch_all(query=query)
        return [row['chat_id'] for row in row]
    except Exception as e:
        print(f"Error fetching user chat IDs: {e}")
        return []


async def get_employee_data(chat_id: int):
    try:
        query = select(EmployeeTable).where(EmployeeTable.c.chat_id == chat_id)
        row = await database.fetch_one(query=query)
        if row:
            return dict(row)
        return False
    except Exception as e:
        print(f"Error getting employee data with chat_id: {e}")
        return None


async def get_employee_role(chat_id: int) -> EmployeeRole:
    try:
        query = select(EmployeeTable.c.role).where(EmployeeTable.c.chat_id == chat_id)
        row = await database.fetch_all(query=query)
        if row:
            return EmployeeRole(row[0]["role"])
        return False
    except Exception as e:
        print(f"Error get employee role with chat_id: {e}")
        return None


async def add_moderator(data: dict):
    try:
        query = EmployeeTable.insert().values(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            chat_id=int(data.get('chat_id')),
            phone_number=data.get('phone_number'),
            role=EmployeeRole.moderator
        ).returning(EmployeeTable.c.id)
        return await database.execute(query)

    except Exception as e:
        error_text = f"Error adding moderator: {e}"
        print(error_text)
        return None
