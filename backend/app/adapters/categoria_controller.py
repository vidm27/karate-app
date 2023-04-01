from fastapi import APIRouter

router = APIRouter(tags=["categoria"])


@router.post("/categorias")
async def create_category():
    pass


@router.get("/categorias/{categoria_id}")
async def get_category(categoria_id):
    pass


@router.put("/categorias/{categoria_id}")
async def update_category(categoria_id):
    pass


@router.delete("/categorias/{categoria_id}")
async def delete_category(categoria_id):
    pass
