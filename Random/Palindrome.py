def main(num):

    orginal = num
    ans = 0

    while(num>0): #11, 1
        digit = num%10 #1, 1
        ans = ans * 10 + digit #1, 11
        num=num//10 #1, 0
    if(orginal == ans):
        print("The number is palindrome!") #A palindromic number reads the same both ways
    else:
        print("Not a palindrome!")

main(11) #Enter an int
