a = 32

def fun():
    global a
    a = 3
    print(a)

fun()
print(a)