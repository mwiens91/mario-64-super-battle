"""Contains an object to keep track of battle results."""
import datetime

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
        self.num_rounds = num_rounds
        self.p1_total_time = 0
        self.p2_total_time = 0
        self.p1_times = [] #list of course times
        self.p2_times = [] #list of course times
    
    def add_times(self, p1_time, p2_time):
        """p1_time and p2_time are ints representing total seconds"""
        self.p1_total_time += p1_time
        self.p2_total_time += p2_time
        self.p1_times.append(p1_time)
        self.p2_times.append(p2_time)
