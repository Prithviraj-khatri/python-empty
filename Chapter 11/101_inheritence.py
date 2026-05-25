class Employee:
    company = "ITC"
    def show(self):
        print(f"the name is {self.name} and the salry is {self.salary}")

# class programmer:
#     company = "ITC"
#     def show(self):
#         print(f"the name is {self.name} and the salry is {self.salary}")

#     def showLanguage(self):
#         print(f"the name is {self.name} and he is good with {self.language} language")

class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"the name is {self.name} and he is good with {self.language} language")


a = Employee()
p = Programmer()
print(a.company,p.company)

