class YogaClub:
    def yoga_role(self):
        print("Role: President - Yoga Club")

class RRCClub:
    def rrc_role(self):
        print("Role: Event Organizer - RRC")

class Student(YogaClub, RRCClub):
    def show_name(self):
        print("Student: Dharshini")

s = Student()
s.show_name()
s.yoga_role()
s.rrc_role()