class Employee:
    def __init__(self, id, name, start_date, end_date, contract, notes = ""):
        # might have to add availability later
        self.id = id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.contract = contract
        self.notes = notes
