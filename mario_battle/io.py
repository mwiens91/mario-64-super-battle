"""Contains functions for displaying and retreiving info.

All using the command line, at present.
"""


def display_welcome_message():
    """Displays a welcome message to the user."""
    print("HEY WELCOME TO MARIO")

def get_player_names():
    """Gets the player names from the user.

    Returns:
        A tuple of two strings, containing the player names.
    """
    return ("Matt", "Branko")

def get_number_of_rounds():
    """Gets the number of rounds from the user.

    The number of rounds must be odd and be no more than 15 (the number
    of courses in Mario 64).

    Returns:
        An integer specifying the number of rounds.
    """
    return 5
