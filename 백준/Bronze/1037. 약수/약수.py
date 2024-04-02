n = int(input())
nums = list(map(int, input().split()))

if n == 1:
    print(nums[0]**2)
elif n == 2:
    print(nums[0]*nums[1])
else:
    print(max(nums)*min(nums))