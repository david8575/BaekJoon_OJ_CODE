from collections import deque
import sys
sys.setrecursionlimit(10*6)

dx = [1,-1,0,0,1,1,-1,-1]
dy = [0,0,1,-1,1,-1,1,-1]

def bfs(a, b, visited):
    q = deque()
    q.append((a,b))
    visited[a][b] = True

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and area[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True

while(True):
    w, h = map(int, input().split())

    if (w == 0 and  h == 0): break

    area = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    
    cnt = 0
    for i in range(h):
        for j in range(w):
            if area[i][j] == 1 and not visited[i][j]:
                bfs(i,j,visited)
                cnt += 1
    
    print(cnt)