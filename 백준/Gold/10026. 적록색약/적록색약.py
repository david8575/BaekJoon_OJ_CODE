import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

n = int(input())
rgb = [list(input().strip()) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

normal_cnt, blind_cnt = 0, 0

def dfs(x, y):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    visited[x][y] = True
    current_color = rgb[x][y]

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if visited[nx][ny] == False:
                if rgb[nx][ny] == current_color:
                    dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            normal_cnt += 1

for i in range(n):
    for j in range(n):
        if rgb[i][j] == 'G':
            rgb[i][j] = 'R'

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            blind_cnt += 1

print(normal_cnt, blind_cnt)