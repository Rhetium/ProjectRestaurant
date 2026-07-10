from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    unit = Column(String)
    cost_per_unit = Column(Float)