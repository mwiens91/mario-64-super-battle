"""Contains an object to keep track of battle results."""
import datetime

class MarioBattle:
    """initialize player names, number of rounds, and the courses chosen to play"""
    def __init__(self, player1, player2, num_rounds, courses):
        self.courses = courses
        self.player1 = player1
        self.player2 = player2
        self.num_rounds = num_rounds
        self.p1_total_time = datetime.time()
        self.p2_total_time = datetime.time()
        self.p1_times = []
        self.p2_times = []
    
    """p1_time and p2_time are datetime.time objects"""
    def add_times(self, p1_time, p2_time):
        temp1 = self.p1_total_time
        temp2 = self.p1_total_time
        self.p1_total_time.replace(temp1.hour+p1_time.hour, temp1.minute+p1_time.minute, 
                                   temp1.second+p1_time.second)
        self.p2_total_time.replace(temp2.hour+p2_time.hour, temp2.minute+p2_time.minute, 
                                   temp2.second+p2_time.second)
        self.p1_times.append(p1_time)
        self.p2_times.append(p2_time)
