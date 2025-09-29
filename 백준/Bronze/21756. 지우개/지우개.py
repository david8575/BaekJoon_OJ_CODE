n = int(input())
nums = list(i for i in range(1,n+1))

while len(nums) != 1:
    nums = [nums[i] for i in range(len(nums)) if (i+1) % 2 == 0]
    
print(nums[0])