from collections import deque

n, k = map(int, input().split())

max_num = 100000
visited = [0] * 100001

q = deque()
q.append(n)
while q:
    x = q.popleft()
    
    if x == k:
        print(visited[x])
        break
    
    for i in (x-1, x+1, 2*x):
        if 0 <= i <= max_num and not visited[i]:
            visited[i] = visited[x] + 1
            q.append(i)
