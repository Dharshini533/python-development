class Calculator:
    def add(self, a, b, c=None):
        if c is not None:
            return a + b + c
        else:
            return a + b

calc = Calculator()
print("Add 2 numbers:", calc.add(10, 20))
print("Add 3 numbers:", calc.add(10, 20, 30))