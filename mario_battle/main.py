"""Contains the main function for battling."""

from mario_battle.battle_class import MarioBattle
from mario_battle.io import (
    display_welcome_message,
    get_courses,
    get_number_of_rounds,
    get_player_names,
)


def main():
    """The main function."""
    # Display a welcome message
    display_welcome_message()

    # Get player names
    player1, player2 = get_player_names()

    # Get number of rounds
    rounds = get_number_of_rounds()

    # Select which stages to use
    courses = get_courses(rounds)
