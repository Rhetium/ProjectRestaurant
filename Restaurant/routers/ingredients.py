from fastapi import APIRouter
from Class.IngredientClass import Ingredient
import Cruds.ingredient_crud as ingredient_crud

router = APIRouter(prefix="/ingredients", tags=["ingredients"])

@router.post("/")
async def create_ingredient(ingredient: Ingredient):
    return ingredient_crud.create_ingredient(ingredient)

@router.get("/")
async def list_ingredients():
    return ingredient_crud.list_ingredients()

@router.get("/{name}")
async def get_ingredient(name: str):
    return ingredient_crud.get_ingredient(name)

@router.put("/{name}")
async def update_ingredient(name: str, price: float):
    return ingredient_crud.update_ingredient(name, price)

@router.delete("/{name}")
async def delete_ingredient(name: str):
    return ingredient_crud.delete_ingredient(name)
