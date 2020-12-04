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

fact = int(input("Enter a number:"))
x = main(fact)
print(x)
