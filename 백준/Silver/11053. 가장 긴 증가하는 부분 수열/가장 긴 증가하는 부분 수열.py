n = int(input())
nums = list(map(int, input().split()))

d = [1] * n

for i in range(1, n):
    for j in range(i):
        if nums[j] < nums[i]:
            d[i] = max(d[i], d[j]+1)

print(max(d))