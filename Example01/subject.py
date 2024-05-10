from student import Student

class Subject:
    """Enrolled in """

    def __init__(self, code, name):
        self._code = code
        self._name = name
        self._students_enrolled = []

    def get_code(self):
        return self._code

    def get_name(self):
        return self._name

    def get_students_enrolled(self):
        return self._students_enrolled

    def enrol_student(self, student):
        self._students_enrolled.append(student)

    def unenrol_student(self, student):
        self._students_enrolled.remove(student)


def _test():
    programming = Subject("CS1001", "Programming")
    english = Subject("EN1002", "English")

    print(programming.get_code(), "== CS1001")
    print(programming.get_name(), "== Programming")
    print(english.get_code(), "== EN1002")
    print(english.get_name(), "== English")

    jack = Student("Jack")
    jill = Student("Jill")

    print(len(programming.get_students_enrolled()), "== 0")
    programming.enrol_student(jack)
    print(len(programming.get_students_enrolled()), "== 1")
    print(programming.get_students_enrolled()[0].get_name(), "== Jack")

    programming.enrol_student(jill)
    print(len(programming.get_students_enrolled()), "== 2")
    print(programming.get_students_enrolled()[0].get_name(), "== Jack")
    print(programming.get_students_enrolled()[1].get_name(), "== Jill")

    programming.unenrol_student(jack)
    print(len(programming.get_students_enrolled()), "== 1")
    print(programming.get_students_enrolled()[0].get_name(), "== Jill")


if __name__ == '__main__':
    _test()
