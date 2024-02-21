import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
S = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
result = 0

def bfs(x, y):
    #상, 하, 좌, 우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    q=deque([(x,y)])
    
    initial = S[x][y]
    height = 9
    result = set()
    result.add((x,y))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not (0<=nx<N and 0<=ny<M):
                return 0, set()
            if S[nx][ny] <= initial and (nx, ny) not in result:
                result.add((nx, ny))
                q.append((nx, ny))
            elif S[nx][ny] > initial:
                height = min(height, S[nx][ny])
            
    return result, height

def pool(s, h):
    global result
    
    for x, y in s:
        result += h - S[x][y]
        S[x][y] = h

for i in range(N):
    for j in range(M):
        s, h = bfs(i, j)
        if s:
            pool(s, h)
        
print(result)