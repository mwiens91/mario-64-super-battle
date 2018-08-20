"""Contains functions for displaying and retreiving info.

All using the command line, at present.
"""

from collections import OrderedDict
from colorama import Fore, Style
from mario_battle.constants import COURSE_DICTIONARY, MARIO_ASCII_ART


class TooFewCoursesError(Exception):
    """An exception for when too few courses are selected."""
    pass

def print_courses(course_dict=COURSE_DICTIONARY, show_played=True):
    """Prints a set of Mario 64 courses.

    By default, this includes all of the courses, all listed as
    unplayed, if the course_dict argument isn't passed in.

    Args:
        course_dict: An optional dictionary (following the schema of
            COURSE_DICTIONARY from constants.py) specifying for each
            course number, what the name of the course is and whether it
            has already been played. Defaults to all courses, with all
            of them unplayed.
        show_played: An optional boolean specifying whether to show if a course
            was played or not. Defaults to True.
    """
    # Make sure the items are in order of course number
    course_dict = OrderedDict(sorted(course_dict.items()))

    # Print the courses
    for number, course_info in course_dict.items():
        # The course string to display
        course_string = "{number}\t".format(number=number)

        if show_played:
            course_string += "({played}) "

        course_string += "{name}".format(name=course_info['name'])

        # Dim the text if the course has already been played
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
    player1 = input("player 1: ")
    player2 = input("player 2: ")
    print()

    return (player1.strip(), player2.strip())

def get_number_of_rounds():
    """Gets the number of rounds from the user.

    The number of rounds must be odd and be no more than 15 (the number
    of courses in Mario 64).

    Returns:
        An integer specifying the number of rounds.
    """
    print("Select number of rounds (1 3 5 7 9 11 13 15 17)")

    while True:
        try:
            # Get the number of rounds
            number = input("> ")

            # Validate
            number = int(number)

            assert number in {1, 3, 5, 7, 9, 11, 13, 15, 17}

            # All good
            break
        except ValueError:
            print(Fore.RED + "One integers only please!" + Style.RESET_ALL)
        except AssertionError:
            print(Fore.RED
                  + "Yikes! Pick an allowed number of rounds!"
                  + Style.RESET_ALL)

    # Print a new line for the next section
    print()

    return number

def get_courses(min_number_of_courses):
    """Gets the courses to select from from the user.

    Arg:
        min_number_of_courses: An integer specifying the minimum number
            of courses that must be selected.
    Returns:
        A dictionary (following the schema of COURSE_DICTIONARY from
        constants.py) specifying for each course number, what the name
        of the course is and whether it has already been played. In this
        case, all the courses will be unplayed.
    """
    # The default set of courses
    DEFAULT_COURSE_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    print("Select which courses to play")
    print("(defaults to 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15)")
    print("-------------------------------------------------")
    print_courses(show_played=False)

    print()

    while True:
        try:
            # Get the courses to choose from
            course_numbers_string = input("> ")

            # Figure out whether to use the default courses
            if not course_numbers_string.strip():
                course_numbers = DEFAULT_COURSE_LIST
                break

            course_numbers = list(set(
                [int(i) for i in course_numbers_string.split()]))

            # Validate
            allowed_course_numbers = COURSE_DICTIONARY.keys()

            for course_number in course_numbers:
                assert course_number in allowed_course_numbers

            if len(course_numbers) < min_number_of_courses:
                raise TooFewCoursesError

            # We're good
            break

        except ValueError:
            print(Fore.RED + "Integers only please!" + Style.RESET_ALL)
        except AssertionError:
            print(Fore.RED
                  + "Yikes! Pick an allowed course number!"
                  + Style.RESET_ALL)
        except TooFewCoursesError:
            print(Fore.RED
                  + "Hey! Pick at least {number} courses!".format(
                      number=min_number_of_courses)
                  + Style.RESET_ALL)

    # Now filter which courses we want to include
    filtered_courses = {}

    for course_number in course_numbers:
        filtered_courses[course_number] = COURSE_DICTIONARY[course_number]

    return filtered_courses

def get_course(course_selection, player, last_stage=False):
    """Asks player which course they want to choose.

    If it's the last stage, the players pick or ban collectively.

    Args:
        course_selection: A dictionary (following the schema of
            COURSE_DICTIONARY from constants.py) specifying for each
            course number, what the name of the course is and whether it
            has already been played. Defaults to all courses, with all
            of them unplayed.
        player: A string containing the name of the player who is
            selecting the course.
        last_stage: An optional boolean specifying if it's the last
            stage.
    Returns:
        A two-tuple containing an integer and a string. The integer
        specifies the course number and the string is the course name.
    """
    return (1, COURSE_DICTIONARY[1]['name'])

def time_player(player, course_name):
    return 1
