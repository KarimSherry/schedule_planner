from enum import Enum

class ContractType(Enum):
    RESPONSABLE = "responsable"
    MANAGER = "manager"
    VENDOR = "vendor"
    EXTRA = "extra"
class Contract:
    def __init__(self, weekly_hours, type):
        self.weekly_hours = weekly_hours
        self.type = type # The type of the contract
        @property
        def is_responsable(self):
            return self.type == ContractType.RESPONSABLE
        @property
        def is_manager(self):
            return self.type == ContractType.MANAGER
        @property
        def is_vendor(self):
            return self.type == ContractType.VENDOR
        @property
        def is_extra(self):
            return self.type == ContractType.EXTRA

responsable_contract = Contract(35, ContractType.RESPONSABLE)
manager_contract = Contract(35, ContractType.MANAGER)
vendor_contract = Contract(35, ContractType.VENDOR)
extra_contract = Contract(20, ContractType.EXTRA)