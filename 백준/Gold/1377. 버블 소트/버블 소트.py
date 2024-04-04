import sys
input = sys.stdin.readline

n = int(input())
nums = []

for i in range(n):
    nums.append((int(input()), i))

max = 0
sorted_nums = sorted(nums)

for i in range(n):
    if max < sorted_nums[i][1] - i:
        max = sorted_nums[i][1] - i

print(max + 1)