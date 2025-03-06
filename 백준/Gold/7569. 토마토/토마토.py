
import sys
from collections import deque
input = sys.stdin.readline

m,n,h = map(int, input().split())

tomato = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
visited =[[[False] * m for _ in range(n)] for _ in range(h)]

queue = deque()

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def bfs():
    while queue:
        x,y,z = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
                continue

            if tomato[nx][ny][nz] == 0 and visited[nx][ny][nz] == False:
                queue.append((nx, ny, nz))
                tomato[nx][ny][nz] = tomato[x][y][z] + 1
                visited[nx][ny][nz] = True

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1 and visited[i][j][k] == 0:
                queue.append((i,j,k))
                visited[i][j][k] = True

bfs()

answer = 0

for i in tomato:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)

        answer = max(answer, max(j))

print(answer-1)
