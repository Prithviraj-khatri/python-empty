try:
    a = int(input("enter the number: "))
    print(a)

except Exception as e:
    print(e)

finally:
    print("hey i am inside finally")
    