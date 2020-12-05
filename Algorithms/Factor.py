def is_factor(n,i):
    if n % i == 0:
        return "Factor"
    else:
        return "Not factor"

x = is_factor(10,2)#give two int values
print(x)
