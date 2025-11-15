class Person:
    def __init__(self, name):
        self.name = name

    def show_person(self):
        print("Person Name:", self.name)

class Student(Person):
    def __init__(self, name, dept):
        super().__init__(name)
        self.dept = dept

    def show_student(self):
        print("Department:", self.dept)

s = Student("Dharshini", "ECE")
s.show_person()
s.show_student()