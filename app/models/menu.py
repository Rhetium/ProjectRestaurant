from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

menu_dish = Table(
    "menu_dish",
    Base.metadata,
    Column("menu_id", Integer, ForeignKey("menu.id")),
    Column("dish_id", Integer, ForeignKey("dishes.id")),
)

class Menu(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    dishes = relationship("Dish", secondary=menu_dish)