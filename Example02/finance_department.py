

class FinanceDepartment:
    def __init__(self, school):
        self._school = school

    def pay_employees(self):
        for employee in self._school.get_employees():
            employee.pay()
