from models import branch, shift, employee, contract, schedule
from datetime import time

branch1 = branch.branch1
responsable_contract = contract.responsable_contract
manager_contract = contract.manager_contract
vendor_contract = contract.vendor_contract
extra_contract = contract.extra_contract

john = employee.Employee(1, "John Doe", "2026-01-01", "2026-12-31", responsable_contract)
smith = employee.Employee(2, "Smith Johnson", "2026-01-01", "2026-12-31", manager_contract)
mary = employee.Employee(3, "Mary Williams", "2026-01-01", "2026-12-31", vendor_contract)
caroline = employee.Employee(4, "Caroline Brown", "2026-01-01", "2026-12-31", extra_contract)

schedule1 = schedule.Schedule(2026, 32)
shift1 = shift.Shift(john, shift.Weekdays.MONDAY, time(8, 0), time(16, 0), branch1)
schedule1.add_shift(shift1)
shift2 = shift.Shift(smith, shift.Weekdays.TUESDAY, time(9, 0), time(17, 0), branch1)
schedule1.add_shift(shift2)
shift3 = shift.Shift(mary, shift.Weekdays.WEDNESDAY, time(10, 0), time(18, 0), branch1)
schedule1.add_shift(shift3)
shift4 = shift.Shift(caroline, shift.Weekdays.THURSDAY, time(11, 0), time(19, 0), branch1)
schedule1.add_shift(shift4)

for shift in schedule1.shifts:
    print(f"Employee: {shift.employee.name}, Day: {shift.day}, Start Time: {shift.start_time}, End Time: {shift.end_time}, Branch: {shift.branch.name}")

