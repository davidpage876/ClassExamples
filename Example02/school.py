from finance_department import FinanceDepartment


class School:
    def __init__(self):
        self._finance_department = FinanceDepartment(school=self)
        self._employees = []

    def get_finance_department(self):
        return self._finance_department

    def get_employees(self):
        return self._employees

    def add_employee(self, employee):
        self._employees.append(employee)

