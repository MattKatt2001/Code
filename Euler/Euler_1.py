#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#For all numbers that are less than 1000 but are multples of 3 or 5 we add them to an array
#We then sum the array elements

y = []
z = []
i = 999

while 0 < i:
    y.append(i)
    i -= 1

#print(y)

for x in y:
    if x % 3 == 0 or x % 5 == 0:
        z.append(x)

#print(z)

ans = sum(z)
print(ans)

#solved
#ans = 233168
