"""Contains functions for displaying and retreiving info.

All using the command line, at present.
"""

from collections import OrderedDict
from colorama import Style
from mario_battle.constants import COURSE_DICTIONARY, MARIO_ASCII_ART


def print_courses(course_dict=COURSE_DICTIONARY):
    """Prints a set of Mario 64 courses.

    By default, this includes all of the courses, all listed as
    unplayed, if the course_dict argument isn't passed in.

    Arg:
        course_dict: An optional dictionary (following the schema of
            COURSE_DICTIONARY from constants.py) specifying for each
            course number, what the name of the course is and whether it
            has already been played. Defaults to all courses, with all
            of them unplayed.
    """
    # Make sure the items are in order of course number
    course_dict = OrderedDict(sorted(course_dict.items()))

    # Print the courses
    for number, course_info in course_dict.items():
        # The course string to display
        course_string = "{number}\t({{played}}) {name}".format(
            number=number,
            name=course_info['name'])

        if course_info['played']:
            print(Style.DIM + course_string.format(played='x') + Style.RESET_ALL)
        else:
            print(course_string.format(played=' '))

def display_welcome_message():
    """Displays a welcome message to the user."""
    print("Mario 64 Super-Star Battle")
    print(MARIO_ASCII_ART)
    print("visit us at github.com/mwiens91/mario-64-super-star-battle!")
    print()

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

def get_courses():
    """Gets the courses to select from from the user.

    Returns:
        A dictionary (following the schema of COURSE_DICTIONARY from
        constants.py) specifying for each course number, what the name
        of the course is and whether it has already been played. In this
        case, all the courses will be unplayed.
    """
    print("Select which courses to play")
    print("(defaults to 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15)")
    print("-------------------------------------------------")
    print_courses()

    print()

    return {}
