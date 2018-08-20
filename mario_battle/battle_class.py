"""Contains an object to keep track of battle results."""
import time
import random

def show_times(seconds):
    """returns time elapsed in "hours:minutes:seconds.millisecond" string"""
    hours = seconds // 3600
    minutes = (seconds - (hours*3600)) // 60
    seconds = seconds - (hours*3600) - (minutes*60)
    time_elapsed = "{:02.0f}:{:02.0f}:{:06.3f}".format(hours,minutes,seconds)
    return time_elapsed

class MarioBattle:
    def __init__(self, player1, player2, num_rounds, courses):
        """initialize player names, number of rounds, and the courses chosen to play"""
        self.courses = courses
        self.player1 = player1
        self.player2 = player2
        self.first_player = random.randint(1,2)
        self.num_rounds = num_rounds
        self.p1_total_time = 0
        self.p2_total_time = 0
        self.results = [] #list of <round_num, course, times> dict

    def get_players(self, _round):
        """returns players in order of whose turn it is"""
        if _round%2 == 1:
            return self.player1, self.player2
        else:
            return self.player2, self.player1

    def post_results(self, post_dict):
        """stores <round, course, times> dict into results list"""
        self.results.append(post_dict)
        self.add_times(post_dict["times"])
    
    def add_times(self, times):
        """p1_time and p2_time are floats representing seconds"""
        self.p1_total_time += times[self.player1]
        self.p2_total_time += times[self.player2]
