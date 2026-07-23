from sqlalchemy.orm import Session
from app.repositories import dish_repository

def calculate_production_cost(dish_ingredients):
    total_cost = 0.0
    for dish_ingredient in dish_ingredients:
        ingredient_cost = dish_ingredient.ingredient.cost_per_unit
        quantity = dish_ingredient.quantity
        total_cost += ingredient_cost * quantity
    return total_cost

def calculate_sale_price(production_cost: float, profit_percentage: float):
    profit_amount = production_cost * (profit_percentage / 100)
    sale_price = production_cost + profit_amount
    return sale_price

def recalculate_dish(db: Session, dish_id: int):
    dish = dish_repository.get_dish_by_id(db, dish_id)
    if not dish:
        return None

    dish_ingredients = dish_repository.get_dish_ingredient(db, dish_id)
    new_production_cost = calculate_production_cost(dish_ingredients)
    new_sale_price = calculate_sale_price(new_production_cost, dish.profit_percentage)

    updated_dish = dish_repository.update_dish_cost(db, dish, new_production_cost, new_sale_price)
    return updated_dish

def create_dish(db: Session, name: str, profit_percentage: float):
    new_dish = dish_repository.create_dish(db, name, profit_percentage)
    return new_dish

def get_dish_by_id(db: Session, dish_id: int):
    return dish_repository.get_dish_by_id(db, dish_id)

def get_all_dishes(db: Session):
    return dish_repository.get_all_dishes(db)

def search_dish(db: Session, search_text: str):
    return dish_repository.get_dish_by_name(db, search_text)

def update_dish(db: Session, dish_id: int, name: str, profit_percentage: float):
    dish = dish_repository.get_dish_by_id(db, dish_id)
    if not dish:
        return None
    dish_repository.update_dish_name_and_profit(db, dish, name, profit_percentage)
    updated_dish = recalculate_dish(db, dish_id)
    return updated_dish

def delete_dish(db: Session, dish_id: int):
    dish = dish_repository.get_dish_by_id(db, dish_id)
    if not dish:
        return None
    dish_repository.delete_dish(db, dish)
    return 

def add_ingredient_to_dish(db: Session, dish_id: int, ingredient_id: int, quantity: float):
    dish_repository.add_ingredient_to_dish(db, dish_id, ingredient_id, quantity)
    updated_dish = recalculate_dish(db, dish_id)
    return updated_dish

def get_dish_ingredients(db: Session, dish_id: int):
    return dish_repository.get_dish_ingredient(db, dish_id)