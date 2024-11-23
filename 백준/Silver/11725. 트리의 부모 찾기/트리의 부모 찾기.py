import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = map(int, input().split())
    
    adj[u-1].append(v-1)
    adj[v-1].append(u-1)

visited = [False] * n
parent = [-1] * n
     
def dfs(u):
    visited[u] = True
    
    for v in adj[u]:
        if not visited[v]:
            parent[v] = u
            dfs(v)

dfs(0)

for i in range(1, n):
    print(parent[i] + 1)