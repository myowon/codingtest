import sys

a = list(str(sys.stdin.readline()))
b = list(str(sys.stdin.readline()))

c = 0

for i in a:
    if i in b:
        b.remove(i)
    else:
        c += 1

c += len(b)
     
print(c)