import sys
from collections import deque
input = sys.stdin.readline

n = int(input()) 
area = [list(map(int, input().split())) for _ in range(n)]
rain = 0
for i in range(n):
    for j in range(n):
        if rain < area[i][j]:
            rain = area[i][j]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x, y, rain, visited):
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        a, b = q.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if area[nx][ny] > rain and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

result = 0
for i in range(rain):
    visited = [[False] * n for _ in range(n)]
    cnt = 0

    for j in range(n):
        for k in range(n):
            if area[j][k] > i and not visited[j][k]:
                bfs(j, k, i, visited)
                cnt += 1
    
    if cnt > result: 
        result = cnt

print(result)