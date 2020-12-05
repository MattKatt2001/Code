#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?
"""
z = 1
num = 1
#y = []

while z <= 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num, "is not a prime")
                #print(i,"times",num//i,"is",num) #//rounds down
                num += 1
                #print(num)
            else:
                print(num, "is a prime")
                num += 1
                z += 1
                #y.append(i)
        else:
            print(num, "is not a prime")
            num += 1

#print(len(y))
"""

def main(num):
    while num < 10001:
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    print(num, "is not a prime")
                    print(i,"times",num//i,"is",num) #//rounds down
                    main(num + 1)
                else:
                    print(num, "is a prime")
                    main(num + 1)
            else:
                print(num, "is not a prime")
                main(num + 1)

    return num

x = main(2)
print(x)
