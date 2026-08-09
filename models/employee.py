from datetime import date
class Employee:
    def __init__(self, id: int, name: str, start_date: date, end_date: date, contract, notes = ""):
        # might have to add availability later
        self.id = id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.contract = contract
        self.notes = notes
