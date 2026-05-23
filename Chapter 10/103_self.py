class employee:
    lan = "python"
    salary = 120000

    def getInfo(self):
        print(f"the language is {self.lan} and the salary is {self.salary}")
    @staticmethod # it is an decorator if we dont wnat to use self
    def greet():
        print("good morning")


harry = employee()
harry.lan = "javascript"
print(harry.lan, harry.salary)
harry.greet()
harry.getInfo()
# employee.getInfo(harry)
