class Employee:
    salary = 234
    increment = 20

    @property
    def salaryIncrement(self):
        return(self.salary + self.salary * (self.increment/100))
    
    @salaryIncrement.setter
    def salaryIncrement(self,salary):
        self.increment = ((salary/self.salary)- 1)*100

e = Employee()
e.salaryIncrement = 280.8
print(e.increment)



