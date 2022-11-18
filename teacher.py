from project_exam.employee import Employee
from project_exam.person import Person

class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."
