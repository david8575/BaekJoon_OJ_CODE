from collections import deque

col, row = map(int, input().split())
tomatos = [list(map(int , input().split())) for _ in range(row)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque()
for i in range(row):
    for j in range(col):
        if tomatos[i][j] == 1:
            q.append((i,j))
            
while q:
    x,y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < row and 0 <= ny < col and tomatos[nx][ny] == 0:
            tomatos[nx][ny] = tomatos[x][y] + 1
            q.append((nx,ny))
            
day = 0
for row_data in tomatos:
    if 0 in row_data:
        print(-1)
        exit()
    day = max(day, max(row_data))

print(day - 1)