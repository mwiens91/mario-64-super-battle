"""Contains an object to keep track of battle results."""

import random


class MarioBattle:
    """Class to store battle results."""
    def __init__(self, player1, player2, num_rounds, courses):
        """Initialize the battle.

        Initialize player names, number of rounds, and the courses chosen to play.

        Args:
            player1: A string containing the name of the first player.
            player2: A string containing the name of the second player.
            num_round: An integer specifying the number of rounds.
            courses: A dictionary (following the schema of
                COURSE_DICTIONARY from constants.py) specifying for each
                selected course number, what the name of the course is
                and whether it has already been played.
        """
        self.courses = courses
        self.player1 = random.choice([player1, player2])
        self.player2 = player2 if self.player1 == player1 else player1
        self.num_rounds = num_rounds
        self.player1_score = 0
        self.player2_score = 0
        self.player1_total_time = 0
        self.player2_total_time = 0
        self.results = [] #list of <round_num, course, times> dict

    def get_players(self, round_):
        """Returns players in order of whose turn it is.

        The players alternate being the first and second player.

        Arg:
            round_: An integer specifying which round it is.

        Returns:
            A tuple of two strings, containing the first and second
            players' names.
        """
        # Alternate first player every round
        if round_ % 2 == 1:
            return (self.player1, self.player2)
        return (self.player2, self.player1)

    def post_results(self, post_dict):
        """Stores round results into results list and updates total times.

        Arg:
            post_dict: A dictionary specifying the results of the round.
                For example,

                {'round': 1,
                 'course': 5,
                 'times': {'Matt': 420.69,
                           'Branko': 69.420}}
        """
        # Append to the results list
        self.results.append(post_dict)

        # Update the total time
        self.add_times(post_dict["times"])

        # Mark the course just played as played
        self.courses[post_dict["course"]]["played"] = True

    def update_scores(
            self,
            first_player,
            second_player,
            first_player_time,
            second_player_time):
        """Update the players' scores after a round.


        Args:
            first_player: A string containing the name of the first
                player.
            second_player: A string containing the name of the second
                player.
            first_player_time A float specifying the round time for the
                first player.
            second_player_time A float specifying  the round time for
                the second player.
        """
        if first_player_time < second_player_time:
            if self.player1 == first_player:
                self.player1_score += 1
            else:
                self.player2_score += 1
        elif second_player_time < first_player_time:
            if self.player1 == first_player:
                self.player2_score += 1
            else:
                self.player1_score += 1
        else:
            pass

    def add_times(self, times):
        """Add round times to the total times.

        Arg:
            times: A dictionary containing the round times of the
                players. For example,

                 {'times': {'Matt': 69.420,
                            'Branko': 420.69}}
        """
        self.player1_total_time += times[self.player1]
        self.player2_total_time += times[self.player2]
