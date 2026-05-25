class Employee:
     a = 1

class pragrammer(Employee):
     b = 2

class manager(pragrammer):
     c = 3

o = Employee
print(o.a)

o = pragrammer
print(o.a,o.b)

o = manager
print(o.a,o.b,o.c)

