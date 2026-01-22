from fastapi import HTTPException
from Class.IngredientClass import Ingredient
from database import ingredient_db, next_ing_id

def create_ingredient(ingredient: Ingredient):
    global next_ing_id
    if ingredient.name in ingredient_db:
        raise HTTPException(status_code=400, detail="Ingredient already exists")
    ingredient.id = next_ing_id
    ingredient_db[ingredient.name] = ingredient
    next_ing_id += 1
    return ingredient

def get_ingredient(name: str):
    ingredient = ingredient_db.get(name)
    if not ingredient:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    return ingredient

def list_ingredients():
    return list(ingredient_db.values())

def update_ingredient(name: str, ingredient: Ingredient):
    if name not in ingredient_db:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    ingredient_db[name] = ingredient
    return ingredient

def delete_ingredient(name: str):
    if name not in ingredient_db:
        raise HTTPException(status_code=404, detail="Ingredient not found")
    del ingredient_db[name]
    return {"detail": "Ingredient deleted"}