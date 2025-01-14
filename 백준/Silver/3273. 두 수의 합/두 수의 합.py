n = int(input())
nums = list(map(int, input().split()))
m = int(input())

nums.sort()
count = 0
i = 0
j = n-1
while i < j:
    if nums[i] + nums[j] == m:
        count += 1
        i += 1
        j -= 1
    elif nums[i] + nums[j] < m:
        i += 1
    else:
        j -= 1

print(count)