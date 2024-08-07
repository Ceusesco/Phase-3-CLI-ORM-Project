from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, validates
from lib.models.database import Base

class Rating(Base):
    __tablename__ = 'ratings'
    id = Column(Integer, primary_key=True)
    score = Column(Integer)
    menu_id = Column(Integer, ForeignKey('menus.id'))
    
    menu = relationship("Menu", back_populates="ratings")
    
    @validates('score')
    def validate_score(self, key, score):
        if score < 1 or score > 5:
            raise ValueError("Score must be between 1 and 5")
        return score
    
    @classmethod
    def create(cls, session, score, menu_id):
        rating = cls(score=score, menu_id=menu_id)
        session.add(rating)
        session.commit()
        return rating
    
    @classmethod
    def delete(cls, session, rating_id):
        rating = session.query(cls).filter_by(id=rating_id).first()
        if rating:
            session.delete(rating)
            session.commit()
        return rating

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, session, rating_id):
        return session.query(cls).filter_by(id=rating_id).first()
