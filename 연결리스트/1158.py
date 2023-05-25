#import sys
#from collections import deque

#N, K = map(int, sys.stdin.readline().split())

#q = deque(range(1, N+1))
#result = []

#while q:
#    for _ in range(K-1):
#        q.append(q.popleft())
#    result.append(q.popleft())

#print(str(result).replace('[','<').replace(']','>'))


import sys

N, K = map(int, sys.stdin.readline().split())
ar = [i for i in range(1,N+1)]
result = []

s = 0

for i in range(N):
    s += K-1
    if s >= len(ar):
        s = s % len(ar)
    result.append(ar.pop(s))
print(str(result).replace('[','<').replace(']','>'))