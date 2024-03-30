n = int(input())
m = int(input())

nums = list(map(int, input().split()))
nums.sort()

cnt = 0
start_idx = 0
end_idx = len(nums)-1

while start_idx < end_idx:
    if nums[start_idx] + nums[end_idx] > m:
        end_idx-=1
    elif nums[start_idx] + nums[end_idx] < m:
        start_idx+=1
    else:
        cnt+=1
        start_idx+=1
        end_idx-=1

print(cnt)