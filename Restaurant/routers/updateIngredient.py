from fastapi import APIRouter
import Cruds.updateIngredient_crud as updateIngredient_crud

router = APIRouter(prefix="/updateIngredient", tags=["updateIngredient"])

@router.put("/{name}")
async def update_ingredient(name: str, price: float):
    return updateIngredient_crud.update_ingredient(name, price)

@router.get("/")
async def list_updates():
    return updateIngredient_crud.list_updates()