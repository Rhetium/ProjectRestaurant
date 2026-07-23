from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database import get_db
from app.services import dish_service

router = APIRouter(prefix="/dishes", tags=["Dishes"])

class DishInput(BaseModel):
    name: str
    profit_percentage: float

class AddIngredientInput(BaseModel):
    ingredient_id: int
    quantity: float

@router.post("/")
def create_dish(dish_input: DishInput, db: Session = Depends(get_db)):
    return dish_service.create_dish(db, dish_input.name, dish_input.profit_percentage)

@router.get("/")
def list_dishes(db: Session = Depends(get_db)):
    return dish_service.get_all_dishes(db)

@router.get("/search")
def search_dishes(search_text: str, db: Session = Depends(get_db)):
    return dish_service.search_dish(db, search_text)

@router.get("/{dish_id}")
def get_dish(dish_id: int, db: Session = Depends(get_db)):
    dish = dish_service.get_dish_by_id(db, dish_id)
    if not dish:
        raise HTTPException(status_code=404, detail="Dish not found")
    return dish

@router.put("/{dish_id}")
def update_dish(dish_id: int, dish_input: DishInput, db: Session = Depends(get_db)):
    updated_dish = dish_service.update_dish(db, dish_id, dish_input.name, dish_input.profit_percentage)
    if not updated_dish:
        raise HTTPException(status_code=404, detail="Dish not found")
    return updated_dish

@router.delete("/{dish_id}")
def delete_dish(dish_id: int, db: Session = Depends(get_db)):
    result = dish_service.delete_dish(db, dish_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Dish not found")
    return {"message": "Dish deleted successfully"}

@router.post("/{dish_id}/ingredients")
def add_ingredient_to_dish(dish_id: int, ingredient_input: AddIngredientInput, db: Session = Depends(get_db)):
    updated_dish = dish_service.add_ingredient_to_dish(db, dish_id, ingredient_input.ingredient_id, ingredient_input.quantity)
    if not updated_dish:
        raise HTTPException(status_code=404, detail="Dish not found")
    return updated_dish

@router.get("/{dish_id}/ingredients")
def get_dish_ingredients(dish_id: int, db: Session = Depends(get_db)):
    ingredients = dish_service.get_dish_ingredients(db, dish_id)
    if ingredients is None:
        raise HTTPException(status_code=404, detail="Dish not found")
    return ingredients