from fastapi import APIRouter, Body, HTTPException, status
from fastapi.encoders import jsonable_encoder
from backend.app.domain.entities.torneo import TorneoModel
from backend.app.domain.repositories import torneo_repository

router = APIRouter(tags=["torneo"])


@router.post("/torneos")
async def create_tournament(torneo: TorneoModel = Body(...)):
    torneo = await torneo_repository.create(jsonable_encoder(torneo))
    return torneo


@router.get("/torneos")
async def get_all_tournament():
    return await torneo_repository.read_all()


@router.get("/torneos/{torneo_id}")
async def get_tournament(torneo_id):
    if (torneo := await torneo_repository.read_torne_by_id(torneo_id)) is not None:
        return torneo

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Torneo {torneo_id} no encontrado")


@router.put("/torneos/{torneo_id}")
async def update_tournament(torneo_id):
    pass


@router.delete("/torneos/{torneo_id}")
async def delete_tournament(torneo_id):
    pass
