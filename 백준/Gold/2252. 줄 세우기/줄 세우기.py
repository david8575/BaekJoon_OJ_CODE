from collections import deque

n, m = map(int, input().split())

adj = [[] for _ in range(n+1)]
seq = [0] * (n+1)
for _ in range(m):
    s,d = map(int, input().split())
    adj[s].append(d)
    seq[d] += 1

q = deque()
for i in range(1,n+1):
    if seq[i] == 0:
        q.append(i)

line = []
while q:
    u = q.popleft()
    line.append(u)

    for v in adj[u]:
        seq[v] -= 1
        if seq[v] == 0:
            q.append(v)

for i in line:
    print(i, end= " ")