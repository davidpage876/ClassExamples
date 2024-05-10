
class Student:
    """Student record in the school."""

    def __init__(self, name):
        """Create a student with name."""
        self._name = name

    def get_name(self):
        """Get the student's name."""
        return self._name


def _test():
    jack = Student("Jack")
    jill = Student("Jill")

    print(jack.get_name(), "== Jack")
    print(jill.get_name(), "== Jill")


if __name__ == '__main__':
    _test()
