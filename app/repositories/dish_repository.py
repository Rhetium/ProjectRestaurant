from sqlalchemy.orm import Session
from app.models.dish import Dish
from app.models.dish_ingredient import DishIngredient

def get_dish_by_id(db: Session, dish_id: int):
    return db.query(Dish).filter(Dish.id == dish_id).first()

def get_all_dishes(db: Session):
    return db.query(Dish).all()

def get_dish_by_name(db: Session, search_text: str):
    search_pattern = f"%{search_text}%"
    return db.query(Dish).filter(Dish.name.ilike(search_pattern)).all()

def create_dish(db: Session, name: str, profit_percentage: float):
    new_dish = Dish(
        name=name,
        profit_percentage=profit_percentage,
        production_cost=0.0,
        sale_price=0.0
    )
    db.add(new_dish)
    db.commit()
    db.refresh(new_dish)
    return 

def update_dish_name_and_profit(db: Session, dish: Dish, name: str, profit_percentage: float):
    dish.name = name
    dish.profit_percentage = profit_percentage
    db.commit()
    db.refresh(dish)
    return dish

def update_dish_cost(db: Session, dish: Dish, production_cost: float, sale_price: float):
    dish.production_cost = production_cost
    dish.sale_price = sale_price
    db.commit()
    db.refresh(dish)
    return dish

def delete_dish(db: Session, dish: Dish):
    db.delete(dish)
    db.commit()

#-------------------------------------------------------------------------------------------------

def get_dish_ingredient(db: Session, dish_id: int):
    return db.query(DishIngredient).filter(DishIngredient.dish_id == dish_id).all()

def add_ingredient_to_dish(db: Session, dish_id: int, ingredient_id: int, quantity: float):
    new_dish_ingredient = DishIngredient(
        dish_id=dish_id,
        ingredient_id=ingredient_id,
        quantity=quantity
    )
    db.add(new_dish_ingredient)
    db.commit()
    db.refresh(new_dish_ingredient)
    return new_dish_ingredient

def remove_ingredient_from_dish(db: Session, dish_ingredient: DishIngredient):
    db.delete(dish_ingredient)
    db.commit()

def get_dish_ids_using_ingredient(db: Session, ingredient_id: int):
    relations =  db.query(DishIngredient).filter(DishIngredient.ingredient_id == ingredient_id).all()
    dish_ids = set()
    for relation in relations:
        dish_ids.add(relation.dish_id)
    return list(dish_ids)