n, m = map(int, input().split())

height = [[float('inf')] * n for _ in range(n)]
for _ in range(m):
    p1, p2 = map(int, input().split())
    height[p1-1][p2-1] = 1

for i in range(n):
    height[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            height[i][j] = min(height[i][j], height[i][k] + height[k][j])

count = 0
for i in range(n):
    can_determine = True
    for j in range(n):
        if i != j and height[i][j] == float('inf') and height[j][i] == float('inf'):
            can_determine = False
            break
    if can_determine:
        count += 1

print(count)