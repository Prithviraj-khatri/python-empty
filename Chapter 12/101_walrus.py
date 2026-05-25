# using walrus operator

if(n := len([1,2,3,4,5]))> 3:
    print (f"list too long ({}elements, expected <= 3)")