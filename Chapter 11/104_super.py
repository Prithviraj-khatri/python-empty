class Employee:
     def __init__(self):
          print("this employee constructor")
     a = 1

class programmer(Employee):
     def __init__(self):
          print("this programmer constructor")
     b = 2

class manager(programmer):
     def __init__(self):
          super(). __init__()
          print("this manager constructor")
     c = 3

# o = Employee
# print(o.a)

# o = programmer
# print(o.a,o.b)

o = manager()
print(o.a,o.b,o.c)

