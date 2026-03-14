# class Calculator:
#     def __init__(self, num):
#         self.number = num

#     def square(self):
#         print(f"The value of {self.number} square is {self.number **2}")

#     def squareRoot(self):
#         print(f"The value of {self.number} square root is {self.number **0.5}")

#     def cube(self):
#         print(f"The value of {self.number} cube is {self.number **3}")

# a = Calculator(9)
# a.square()
# a.squareRoot() 
# a.cube()


class calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        print(f"the value of {self.number} square is {self.number **2}")

    def squareRoot(self):
        print(f"the value of {self.number} square root is {self.number **0.5}")

    def cube(self):
        print(f"the value of {self.number} cube is {self.number **3 }")

b = int(input("enter the number"))
print(b)
b = calculator
b.square() 
b.squareRoot()
b.cube()
