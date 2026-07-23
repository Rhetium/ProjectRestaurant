from sqlalchemy.orm import Session
from app.repositories import menu_repository, dish_repository

def  create_menu(db: Session, name: str):
    return menu_repository.create_menu(db, name)

def get_menu_by_id(db: Session, menu_id: int):
    return menu_repository.get_menu_by_id(db, menu_id)

def get_all_menus(db: Session):
    return menu_repository.get_all_menus(db)

def update_menu_name(db: Session, menu_id: int, new_name: str):
    menu = menu_repository.get_menu_by_id(db, menu_id)
    return menu_repository.update_menu_name(db, menu, new_name)

def delete_menu(db: Session, menu_id: int):
    menu = menu_repository.get_menu_by_id(db, menu_id)
    return menu_repository.delete_menu(db, menu)

def add_dish_to_menu(db: Session, menu_id: int, dish_id: int):
    menu = menu_repository.get_menu_by_id(db, menu_id)
    dish = dish_repository.get_dish_by_id(db, dish_id)
    return menu_repository.add_dish_to_menu(db, menu, dish)

def remove_dish_from_menu(db: Session, menu_id: int, dish_id: int):
    menu = menu_repository.get_menu_by_id(db, menu_id)
    dish = dish_repository.get_dish_by_id(db, dish_id)
    return menu_repository.remove_dish_from_menu(db, menu, dish)