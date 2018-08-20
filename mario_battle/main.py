"""Contains the main function for battling."""

import signal
import sys
from mario_battle.battle_class import MarioBattle
from mario_battle.io import (
    display_welcome_message,
    get_course,
    get_courses,
    get_number_of_rounds,
    get_player_names,
    time_player,
)


def exit_program(*_, **__):
    """Exits the program."""
    print("\n\nSee ya!")
    sys.exit(0)

def main():
    """The main function."""
    # Register the ending message for a keyboard interrupt
    signal.signal(signal.SIGINT, exit_program)

    # Display a welcome message
    display_welcome_message()

    # Get player names
    player1, player2 = get_player_names()

    # Get number of rounds
    rounds = get_number_of_rounds()

    # Select which stages to use
    courses = get_courses(rounds)

    # Initialize the battle
    battle = MarioBattle(
        player1=player1,
        player2=player2,
        num_rounds=rounds,
        courses=courses)

    # Battle!
    for round_ in range(1, rounds + 1):
        # Determine starting player
        first_player, second_player = battle.get_players(round_)

        # Determine stage
        if round_ == rounds:
            course_number, course_name = get_course(
                course_selection=battle.courses,
                player=first_player,
                last_stage=True)
        else:
            course_number, course_name = get_course(
                course_selection=battle.courses,
                player=first_player,
                last_stage=False)

        # First player's turn!
        first_player_time = time_player(
            player=first_player,
            course_name=course_name)

        # Second player's turn!
        second_player_time = time_player(
            player=second_player,
            course_name=course_name)

        # Return results
        post_dict = {
            'round': round_,
            'course': course_number,
            'times': {
                first_player: first_player_time,
                second_player: second_player_time
            }
        }

        battle.post_results(post_dict)
