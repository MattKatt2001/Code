def Addnum(x):
    i = 0
    arr = []
    while x > i:
        num=int(input("Enter a number:"))
        arr.append(num)
        x = x - 1

    return sum(arr)


num1=int(input("How many numbers do you want to add:"))
print(Addnum(num1))
