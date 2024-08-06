from sqlalchemy import Column, Integer, String
from lib.models.database import Base

class Menu(Base):
    __tablename__ = 'menus'
    id = Column(Integer, primary_key=True)
    meal_type = Column(String)  # e.g., breakfast, lunch, dinner, specialties
    item = Column(String)
