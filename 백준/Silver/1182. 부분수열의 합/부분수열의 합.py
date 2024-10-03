from itertools import combinations

n, s = map(int, input().split())
nums = list(map(int, input().split()))

count = 0

for i in range(1, n+1):
    for combination in combinations(nums, i):
        if sum(combination) == s:
            count+=1
    
    
print(count)