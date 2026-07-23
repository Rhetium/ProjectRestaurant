from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database import get_db
from app.services import menu_service

router = APIRouter(prefix="/menus", tags=["Menus"])

class MenuInput(BaseModel):
    name: str

class AddDishInput(BaseModel):
    dish_id: int

@router.post("/")
def create_menu(menu_input: MenuInput, db: Session = Depends(get_db)):
    return menu_service.create_menu(db, menu_input.name)

@router.get("/{menu_id}")
def get_menu(menu_id: int, db: Session = Depends(get_db)):
    return menu_service.get_menu_by_id(db, menu_id)

@router.get("/")
def get_all_menus(db: Session = Depends(get_db)):
    return menu_service.get_all_menus(db)

@router.put("/{menu_id}")
def update_menu_name(menu_id: int, new_name: str, db: Session = Depends(get_db)):
    return menu_service.update_menu_name(db, menu_id, new_name)

@router.delete("/{menu_id}")
def delete_menu(menu_id: int, db: Session = Depends(get_db)):
    return menu_service.delete_menu(db, menu_id)

@router.post("/{menu_id}/dishes")
def add_dish_to_menu(menu_id: int, dish_input: AddDishInput, db: Session = Depends(get_db)):
    return menu_service.add_dish_to_menu(db, menu_id, dish_input.dish_id)

@router.delete("/{menu_id}/dishes/{dish_id}")
def remove_dish_from_menu(menu_id: int, dish_id: int, db: Session = Depends(get_db)):
    return menu_service.remove_dish_from_menu(db, menu_id, dish_id)