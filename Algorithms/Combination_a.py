def filter(x):
    i = 0
    z = x
    o = x
    while x >= i:
        y = x + z
        print(y,"=",x,"+",z) #
        z = z - 1
        if z == 0:
            z = o
            x = x - 1


x = filter(50) #enter X
print(x) #This shows every possible combination for +
