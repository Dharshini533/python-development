python
class College:
    def show_college(self):
        print("College: SNS College of Technology")

class Department(College):
    def show_dept(self):
        print("Department: ECE")

class Student(Department):
    def show_student(self):
        print("Student: Dharshini")

s = Student()
s.show_college()
s.show_dept()
s.show_student()