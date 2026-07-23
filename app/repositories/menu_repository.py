from sqlalchemy.orm import Session
from app.models.menu import Menu
from app.models.dish import Dish

def get_menu_by_id(db: Session, menu_id: int):
    return db.query(Menu).filter(Menu.id == menu_id).first()

def get_all_menus(db: Session):
    return db.query(Menu).all()

def create_menu(db: Session, name: str):
    new_menu = Menu(name=name)

    db.add(new_menu)
    db.commit()
    db.refresh(new_menu)
    return new_menu

def update_menu_name(db: Session, menu: Menu, new_name: str):
    menu.name = new_name

    db.commit()
    db.refresh(menu)
    return menu

def delete_menu(db: Session, menu: Menu):
    db.delete(menu)
    db.commit()

def add_dish_to_menu(db: Session, menu: Menu, dish: Dish):
    menu.dishes.append(dish)

    db.commit()
    db.refresh(menu)
    return menu


def remove_dish_from_menu(db: Session, menu: Menu, dish: Dish):
    menu.dishes.remove(dish)

    db.commit()
    db.refresh(menu)
    return menu
