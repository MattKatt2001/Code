def fib():
    x = 0
    y = 1
    c = 0

    while c < 10: #make this for how many terms you want
        print(x)
        z = x + y
        x = y
        y = z
        c += 1


fib()
