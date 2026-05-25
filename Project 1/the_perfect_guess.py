import random
n = random.randint(1,100)
a = -1
guess = 1
while (a != n):
    a = int(input("guuess the number :"))
    if(a>n):
        print("lower number please")
        guess+=1

    elif(a<n):
        print("higher number pleaase")
        guess+=1

print(f"you have guessed the number {n} in {guess} attempts")
