class employee:
    lan = "python"
    salary = 120000

    def __init__(self,name,salary,lan): # it is an dunder method which is called automatically
        self.name = name
        self.salary = salary
        self.lan = lan
        print("i am creating an object")

    def getInfo(self):
        print(f"the language is {self.lan} and the salary is {self.salary}")
    @staticmethod # it is an decorator if we dont wnat to use self
    def greet():
        print("good morning")


harry = employee("Harry",1300000, "javascript")
# harry.name = "harry"
print(harry.name,harry.salary,harry.lan)
