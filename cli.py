
from sqlalchemy import create_engine # type: ignore
from sqlalchemy.orm import sessionmaker
from lib.models.database import Base
from lib.models.menu import Menu
from lib.models.rating import Rating

engine = create_engine('sqlite:///lib.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Manage Menus")
        print("2. Manage Ratings")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            manage_menus()
        elif choice == '2':
            manage_ratings()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_menus():
    while True:
        print("\nManage Menus")
        print("1. Create Menu")
        print("2. Delete Menu")
        print("3. Display All Menus")
        print("4. Find Menu by ID")
        print("5. Back to Main Menu")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            create_menu()
        elif choice == '2':
            delete_menu()
        elif choice == '3':
            display_all_menus()
        elif choice == '4':
            find_menu_by_id()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_ratings():
    while True:
        print("\nManage Ratings")
        print("1. Create Rating")
        print("2. Delete Rating")
        print("3. Display All Ratings")
        print("4. Find Rating by ID")
        print("5. View Ratings by Menu ID")
        print("6. Back to Main Menu")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            create_rating()
        elif choice == '2':
            delete_rating()
        elif choice == '3':
            display_all_ratings()
        elif choice == '4':
            find_rating_by_id()
        elif choice == '5':
            view_ratings_by_menu_id()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

def create_menu():
    meal_type = input("Enter meal type (breakfast, lunch, dinner, specialties): ")
    item = input("Enter menu item: ")
    try:
        Menu.create(session, meal_type, item)
        print("Menu created successfully.")
    except ValueError as e:
        print(f"Error: {e}")

def delete_menu():
    menu_id = input("Enter menu ID to delete: ")
    if Menu.delete(session, menu_id):
        print("Menu deleted successfully.")
    else:
        print("Menu not found.")

def display_all_menus():
    menus = Menu.get_all(session)
    for menu in menus:
        print(f"ID: {menu.id}, Meal Type: {menu.meal_type}, Item: {menu.item}")

def find_menu_by_id():
    menu_id = input("Enter menu ID: ")
    menu = Menu.find_by_id(session, menu_id)
    if menu:
        print(f"ID: {menu.id}, Meal Type: {menu.meal_type}, Item: {menu.item}")
    else:
        print("Menu not found.")

def create_rating():
    score = input("Enter rating score (1-5): ")
    menu_id = input("Enter menu ID for the rating: ")
    try:
        Rating.create(session, int(score), int(menu_id))
        print("Rating created successfully.")
    except ValueError as e:
        print(f"Error: {e}")

def delete_rating():
    rating_id = input("Enter rating ID to delete: ")
    if Rating.delete(session, rating_id):
        print("Rating deleted successfully.")
    else:
        print("Rating not found.")

def display_all_ratings():
    ratings = Rating.get_all(session)
    for rating in ratings:
        print(f"ID: {rating.id}, Score: {rating.score}, Menu ID: {rating.menu_id}")

def find_rating_by_id():
    rating_id = input("Enter rating ID: ")
    rating = Rating.find_by_id(session, rating_id)
    if rating:
        print(f"ID: {rating.id}, Score: {rating.score}, Menu ID: {rating.menu_id}")
    else:
        print("Rating not found.")

def view_ratings_by_menu_id():
    menu_id = input("Enter menu ID to view ratings: ")
    menu = Menu.find_by_id(session, menu_id)
    if menu:
        print(f"Ratings for {menu.item}:")
        for rating in menu.ratings:
            print(f"  Score: {rating.score}")
    else:
        print("Menu not found.")

if __name__ == "__main__":
    main_menu()