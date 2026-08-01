class Employee:
    def __init__(self, id, name, start_date, end_date, contract, notes = ""):
        self.id = id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.contract = contract
        self.notes = notes
