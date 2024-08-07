

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import the base class and models
from lib.models.database import Base, engine, Session
from lib.models.menu import Menu
from lib.models.rating import Rating


# #Create an engine [added from debbugging]
engine = create_engine ('sqlite:///lib.db')

# Create all tables in the engine (database)
Base.metadata.create_all(engine)

# Create a Session
session = Session()

# Create and add dummy data
def populate_db(session):
    # Dummy menus
    menus = [
        Menu(meal_type="breakfast", item="Pancakes"),
        Menu(meal_type="lunch", item="Caesar Salad"),
        Menu(meal_type="dinner", item="Spaghetti Bolognese"),
        Menu(meal_type="specialties", item="Lobster Bisque")
    ]
    
    session.add_all(menus)
    session.commit()

    # Dummy ratings
    ratings = [
        Rating(score=5, menu_id=menus[0].id),
        Rating(score=4, menu_id=menus[0].id),
        Rating(score=3, menu_id=menus[1].id),
        Rating(score=4, menu_id=menus[2].id),
        Rating(score=5, menu_id=menus[3].id)
    ]
    
    session.add_all(ratings)
    session.commit()

# Populate the database with dummy data
populate_db(session)

# Query and print the data to verify
menus = session.query(Menu).all()
for menu in menus:
    print(f"Menu: {menu.meal_type} - {menu.item}")
    for rating in menu.ratings:
        print(f"  Rating: {rating.score}")

session.close()
