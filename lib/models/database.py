from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Import models to register them with SQLAlchemy
from lib.models import Menu, Rating

engine = create_engine('sqlite:///lib.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
