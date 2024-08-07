# 

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, validates
from lib.models.database import Base

class Menu(Base):
    __tablename__ = 'menus'
    id = Column(Integer, primary_key=True)
    meal_type = Column(String)
    item = Column(String)
    
    ratings = relationship("Rating", back_populates="menu")
    
    @validates('meal_type')
    def validate_meal_type(self, key, meal_type):
        if meal_type not in ['breakfast', 'lunch', 'dinner', 'specialties']:
            raise ValueError("Invalid meal type")
        return meal_type
    
    @classmethod
    def create(cls, session, meal_type, item):
        menu = cls(meal_type=meal_type, item=item)
        session.add(menu)
        session.commit()
        return menu
    
    @classmethod
    def delete(cls, session, menu_id):
        menu = session.query(cls).filter_by(id=menu_id).first()
        if menu:
            session.delete(menu)
            session.commit()
        return menu


    
    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod 
    def get_by_id(cls, session, menu_id):
        return session.query(cls).filter_by(id=menu_id).first()