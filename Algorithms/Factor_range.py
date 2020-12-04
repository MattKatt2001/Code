def main(n):
    divs = [x for x in range(1,11) if n % x == 0]#change the factor range here
    return divs

x = main(2520)#give an int and it will print its factors
print(x)
