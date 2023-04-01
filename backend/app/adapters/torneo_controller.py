from fastapi import APIRouter, Body, HTTPException, status
from fastapi import Response
from fastapi.encoders import jsonable_encoder

from backend.app.domain.entities.torneo import TorneoModel, UpdateTorneoModel
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
async def update_tournament(torneo_id, torneo: UpdateTorneoModel):
    current_torneo = torneo.dict(exclude_none=True)
    torneo = await torneo_repository.update_torneo(torneo_id, current_torneo)

    if torneo is not None:
        return torneo

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Torneo {torneo_id} no encontrado")


@router.delete("/torneos/{torneo_id}")
async def delete_tournament(torneo_id: str):
    delete_result = await torneo_repository.delete_torneo(torneo_id)
    if delete_result:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Torneo {torneo_id} no encontrado")
