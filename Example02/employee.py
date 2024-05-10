
class Employee:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def pay(self):
        print(f"{self._name} got paid!")
