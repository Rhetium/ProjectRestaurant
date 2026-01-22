from typing import Dict
from Class.IngredientClass import Ingredient
from Class.UpdateIngredientClass import UpdateIngredient

ingredient_db: Dict[int, Ingredient] = {}
updates_db: Dict[int, UpdateIngredient] = {}

next_ing_id = 1
next_up_id = 1