from backend.app.domain.entities.torneo import TorneoModel
from backend.db.session import db


async def read_torne_by_id(torneo_id: str) -> TorneoModel:
    torneo = await db["torneo"].find_one({"_id": torneo_id})
    return torneo


async def read_all() -> list[TorneoModel]:
    torneos = await db["torneo"].find().to_list(1000)
    return torneos


async def create(torneo: TorneoModel) -> TorneoModel:
    new_torneo = await db["torneo"].insert_one(torneo)
    created_torneo = await db["torneo"].find_one({"_id": new_torneo.inserted_id})
    return created_torneo


async def update_product(torneo_id: str, torneo: TorneoModel) -> TorneoModel:
    ...


async def delete_torneo(torneo_id: str) -> None:
    ...
