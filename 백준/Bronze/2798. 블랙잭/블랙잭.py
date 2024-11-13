from itertools import combinations
n, m = map(int, input().split())
cards = list(map(int, input().split()))

answer = 0
for combination in combinations(cards, 3):
    res = sum(combination)
    if (answer < res and res <= m):
        answer = res

print(answer)