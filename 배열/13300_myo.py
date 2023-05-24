import sys
import math

n, k = map(int, sys.stdin.readline().split())

student = [[0, 0] for _ in range(7)]

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    student[y][x] += 1

room = 0

for i in student:
    for j in i:
        room += math.ceil(j/k)
        
print(room)