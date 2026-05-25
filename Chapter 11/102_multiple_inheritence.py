class Employee:
    company = "ITC"
    name = "default"
    def show(self):
        print(f"the name is {self.name} and the salry is {self.company}")

class coder:
    language = "python"

    def printlanguages(self):
        print(f"this is your language: {self.language}")


class Programmer(Employee, coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"the name is {self.company} and he is good with {self.language} language")


a = Employee()
p = Programmer()
p.show()
p.showLanguage()
p.printlanguages()
print(a.company,p.company)

