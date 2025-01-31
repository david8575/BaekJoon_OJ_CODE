from itertools import permutations

n, m = map(int, input().split())
nums = [i for i in range(1, n + 1)]

for permutation in permutations(nums, m):
    for num in permutation:
        print(num, end=' ')
    print()