def main(num, x, z):
    orginal = num
    ans = 0

    while(num > 0):
        #arr.append()
        digit = num%10
        ans = ans * 10 + digit
        num=num//10

        if(orginal == ans):
            pass
            print(orginal, "is a palindrome!", x , "x", z) #A palindromic number reads the same both ways

        else:
            pass

def filter(x):
    i = 0
    z = x
    o = x
    while x > i:
        y = x * z
        main(y,x,z)
        z = z - 1
        if z == 0:
            z = o
            x = x - 1


x = filter() #input an !int
print(x)
