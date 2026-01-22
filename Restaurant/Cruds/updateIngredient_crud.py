from fastapi import HTTPException
from Class.UpdateIngredientClass import UpdateIngredient
from database import ingredient_db, updates_db, next_up_id
from datetime import datetime

def update_ingredient(name: str, price: float):
    global next_up_id
    for ing in ingredient_db.values():
        if ing.name == name:
            # Crear registro de actualización
            update = UpdateIngredient(
                update_id=next_up_id,
                ingredient=ing,
                price=price,
                date_added=datetime.now()
            )
            updates_db[update.update_id] = update
            next_up_id += 1
            return update
    raise HTTPException(status_code=404, detail="Ingredient not found")

def list_updates():
    return list(updates_db.values())