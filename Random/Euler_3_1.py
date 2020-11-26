def main(x):
    num = x #Give int value
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(i,"times",num//i,"is",num) #//rounds down
                main(num//i)
                break
        else:
            print(num, "is the answer")
    else:
        print(num, "is not a prime")

main(600851475143)  #testing for euler 3
