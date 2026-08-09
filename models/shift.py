from datetime import time
from enum import Enum

class Weekdays(Enum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"
class Shift:
    def __init__(self, employee, day, start_time, end_time, branch, break_start_time = None):
        self.employee = employee
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.branch = branch
        self.break_start_time = break_start_time
        '''
        break logic to be implemented later, for now we will just store the break start time and assume a fixed break duration of 30 minutes.
        '''
        # if self.break_start_time is not None:
        #     self.break_end_time = self.break_start_time + 30  # Assuming a fixed break duration of 30 minutes to be adjusted later with proper timing input
        self.break_end_time = None