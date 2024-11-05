from sqlalchemy import select
from main.database import database
from main.models import CategoryModel


async def view_all_categories():
    try:
        query = select(CategoryModel)
        results = await database.fetch_all(query)
        return results

    except Exception as e:
        print(f"Xato: Kategoriyalarni olishda muammo: {e}")
        return None



async def get_all_category_names() -> list[str]:
    try:
        query = select(CategoryModel.c.name)
        rows = await database.fetch_all(query=query)
        return [row['name'] for row in rows]
    except Exception as e:
        print(f"Error fetching category names: {e}")
        return []


async def get_category_id_by_name(category_name: str):
    try:
        category_name_lower = category_name.lower()
        query = select(CategoryModel).where(CategoryModel.c.name == category_name_lower)
        row = await database.fetch_one(query=query)

        if row is not None:
            return row.id
        else:
            return False
    except Exception as e:
        print(f"Error fetching category: {e}")
        return False


async def delete_category_def(category_name: str):
    try:
        category_name = category_name.strip()
        category_query = select(CategoryModel.c.id).where(CategoryModel.c.name == category_name)
        category = await database.fetch_one(category_query)

        if category is None:
            return False

        category_id = category[0]
        delete_query = CategoryModel.delete().where(CategoryModel.c.id == category_id)
        await database.execute(delete_query)

        return True

    except Exception as e:
        print(f"Error: There was a problem deleting the category: {e}")
        return None


async def add_category_def(data: dict, employee_id):
    try:
        select_query = select(CategoryModel.c.id).where(CategoryModel.c.name == data["name"])
        exists = await database.fetch_one(select_query)

        if exists:
            return False

        query = CategoryModel.insert().values(
            name=data["name"],
            description=data["description"],
            employee_id=employee_id
        ).returning(CategoryModel.c.id)

        await database.execute(query)
        return True

    except Exception as e:
        print(f"Error adding category: {e}")
        return False
