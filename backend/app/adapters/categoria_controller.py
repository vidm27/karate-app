from fastapi import APIRouter, Body, HTTPException, status, Response
from fastapi.encoders import jsonable_encoder

from backend.app.domain.entities.categoria import CategoriaModel
from backend.app.domain.repositories import categoria_repository

router = APIRouter(tags=["categoria"])


@router.post("/categorias")
async def create_category(categoria: CategoriaModel = Body(...)):
    category = await categoria_repository.create_category(jsonable_encoder(categoria))
    return category


@router.get("/categorias/{categoria_id}")
async def get_category(categoria_id):
    category = await categoria_repository.read_by_id(categoria_id)
    if (res := category) is not None:
        return res
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Categoria {categoria_id} no encontrado")


@router.put("/categorias/{categoria_id}")
async def update_category(categoria_id: str, categoria: CategoriaModel):
    current_category = categoria.dict(exclude_none=True)
    torneo = await categoria_repository.update_category(categoria_id, current_category)

    if torneo is not None:
        return torneo

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Categoria {categoria_id} no encontrado")


@router.delete("/categorias/{categoria_id}")
async def delete_category(categoria_id):
    delete_result = await categoria_repository.delete_category(categoria_id)
    if delete_result:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Categoria {categoria_id} no encontrado")
