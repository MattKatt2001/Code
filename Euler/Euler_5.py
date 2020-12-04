#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


#If we leave the 20 in, there is no need to leave the 2 in. Any integer evenly divisible by 20 is evenly divisible by 2 (but the reverse might not be true).
#So we leave the 20 and take out the 2, the 4, and the 5. Leave the 19, as it's prime.
#Leave the 18, but now we can take out the 3 and the 6. If you repeat this process, you wind up with a much shorter list of numbers to try.

#while/if for i in range
#1..20


x = 20
for i in range (1,21): #Goes through every one without recursion
    if x % i > 0: # If the number is not divisible by i
        for y in range (1,21):
            if (x * y) % i == 0: # Find the smallest number divisible by i
                x = x * y
                break
print(x)

#solved
#ans = 232792560


#https://stackoverflow.com/questions/8024911/project-euler-5-in-python-how-can-i-optimize-my-solution
#Irmak Aydeniz's post was very helpful to finding this answer
