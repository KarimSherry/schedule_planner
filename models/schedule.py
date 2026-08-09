from models import shift


class Schedule:
    def __init__(self, year: int, week: int, shifts = None):
        self.year = year
        self.week = week
        self.shifts = shifts if shifts is not None else []
    def add_shift(self, shift: shift.Shift):
        self.shifts.append(shift)