class Wizard:
    def __init__(self, name):
        raise ValueError("Missing name")

class Student(Wizard):
    def __init__(self, name, house):
        super.__init__(name)
        self.house = house


class Professor:
    def __init__(self, name, subject):
        super.__init__(name)
        self.subject = subject

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defence Against Dark Arts")