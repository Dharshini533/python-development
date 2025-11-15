python
class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def start(self):
        print("Car started with key")

class Bike(Vehicle):
    def start(self):
        print("Bike started with self-start")

v = Vehicle()
c = Car()
b = Bike()

v.start()
c.start()
b.start()