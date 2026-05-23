class employee:
    lan = "python"
    salary = 120000

harry = employee
harry.lan = "javascript"
print(harry.lan, harry.salary)