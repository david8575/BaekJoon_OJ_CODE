import sys
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
    
for _ in range(int(input())):
    t, k = map(int, input().split())
    if t == 1:
        if len(adj[k]) == 1:
            print("no")
        else:
            print("yes")
    if t == 2:
        print("yes")