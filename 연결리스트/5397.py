import sys

c = int(sys.stdin.readline())

for _ in range(c):
    a = sys.stdin.readline().strip()
    l = []
    r = []

    for i in a:
        if i == '<' and l:
            r.append(l.pop())
        elif i == '>' and r:
            l.append(r.pop())
        elif i == '-' and l:
            l.pop()
        elif i != '<' and i != '>' and i != '-':
            l.append(i)
    
    result = l + r[::-1]
    
    print(''.join(result))
            