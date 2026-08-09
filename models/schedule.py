class Schedule:
    def __init__(self, year, week, shifts = None):
        self.year = year
        self.week = week
        self.shifts = shifts if shifts is not None else []
    def add_shift(self, shift):
        self.shifts.append(shift)