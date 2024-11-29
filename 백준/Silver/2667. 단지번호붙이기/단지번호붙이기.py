from collections import deque

n = int(input())
vilage = []
for _ in range(n):
    vilage.append(list(map(int, input())))
    
def bfs(graph, x,y):
    max = len(graph)
    q = deque()
    q.append((x,y))
    graph[x][y] = 0
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    cnt = 1
    while q:
        u, v = q.popleft()
        for i in range(4):
            nx = u + dx[i]
            ny = v + dy[i]
            
            if 0 <= nx < max and 0 <= ny < max and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                cnt+=1
                q.append((nx,ny))

    return cnt

cnts = []
for i in range(n):
    for j in range(n):
        if vilage[i][j] == 1:
            cnts.append(bfs(vilage, i, j))
            
cnts.sort()
print(len(cnts))
for cnt in cnts:
    print(cnt) 