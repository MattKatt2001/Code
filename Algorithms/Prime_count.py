num = 2
x = 0
while x < 6: #change this
    for i in range(2,num):
        if (num % i) == 0:
            num += 1
    else:
        print(num)
        x +=1
        num += 1


#THIS DOESN'T WORK I INCREMENTS FOR SOME REASON
