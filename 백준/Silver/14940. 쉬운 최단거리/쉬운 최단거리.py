import sys
from collections import deque 
input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)] 

dist = [[-1] * m for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

start_x, start_y = 0, 0
for i in range(n):
    for j in range(m):
        if map[i][j] == 2:
            start_x, start_y = i, j
            break

q = deque()
q.append((start_x, start_y))
dist[start_x][start_y] = 0

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and map[nx][ny] == 1 and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

for i in range(n):
    for j in range(m):
        if map[i][j] == 0:
            dist[i][j] = 0

for row in dist:
    for i in row:
        print(i, end=' ')
    print()