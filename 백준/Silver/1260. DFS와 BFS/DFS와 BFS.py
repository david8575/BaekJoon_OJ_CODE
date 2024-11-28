from collections import deque

n, m, s = map(int, input().split())

adj = [[] for _ in range(n)]

for _ in range(m):
    u,v = map(int, input().split())
    adj[(u-1)].append(v-1)
    adj[(v-1)].append(u-1)
    
dfs_seq = []
visited = [False] * n
def dfs(u):
    visited[u] = True
    dfs_seq.append(u+1)
    for v in sorted(adj[u]):
        if not visited[v]:
            dfs(v)
dfs(s-1)

bfs_seq = []
visited = [False] * n
def bfs(u):
    visited[u] = True
    q =  deque()
    q.append(u)
    while(q):
        curr = q.popleft()
        bfs_seq.append(curr + 1)
        for v in sorted(adj[curr]):
            if not visited[v]:
                visited[v] = True
                q.append(v)   
    
bfs(s-1)

print(" ".join(map(str,dfs_seq)))
print(" ".join(map(str,bfs_seq)))