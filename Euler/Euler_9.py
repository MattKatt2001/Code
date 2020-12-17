#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

def main(a,b,c):
    while (c < 1000):
        if a**2 * b**2 == c**2:
            print("found")
            break
        else:
            print(a,b,c)
            a+= 1
            if a > 999:
                a = 1
                b +=1
            if b > 999:
                a = 1
                b = 1
                c+=1
    print("no find")

main(375,199,425)
