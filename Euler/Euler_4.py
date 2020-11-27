#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

#We have a workin alogrithim that will determine a palindrome now we need to run it through different combinations of ints

def main(num, x, z):
    #arr = []
    orginal = num
    ans = 0

    while(num > 0): #11, 1
        #arr.append()
        digit = num%10 #1, 1
        ans = ans * 10 + digit #1, 11
        num=num//10 #1, 0

        if(orginal == ans):
            pass
            print(orginal, "is a palindrome!", x , "x", z) #A palindromic number reads the same both ways

        else:
            pass
    #print(arr)

def filter(x):
    i = 0
    z = x
    while x > i:
        y = x * z
        main(y,x,z)
        z = z - 1
        if z == 1:
            z = 999
            x = x - 1


x = filter(999)
print(x)

#solved 
#ans = 906609   919 x 913
