from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.sql import func

from app.database import Base

class IngredientHistory(Base):
    __tablename__ = "ingredient_history"

    id = Column(Integer, primary_key=True, index=True)

    ingredient_id = Column(Integer, ForeignKey("ingredients.id"))
    cost = Column(Float)
    changed_at = Column(DateTime(timezone=True), server_default=func.now())