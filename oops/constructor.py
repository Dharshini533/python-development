class Student:
    def __init__(self, name, reg_no):
        self.name = name
        self.reg_no = reg_no

    def display(self):
        print("Name:", self.name)
        print("Reg No:", self.reg_no)

s1 = Student("Dharshini", "22EC001")
s1.display()