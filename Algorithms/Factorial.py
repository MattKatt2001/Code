import math

def main(x):
    return (math.factorial(x))#this one is better for longer numbers

def factorial(x):
    if x == 1:
        return x
    elif x < 1:
        return(1)
    else:
        return x * factorial(x-1)


x = main(999)# input an int both methods work
print(x)
