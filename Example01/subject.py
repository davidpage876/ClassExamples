from student import Student


class Subject:
    """School subject."""

    def __init__(self, code, name):
        """Create a school subject with a subject code (XX####) and name."""
        self._code = code
        self._name = name
        self._students_enrolled = []

    def get_code(self):
        """Get the subject code."""
        return self._code

    def get_name(self):
        """Get the subject name."""
        return self._name

    def get_name_with_code(self):
        """Get the subject code and name as one string (e.g. 'CP1001 Programming')"""
        return f"{self._code} {self._name}"

    def get_students_enrolled(self):
        """Get a list of all students enrolled in the subject."""
        return self._students_enrolled

    def enrol_student(self, student):
        """Enrol a student into the subject.
        Enrolling a student more than once has no effect."""
        if student not in self._students_enrolled:
            self._students_enrolled.append(student)

    def unenrol_student(self, student):
        """Remove an enrolled student from the subject.
        Raises ValueError if trying to remove a student that was not enrolled."""
        if student in self._students_enrolled:
            self._students_enrolled.remove(student)
        else:
            raise ValueError(
                f"Tried to unenrol a student {student.get_name()} "
                f"that was not enrolled in subject {self.get_name_with_code()}")


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

    # Test enrolling a student twice.
    math = Subject("MS1002", "Math Foundations")
    math.enrol_student(jack)
    math.enrol_student(jack)
    print(len(math.get_students_enrolled()), "== 1")
    print(math.get_students_enrolled()[0].get_name(), "== Jack")

    # Test that unenrolling a student not enrolled throws an error.
    try:
        math.unenrol_student(jill)
    except ValueError as error:
        print(error, "== Tried to unenrol Jill")


if __name__ == '__main__':
    _test()
