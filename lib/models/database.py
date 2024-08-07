

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the Base class
Base = declarative_base()

# Create an engine
engine = create_engine('sqlite:///lib.db')

# Create a configured "Session" class
Session = sessionmaker(bind=engine)



