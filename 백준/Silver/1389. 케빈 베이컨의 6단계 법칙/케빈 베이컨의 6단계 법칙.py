n, m = map(int, input().split())

graph = [[float('inf')] * n for _ in range(n)]

for _ in range(m):
    src, des = map(int, input().split())
    graph[src-1][des-1]=1
    graph[des-1][src-1]=1

for i in range(n):
    graph[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

row_sum = [sum(row) for row in graph]
min_sum = min(row_sum)
print(row_sum.index(min_sum) + 1)

