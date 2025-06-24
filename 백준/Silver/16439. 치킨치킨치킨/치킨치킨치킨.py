from itertools import combinations
n, m = map(int, input().split())

preferences = []
for _ in range(n):
    preferences.append(list(map(int, input().split())))

ans = 0
for x, y, z in combinations(range(m), 3):
    sum = 0
    for i in range(n):
        sum += max(preferences[i][x], preferences[i][y], preferences[i][z])

    ans = max(ans, sum)

print(ans)