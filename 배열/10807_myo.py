import sys

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))

v = int(sys.stdin.readline())
count = 0

for i in range(n):
    if m[i] == v:
        count += 1

print(count)