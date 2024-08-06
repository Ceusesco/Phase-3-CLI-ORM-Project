from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from lib.models.database import Base

class Rating(Base):
    __tablename__ = 'ratings'
    id = Column(Integer, primary_key=True)
    menu_id = Column(Integer, ForeignKey('menus.id'))
    rating = Column(Integer)
    menu = relationship('Menu', back_populates='ratings')

Menu.ratings = relationship('Rating', order_by=Rating.id, back_populates='menu')
