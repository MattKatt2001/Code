#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#while/if for i in range

#import pdb
#pdb.set_trace()


def main(x):
    i = 1
    while i <= 20:
            if x % i == 0:
                i = i + 1
            else:
                main(x+1)

main(1)
