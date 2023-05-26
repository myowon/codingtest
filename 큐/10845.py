import sys

N = int(sys.stdin.readline())

q = []

for _ in range(N):
    c = list(sys.stdin.readline().split())
    
    if c[0] == 'push':
        q.append(c[1])
    elif c[0] == 'front':
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)
    elif c[0] == 'back':
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)
    elif c[0] == 'pop':
        if len(q) > 0:
            print(q.pop(0))
        else:
            print(-1)
    elif c[0] == 'size':
        print(len(q))
    elif c[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
