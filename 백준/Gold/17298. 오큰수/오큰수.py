n = int(input())

ans = [0] * n
nums = list(map(int, input().split()))
mystack = []

for i in range(n):
    while mystack and nums[mystack[-1]] < nums[i]:
        ans[mystack.pop()] = nums[i]
    mystack.append(i)

while mystack:
    ans[mystack.pop()] = -1

for i in range(n):
    print(ans[i], end=" ")