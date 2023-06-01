import sys

n, m = map(int, sys.stdin.readline().split())

a = []

def dfs(x):
    if len(a) == m:
        print(' '.join(map(str, a)))
        return
    
    for i in range(x, n+1):
        a.append(i)
        dfs(i)
        a.pop()

dfs(1)