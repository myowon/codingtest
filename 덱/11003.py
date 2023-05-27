# 시간 초과
# import sys
# from collections import deque

# N, L = map(int, sys.stdin.readline().split())

# q = deque(sys.stdin.readline().split())
# mini = []

# for i in range(N):
#     s = i-L+1
#     if s < 0:
#         n = list(q)[s:] + list(q)[:i+1]
#         mini.append(min(n))
#     else:
#         m = list(q)[s:i+1]
#         mini.append(min(m))
        
# print(' '.join(mini))


# import sys
# from collections import deque

# N, L = map(int, sys.stdin.readline().split())

# q = deque(map(int,sys.stdin.readline().split()))
# mini = []

# for i in range(N):
#     if i < L:
#         mini.append(min(list(q)[:L]))
#     else:
#         q.popleft()
#         mini.append(min(q))
        
# print(' '.join(map(str,mini)))

import sys
from collections import deque

N, L = map(int, sys.stdin.readline().split())
ar = list(map(int, sys.stdin.readline().split()))

q = deque()

for i in range(N):
    if q and q[0][0] <= i - L:
        q.popleft()
    while q and q[-1][1] > ar[i]:
        q.pop()
    q.append((i, ar[i]))
    print(q[0][1], end=" ")


# import sys
# from collections import deque

# N, L = map(int, sys.stdin.readline().split())

# q = deque()
# ar = list(map(int,sys.stdin.readline().split()))

# for i in range(N):
#     while q and q[0] <= i-L:
#         q.popleft()
#     while q and ar[q[-1]] > ar[i]:
#         q.pop()
#     q.append(i)
#     print(ar[q[0]], end=' ')