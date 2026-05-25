a = int(input("enter the first number: "))
b = int(input("enter the first number: "))

if(b == 0):
    raise ZeroDivisionError("our program is not meant to be divisible by zero")
else:
    print(f"the divsion a/b is {a/b}")