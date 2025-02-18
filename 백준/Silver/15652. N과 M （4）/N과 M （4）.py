from itertools import combinations_with_replacement

n, m = map(int, input().split())

nums = [i+1 for i in range(n)]

for com in combinations_with_replacement(nums, m):
    com = list(com)
    for i in com:
        print(i, end=" ")

    print()