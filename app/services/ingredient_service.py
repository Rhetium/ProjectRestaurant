from sqlalchemy.orm import Session
from  app.repositories import ingredient_repository
from app.repositories import dish_repository
from app.services import dish_service

def register_or_update_ingredient(db: Session, name: str, unit: str, cost_per_unit: float):
    existing_ingredient = ingredient_repository.get_ingredient_by_name(db, name)

    if existing_ingredient:
        updated_ingredient = ingredient_repository.update_ingredient_cost(db, existing_ingredient, cost_per_unit)
        
        return updated_ingredient
    else:
        new_ingredient = ingredient_repository.create_ingredient(db, name, unit, cost_per_unit)
    
        return new_ingredient
    

def get_ingredient_by_name(db: Session, ingredient_name: str):
    return ingredient_repository.get_ingredient_by_name(db, ingredient_name)

def list_ingredients(db: Session):
    return ingredient_repository.get_ingredients(db)

def get_ingredient_by_id(db: Session, ingredient_id: int):
    return ingredient_repository.get_ingredient_by_id(db, ingredient_id)

def register_or_update_ingredient(db: Session, name: str, unit: str, cost_per_unit: float):
    existing_ingredient =  ingredient_repository.get_ingredient_by_name(db, name)
    if existing_ingredient:
        updated_ingredient = ingredient_repository.update_ingredient_cost(db, existing_ingredient, cost_per_unit)
        affected_dishes = dish_repository.get_dish_ids_using_ingredient(db, existing_ingredient.id)
        for dish_id in affected_dishes:
            dish_service.recalculate_dish(db, dish_id)
        return updated_ingredient
    else:
        new_ingredient =  ingredient_repository.create_ingredient(db, name, unit, cost_per_unit)
        return new_ingredient
    
