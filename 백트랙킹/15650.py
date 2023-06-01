import sys

n, m = map(int, sys.stdin.readline().split())

a = []

def dfs(x):
    if len(a) == m:
        print(' '.join(map(str, a)))
        return

    for i in range(x, 1+n):
        a.append(i)
        dfs(i+1)
        a.pop()

dfs(1)