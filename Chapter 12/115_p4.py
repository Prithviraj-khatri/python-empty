try:
    a = int(input("enter the a: "))
    b = int(input("enter the b: "))
    print(a/b)

except ZeroDivisionError as v:
    print("infinite")