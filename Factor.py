def is_factor(n,i):
    if n % i == 0:
        return 1
    else:
        return 0

x = is_factor(10,2)#give two int values
print(x)
