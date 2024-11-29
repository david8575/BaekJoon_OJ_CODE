from collections import deque
    
def bfs(graph, x, y):
    max_x = len(graph[0])
    max_y = len(graph)
    q = deque()
    q.append((x, y))
    graph[y][x] = 0
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while q:
        col, row = q.popleft()
        for i in range(4):
            nx = col + dx[i]
            ny = row + dy[i]
            
            if 0 <= nx < max_x and 0 <= ny < max_y and graph[ny][nx] == 1:
                graph[ny][nx] = 0
                q.append((nx, ny))
    
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    field= [[0] * m for _ in range(n)]
    
    for i in range(k):
        u, v = map(int, input().split())
        field[v][u]+=1
    
    cnt = 0 
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
             bfs(field, j, i)
             cnt += 1
    
    print(cnt)
