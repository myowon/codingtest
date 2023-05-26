# 런타임 에러
# import sys
# from collections import deque

# N = int(sys.stdin.readline())

# q = deque(i for i in range(1, N+1))

# for _ in range(N):
#     q.popleft()
#     q.append(q[0])
#     q.popleft()

#     if(len(q) == 1):
#         print(q[0])
#         break
    
import sys
from collections import deque

N = int(sys.stdin.readline())

q = deque(i for i in range(1, N+1))

while(len(q) > 1):
    q.popleft()
    q.append(q[0])
    q.popleft()

print(q[0])