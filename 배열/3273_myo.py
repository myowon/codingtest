import sys

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
m.sort()

x = int(sys.stdin.readline())

c = 0
left = 0
right = n-1

while left != right:
    if m[left] + m[right] == x:
        c += 1
        left += 1
    elif m[left] + m[right] > x:
        right -= 1
    else:
        left += 1

print(c)