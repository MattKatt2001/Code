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
