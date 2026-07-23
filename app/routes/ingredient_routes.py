from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database import get_db
from app.services import ingredient_service

router = APIRouter(prefix="/ingredients", tags=["Ingredients"])

class IngredientCreate(BaseModel):
    name: str
    unit: str
    cost_per_unit: float

@router.post("/")
def create_ingredient(data: IngredientCreate, db: Session = Depends (get_db)):
    result = ingredient_service.register_or_update_ingredient(db, data.name, data.unit, data.cost_per_unit)
    return result

@router.get("/")
def list_ingredients(db: Session = Depends(get_db)):
    return ingredient_service.list_ingredients(db)

@router.get("/{ingredient_id}")
def get_ingredient(ingredient_id: int, db: Session = Depends(get_db)):
    ingredient = ingredient_service.get_ingredient_by_id(db, ingredient_id)
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return ingredient

#-----------------------------------------------------------------------------