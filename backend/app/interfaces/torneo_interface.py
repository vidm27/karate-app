from typing import Protocol

from backend.app.domain.entities.torneo import TorneoModel


class TorneoInterface(Protocol):
    async def read_torne_by_id(self, torneo_id: str) -> TorneoModel:
        ...

    async def read_all(self) -> list[TorneoModel]:
        ...

    async def create(self, torneo: TorneoModel) -> TorneoModel:
        ...

    async def update_product(self, torneo_id: str, torneo: TorneoModel) -> TorneoModel:
        ...

    async def delete_torneo(self, torneo_id: str) -> None:
        ...
