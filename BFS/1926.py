import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

a = [[False] * m for _ in range(n)]

g = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def bfs(x, y):
    # 상, 하, 좌, 우
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    
    count = 0
    
    queue = deque([(x, y)])
    a[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        count += 1
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == False and g[nx][ny] == 1:
                    a[nx][ny] = True
                    queue.append((nx, ny))
    return count

picture_count = 0
picture_max = 0
   
for i in range(n):
    for j in range(m):
        if a[i][j] == False and g[i][j] == 1:
            area = bfs(i, j)
            picture_count += 1
            picture_max = max(picture_max, area)
            
print(picture_count)
print(picture_max)