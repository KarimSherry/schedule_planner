from datetime import time
class Branch:
    def __init__(self, name: str, opening_time: time, closing_time: time):
        self.name = name
        self.opening_time = opening_time
        self.closing_time = closing_time

branch1 = Branch("Branch 1", time(8, 0), time(0, 0))  # Branch 1: Open from 8 AM to 12 AM (midnight)
branch2 = Branch("Branch 2", time(8, 0), time(0, 0))  # Branch 2: Open from 8 AM to 12 AM (midnight)
branch3 = Branch("Branch 3", time(12, 0), time(20, 0))  # Branch 3: Open from 12 PM to 8 PM
branch4 = Branch("Branch 4", time(11, 0), time(23, 0))  # Branch 4: Open from 11 AM to 11 PM
branch5 = Branch("Branch 5", time(11, 0), time(23, 0))  # Branch 5: Open from 11 AM to 11 PM