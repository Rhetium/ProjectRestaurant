from datetime import datetime
from pydantic import BaseModel
from Class.IngredientClass import Ingredient

class UpdateIngredient(BaseModel):
    update_id: int | None = None
    ingredient: Ingredient
    price: float
    date_added: datetime
