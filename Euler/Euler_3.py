#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143

#Prime Factorization

def main(x):
    num = x #Give int value
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(i,"times",num//i,"is",num) #// rounds the result down to the nearest whole number
                main(num//i)
                break
        else:
            print(num, "is the answer")
main(600851475143)

#solved
#ans = 6857
