import sys

n = int(sys.stdin.readline())

for _ in range(n):
    a, b = map(str, sys.stdin.readline().split())
    a = list(a)
    b = list(b)
    
    a.sort()
    b.sort()
    
    if(a == b):
        print("Possible")
    else:
        print("Impossible")