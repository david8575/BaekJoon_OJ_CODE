n = int(input())
nums = list(map(int, input().split()))

nums_sorted = sorted(list(set(nums)))

dic = {}

for i in range(len(nums_sorted)):
    dic[nums_sorted[i]] = i

for i in nums:
    print(dic[i], end=" ")