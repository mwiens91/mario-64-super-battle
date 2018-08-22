"""Contains an object to keep track of battle results."""

import random


class MarioBattle:
    """Class to store battle results.

    Attributes:
        player1: A string containing the name of the first player.
        player2: A string containing the name of the second player.
        player1_score: An integer specifying the score of the first
            player.
        player2_score: An integer specifying the score of the second
            player.
        player1_total_time: A float specifying the total time (in
            seconds) taken by the first player.
        player2_total_time: A float specifying the total time (in
            seconds) taken by the second player.
        courses: A dictionary containing the courses that are eligible
            to be played. This, following the schema of
            COURSE_DICTIONARY from constants.py, specified for each
            course number, what the name of the course is and whether it
            has already been played.
        num_rounds: An integer specifying the total number of rounds.
        results: A list containing dictionaries specifing the results of
            each round. For example,

            {'round': 1,
             'course': 5,
             'times': {'Matt': 420.69,
                       'Branko': 69.420}}
    """
    def __init__(self, player1, player2, courses, num_rounds):
        """Initialize the battle.

        Initialize player names, number of rounds, and the courses chosen to play.

        Args:
            player1: A string containing the name of the first player.
            player2: A string containing the name of the second player.
            courses: A dictionary (following the schema of
                COURSE_DICTIONARY from constants.py) specifying for each
                selected course number, what the name of the course is
                and whether it has already been played.
            num_rounds: An integer specifying the total number of rounds.
        """
        self.player1 = random.choice([player1, player2])
        self.player2 = player2 if self.player1 == player1 else player1
        self.player1_score = 0
        self.player2_score = 0
        self.player1_total_time = 0
        self.player2_total_time = 0
        self.courses = courses
        self.num_rounds = num_rounds
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
        self.update_total_times(post_dict["times"])

        # Update the players' scores
        self.update_scores(post_dict["times"])

        # Mark the course just played as played
        self.courses[post_dict["course"]]["played"] = True

    def update_scores(self, times):
        """Update the players' scores after a round.

        Arg:
            times: A dictionary containing the round times of the
                players. For example,

                 {'times': {'Matt': 69.420,
                            'Branko': 420.69}}
        """
        if times[self.player1] < times[self.player2]:
            self.player1_score += 1
        elif times[self.player1] > times[self.player2]:
            self.player2_score += 1
        else:
            # Tie!
            pass

    def update_total_times(self, times):
        """Add round times to the total times.

        Arg:
            times: A dictionary containing the round times of the
                players. For example,

                 {'times': {'Matt': 69.420,
                            'Branko': 420.69}}
        """
        self.player1_total_time += times[self.player1]
        self.player2_total_time += times[self.player2]
