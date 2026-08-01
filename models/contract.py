type_of_contract = ["responsable", "manager", "vendor", "extra"]
class Contract:
    def __init__(self, weekly_hours, type):
        self.weekly_hours = weekly_hours
        self.type = type # The type of the contract
        self.is_responsable = True if type == type_of_contract[0] else False
        self.is_manager = True if type == type_of_contract[1] else False

responsable_contract = Contract(35, type_of_contract[0])
manager_contract = Contract(35, type_of_contract[1])
vendor_contract = Contract(20, type_of_contract[2])
extra_contract = Contract(20, type_of_contract[3])