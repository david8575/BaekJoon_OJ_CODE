from collections import deque
from itertools import combinations

n, m = map(int, input().split())
map = [list(map(int, input().split())) for i in range(n)]

cells = [(i,j) for i in range(n) for j in range(m) if map[i][j] == 0]


answer = 0
for combination in combinations(cells, 3):
    for row, col in combination:
        map[row][col] = 1
        
    visit = [[False] * m for _ in range(n)]
    queue = deque()
    
    for i in range(n):
        for j in range(m):
            if (map[i][j] == 2):
                queue.append((i,j))
                visit[i][j] = True

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while len(queue) != 0:
        r, c = queue.popleft()
        
        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]
            
            if nx < 0 or n <= nx or ny < 0 or m <= ny:
                continue
            if map[nx][ny] == 1:
                continue
            if not visit[nx][ny]:
                queue.append((nx, ny))
                visit[nx][ny] = True
    
    safe = 0
    for i in range(n):
        for j in range(m):
            if map[i][j] == 0 and not visit[i][j]:
                safe += 1
                
    answer = max(answer, safe)
    
    for row, col in combination:
        map[row][col] = 0
        
print(answer)