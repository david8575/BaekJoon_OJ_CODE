def josephus(n,k):
    nums = [i+1 for i in range(n)]
    result = []
    idx = 0
    while len(nums) != 0:
        idx = (idx + k - 1) % len(nums)
        result.append(nums.pop(idx))

    return result

n, k = map(int, input().split())
result = josephus(n,k)
print("<", end="")
for i in range(n-1):
    print(result[i], end=", ")
print(result[n-1], end="")
print(">", end="")