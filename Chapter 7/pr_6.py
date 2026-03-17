n = int(input("Enter the number: "))
for i in range(1, n+1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1), end="")
    print("")

for j in range(1, n+1):
    print("*" * j, end="")
    print("")

for k in range(1,n+1):
    if(k==1 or k==n):
        print("*"*n, end="")
    else:
        print("*", end="")
        print(" "*(n-2),end="")
        print("*", end ="")
    print("")