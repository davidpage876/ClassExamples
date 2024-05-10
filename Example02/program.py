from school import School
from employee import Employee


class Program:
    def main(self):
        school = School()
        school.add_employee(Employee("David Page"))
        school.add_employee(Employee("Erica Finlay"))

        print("Paying employees...")
        school.get_finance_department().pay_employees()


if __name__ == '__main__':
    program = Program()
    program.main()
