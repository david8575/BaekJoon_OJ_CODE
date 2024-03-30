import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
cnt = 0

for i in range(n):
    num = nums[i]
    start_idx, end_idx = 0, n-1
    while start_idx < end_idx:
        if nums[start_idx] + nums[end_idx] == num:
            if start_idx != i and end_idx != i:
                cnt += 1
                break
            elif start_idx == i:
                start_idx += 1
            elif end_idx == i:
                end_idx -= 1
        elif nums[start_idx] + nums[end_idx] < num:
            start_idx+=1
        else:
            end_idx-=1

print(cnt)