def fib(i):
    x = 0
    y = 1
    c = 0

    while c < i:
        print(x)
        z = x + y
        x = y
        y = z
        c += 1

num1 = int(input("How many terms do you want to add:"))
print(fib(num1))



#Inline but prints none for some reason
