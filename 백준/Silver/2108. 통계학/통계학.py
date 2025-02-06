import sys
import statistics
from collections import Counter
input = sys.stdin.readline

n = int(input())    
nums = []

for _ in range(n):
    nums.append(int(input()))

print(round(sum(nums)/n))
print(sorted(nums)[n//2])

count = Counter(nums)
mode = count.most_common()
if len(mode) > 1 and mode[0][1] == mode[1][1]:
    modes = [mode[0][0]]
    for i in range(1, len(mode)):
        if mode[i][1] == mode[0][1]:
            modes.append(mode[i][0])
        else:
            break
    mode = sorted(modes)[1] 
else:
    mode = mode[0][0]
print(mode)

range_value = max(nums) - min(nums)
print(range_value)