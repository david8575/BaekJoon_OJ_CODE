from collections import deque

row, col = map(int, input().split())

maze = []

for _ in range(row):
    maze.append(input())

visit = [[False] * col for _ in range(row)]
dist = [[-1] * col for _ in range(row)]
q = deque([(0, 0)])
visit[0][0] = True
dist[0][0] = 0

while len(q) != 0:
    r, c = q.popleft()
    
    if r > 0 and maze[r-1][c] == '1' and not visit[r-1][c]:
        q.append((r-1, c))
        visit[r-1][c] = True
        dist[r-1][c] = dist[r][c] + 1
        
    if r < row - 1 and maze[r+1][c] == '1' and not visit[r+1][c]:
        q.append((r+1, c))
        visit[r+1][c] = True
        dist[r+1][c] = dist[r][c] + 1
        
    if c > 0 and maze[r][c-1] == '1' and not visit[r][c-1]:
        q.append((r, c-1))
        visit[r][c-1] = True
        dist[r][c-1] = dist[r][c] + 1
        
    if c < col - 1 and maze[r][c+1] == '1' and not visit[r][c+1]:
        q.append((r, c+1))
        visit[r][c+1] = True
        dist[r][c+1] = dist[r][c] + 1
        
print(dist[row-1][col-1] + 1)