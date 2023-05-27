import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
S = list(map(int, sys.stdin.readline().split()))
q = deque(list(i for i in range(1,N+1)))

count = 0

for i in S:
    while True:
        if q[0] == i:
            q.popleft()
            break
        else:
            if q.index(i) <= len(q) // 2:
                q.append(q.popleft())
                count += 1
            else:
                q.appendleft(q.pop())
                count += 1

print(count)