from collections import deque

n,m = map(int,input().split())
map = [list(map(int, input().split())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 1, 0, 1, -1, -1, 1, 0]

q = deque()

for i in range(n):
    for j in range(m):
        if map[i][j] == 1:
            q.append((i, j))
            dist[i][j] = 0

while q:
    x, y = q.popleft()
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1 and map[nx][ny] == 0:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

max_dist = 0
for i in range(n):
    for j in range(m):
        if dist[i][j] > max_dist:
            max_dist = dist[i][j]

print(max_dist)