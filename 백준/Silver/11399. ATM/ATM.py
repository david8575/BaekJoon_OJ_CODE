def insertionSort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j-=1
        nums[j+1] = key
def preFix(nums):
    preFixSum = [0]
    for num in nums:
        preFixSum.append(preFixSum[-1] + num)
    return preFixSum

n = int(input())
nums = list(map(int, input().split()))
insertionSort(nums)
prefixnums = preFix(nums)

sum = 0
for i in range(n+1):
    sum += prefixnums[i]
print(sum)