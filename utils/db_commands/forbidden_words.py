from sqlalchemy import select

from main.models import ForbiddenWordTable
from main.database import database

from sqlalchemy.exc import IntegrityError


async def get_all_forbidden_words() -> list[str]:
    try:
        query = select(ForbiddenWordTable)
        rows = await database.fetch_all(query=query)
        return [row['word'] for row in rows]
    except Exception as e:
        print(f"Error fetching user chat IDs: {e}")
        return []


async def delete_forbidden_word(word: str):
    try:
        select_query = select(ForbiddenWordTable.c.word).where(ForbiddenWordTable.c.word == word)
        exists = await database.fetch_one(select_query)

        if exists:
            delete_query = ForbiddenWordTable.delete().where(ForbiddenWordTable.c.word == word)
            await database.execute(delete_query)
            return True
        else:
            return False

    except Exception as e:
        print(f"Error: There was a problem deleting the forbidden word: {e}")
        return None


async def add_forbidden_word(data: dict, employee_id: int):
    try:
        select_query = select(ForbiddenWordTable.c.word).where(ForbiddenWordTable.c.word == data.get('word'))
        exists = await database.fetch_one(select_query)

        if exists:
            return False

        query = ForbiddenWordTable.insert().values(
            word=data.get('word'),
            employee_id=employee_id
        ).returning(ForbiddenWordTable.c.id)

        return await database.execute(query)

    except Exception as e:
        error_text = f"Error: There was a problem creating the forbidden word: {e}"
        print(error_text)
        return None

