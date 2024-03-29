import sys
input = sys.stdin.readline
def preFix(nums):
    preFixSum = [0]
    for num in nums:
        preFixSum.append(preFixSum[-1] + num)
    return preFixSum

n, m = map(int,input().split())
nums = list(map(int, input().split()))

preFixSum = preFix(nums)
for i in range(m):
    s, e = map(int, input().split())
    print(preFixSum[e] - preFixSum[s-1])