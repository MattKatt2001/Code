def main(x):
    i = 0
    arr = []
    while x > i:
        num=int(input("Enter a number:"))
        arr.append(num)
        x = x - 1

    arr.sort()
    print(arr)

main(4) #the ammount of numbers
