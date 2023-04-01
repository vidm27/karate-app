from backend.app.domain.entities.categoria import CategoriaModel
from backend.db.session import db


async def create_category(category: CategoriaModel) -> CategoriaModel:
    new_category = await db.categoria.insert_one(category)
    created_category = await db.categoria.find_one({"_id": new_category.inserted_id})
    return created_category


async def read_by_id(category_id: str) -> CategoriaModel:
    category = await db.categoria.find_one({"_id": category_id})
    return category


async def update_category(category_id: str, category: dict) -> CategoriaModel:
    update_result = await db.categoria.update_one({"_id": category_id}, {"$set": category})

    if update_result.modified_count == 1:
        if (current_categoria := await db.categoria.find_one({"_id": category_id})) is not None:
            return current_categoria


async def delete_category(categoria_id) -> bool:
    delete_result = await db.categoria.delete_one({"_id": categoria_id})
    if delete_result.deleted_count == 1:
        return True
    return False
