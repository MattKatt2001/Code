# "Prime Factorization" is finding which prime numbers multiply together to make the original number.

def main(x):
    num = x #Give int value
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(i,"times",num//i,"is",num) #//rounds down
                main(num//i)
                break
        else:
            print(num, "is as far as this can go (this is the highest prime number)")
    else:
        print(num, "is not a prime")

main(249867009)  #give input it will execute prime Factorization
