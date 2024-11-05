from sqlalchemy import select

from main.models import ForbiddenWordModel
from main.database import database


async def get_all_forbidden_words() -> list[str]:
    try:
        query = select(ForbiddenWordModel)
        rows = await database.fetch_all(query=query)
        return [row['word'] for row in rows]
    except Exception as e:
        print(f"Error fetching user chat IDs: {e}")
        return []


async def delete_forbidden_word(word: str):
    try:
        delete_query = ForbiddenWordModel.delete().where(ForbiddenWordModel.c.word == word)
        result = await database.execute(delete_query)

        if result is None or result > 0:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: There was a problem deleting the forbidden word: {e}")
        return None




async def add_forbidden_word(data: dict, employee_id: int):
    try:
        select_query = select(ForbiddenWordModel.c.word).where(ForbiddenWordModel.c.word == data.get('word'))
        exists = await database.fetch_one(select_query)

        if exists:
            return False

        query = ForbiddenWordModel.insert().values(
            word=data.get('word'),
            answer=data.get('answer'),
            category_id=data.get('category_id'),
            employee_id=employee_id
        ).returning(ForbiddenWordModel.c.id)

        return await database.execute(query)

    except Exception as e:
        error_text = f"Error: There was a problem creating the forbidden word: {e}"
        print(error_text)
        return None

