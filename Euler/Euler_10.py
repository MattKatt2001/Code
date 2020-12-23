#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.
x = []
num = 2 #Give int value
while num < 2000000:
    for i in range(2,num):
        if (num % i) == 0:
            #print(num, "is not a prime")
            #print(i,"times",num//i,"is",num) #//rounds down
            num += 1
    else:
            #print(num, "is a prime")
            num += 1
            x.append(num)
print(x)
