from sqlalchemy.orm import Session
from app.models.ingredient import Ingredient

def get_ingredient_by_id(db: Session, ingredient_id: int):
    return db.query(Ingredient).filter(Ingredient.id == ingredient_id).first()

def get_ingredient_by_name(db: Session, name: str):
    return db.query(Ingredient).filter(Ingredient.name == name).first()

def get_ingredients(db: Session):
    return db.query(Ingredient).all()

def create_ingredient(db: Session, name: str, unit:str, cost_per_unit: float):
    new_ingredient = Ingredient(name=name, unit=unit, cost_per_unit=cost_per_unit)
    db.add(new_ingredient)
    db.commit()
    db.refresh(new_ingredient)
    return new_ingredient

def update_ingredient_cost(db:Session, ingredient: Ingredient, new_cost: float):
    ingredient.cost_per_unit = new_cost
    db.commit()
    db.refresh(ingredient)
    return ingredient

