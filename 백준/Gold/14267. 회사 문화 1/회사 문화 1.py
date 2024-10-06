n, m = map(int, input().split())
parent = list(map(int, input().split()))

for i in range(1, n):
    parent[i] -= 1

good = [0] * n
for _ in range(m):
    i, w = list(map(int,input().split()))
    good[i-1] += w
    
total_good = [0] * n
for i in range(n):
    total_good[i] = total_good[parent[i]] + good[i]
    
print(*total_good)