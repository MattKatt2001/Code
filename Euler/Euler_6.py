#https://projecteuler.net/problem=6

x1 = []
x2 = []
for i in range (1,101):
    x1.append(i)
    x2.append(i**2)

y1 = sum(x1)
y2 = sum(x2)

z = y1 ** 2


#print(y1)
#print(y2)
#print(z)

ans = z - y2
print(ans)



#solved
#ans = 25164150
