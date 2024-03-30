import sys
input = sys.stdin.readline

def preFix2(nums):
    preFixSum = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            preFixSum[i][j] = preFixSum[i][j-1] + preFixSum[i-1][j] - preFixSum[i-1][j-1] + nums[i][j]
    return preFixSum

n, m = map(int, input().split())

nums = [[0] * (n+1)]
for i in range(n):
    row = [0] + list(map(int, input().split()))
    nums.append(row)

preFixSum = preFix2(nums)
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(preFixSum[x2][y2] - preFixSum[x1-1][y2] - preFixSum[x2][y1-1] + preFixSum[x1-1][y1-1])