from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.database import Base

class Dish(Base):
    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    production_cost = Column(Float, default=0.0)
    profit_percentage = Column(Float, default=0.0)
    sale_price = Column(Float, default=0.0)

    dish_ingredients = relationship("DishIngredient", back_populates="dish")