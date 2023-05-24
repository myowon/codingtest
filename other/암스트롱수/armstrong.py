import math

n = 0

for i in range(153, 1000):
    n = i
    sum = 0
    while(n != 0):
        sum += int(math.pow(n%10, 3))
        n = n//10
    if(sum == i):
        print(i)
