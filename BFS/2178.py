import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

#붙여서 입력하면 rstrip 사용
g = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

def bfs(x, y):
    #상, 하, 좌, 우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    q = deque([(x, y)])
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 1:
                    q.append((nx, ny))
                    #print(g[x][y] + 1)
                    g[nx][ny] = g[x][y] + 1
                    
    return g[n-1][m-1]

result = bfs(0,0)
print(result)