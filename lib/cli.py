#!/usr/bin/env python3

import click
from lib.models.database import session
from lib.models.menu import Menu
from lib.models.rating import Rating
from lib.utils import log_debug, log_error 





@click.group()
def cli():
    """A simple CLI application to check menus and ratings."""
    pass

@click.command()
@click.option('--meal', type=click.Choice(['breakfast', 'lunch', 'dinner', 'specialties']), prompt='Meal type', help='Type of meal to check.')
def check_menu(meal):
    try:
        menus = session.query(Menu).filter_by(meal_type=meal).all()
        if menus:
            click.echo(f"Available {meal} options:")
            for menu in menus:
                click.echo(f"- {menu.item}")
            log_debug(f"Checked menu for {meal}")
        else:
            click.echo(f"No {meal} options available.")
            log_debug(f"No {meal} options found")
    except Exception as e:
        log_error(f"Error checking menu: {e}")

@click.command()
@click.option('--meal', type=click.Choice(['breakfast', 'lunch', 'dinner', 'specialties']), prompt='Meal type', help='Type of meal to get recommendations for.')
def recommend(meal):
    try:
        best_rated = session.query(Menu).join(Rating).filter(Menu.meal_type == meal).order_by(Rating.rating.desc()).first()
        if best_rated:
            click.echo(f"Recommended {meal} option: {best_rated.item} with rating {best_rated.ratings[0].rating}")
            log_debug(f"Recommended {meal} option: {best_rated.item}")
        else:
            click.echo(f"No recommendations available for {meal}.")
            log_debug(f"No recommendations found for {meal}")
    except Exception as e:
        log_error(f"Error getting recommendations: {e}")

cli.add_command(check_menu)
cli.add_command(recommend)

if __name__ == '__main__':
    cli()
