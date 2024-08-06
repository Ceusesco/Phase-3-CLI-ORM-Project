# Phase-3-CLI-ORM-Project
# CLI Menu Application

## Overview
This CLI application allows users to check available menu options for breakfast, lunch, dinner, and specialties, ask for recommendations, and view the best-rated menus. It uses the `Click` framework for the command-line interface and SQLAlchemy ORM for database interactions.

## Setup

### Prerequisites
- Python 3.8 or higher
- Pipenv

### Installation

<!-- Install Pipenv: -->
pip install pipenv

<!-- Create and activate the virtual environment: -->
pipenv install
pipenv shell

<!-- Set up the database -->
python -c "from lib.models.database import Base, engine; Base.metadata.create_all(engine)"

<!-- Usage -->
Check Menu
To check the available menu options for a specific meal type:

python app/cli.py check-menu --meal <meal_type>

Replace <meal_type> with breakfast, lunch, dinner, or specialties.

Get Recommendation
To get a recommendation for the best-rated menu item for a specific meal type:

python app/cli.py recommend --meal <meal_type>

Replace <meal_type> with breakfast, lunch, dinner, or specialties.


Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Click for the CLI framework.
SQLAlchemy for the ORM.
Pipenv for dependency management.
