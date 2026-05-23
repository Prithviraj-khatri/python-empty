class demo:
    a = 4

o = demo()
print(o.a) # prints the class attribute because instance attributes is not present
o.a = 0 # instace attribute is set
print(o.a) # prints the instance attribute because instance attribute is present
print(demo.a) # prints the class attributes 